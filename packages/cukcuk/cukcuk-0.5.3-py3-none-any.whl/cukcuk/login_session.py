import hmac
import hashlib
import json
from datetime import datetime
import pytz
import requests

from .common import BASE_URL, handle_response
from .branch import Branch
from .invoice import Invoice, InvoiceList

from typing import Union


class LoginSession:
    def __init__(self, *, app_id, domain, secret_key):
        self.app_id = app_id
        self.domain = domain
        self.secret_key = secret_key
        self.login_time = datetime.now(pytz.UTC)
        self.__access_token = None
        self.__login()

    @classmethod
    def from_json(cls, file_path: str):
        with open(file_path, "r") as f:
            json_data = f.read()
            kwargs = json.loads(json_data)
            return cls(**kwargs)

    @property
    def access_token(self):
        if self.__access_token == None:
            raise Exception("Must login before retrieving access token")
        return self.__access_token

    @property
    def api_client(self) -> requests.Session:
        if "__api_client" not in self.__dict__:
            self.__api_client = requests.Session()
            self.__api_client.headers.update(self._auth_headers)
        return self.__api_client

    def get_all_branches(self, details=True) -> list[Branch]:
        url = f"{BASE_URL}/api/v1/branchs/all"
        resp = self.api_client.get(url, params={"includeInactive": True})

        records = handle_response(resp)
        branches = []
        for record in records:
            branch_id = record.get("Id", None)
            if branch_id != None:
                branch = self.__get_branch_detail(branch_id)
                branches.append(branch)

        return branches

    def get_invoices(self,
                     last_sync_date: datetime,
                     before_date: datetime = None,
                     branch: Union[Branch, None] = None,
                     get_details: bool = False) -> InvoiceList:
        all_invoices = InvoiceList()
        page = 1
        while True:
            invoices = self.get_invoice_paging(
                page=page,
                last_sync_date=last_sync_date,
                branch=branch,
                before_date=before_date,
                get_details=get_details
            )
            if len(invoices) == 0:
                break
            all_invoices.extend(invoices)
            page += 1

        return all_invoices

    def get_invoice_paging(self, page: int,
                           last_sync_date: datetime,
                           before_date: datetime = None,
                           branch: Union[Branch, None] = None,
                           limit: int = 100,
                           get_details: bool = False) -> InvoiceList:
        # Process time
        local_tz = pytz.timezone('Asia/Ho_Chi_Minh')

        if last_sync_date.tzinfo == None:
            last_sync_date = last_sync_date.replace(tzinfo=local_tz)

        if before_date == None:
            before_date = datetime.utcnow()
        if before_date.tzinfo == None:
            before_date = before_date.replace(tzinfo=local_tz)

        # Send requests
        url = f"{BASE_URL}/api/v1/sainvoices/paging"

        payload = {
            "Page": page,
            "Limit": limit,
            "BranchId": branch.Id if branch != None else None,
            "LastSyncDate": last_sync_date.isoformat(),
            "HaveCustomer": None,
        }
        resp = self.api_client.post(url, json=payload)
        records = handle_response(resp)
        invoices = InvoiceList()

        for record in records:
            if not get_details:
                invoice = Invoice.deserialize(record)
            else:
                invoice_ref = record.get("RefId", "")
                invoice = self.get_invoice(invoice_ref)

            try:
                invoice_date = datetime.fromisoformat(invoice.RefDate)
            except Exception:
                invoice_date = datetime.max.replace(tzinfo=local_tz)

            if invoice_date < before_date:
                invoices.append(invoice)

        return invoices

    def get_invoice(self, invoice_ref: str) -> Invoice:
        # get basic invoice info
        url = f"{BASE_URL}/api/v1/sainvoices/{invoice_ref}"
        resp = self.api_client.get(url)
        record = handle_response(resp)
        invoice = Invoice.deserialize(record)
        return invoice

    def __get_branch_detail(self, branch_id: str) -> Branch:
        url = f"{BASE_URL}/api/v1/branchs/setting/{branch_id}"
        resp = self.api_client.get(url)

        record = handle_response(resp)
        branch = Branch.deserialize(record)
        return branch

    @property
    def __signature(self):
        message = json.dumps(self.__info_no_signature, separators=(",", ":"))
        signature = hmac.new(
            key=self.secret_key.encode("utf-8"),
            msg=message.encode("utf-8"),
            digestmod=hashlib.sha256
        )
        return signature.hexdigest()

    @property
    def __info_no_signature(self):
        return {
            "AppID": self.app_id,
            "Domain": self.domain,
            "LoginTime": self.login_time.strftime("%Y-%m-%dT%H:%M:%SZ")
        }

    @property
    def _auth_headers(self):
        return {
            "CompanyCode": self.domain,
            "Authorization": f"Bearer {self.access_token}"
        }

    def __login(self):
        url = f"{BASE_URL}/api/Account/Login"
        payload = self.__info_no_signature
        payload["SignatureInfo"] = self.__signature
        resp = requests.post(url, json=payload)
        if not resp.ok:
            raise Exception(
                f"Failed to login with status {resp.status_code}. Check your login info"
            )

        content = json.loads(resp.text)
        if not content.get("Success", False):
            raise Exception(
                f'Failed to login with error message {content["ErrorMessage"]}'
            )

        self.__access_token = content["Data"]["AccessToken"]

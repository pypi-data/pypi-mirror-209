from datetime import datetime
import aiohttp
import asyncio
import pytz

from .branch import Branch
from .invoice import Invoice, InvoiceList
from .login_session import LoginSession
from .common import BASE_URL, handle_response_async

from typing import Union


class AsyncLoginSession(LoginSession):
    def __init__(self, *, app_id, domain, secret_key):
        super().__init__(app_id=app_id, domain=domain, secret_key=secret_key)

    def api_client(self) -> aiohttp.ClientSession:
        return aiohttp.ClientSession(
            base_url=BASE_URL,
            headers=self._auth_headers,
        )

    async def get_all_branches(self, details=True) -> list[Branch]:
        url = "/api/v1/branchs/all"
        async with self.api_client() as client:
            resp = await client.get(url, params={"includeInactive": "true"})
            records = await handle_response_async(resp)
            tasks = []
            for record in records:
                branch_id = record.get("Id")
                if branch_id != None:
                    task = self.__get_branch_detail(client, branch_id)
                    tasks.append(task)
            branches = await asyncio.gather(*tasks)
            return branches

    async def get_invoices(self,
                           last_sync_date: datetime,
                           before_date: datetime = None,
                           branch: Union[Branch, None] = None,
                           get_details: bool = False) -> InvoiceList:
        all_invoices = InvoiceList()
        page = 1
        while True:
            invoices = await self.get_invoice_paging(page=page,
                                                     last_sync_date=last_sync_date,
                                                     before_date=before_date,
                                                     branch=branch,
                                                     get_details=get_details)
            if len(invoices) == 0:
                break
            all_invoices.extend(invoices)
            page += 1

        return all_invoices

    async def get_invoice_paging(self,
                                 page: int,
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
        url = "/api/v1/sainvoices/paging"

        payload = {
            "Page": page,
            "Limit": limit,
            "BranchId": branch.Id if branch != None else None,
            "LastSyncDate": last_sync_date.isoformat(),
            "HaveCustomer": None,
        }

        async with self.api_client() as client:
            resp = await client.post(url, json=payload)
            records = await handle_response_async(resp)
            if not get_details:
                invoices = [Invoice.deserialize(record) for record in records]
            else:
                tasks = []
                for record in records:
                    invoice_ref = record.get("RefId")
                    if invoice_ref != None:
                        task = self.get_invoice(invoice_ref)
                        tasks.append(task)
                invoices = await asyncio.gather(*tasks)

        # Filter invoices using before date
        results = []
        for invoice in invoices:
            try:
                invoice_date = datetime.fromisoformat(invoice.RefDate)
            except Exception:
                invoice_date = datetime.max.replace(tzinfo=local_tz)

            if invoice_date <= before_date:
                results.append(invoice)

        return InvoiceList(results)

    async def get_invoice(self, invoice_ref: str) -> Invoice:
        async with self.api_client() as client:
            # get basic invoice info
            url = f"/api/v1/sainvoices/{invoice_ref}"
            resp = await client.get(url)
            record = await handle_response_async(resp)

        invoice = Invoice.deserialize(record)
        return invoice

    async def __get_branch_detail(self, client: aiohttp.ClientSession, branch_id: str) -> Branch:
        url = f"/api/v1/branchs/setting/{branch_id}"
        resp = await client.get(url)
        record = await handle_response_async(resp)
        branch = Branch.deserialize(record)
        return branch

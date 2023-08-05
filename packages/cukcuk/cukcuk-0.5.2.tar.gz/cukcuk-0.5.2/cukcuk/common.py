from sqlalchemy.sql.schema import Table as SqlTable
from sqlalchemy import Engine as SqlEngine, Connection as SqlConnection
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session as SqlSession
from sqlalchemy.exc import IntegrityError as SqlIntegrityError
import aiohttp
import requests
import pandas as pd
import json
from http.client import responses as http_responses
from typing import Union

BASE_URL = "https://graphapi.cukcuk.vn"


class SqlTableBase(DeclarativeBase):
    pass


class SqlTableMixin:
    def __init__(self):
        super().__init__()
        for column in self.column_names():
            self.__dict__[column] = None

    def save(self, session: SqlSession):
        key_names = [col.key for col in self.__table__.primary_key.columns]
        primary_keys = [self.__dict__.get(key) for key in key_names]
        existing_obj = session.get(self.__class__, ident=primary_keys)
        if existing_obj == None:
            session.add(self)

    @classmethod
    def this_table(self) -> SqlTable:
        return self.__table__

    @classmethod
    def relationship_names(cls) -> list[str]:
        return [rel.key for rel in cls.__mapper__.relationships]

    @classmethod
    def column_names(cls) -> list[str]:
        return [column.name for column in cls.this_table().columns]

    @classmethod
    def create_table(cls, engine: Union[SqlEngine, SqlConnection]):
        cls.this_table.create(engine)

    @classmethod
    def deserialize(cls, record: Union[dict, list]):
        # record is of type list
        if type(record) == list:
            return [cls.deserialize(item) for item in record]

        # record is of type dict
        result = cls()
        for key, value in record.items():
            if key in cls.column_names():
                result.__dict__[key] = value
        return result

    @classmethod
    def to_df(cls, instances: list, **kwargs) -> pd.DataFrame:
        records = [instance.to_dict() for instance in instances]
        return pd.DataFrame(records, **kwargs)

    def to_dict(self) -> dict:
        fields = {}
        for column in self.column_names():
            fields[column] = self.__dict__.get(column, None)
        return fields

    def __repr__(self) -> str:
        fields = self.to_dict()
        result = json.dumps(fields, indent=4)
        return result


def handle_response(resp: requests.Response) -> Union[dict, list]:
    if not resp.ok:
        raise Exception(
            f"Failed to send {resp.request.method} request to {resp.url} "
            f"with HTTP code {resp.status_code} - {http_responses[resp.status_code]}"
        )

    try:
        message = json.loads(resp.text)
    except json.JSONDecodeError as err:
        raise Exception(
            f"Failed to decode response from url {resp.url} with error {err.msg}"
        )

    if not message.get("Success", False):
        raise Exception(
            f"Failed to request branch list from {resp.url} with error "
            f"HTTP code: {message.get('Code','')} - "
            f"ErrorType: {message.get('ErrorType','')} - "
            f"ErrorMessage: {message.get('ErrorMessage','')}"
        )

    data = message["Data"]
    return data


async def handle_response_async(resp: aiohttp.ClientResponse) -> Union[dict, list]:
    if not resp.ok:
        raise Exception(
            f"Failed to send {resp.request.method} request to {resp.url} "
            f"with HTTP code {resp.status_code} - {http_responses[resp.status_code]}"
        )

    content = await resp.text()
    try:
        message = json.loads(content)
    except json.JSONDecodeError as err:
        raise Exception(
            f"Failed to decode response from url {resp.url} with error {err.msg}"
        )

    if not message.get("Success", False):
        raise Exception(
            f"Failed to request branch list from {resp.url} with error "
            f"HTTP code: {message.get('Code','')} - "
            f"ErrorType: {message.get('ErrorType','')} - "
            f"ErrorMessage: {message.get('ErrorMessage','')}"
        )

    data = message["Data"]
    return data

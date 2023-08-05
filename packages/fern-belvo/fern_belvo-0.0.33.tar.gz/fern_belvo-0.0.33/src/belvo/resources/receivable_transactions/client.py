# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import httpx
import pydantic

from ...core.api_error import ApiError
from ...core.jsonable_encoder import jsonable_encoder
from ...environment import BelvoEnvironment
from ...errors.bad_request_error import BadRequestError
from ...errors.internal_server_error import InternalServerError
from ...errors.not_found_error import NotFoundError
from ...errors.precondition_error import PreconditionError
from ...errors.unauthorized_error import UnauthorizedError
from ...types.bad_request_error_body_item import BadRequestErrorBodyItem
from ...types.not_found_error_body import NotFoundErrorBody
from ...types.receivables_transaction import ReceivablesTransaction
from ...types.receivables_transactions_paginated_response import ReceivablesTransactionsPaginatedResponse
from ...types.token_required_response import TokenRequiredResponse
from ...types.unauthorized_error_body import UnauthorizedErrorBody
from ...types.unexpected_error import UnexpectedError

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ReceivableTransactionsClient:
    def __init__(
        self, *, environment: BelvoEnvironment = BelvoEnvironment.PRODUCTION, secret_id: str, secret_password: str
    ):
        self._environment = environment
        self._secret_id = secret_id
        self._secret_password = secret_password

    def list_receivable_transactions(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        omit: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        link: typing.Optional[str] = None,
        account: typing.Optional[str] = None,
        account_in: typing.Optional[str] = None,
        created_at_gt: typing.Optional[str] = None,
        created_at_gte: typing.Optional[str] = None,
        created_at_lt: typing.Optional[str] = None,
        created_at_lte: typing.Optional[str] = None,
        created_at_range: typing.Optional[str] = None,
        link_in: typing.Optional[str] = None,
        value_date: typing.Optional[str] = None,
        value_date_gt: typing.Optional[str] = None,
        value_date_gte: typing.Optional[str] = None,
        value_date_lt: typing.Optional[str] = None,
        value_date_lte: typing.Optional[str] = None,
        value_date_range: typing.Optional[str] = None,
    ) -> ReceivablesTransactionsPaginatedResponse:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", "receivables/transactions"),
            params={
                "page": page,
                "page_size": page_size,
                "omit": omit,
                "fields": fields,
                "link": link,
                "account": account,
                "account__in": account_in,
                "created_at__gt": created_at_gt,
                "created_at__gte": created_at_gte,
                "created_at__lt": created_at_lt,
                "created_at__lte": created_at_lte,
                "created_at__range": created_at_range,
                "link__in": link_in,
                "value_date": value_date,
                "value_date__gt": value_date_gt,
                "value_date__gte": value_date_gte,
                "value_date__lt": value_date_lt,
                "value_date__lte": value_date_lte,
                "value_date__range": value_date_range,
            },
            auth=(self._secret_id, self._secret_password)
            if self._secret_id is not None and self._secret_password is not None
            else None,
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ReceivablesTransactionsPaginatedResponse, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(
                pydantic.parse_obj_as(typing.List[UnauthorizedErrorBody], _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def retrieve_receivable_transactions(
        self,
        *,
        omit: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        link: str,
        date_from: str,
        date_to: str,
        token: typing.Optional[str] = OMIT,
        save_data: typing.Optional[bool] = OMIT,
    ) -> ReceivablesTransaction:
        _request: typing.Dict[str, typing.Any] = {"link": link, "date_from": date_from, "date_to": date_to}
        if token is not OMIT:
            _request["token"] = token
        if save_data is not OMIT:
            _request["save_data"] = save_data
        _response = httpx.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "receivables/transactions"),
            params={"omit": omit, "fields": fields},
            json=jsonable_encoder(_request),
            auth=(self._secret_id, self._secret_password)
            if self._secret_id is not None and self._secret_password is not None
            else None,
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ReceivablesTransaction, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(
                pydantic.parse_obj_as(typing.List[BadRequestErrorBodyItem], _response.json())  # type: ignore
            )
        if _response.status_code == 401:
            raise UnauthorizedError(
                pydantic.parse_obj_as(typing.List[UnauthorizedErrorBody], _response.json())  # type: ignore
            )
        if _response.status_code == 428:
            raise PreconditionError(
                pydantic.parse_obj_as(typing.List[TokenRequiredResponse], _response.json())  # type: ignore
            )
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic.parse_obj_as(typing.List[UnexpectedError], _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def detail_receivable_transaction(
        self, id: str, *, omit: typing.Optional[str] = None, fields: typing.Optional[str] = None
    ) -> ReceivablesTransaction:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", f"receivables/transactions/{id}"),
            params={"omit": omit, "fields": fields},
            auth=(self._secret_id, self._secret_password)
            if self._secret_id is not None and self._secret_password is not None
            else None,
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ReceivablesTransaction, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(
                pydantic.parse_obj_as(typing.List[UnauthorizedErrorBody], _response.json())  # type: ignore
            )
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.List[NotFoundErrorBody], _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def destroy_receivable_transaction(self, id: str) -> None:
        _response = httpx.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._environment.value}/", f"receivables/transactions/{id}"),
            auth=(self._secret_id, self._secret_password)
            if self._secret_id is not None and self._secret_password is not None
            else None,
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        if _response.status_code == 401:
            raise UnauthorizedError(
                pydantic.parse_obj_as(typing.List[UnauthorizedErrorBody], _response.json())  # type: ignore
            )
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.List[NotFoundErrorBody], _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncReceivableTransactionsClient:
    def __init__(
        self, *, environment: BelvoEnvironment = BelvoEnvironment.PRODUCTION, secret_id: str, secret_password: str
    ):
        self._environment = environment
        self._secret_id = secret_id
        self._secret_password = secret_password

    async def list_receivable_transactions(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        omit: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        link: typing.Optional[str] = None,
        account: typing.Optional[str] = None,
        account_in: typing.Optional[str] = None,
        created_at_gt: typing.Optional[str] = None,
        created_at_gte: typing.Optional[str] = None,
        created_at_lt: typing.Optional[str] = None,
        created_at_lte: typing.Optional[str] = None,
        created_at_range: typing.Optional[str] = None,
        link_in: typing.Optional[str] = None,
        value_date: typing.Optional[str] = None,
        value_date_gt: typing.Optional[str] = None,
        value_date_gte: typing.Optional[str] = None,
        value_date_lt: typing.Optional[str] = None,
        value_date_lte: typing.Optional[str] = None,
        value_date_range: typing.Optional[str] = None,
    ) -> ReceivablesTransactionsPaginatedResponse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(f"{self._environment.value}/", "receivables/transactions"),
                params={
                    "page": page,
                    "page_size": page_size,
                    "omit": omit,
                    "fields": fields,
                    "link": link,
                    "account": account,
                    "account__in": account_in,
                    "created_at__gt": created_at_gt,
                    "created_at__gte": created_at_gte,
                    "created_at__lt": created_at_lt,
                    "created_at__lte": created_at_lte,
                    "created_at__range": created_at_range,
                    "link__in": link_in,
                    "value_date": value_date,
                    "value_date__gt": value_date_gt,
                    "value_date__gte": value_date_gte,
                    "value_date__lt": value_date_lt,
                    "value_date__lte": value_date_lte,
                    "value_date__range": value_date_range,
                },
                auth=(self._secret_id, self._secret_password)
                if self._secret_id is not None and self._secret_password is not None
                else None,
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ReceivablesTransactionsPaginatedResponse, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(
                pydantic.parse_obj_as(typing.List[UnauthorizedErrorBody], _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def retrieve_receivable_transactions(
        self,
        *,
        omit: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        link: str,
        date_from: str,
        date_to: str,
        token: typing.Optional[str] = OMIT,
        save_data: typing.Optional[bool] = OMIT,
    ) -> ReceivablesTransaction:
        _request: typing.Dict[str, typing.Any] = {"link": link, "date_from": date_from, "date_to": date_to}
        if token is not OMIT:
            _request["token"] = token
        if save_data is not OMIT:
            _request["save_data"] = save_data
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "POST",
                urllib.parse.urljoin(f"{self._environment.value}/", "receivables/transactions"),
                params={"omit": omit, "fields": fields},
                json=jsonable_encoder(_request),
                auth=(self._secret_id, self._secret_password)
                if self._secret_id is not None and self._secret_password is not None
                else None,
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ReceivablesTransaction, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(
                pydantic.parse_obj_as(typing.List[BadRequestErrorBodyItem], _response.json())  # type: ignore
            )
        if _response.status_code == 401:
            raise UnauthorizedError(
                pydantic.parse_obj_as(typing.List[UnauthorizedErrorBody], _response.json())  # type: ignore
            )
        if _response.status_code == 428:
            raise PreconditionError(
                pydantic.parse_obj_as(typing.List[TokenRequiredResponse], _response.json())  # type: ignore
            )
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic.parse_obj_as(typing.List[UnexpectedError], _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def detail_receivable_transaction(
        self, id: str, *, omit: typing.Optional[str] = None, fields: typing.Optional[str] = None
    ) -> ReceivablesTransaction:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(f"{self._environment.value}/", f"receivables/transactions/{id}"),
                params={"omit": omit, "fields": fields},
                auth=(self._secret_id, self._secret_password)
                if self._secret_id is not None and self._secret_password is not None
                else None,
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ReceivablesTransaction, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(
                pydantic.parse_obj_as(typing.List[UnauthorizedErrorBody], _response.json())  # type: ignore
            )
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.List[NotFoundErrorBody], _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def destroy_receivable_transaction(self, id: str) -> None:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "DELETE",
                urllib.parse.urljoin(f"{self._environment.value}/", f"receivables/transactions/{id}"),
                auth=(self._secret_id, self._secret_password)
                if self._secret_id is not None and self._secret_password is not None
                else None,
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return
        if _response.status_code == 401:
            raise UnauthorizedError(
                pydantic.parse_obj_as(typing.List[UnauthorizedErrorBody], _response.json())  # type: ignore
            )
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.List[NotFoundErrorBody], _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

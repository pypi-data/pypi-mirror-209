# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .payment_transaction import PaymentTransaction


class PaymentsTransactionsPaginatedResponse(pydantic.BaseModel):
    count: typing.Optional[int] = pydantic.Field(description=("The total number of results in your Belvo account.\n"))
    next: typing.Optional[str] = pydantic.Field(
        description=(
            "The URL to next page of results. Each page consists of up to 100 items. If there are not enough results for an additional page, the value is `null`.\n"
            "\n"
            "In our documentation example, we use `{endpoint}` as a placeholder value. In production, this value will be replaced by the actual endpoint you are currently using (for example, `customer` or `bank-accounts`).\n"
        )
    )
    previous: typing.Optional[str] = pydantic.Field(
        description=("The URL to the previous page of results. If there is no previous page, the value is `null`.\n")
    )
    results: typing.Optional[typing.List[PaymentTransaction]] = pydantic.Field(
        description=("Array of transaction objects.\n")
    )

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}

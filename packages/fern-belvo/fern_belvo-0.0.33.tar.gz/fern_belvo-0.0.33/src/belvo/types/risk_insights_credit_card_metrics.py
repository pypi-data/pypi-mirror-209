# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime


class RiskInsightsCreditCardMetrics(pydantic.BaseModel):
    num_accounts: int = pydantic.Field(description=("Number of credit cards accounts associated to the link.\n"))
    sum_credit_limit: typing.Optional[float] = pydantic.Field(description=("Sum total of all credit cards' limits.\n"))
    sum_credit_used: typing.Optional[float] = pydantic.Field(description=("Sum total of all credit used.\n"))

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}

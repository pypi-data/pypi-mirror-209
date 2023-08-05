# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .holder_business_response_pse import HolderBusinessResponsePse


class BeneficiaryBankAccountPse(pydantic.BaseModel):
    id: typing.Optional[str] = pydantic.Field(description=("Belvo's unique ID for the beneficiary bank account.\n"))
    institution: typing.Optional[str] = pydantic.Field(
        description=("Belvo's unique ID for the institution that the bank account is created in.\n")
    )
    number: typing.Optional[str] = pydantic.Field(description=("The bank account number.\n"))
    holder: typing.Optional[HolderBusinessResponsePse]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}

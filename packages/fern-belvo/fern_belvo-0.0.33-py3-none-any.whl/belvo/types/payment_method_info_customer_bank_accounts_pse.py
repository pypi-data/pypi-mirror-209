# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .holder_bank_account_pse import HolderBankAccountPse
from .payment_institution import PaymentInstitution
from .payment_method_information_details_pse import PaymentMethodInformationDetailsPse


class PaymentMethodInfoCustomerBankAccountsPse(pydantic.BaseModel):
    id: typing.Optional[str] = pydantic.Field(
        description=("Belvo's unique ID used to identify the customer’s bank account.\n")
    )
    customer: typing.Optional[str] = pydantic.Field(description=("Belvo's unique ID for the current customer.\n"))
    institution: typing.Optional[PaymentInstitution]
    number: typing.Optional[str] = pydantic.Field(
        description=("The customer's bank account number. This value is obfuscated.\n")
    )
    holder: typing.Optional[HolderBankAccountPse]
    details: typing.Optional[PaymentMethodInformationDetailsPse]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}

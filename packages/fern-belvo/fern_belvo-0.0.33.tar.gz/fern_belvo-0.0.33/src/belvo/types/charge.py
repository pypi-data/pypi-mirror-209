# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .charge_payment_method_details import ChargePaymentMethodDetails
from .charge_status import ChargeStatus
from .enum_payment_link_allowed_payment_method import EnumPaymentLinkAllowedPaymentMethod
from .enum_payment_link_provider import EnumPaymentLinkProvider
from .enum_payments_currency import EnumPaymentsCurrency
from .payment_method_information_pse import PaymentMethodInformationPse
from .payment_transaction import PaymentTransaction


class Charge(pydantic.BaseModel):
    id: str = pydantic.Field(description=("Belvo's unique ID for the current charge.\n"))
    created_at: str = pydantic.Field(
        description=("The ISO-8601 timestamp of when the data point was last updated in Belvo's database.\n")
    )
    created_by: typing.Optional[str] = pydantic.Field(
        description=("Belvo's unique ID for the user that created the charge.\n")
    )
    customer: typing.Optional[str] = pydantic.Field(
        description=("Belvo's unique ID for the customer that the charge was created for.\n")
    )
    failure_code: typing.Optional[str] = pydantic.Field(
        description=("Error code that explains the reason behind a payment being unsuccessful (if applicable).\n")
    )
    failure_message: typing.Optional[str] = pydantic.Field(
        description=("Further information regarding the `failure_code`.\n")
    )
    status: ChargeStatus = pydantic.Field(description=("The current status of the charge.\n"))
    amount: typing.Optional[str] = pydantic.Field(description=("The amount of the charge.\n"))
    currency: typing.Optional[EnumPaymentsCurrency]
    description: typing.Optional[str] = pydantic.Field(description=("The description of the payment.\n"))
    metadata: typing.Dict[str, typing.Any] = pydantic.Field(
        description=(
            "Optional and customizable object where you can provide any additional key-value pairs for your internal purposes. For example, an internal reference number.\n"
            "\n"
            "⚠️ **Note**: You can only provide up to 50 keys (keys can have up to 50 characters each and each value can be up to 500 characters). We do not support nested objects, only ASCII values.\n"
        )
    )
    beneficiary: str = pydantic.Field(
        description=("Belvo's unique ID used to identify the beneficiary’s bank account.\n")
    )
    provider: EnumPaymentLinkProvider
    payment_method_type: typing.Optional[EnumPaymentLinkAllowedPaymentMethod]
    payment_method_details: ChargePaymentMethodDetails
    payment_method_information: PaymentMethodInformationPse
    payment_intent: typing.Optional[str] = pydantic.Field(
        description=("The `payment_intent.id` associated with this charge.\n")
    )
    transactions: typing.Optional[typing.List[PaymentTransaction]] = pydantic.Field(
        description=("An array of Transaction objects relating to the charge.\n")
    )
    updated_at: typing.Optional[str] = pydantic.Field(
        description=("The ISO-8601 timestamp of when the status of the charge was last updated.\n")
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

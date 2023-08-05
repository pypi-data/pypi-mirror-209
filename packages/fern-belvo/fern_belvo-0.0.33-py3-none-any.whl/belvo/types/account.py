# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .accounts_balance import AccountsBalance
from .accounts_credit_data import AccountsCreditData
from .accounts_funds_data import AccountsFundsData
from .accounts_loan_data import AccountsLoanData
from .accounts_receivables_data import AccountsReceivablesData
from .enum_account_category import EnumAccountCategory
from .institution_account import InstitutionAccount


class Account(pydantic.BaseModel):
    id: typing.Optional[str] = pydantic.Field(
        description=("The unique identifier created by Belvo used to reference the current account.\n")
    )
    link: typing.Optional[str] = pydantic.Field(description=("The `link.id` the account belongs to.\n"))
    institution: typing.Optional[InstitutionAccount]
    collected_at: str = pydantic.Field(description=("The ISO-8601 timestamp when the data point was collected.\n"))
    created_at: typing.Optional[str] = pydantic.Field(
        description=("The ISO-8601 timestamp of when the data point was last updated in Belvo's database.\n")
    )
    category: EnumAccountCategory
    balance_type: typing.Optional[str] = pydantic.Field(
        description=(
            "Indicates whether this account is either an `ASSET` or a `LIABILITY`. You can consider the balance of an `ASSET` as being positive, while the balance of a `LIABILITY` as negative.\n"
        )
    )
    type: typing.Optional[str] = pydantic.Field(description=("The account type, as designated by the institution.\n"))
    name: typing.Optional[str] = pydantic.Field(description=("The account name, as given by the institution.\n"))
    number: typing.Optional[str] = pydantic.Field(
        description=("The account number, as designated by the institution.\n")
    )
    balance: AccountsBalance
    currency: typing.Optional[str] = pydantic.Field(
        description=(
            "The currency of the account. For example:\n"
            "- 🇧🇷 BRL (Brazilian Real)\n"
            "- 🇨🇴 COP (Colombian Peso)\n"
            "- 🇲🇽 MXN (Mexican Peso)\n"
            "\n"
            " Please note that other currencies other than in the list above may be returned.\n"
        )
    )
    public_identification_name: typing.Optional[str] = pydantic.Field(
        description=(
            'The public name for the type of identification. For example: `"CLABE"`.\n'
            "\n"
            "ℹ️ For 🇧🇷 Brazilian savings and checking accounts, this field will be `AGENCY/ACCOUNT`.\n"
        )
    )
    public_identification_value: typing.Optional[str] = pydantic.Field(
        description=(
            "The value for the `public_identification_name`.\n"
            "\n"
            "ℹ️ For 🇧🇷 Brazilian savings and checking accounts, this field will be the agency and bank account number, separated by a slash.\n"
            "For example: `0444/45722-0`.\n"
        )
    )
    last_accessed_at: typing.Optional[str] = pydantic.Field(
        description=(
            "The ISO-8601 timestamp of Belvo's most recent successful access to the institution for the given link.\n"
        )
    )
    credit_data: AccountsCreditData
    loan_data: AccountsLoanData
    funds_data: typing.Optional[typing.List[AccountsFundsData]] = pydantic.Field(
        description=("One or more funds that contribute to the the pension account.\n")
    )
    receivables_data: typing.Optional[AccountsReceivablesData]
    bank_product_id: typing.Optional[str] = pydantic.Field(
        description=(
            "*This field has been deprecated.*\n" "\n" "*The institution's product ID for the account type.*\n"
        )
    )
    internal_identification: typing.Optional[str] = pydantic.Field(
        description=(
            "*This field has been deprecated.*\n" "\n" "*The institution's internal identification for the account.*\n"
        )
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

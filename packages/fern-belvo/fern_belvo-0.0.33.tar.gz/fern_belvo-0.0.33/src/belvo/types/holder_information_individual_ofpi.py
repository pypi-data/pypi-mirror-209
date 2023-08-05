# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .enum_customer_identifier_type_ofpi import EnumCustomerIdentifierTypeOfpi


class HolderInformationIndividualOfpi(pydantic.BaseModel):
    """
    Additional information about the bank account holder required in order to create the account for OFPI.
    """

    first_name: str = pydantic.Field(description=("The bank account holder's first name.\n"))
    last_name: str = pydantic.Field(description=("The bank account holder's last name.\n"))
    identifier_type: EnumCustomerIdentifierTypeOfpi
    identifier: str = pydantic.Field(description=("The document number of the customer's ID.\n"))

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}

# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime


class TaxStatusObligationsDian(pydantic.BaseModel):
    """
    Details regarding a business's obligations.

    ℹ️ For non-business accounts, this field will return empty.
    """

    obligation: typing.Optional[str] = pydantic.Field(
        description=("**Note**: This field is not applicable for DIAN Colombia and will return `null`.\n")
    )
    expiration: typing.Optional[str] = pydantic.Field(
        description=("**Note**: This field is not applicable for DIAN Colombia and will return `null`.\n")
    )
    initial_date: typing.Optional[str] = pydantic.Field(
        description=("**Note**: This field is not applicable for DIAN Colombia and will return `null`.\n")
    )
    end_date: typing.Optional[str] = pydantic.Field(
        description=("**Note**: This field is not applicable for DIAN Colombia and will return `null`.\n")
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

# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime


class DocumentIdBusiness(pydantic.BaseModel):
    """
    Object containing information about the ID document of the tax payer.
    """

    document_type: str = pydantic.Field(description=("The type of ID document.\n"))
    document_number: str = pydantic.Field(description=("The number of the ID document.\n"))

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}

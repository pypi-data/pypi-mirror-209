# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime


class TaxReturnsYearlyRequest(pydantic.BaseModel):
    """
    Request body for yearly tax returns
    """

    link: str = pydantic.Field(description=("The fiscal `link.id` you want specific tax return information for.\n"))
    attach_pdf: typing.Optional[bool] = pydantic.Field(
        description=("When this is set to `true`, you will receive the PDF as a binary string in the response.\n")
    )
    save_data: typing.Optional[bool] = pydantic.Field(
        description=(
            "Indicates whether or not to persist the data in Belvo. By default, this is set to `true` and we return a 201 Created response.\n"
            "When set to `false`, the data won't be persisted and we return a 200 OK response.\n"
        )
    )
    type: str = pydantic.Field(
        description=(
            "The type of tax return to return. For yearly tax returns this must be set to `yearly`.\n"
            "\n"
            "By default, Belvo returns the yearly (annual) tax returns.\n"
        )
    )
    year_from: str = pydantic.Field(
        description=("The starting year you want to get tax returns for, in `YYYY` format.\n")
    )
    year_to: str = pydantic.Field(
        description=("The year you want to stop getting tax returns for, in `YYYY` format.\n")
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

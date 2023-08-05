# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime


class InstitutionDownError(pydantic.BaseModel):
    """
    This error occurs when the institution's website that you're trying to access is down due to maintenance or other issues, which means Belvo is unable to create new links or retrieve new data.
    """

    code: typing.Optional[str] = pydantic.Field(
        description=(
            "A unique error code (`institution_down`) that allows you to classify and handle the error programmatically.\n"
            "\n"
            'ℹ️ Check our DevPortal for more information on how to handle <a href="https://developers.belvo.com/docs/belvo-api-errors#400-institution_down" target="_blank">400 institution_down errors</a>.\n'
        )
    )
    message: typing.Optional[str] = pydantic.Field(
        description=(
            "A short description of the error.\n"
            "\n"
            "For `institution_down` errors, the description is:\n"
            "\n"
            "  - `The financial institution is down, try again later`.\n"
        )
    )
    request_id: typing.Optional[str] = pydantic.Field(
        description=(
            "A 32-character unique ID of the request (matching a regex pattern of: `[a-f0-9]{32}`). Provide this ID when contacting the Belvo support team to accelerate investigations.\n"
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

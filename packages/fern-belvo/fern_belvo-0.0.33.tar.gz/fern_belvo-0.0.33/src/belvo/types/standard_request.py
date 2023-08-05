# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime


class StandardRequest(pydantic.BaseModel):
    link: str = pydantic.Field(description=("The `link.id` that you want to get information for.\n"))
    token: typing.Optional[str] = pydantic.Field(description=("The OTP token generated by the bank.\n"))
    save_data: typing.Optional[bool] = pydantic.Field(
        description=(
            "Indicates whether or not to persist the data in Belvo. By default, this is set to `true` and we return a 201 Created response.\n"
            "When set to `false`, the data won't be persisted and we return a 200 OK response.\n"
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

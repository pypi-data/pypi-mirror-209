# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .document_id_individual import DocumentIdIndividual
from .reporting_id import ReportingId


class TaxPayerInformationIndividual(pydantic.BaseModel):
    """
    Object containing information about the tax payer.
    """

    first_last_name: str = pydantic.Field(description=("The tax payer's first last name.\n"))
    second_last_name: str = pydantic.Field(description=("The tax payer's second last name.\n"))
    first_name: str = pydantic.Field(description=("The tax payer's first name.\n"))
    other_names: str = pydantic.Field(description=("Additional names of the tax payer.\n"))
    main_economic_activity: str = pydantic.Field(
        description=("The main economic activity the tax payer is involved in.\n")
    )
    document_id: DocumentIdIndividual
    reporting_id: ReportingId

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}

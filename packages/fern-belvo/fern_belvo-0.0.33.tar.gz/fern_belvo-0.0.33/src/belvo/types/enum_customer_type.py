# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class EnumCustomerType(str, enum.Enum):
    """
    The type of customer. Can be either:

      - `INDIVIDUAL`
      - `BUSINESS`


    **Notes:** For 🇨🇴 Colombia's PSE, you can only create customers of type `INDIVIDUAL`.
    """

    INDIVIDUAL = "INDIVIDUAL"
    BUSINESS = "BUSINESS"

    def visit(self, individual: typing.Callable[[], T_Result], business: typing.Callable[[], T_Result]) -> T_Result:
        if self is EnumCustomerType.INDIVIDUAL:
            return individual()
        if self is EnumCustomerType.BUSINESS:
            return business()

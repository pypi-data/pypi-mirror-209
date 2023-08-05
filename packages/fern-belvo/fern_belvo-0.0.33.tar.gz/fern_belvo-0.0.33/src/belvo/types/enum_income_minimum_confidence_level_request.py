# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class EnumIncomeMinimumConfidenceLevelRequest(str, enum.Enum):
    """
    The minimum confidence level of the incomes you want to get information for.

    You can send through one of the following values:

      - `HIGH`
      - `MEDIUM`
      - `LOW`
    """

    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"

    def visit(
        self,
        high: typing.Callable[[], T_Result],
        medium: typing.Callable[[], T_Result],
        low: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EnumIncomeMinimumConfidenceLevelRequest.HIGH:
            return high()
        if self is EnumIncomeMinimumConfidenceLevelRequest.MEDIUM:
            return medium()
        if self is EnumIncomeMinimumConfidenceLevelRequest.LOW:
            return low()

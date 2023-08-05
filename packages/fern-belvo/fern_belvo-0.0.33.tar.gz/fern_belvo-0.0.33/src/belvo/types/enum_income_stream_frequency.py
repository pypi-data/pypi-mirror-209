# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class EnumIncomeStreamFrequency(str, enum.Enum):
    """
    How often the income is received.

    We return one of the following enum values:

      - `MONTHLY` - For transactions that occur once per month.
      - `FORTNIGHTLY` - For transactions that occur once every two weeks.
      - `WEEKLY` - For transactions that occur once per week.
      - `IRREGULAR` - For transactions that do not occur on a defined frequency pattern.
      - `SINGLE` - For transactions that occur only once and do not repeat.
    """

    MONTHLY = "MONTHLY"
    FORTNIGHTLY = "FORTNIGHTLY"
    WEEKLY = "WEEKLY"
    IRREGULAR = "IRREGULAR"
    SINGLE = "SINGLE"

    def visit(
        self,
        monthly: typing.Callable[[], T_Result],
        fortnightly: typing.Callable[[], T_Result],
        weekly: typing.Callable[[], T_Result],
        irregular: typing.Callable[[], T_Result],
        single: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EnumIncomeStreamFrequency.MONTHLY:
            return monthly()
        if self is EnumIncomeStreamFrequency.FORTNIGHTLY:
            return fortnightly()
        if self is EnumIncomeStreamFrequency.WEEKLY:
            return weekly()
        if self is EnumIncomeStreamFrequency.IRREGULAR:
            return irregular()
        if self is EnumIncomeStreamFrequency.SINGLE:
            return single()

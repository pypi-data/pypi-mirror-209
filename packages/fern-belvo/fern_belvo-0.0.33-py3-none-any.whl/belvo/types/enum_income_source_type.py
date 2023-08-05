# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class EnumIncomeSourceType(str, enum.Enum):
    """
    The type of source we generate income insights from.
    We return one of the following enum values:

      - `BANK`
    """

    BANK = "BANK"

    def visit(self, bank: typing.Callable[[], T_Result]) -> T_Result:
        if self is EnumIncomeSourceType.BANK:
            return bank()

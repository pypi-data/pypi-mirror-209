# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class EnumTaxRetentionReceiverNationality(str, enum.Enum):
    NATIONAL = "NATIONAL"
    FOREIGN = "FOREIGN"

    def visit(self, national: typing.Callable[[], T_Result], foreign: typing.Callable[[], T_Result]) -> T_Result:
        if self is EnumTaxRetentionReceiverNationality.NATIONAL:
            return national()
        if self is EnumTaxRetentionReceiverNationality.FOREIGN:
            return foreign()

# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class EnumCustomerIdentifierTypePse(str, enum.Enum):
    """
    The customer's ID document type.

    - 🇨🇴 Colombia options: `CC`, `PP`, `CE`, `TI`, or `NIT`.
    """

    CC = "CC"
    PP = "PP"
    CE = "CE"
    TI = "TI"
    NIT = "NIT"

    def visit(
        self,
        cc: typing.Callable[[], T_Result],
        pp: typing.Callable[[], T_Result],
        ce: typing.Callable[[], T_Result],
        ti: typing.Callable[[], T_Result],
        nit: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EnumCustomerIdentifierTypePse.CC:
            return cc()
        if self is EnumCustomerIdentifierTypePse.PP:
            return pp()
        if self is EnumCustomerIdentifierTypePse.CE:
            return ce()
        if self is EnumCustomerIdentifierTypePse.TI:
            return ti()
        if self is EnumCustomerIdentifierTypePse.NIT:
            return nit()

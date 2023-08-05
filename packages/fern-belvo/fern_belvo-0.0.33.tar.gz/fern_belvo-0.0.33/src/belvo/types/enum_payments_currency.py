# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class EnumPaymentsCurrency(str, enum.Enum):
    """
    The currency of the amount paid.


      - 🇧🇷 BRL (Brazilian Real)
      - 🇨🇴 COP (Colombian Peso)
    """

    BRL = "BRL"
    COP = "COP"

    def visit(self, brl: typing.Callable[[], T_Result], cop: typing.Callable[[], T_Result]) -> T_Result:
        if self is EnumPaymentsCurrency.BRL:
            return brl()
        if self is EnumPaymentsCurrency.COP:
            return cop()

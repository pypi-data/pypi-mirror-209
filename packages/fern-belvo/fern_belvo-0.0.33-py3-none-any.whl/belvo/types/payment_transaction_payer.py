# This file was auto-generated by Fern from our API Definition.

import typing

from .transaction_bank_account_ofpi import TransactionBankAccountOfpi
from .transaction_bank_account_pse import TransactionBankAccountPse

PaymentTransactionPayer = typing.Union[TransactionBankAccountOfpi, TransactionBankAccountPse]

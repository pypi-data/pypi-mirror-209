# This file was auto-generated by Fern from our API Definition.

import typing

from .create_customer_ofpi import CreateCustomerOfpi
from .create_customer_pse import CreateCustomerPse

CreateCustomerRequest = typing.Union[CreateCustomerOfpi, CreateCustomerPse]

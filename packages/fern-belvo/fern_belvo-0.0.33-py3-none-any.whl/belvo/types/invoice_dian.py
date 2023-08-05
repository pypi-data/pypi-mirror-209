# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .enum_invoice_dian_invoice_type import EnumInvoiceDianInvoiceType
from .enum_invoice_dian_payment_method import EnumInvoiceDianPaymentMethod
from .enum_invoice_type import EnumInvoiceType
from .invoice_detail_dian import InvoiceDetailDian
from .invoice_sender_details_dian import InvoiceSenderDetailsDian
from .invoice_warnings_dian import InvoiceWarningsDian
from .invoices_payments_dian import InvoicesPaymentsDian
from .invoices_payroll_dian import InvoicesPayrollDian
from .invoices_receiver_details_dian import InvoicesReceiverDetailsDian


class InvoiceDian(pydantic.BaseModel):
    id: typing.Optional[str] = pydantic.Field(description=("Belvo's unique identifier for the current invoice.\n"))
    link: typing.Optional[str] = pydantic.Field(description=("The `link.id` the invoice belongs to.\n"))
    collected_at: typing.Optional[str] = pydantic.Field(
        description=("The ISO-8601 timestamp when the data point was collected.\n")
    )
    created_at: typing.Optional[str] = pydantic.Field(
        description=("The ISO-8601 timestamp of when the data point was last updated in Belvo's database.\n")
    )
    invoice_identification: typing.Optional[str] = pydantic.Field(
        description=("The fiscal institution's unique ID for the invoice.\n")
    )
    invoice_date: typing.Optional[str] = pydantic.Field(description=("The date of the invoice.\n"))
    status: typing.Optional[str] = pydantic.Field(
        description=(
            "The status of the invoice. Can be one of:\n"
            "\n"
            "  - *Vigente* (valid)\n"
            "  - *Cancelado* (cancelled)\n"
            "  - *Aprobado* (approved)\n"
        )
    )
    expiration_date: typing.Optional[str] = pydantic.Field(
        description=(
            "Indicates when the invoice is set to expire.\n"
            "\n"
            "For example: If the invoice is paid in installments, this field indicates the date when the installment is to be paid.\n"
        )
    )
    invoice_type: EnumInvoiceDianInvoiceType
    type: EnumInvoiceType
    sender_id: typing.Optional[str] = pydantic.Field(description=("The fiscal ID of the invoice sender.\n"))
    sender_name: typing.Optional[str] = pydantic.Field(description=("The name of the invoice sender.\n"))
    sender_details: typing.Optional[InvoiceSenderDetailsDian]
    sender_tax_fraud_status: typing.Optional[str] = pydantic.Field(
        description=(
            "Indicates whether or not the sender is on a tax fraud list for having submitted incorrect data, having outstanding payments, or having conducted business that is in violation of the fiscal institution's regulations.\n"
            "**Note**: This field is not applicable for DIAN Colombia and will return `null`.\n"
        )
    )
    receiver_id: typing.Optional[str] = pydantic.Field(description=("The fiscal ID of the invoice receiver.\n"))
    receiver_name: typing.Optional[str] = pydantic.Field(description=("The name of the invoice receiver.\n"))
    receiver_details: typing.Optional[InvoicesReceiverDetailsDian]
    receiver_tax_fraud_status: typing.Optional[str] = pydantic.Field(
        description=("**Note**: This field is not applicable for DIAN Colombia and will return `null`.\n")
    )
    cancelation_status: typing.Optional[str] = pydantic.Field(
        description=("**Note**: This field is not applicable for DIAN Colombia and will return `null`.\n")
    )
    cancelation_update_date: typing.Optional[str] = pydantic.Field(
        description=("**Note**: This field is not applicable for DIAN Colombia and will return `null`.\n")
    )
    certification_date: typing.Optional[str] = pydantic.Field(
        description=("**Note**: This field is not applicable for DIAN Colombia and will return `null`.\n")
    )
    certification_authority: typing.Optional[str] = pydantic.Field(
        description=("**Note**: This field is not applicable for DIAN Colombia and will return `null`.\n")
    )
    payment_type: typing.Optional[str] = pydantic.Field(
        description=(
            "The payment type code used for this invoice, as defined by the country legal entity.\n"
            "\n"
            "For detailed information regarding DIAN's payment types, please see their [official PDF](https://www.dian.gov.co/impuestos/factura-electronica/Documents/Anexo_tecnico_factura_electronica_vr_1_7_2020.pdf).\n"
        )
    )
    payment_type_description: typing.Optional[str] = pydantic.Field(
        description=("The description of the payment method used for this invoice.\n")
    )
    payment_method: typing.Optional[EnumInvoiceDianPaymentMethod]
    payment_method_description: typing.Optional[str] = pydantic.Field(
        description=("The description of the payment method used for this invoice.\n")
    )
    usage: typing.Optional[str] = pydantic.Field(
        description=("**Note**: This field is not applicable for DIAN Colombia and will return `null`.\n")
    )
    version: typing.Optional[str] = pydantic.Field(
        description=("**Note**: This field is not applicable for DIAN Colombia and will return `null`.\n")
    )
    place_of_issue: typing.Optional[str] = pydantic.Field(
        description=("**Note**: This field is not applicable for DIAN Colombia and will return `null`.\n")
    )
    invoice_details: typing.List[InvoiceDetailDian] = pydantic.Field(
        description=("**Note**: This field is not applicable for DIAN Colombia and will return `null`.\n")
    )
    currency: typing.Optional[str] = pydantic.Field(
        description=(
            "The currency of the invoice. For example:\n"
            "\n"
            " - 🇧🇷 BRL (Brazilian Real)\n"
            " - 🇨🇴 COP (Colombian Peso)\n"
            " - 🇲🇽 MXN (Mexican Peso)\n"
            " - 🇺🇸 USD (United States Dollar)\n"
        )
    )
    subtotal_amount: typing.Optional[float] = pydantic.Field(
        description=("The pretax amount of this invoice (sum of each item's `pre_tax_amount`).\n")
    )
    exchange_rate: typing.Optional[float] = pydantic.Field(
        description=("The exchange rate used in this invoice for the currency.\n")
    )
    tax_amount: typing.Optional[float] = pydantic.Field(
        description=("The amount of tax for this invoice (sum of each item's `tax_amount`).\n")
    )
    discount_amount: typing.Optional[float] = pydantic.Field(
        description=("The total amount discounted in this invoice.\n")
    )
    total_amount: typing.Optional[float] = pydantic.Field(
        description=("The total amount of the invoice (`subtotal_amount` + `tax_amount` - `discount_amount`)\n")
    )
    payments: typing.List[InvoicesPaymentsDian] = pydantic.Field(
        description=("**Note**: This field is not applicable for DIAN Colombia and will return `null`.\n")
    )
    payroll: InvoicesPayrollDian
    folio: typing.Optional[str] = pydantic.Field(
        description=("**Note**: This field is not applicable for DIAN Colombia and will return `null`.\n")
    )
    xml: typing.Optional[str] = pydantic.Field(
        description=("**Note**: This field is not applicable for DIAN Colombia and will return `null`.\n")
    )
    warnings: typing.Optional[InvoiceWarningsDian]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}

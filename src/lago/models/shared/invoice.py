"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import invoiceobject as shared_invoiceobject
from dataclasses_json import Undefined, dataclass_json
from lago import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Invoice:
    r"""Successful response"""
    
    invoice: shared_invoiceobject.InvoiceObject = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoice') }})
    
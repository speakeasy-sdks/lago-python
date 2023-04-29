"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from lago import utils

class FeeUpdateInputInvoicePaymentStatusEnum(str, Enum):
    r"""Status"""
    PENDING = 'pending'
    SUCCEEDED = 'succeeded'
    FAILED = 'failed'
    REFUNDED = 'refunded'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class FeeUpdateInputInvoice:
    
    payment_status: FeeUpdateInputInvoicePaymentStatusEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payment_status') }})
    r"""Status"""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class FeeUpdateInput:
    r"""Payload to update a fee"""
    
    invoice: FeeUpdateInputInvoice = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoice') }})
    
"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils

class CreditObjectInvoicePaymentStatusEnum(str, Enum):
    PENDING = 'pending'
    SUCCEEDED = 'succeeded'
    FAILED = 'failed'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreditObjectInvoice:
    
    lago_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lago_id') }})  
    payment_status: CreditObjectInvoicePaymentStatusEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payment_status') }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreditObjectItem:
    
    code: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('code') }})  
    lago_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lago_id') }})  
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})  
    type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreditObject:
    
    amount_cents: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount_cents') }})  
    amount_currency: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount_currency') }})  
    invoice: CreditObjectInvoice = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoice') }})  
    item: CreditObjectItem = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('item') }})  
    lago_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lago_id') }})  
    
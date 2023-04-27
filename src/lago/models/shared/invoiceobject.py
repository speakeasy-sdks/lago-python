"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import creditobject as shared_creditobject
from ..shared import customerobject as shared_customerobject
from ..shared import feeobject as shared_feeobject
from ..shared import invoicemetadataobject as shared_invoicemetadataobject
from ..shared import subscriptionobject as shared_subscriptionobject
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from lago import utils
from marshmallow import fields
from typing import Optional

class InvoiceObjectInvoiceTypeEnum(str, Enum):
    SUBSCRIPTION = 'subscription'
    ADD_ON = 'add_on'
    CREDIT = 'credit'

class InvoiceObjectPaymentStatusEnum(str, Enum):
    PENDING = 'pending'
    SUCCEEDED = 'succeeded'
    FAILED = 'failed'

class InvoiceObjectStatusEnum(str, Enum):
    DRAFT = 'draft'
    FINALIZED = 'finalized'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class InvoiceObject:
    
    amount_cents: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount_cents') }})  
    amount_currency: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount_currency') }})  
    charges_from_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('charges_from_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})  
    credit_amount_cents: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credit_amount_cents') }})  
    credit_amount_currency: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credit_amount_currency') }})  
    credits: list[shared_creditobject.CreditObject] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credits') }})  
    customer: shared_customerobject.CustomerObject = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customer') }})  
    fees: list[shared_feeobject.FeeObject] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fees') }})  
    issuing_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('issuing_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})  
    lago_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lago_id') }})  
    legacy: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('legacy') }})  
    number: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('number') }})  
    payment_status: InvoiceObjectPaymentStatusEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payment_status') }})  
    sequential_id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sequential_id') }})  
    status: InvoiceObjectStatusEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})  
    subscriptions: list[shared_subscriptionobject.SubscriptionObject] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subscriptions') }})  
    total_amount_cents: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total_amount_cents') }})  
    total_amount_currency: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total_amount_currency') }})  
    vat_amount_cents: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('vat_amount_cents') }})  
    vat_amount_currency: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('vat_amount_currency') }})  
    file_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('file_url'), 'exclude': lambda f: f is None }})  
    invoice_type: Optional[InvoiceObjectInvoiceTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoice_type'), 'exclude': lambda f: f is None }})  
    metadata: Optional[list[shared_invoicemetadataobject.InvoiceMetadataObject]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is None }})  
    
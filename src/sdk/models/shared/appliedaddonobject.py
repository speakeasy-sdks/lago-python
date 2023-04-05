"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from marshmallow import fields
from sdk import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AppliedAddOnObject:
    
    add_on_code: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('add_on_code') }})  
    amount_cents: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount_cents') }})  
    amount_currency: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount_currency') }})  
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})  
    external_customer_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('external_customer_id') }})  
    lago_add_on_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lago_add_on_id') }})  
    lago_customer_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lago_customer_id') }})  
    lago_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lago_id') }})  
    
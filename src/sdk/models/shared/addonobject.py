"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from marshmallow import fields
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AddOnObject:
    
    amount_cents: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount_cents') }})  
    amount_currency: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount_currency') }})  
    code: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('code') }})  
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})  
    lago_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lago_id') }})  
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})  
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})  
    
"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from lago import utils
from marshmallow import fields
from typing import Optional

class WalletObjectStatusEnum(str, Enum):
    r"""Status"""
    ACTIVE = 'active'
    TERMINATED = 'terminated'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class WalletObject:
    
    balance: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('balance') }})  
    consumed_credits: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('consumed_credits') }})  
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})  
    credits_balance: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credits_balance') }})  
    currency: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currency') }})  
    external_customer_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('external_customer_id') }})  
    lago_customer_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lago_customer_id') }})  
    lago_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lago_id') }})  
    rate_amount: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rate_amount') }})  
    status: WalletObjectStatusEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""Status"""  
    expiration_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expiration_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})  
    last_balance_sync_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('last_balance_sync_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})  
    last_consumed_credit_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('last_consumed_credit_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})  
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})  
    terminated_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('terminated_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})  
    
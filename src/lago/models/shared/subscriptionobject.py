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

class SubscriptionObjectBillingTimeEnum(str, Enum):
    r"""Billing time"""
    CALENDAR = 'calendar'
    ANNIVERSARY = 'anniversary'

class SubscriptionObjectStatusEnum(str, Enum):
    r"""Subscription status"""
    ACTIVE = 'active'
    PENDING = 'pending'
    TERMINATED = 'terminated'
    CANCELED = 'canceled'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SubscriptionObject:
    
    billing_time: SubscriptionObjectBillingTimeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('billing_time') }})
    r"""Billing time"""  
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})  
    external_customer_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('external_customer_id') }})  
    external_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('external_id') }})  
    lago_customer_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lago_customer_id') }})  
    lago_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lago_id') }})  
    plan_code: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('plan_code') }})  
    started_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('started_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})  
    status: SubscriptionObjectStatusEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""Subscription status"""  
    subscription_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subscription_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})  
    canceled_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('canceled_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})  
    downgrade_plan_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('downgrade_plan_date'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})  
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})  
    next_plan_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('next_plan_code'), 'exclude': lambda f: f is None }})  
    previous_plan_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('previous_plan_code'), 'exclude': lambda f: f is None }})  
    terminated_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('terminated_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})  
    
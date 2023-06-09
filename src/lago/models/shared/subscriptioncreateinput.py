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

class SubscriptionCreateInputSubscriptionBillingTimeEnum(str, Enum):
    r"""Billing time"""
    CALENDAR = 'calendar'
    ANNIVERSARY = 'anniversary'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SubscriptionCreateInputSubscription:
    
    external_customer_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('external_customer_id') }})  
    external_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('external_id') }})  
    plan_code: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('plan_code') }})  
    billing_time: Optional[SubscriptionCreateInputSubscriptionBillingTimeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('billing_time'), 'exclude': lambda f: f is None }})
    r"""Billing time"""  
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})  
    subscription_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subscription_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SubscriptionCreateInput:
    r"""Subscription payload"""
    
    subscription: SubscriptionCreateInputSubscription = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subscription') }})  
    
"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import chargeobject as shared_chargeobject
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from lago import utils
from marshmallow import fields
from typing import Optional

class PlanObjectIntervalEnum(str, Enum):
    r"""Plan interval"""
    WEEKLY = 'weekly'
    MONTHLY = 'monthly'
    YEARLY = 'yearly'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PlanObject:
    
    active_subscriptions_count: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('active_subscriptions_count') }})

    amount_cents: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount_cents') }})

    amount_currency: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount_currency') }})

    code: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('code') }})

    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})

    draft_invoices_count: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('draft_invoices_count') }})

    interval: PlanObjectIntervalEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('interval') }})

    r"""Plan interval"""
    lago_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lago_id') }})

    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})

    bill_charges_monthly: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bill_charges_monthly'), 'exclude': lambda f: f is None }})

    charges: Optional[list[shared_chargeobject.ChargeObject]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('charges'), 'exclude': lambda f: f is None }})

    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})

    pay_in_advance: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pay_in_advance'), 'exclude': lambda f: f is None }})

    trial_period: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('trial_period'), 'exclude': lambda f: f is None }})

    
"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import billablemetricgroup as shared_billablemetricgroup
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from lago import utils
from marshmallow import fields
from typing import Optional

class BillableMetricObjectAggregationTypeEnum(str, Enum):
    r"""Aggregation type"""
    COUNT_AGG = 'count_agg'
    SUM_AGG = 'sum_agg'
    MAX_AGG = 'max_agg'
    UNIQUE_COUNT_AGG = 'unique_count_agg'
    RECURRING_COUNT_AGG = 'recurring_count_agg'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BillableMetricObject:
    
    active_subscriptions_count: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('active_subscriptions_count') }})
    aggregation_type: BillableMetricObjectAggregationTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('aggregation_type') }})
    r"""Aggregation type"""
    code: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('code') }})
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    draft_invoices_count: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('draft_invoices_count') }})
    lago_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lago_id') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    plans_count: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('plans_count') }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    field_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('field_name'), 'exclude': lambda f: f is None }})
    group: Optional[shared_billablemetricgroup.BillableMetricGroup] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('group'), 'exclude': lambda f: f is None }})
    
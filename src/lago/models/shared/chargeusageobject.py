"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from lago import utils
from typing import Optional

class ChargeUsageObjectBillableMetricAggregationTypeEnum(str, Enum):
    r"""Aggregation type"""
    COUNT_AGG = 'count_agg'
    SUM_AGG = 'sum_agg'
    MAX_AGG = 'max_agg'
    UNIQUE_COUNT_AGG = 'unique_count_agg'
    RECURRING_COUNT_AGG = 'recurring_count_agg'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ChargeUsageObjectBillableMetric:
    
    aggregation_type: Optional[ChargeUsageObjectBillableMetricAggregationTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('aggregation_type'), 'exclude': lambda f: f is None }})
    r"""Aggregation type"""
    code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('code'), 'exclude': lambda f: f is None }})
    lago_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lago_id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    
class ChargeUsageObjectChargeChargeModelEnum(str, Enum):
    r"""Charge model type"""
    STANDARD = 'standard'
    GRADUATED = 'graduated'
    PACKAGE = 'package'
    PERCENTAGE = 'percentage'
    VOLUME = 'volume'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ChargeUsageObjectCharge:
    
    charge_model: Optional[ChargeUsageObjectChargeChargeModelEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('charge_model'), 'exclude': lambda f: f is None }})
    r"""Charge model type"""
    instant: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('instant'), 'exclude': lambda f: f is None }})
    lago_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lago_id'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ChargeUsageObjectGroups:
    
    amount_cents: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount_cents'), 'exclude': lambda f: f is None }})
    key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('key'), 'exclude': lambda f: f is None }})
    lago_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lago_id'), 'exclude': lambda f: f is None }})
    units: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('units'), 'exclude': lambda f: f is None }})
    value: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ChargeUsageObject:
    
    amount_cents: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount_cents') }})
    amount_currency: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount_currency') }})
    billable_metric: ChargeUsageObjectBillableMetric = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('billable_metric') }})
    charge: ChargeUsageObjectCharge = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('charge') }})
    groups: list[ChargeUsageObjectGroups] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('groups') }})
    units: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('units') }})
    
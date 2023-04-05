"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import grouppropertiesobject as shared_grouppropertiesobject
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from sdk import utils
from typing import Any, Optional

class ChargeObjectChargeModelEnum(str, Enum):
    r"""Charge model type"""
    STANDARD = 'standard'
    GRADUATED = 'graduated'
    PACKAGE = 'package'
    PERCENTAGE = 'percentage'
    VOLUME = 'volume'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ChargeObject:
    
    billable_metric_code: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('billable_metric_code') }})  
    charge_model: ChargeObjectChargeModelEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('charge_model') }})
    r"""Charge model type"""  
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})  
    lago_billable_metric_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lago_billable_metric_id') }})  
    lago_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lago_id') }})  
    group_properties: Optional[list[shared_grouppropertiesobject.GroupPropertiesObject]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('group_properties'), 'exclude': lambda f: f is None }})  
    instant: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('instant'), 'exclude': lambda f: f is None }})  
    properties: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('properties'), 'exclude': lambda f: f is None }})  
    
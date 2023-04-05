"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BatchEventInputEvent:
    
    code: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('code') }})  
    external_subscription_ids: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('external_subscription_ids') }})  
    transaction_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transaction_id') }})  
    external_customer_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('external_customer_id'), 'exclude': lambda f: f is None }})  
    properties: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('properties'), 'exclude': lambda f: f is None }})  
    timestamp: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timestamp'), 'exclude': lambda f: f is None }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BatchEventInput:
    r"""Batch events payload"""
    
    event: BatchEventInputEvent = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('event') }})  
    
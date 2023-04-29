"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import customerusageobject as shared_customerusageobject
from dataclasses_json import Undefined, dataclass_json
from lago import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CustomerUsage:
    r"""Successful response"""
    
    customer_usage: shared_customerusageobject.CustomerUsageObject = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customer_usage') }})
    
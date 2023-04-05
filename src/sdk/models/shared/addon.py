"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import addonobject as shared_addonobject
from dataclasses_json import Undefined, dataclass_json
from sdk import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AddOn:
    r"""Successful response"""
    
    add_on: shared_addonobject.AddOnObject = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('add_on') }})  
    
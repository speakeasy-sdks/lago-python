"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import feeobject as shared_feeobject
from dataclasses_json import Undefined, dataclass_json
from lago import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Fees:
    r"""Successful response"""
    
    fees: list[shared_feeobject.FeeObject] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fees') }})

    
"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import appliedcouponobject as shared_appliedcouponobject
from dataclasses_json import Undefined, dataclass_json
from lago import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AppliedCoupon:
    r"""Successful response"""
    
    applied_coupon: shared_appliedcouponobject.AppliedCouponObject = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('applied_coupon') }})
    
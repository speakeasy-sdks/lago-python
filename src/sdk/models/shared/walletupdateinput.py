"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from marshmallow import fields
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class WalletUpdateInputWallet:
    
    expiration_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expiration_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})  
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class WalletUpdateInput:
    r"""Update an existing wallet"""
    
    wallet: WalletUpdateInputWallet = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('wallet') }})  
    
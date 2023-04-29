"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import walletobject as shared_walletobject
from dataclasses_json import Undefined, dataclass_json
from lago import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Wallets:
    r"""Successful response"""
    
    wallets: list[shared_walletobject.WalletObject] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('wallets') }})
    
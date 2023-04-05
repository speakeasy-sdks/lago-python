"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import wallettransactionobject as shared_wallettransactionobject
from dataclasses_json import Undefined, dataclass_json
from sdk import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class WalletTransactions:
    r"""Successful response"""
    
    wallet_transactions: list[shared_wallettransactionobject.WalletTransactionObject] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('wallet_transactions') }})  
    
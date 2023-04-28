"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from lago import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class WalletTransactionInputWalletTransaction:
    
    wallet_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('wallet_id') }})

    granted_credits: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('granted_credits'), 'exclude': lambda f: f is None }})

    paid_credits: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('paid_credits'), 'exclude': lambda f: f is None }})

    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class WalletTransactionInput:
    r"""Wallet transaction payload"""
    
    wallet_transaction: WalletTransactionInputWalletTransaction = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('wallet_transaction') }})

    
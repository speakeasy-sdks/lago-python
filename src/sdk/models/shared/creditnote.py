"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import creditnoteobject as shared_creditnoteobject
from dataclasses_json import Undefined, dataclass_json
from sdk import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreditNote:
    r"""Successful response"""
    
    credit_note: shared_creditnoteobject.CreditNoteObject = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credit_note') }})  
    
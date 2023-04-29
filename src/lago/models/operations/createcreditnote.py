"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import apiresponsebadrequest as shared_apiresponsebadrequest
from ..shared import apiresponseunauthorized as shared_apiresponseunauthorized
from ..shared import apiresponseunprocessableentity as shared_apiresponseunprocessableentity
from ..shared import creditnote as shared_creditnote
from typing import Optional


@dataclasses.dataclass
class CreateCreditNoteResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    api_response_bad_request: Optional[shared_apiresponsebadrequest.APIResponseBadRequest] = dataclasses.field(default=None)
    r"""Bad Request error"""
    api_response_unauthorized: Optional[shared_apiresponseunauthorized.APIResponseUnauthorized] = dataclasses.field(default=None)
    r"""Unauthorized error"""
    api_response_unprocessable_entity: Optional[shared_apiresponseunprocessableentity.APIResponseUnprocessableEntity] = dataclasses.field(default=None)
    r"""Unprocessable entity error"""
    credit_note: Optional[shared_creditnote.CreditNote] = dataclasses.field(default=None)
    r"""Successful response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    
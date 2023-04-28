"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import apiresponsenotfound as shared_apiresponsenotfound
from ..shared import apiresponseunauthorized as shared_apiresponseunauthorized
from ..shared import event as shared_event
from typing import Optional


@dataclasses.dataclass
class FindEventRequest:
    
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})

    r"""Id of the existing transaction"""
    

@dataclasses.dataclass
class FindEventResponse:
    
    content_type: str = dataclasses.field()

    status_code: int = dataclasses.field()

    api_response_not_found: Optional[shared_apiresponsenotfound.APIResponseNotFound] = dataclasses.field(default=None)

    r"""Not Found error"""
    api_response_unauthorized: Optional[shared_apiresponseunauthorized.APIResponseUnauthorized] = dataclasses.field(default=None)

    r"""Unauthorized error"""
    event: Optional[shared_event.Event] = dataclasses.field(default=None)

    r"""Successful response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)

    
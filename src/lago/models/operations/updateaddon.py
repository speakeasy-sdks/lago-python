"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import addon as shared_addon
from ..shared import addoninput as shared_addoninput
from ..shared import apiresponsebadrequest as shared_apiresponsebadrequest
from ..shared import apiresponsenotfound as shared_apiresponsenotfound
from ..shared import apiresponseunauthorized as shared_apiresponseunauthorized
from ..shared import apiresponseunprocessableentity as shared_apiresponseunprocessableentity
from typing import Optional


@dataclasses.dataclass
class UpdateAddOnRequest:
    
    add_on_input: shared_addoninput.AddOnInput = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    r"""Update an existing add-on"""
    code: str = dataclasses.field(metadata={'path_param': { 'field_name': 'code', 'style': 'simple', 'explode': False }})
    r"""Code of the existing add-on"""
    

@dataclasses.dataclass
class UpdateAddOnResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    add_on: Optional[shared_addon.AddOn] = dataclasses.field(default=None)
    r"""Successful response"""
    api_response_bad_request: Optional[shared_apiresponsebadrequest.APIResponseBadRequest] = dataclasses.field(default=None)
    r"""Bad Request error"""
    api_response_not_found: Optional[shared_apiresponsenotfound.APIResponseNotFound] = dataclasses.field(default=None)
    r"""Not Found error"""
    api_response_unauthorized: Optional[shared_apiresponseunauthorized.APIResponseUnauthorized] = dataclasses.field(default=None)
    r"""Unauthorized error"""
    api_response_unprocessable_entity: Optional[shared_apiresponseunprocessableentity.APIResponseUnprocessableEntity] = dataclasses.field(default=None)
    r"""Unprocessable entity error"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    
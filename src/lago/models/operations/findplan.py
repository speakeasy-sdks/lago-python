"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import apiresponsenotfound as shared_apiresponsenotfound
from ..shared import apiresponseunauthorized as shared_apiresponseunauthorized
from ..shared import plan as shared_plan
from typing import Optional


@dataclasses.dataclass
class FindPlanRequest:
    
    code: str = dataclasses.field(metadata={'path_param': { 'field_name': 'code', 'style': 'simple', 'explode': False }})
    r"""Code of the existing plan"""
    

@dataclasses.dataclass
class FindPlanResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    api_response_not_found: Optional[shared_apiresponsenotfound.APIResponseNotFound] = dataclasses.field(default=None)
    r"""Not Found error"""
    api_response_unauthorized: Optional[shared_apiresponseunauthorized.APIResponseUnauthorized] = dataclasses.field(default=None)
    r"""Unauthorized error"""
    plan: Optional[shared_plan.Plan] = dataclasses.field(default=None)
    r"""Successful response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    
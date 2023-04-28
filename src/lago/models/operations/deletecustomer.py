"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import apiresponsenotfound as shared_apiresponsenotfound
from ..shared import apiresponseunauthorized as shared_apiresponseunauthorized
from ..shared import customer as shared_customer
from typing import Optional


@dataclasses.dataclass
class DeleteCustomerRequest:
    
    external_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'external_id', 'style': 'simple', 'explode': False }})

    r"""External ID of the existing customer"""
    

@dataclasses.dataclass
class DeleteCustomerResponse:
    
    content_type: str = dataclasses.field()

    status_code: int = dataclasses.field()

    api_response_not_found: Optional[shared_apiresponsenotfound.APIResponseNotFound] = dataclasses.field(default=None)

    r"""Not Found error"""
    api_response_unauthorized: Optional[shared_apiresponseunauthorized.APIResponseUnauthorized] = dataclasses.field(default=None)

    r"""Unauthorized error"""
    customer: Optional[shared_customer.Customer] = dataclasses.field(default=None)

    r"""Successful response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)

    
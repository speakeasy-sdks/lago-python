"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import apiresponsenotfound as shared_apiresponsenotfound
from ..shared import apiresponseunauthorized as shared_apiresponseunauthorized
from ..shared import subscriptions as shared_subscriptions
from typing import Optional


@dataclasses.dataclass
class FindAllSubscriptionsRequest:
    
    external_customer_id: str = dataclasses.field(metadata={'query_param': { 'field_name': 'external_customer_id', 'style': 'form', 'explode': True }})

    r"""External customer ID"""
    page: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'page', 'style': 'form', 'explode': True }})

    r"""Number of page"""
    per_page: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'per_page', 'style': 'form', 'explode': True }})

    r"""Number of records per page"""
    

@dataclasses.dataclass
class FindAllSubscriptionsResponse:
    
    content_type: str = dataclasses.field()

    status_code: int = dataclasses.field()

    api_response_not_found: Optional[shared_apiresponsenotfound.APIResponseNotFound] = dataclasses.field(default=None)

    r"""Not Found error"""
    api_response_unauthorized: Optional[shared_apiresponseunauthorized.APIResponseUnauthorized] = dataclasses.field(default=None)

    r"""Unauthorized error"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)

    subscriptions: Optional[shared_subscriptions.Subscriptions] = dataclasses.field(default=None)

    r"""Successful response"""
    
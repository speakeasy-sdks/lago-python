"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import apiresponseunauthorized as shared_apiresponseunauthorized
from ..shared import coupons as shared_coupons
from typing import Optional


@dataclasses.dataclass
class FindAllCouponsRequest:
    
    page: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'page', 'style': 'form', 'explode': True }})
    r"""Number of page"""  
    per_page: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'per_page', 'style': 'form', 'explode': True }})
    r"""Number of records per page"""  
    

@dataclasses.dataclass
class FindAllCouponsResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    api_response_unauthorized: Optional[shared_apiresponseunauthorized.APIResponseUnauthorized] = dataclasses.field(default=None)
    r"""Unauthorized error"""  
    coupons: Optional[shared_coupons.Coupons] = dataclasses.field(default=None)
    r"""Successful response"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    
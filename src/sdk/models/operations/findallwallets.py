"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import apiresponseunauthorized as shared_apiresponseunauthorized
from ..shared import wallets as shared_wallets
from typing import Optional


@dataclasses.dataclass
class FindAllWalletsRequest:
    
    external_customer_id: str = dataclasses.field(metadata={'query_param': { 'field_name': 'external_customer_id', 'style': 'form', 'explode': True }})
    r"""External customer ID"""  
    page: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'page', 'style': 'form', 'explode': True }})
    r"""Number of page"""  
    per_page: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'per_page', 'style': 'form', 'explode': True }})
    r"""Number of records per page"""  
    

@dataclasses.dataclass
class FindAllWalletsResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    api_response_unauthorized: Optional[shared_apiresponseunauthorized.APIResponseUnauthorized] = dataclasses.field(default=None)
    r"""Unauthorized error"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    wallets: Optional[shared_wallets.Wallets] = dataclasses.field(default=None)
    r"""Successful response"""  
    
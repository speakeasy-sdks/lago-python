"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import apiresponsenotfound as shared_apiresponsenotfound
from ..shared import apiresponseunauthorized as shared_apiresponseunauthorized
from ..shared import wallet as shared_wallet
from typing import Optional


@dataclasses.dataclass
class FindWalletRequest:
    
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Lago ID of the existing wallet"""  
    

@dataclasses.dataclass
class FindWalletResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    api_response_not_found: Optional[shared_apiresponsenotfound.APIResponseNotFound] = dataclasses.field(default=None)
    r"""Not Found error"""  
    api_response_unauthorized: Optional[shared_apiresponseunauthorized.APIResponseUnauthorized] = dataclasses.field(default=None)
    r"""Unauthorized error"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    wallet: Optional[shared_wallet.Wallet] = dataclasses.field(default=None)
    r"""Successful response"""  
    
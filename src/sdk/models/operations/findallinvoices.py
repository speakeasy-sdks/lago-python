"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import apiresponseunauthorized as shared_apiresponseunauthorized
from ..shared import invoices as shared_invoices
from datetime import date
from enum import Enum
from typing import Optional

class FindAllInvoicesStatusEnum(str, Enum):
    r"""Status"""
    DRAFT = 'draft'
    FINALIZED = 'finalized'


@dataclasses.dataclass
class FindAllInvoicesRequest:
    
    external_customer_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'external_customer_id', 'style': 'form', 'explode': True }})
    r"""External customer ID"""  
    issuing_date_from: Optional[date] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'issuing_date_from', 'style': 'form', 'explode': True }})
    r"""Date from"""  
    issuing_date_to: Optional[date] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'issuing_date_to', 'style': 'form', 'explode': True }})
    r"""Date to"""  
    page: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'page', 'style': 'form', 'explode': True }})
    r"""Number of page"""  
    per_page: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'per_page', 'style': 'form', 'explode': True }})
    r"""Number of records per page"""  
    status: Optional[FindAllInvoicesStatusEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'status', 'style': 'form', 'explode': True }})
    r"""Status"""  
    

@dataclasses.dataclass
class FindAllInvoicesResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    api_response_unauthorized: Optional[shared_apiresponseunauthorized.APIResponseUnauthorized] = dataclasses.field(default=None)
    r"""Unauthorized error"""  
    invoices: Optional[shared_invoices.Invoices] = dataclasses.field(default=None)
    r"""Successful response"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    
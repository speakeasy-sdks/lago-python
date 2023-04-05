"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import apiresponsebadrequest as shared_apiresponsebadrequest
from ..shared import apiresponsenotfound as shared_apiresponsenotfound
from ..shared import apiresponseunauthorized as shared_apiresponseunauthorized
from ..shared import apiresponseunprocessableentity as shared_apiresponseunprocessableentity
from ..shared import feeobject as shared_feeobject
from ..shared import feeupdateinput as shared_feeupdateinput
from typing import Optional


@dataclasses.dataclass
class UpdateFeeRequest:
    
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""ID of the existing Lago Fee"""  
    fee_update_input: Optional[shared_feeupdateinput.FeeUpdateInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""Payload to update a fee"""  
    

@dataclasses.dataclass
class UpdateFeeResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    api_response_bad_request: Optional[shared_apiresponsebadrequest.APIResponseBadRequest] = dataclasses.field(default=None)
    r"""Bad Request error"""  
    api_response_not_found: Optional[shared_apiresponsenotfound.APIResponseNotFound] = dataclasses.field(default=None)
    r"""Not Found error"""  
    api_response_unauthorized: Optional[shared_apiresponseunauthorized.APIResponseUnauthorized] = dataclasses.field(default=None)
    r"""Unauthorized error"""  
    api_response_unprocessable_entity: Optional[shared_apiresponseunprocessableentity.APIResponseUnprocessableEntity] = dataclasses.field(default=None)
    r"""Unprocessable entity error"""  
    fee_object: Optional[shared_feeobject.FeeObject] = dataclasses.field(default=None)
    r"""Successful response"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    
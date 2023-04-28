"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import apiresponsebadrequest as shared_apiresponsebadrequest
from ..shared import apiresponsenotfound as shared_apiresponsenotfound
from ..shared import apiresponseunauthorized as shared_apiresponseunauthorized
from ..shared import apiresponseunprocessableentity as shared_apiresponseunprocessableentity
from ..shared import appliedcoupon as shared_appliedcoupon
from typing import Optional


@dataclasses.dataclass
class ApplyCouponResponse:
    
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
    applied_coupon: Optional[shared_appliedcoupon.AppliedCoupon] = dataclasses.field(default=None)

    r"""Successful response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)

    
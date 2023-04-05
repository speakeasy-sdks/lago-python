"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from sdk.models import operations, shared
from typing import Optional

class AddOns:
    r"""Everything about Add-on collection
    https://doc.getlago.com/docs/api/add_ons/add-on-object - Find out more
    """
    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str
    _language: str
    _sdk_version: str
    _gen_version: str

    def __init__(self, client: requests_http.Session, security_client: requests_http.Session, server_url: str, language: str, sdk_version: str, gen_version: str) -> None:
        self._client = client
        self._security_client = security_client
        self._server_url = server_url
        self._language = language
        self._sdk_version = sdk_version
        self._gen_version = gen_version
        
    def apply(self, request: shared.AppliedAddOnInput) -> operations.ApplyAddOnResponse:
        r"""Apply an add-on to a customer
        Apply an add-on to a customer
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/applied_add_ons'
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ApplyAddOnResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.AppliedAddOn])
                res.applied_add_on = out
        elif http_res.status_code == 400:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.APIResponseBadRequest])
                res.api_response_bad_request = out
        elif http_res.status_code == 401:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.APIResponseUnauthorized])
                res.api_response_unauthorized = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.APIResponseNotFound])
                res.api_response_not_found = out
        elif http_res.status_code == 422:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.APIResponseUnprocessableEntity])
                res.api_response_unprocessable_entity = out

        return res

    def create(self, request: shared.AddOnInput) -> operations.CreateAddOnResponse:
        r"""Create a new add-on
        Create a new add-on
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/add_ons'
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateAddOnResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.AddOn])
                res.add_on = out
        elif http_res.status_code == 400:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.APIResponseBadRequest])
                res.api_response_bad_request = out
        elif http_res.status_code == 401:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.APIResponseUnauthorized])
                res.api_response_unauthorized = out
        elif http_res.status_code == 422:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.APIResponseUnprocessableEntity])
                res.api_response_unprocessable_entity = out

        return res

    def destroy(self, request: operations.DestroyAddOnRequest) -> operations.DestroyAddOnResponse:
        r"""Delete an add-on
        Delete an add-on
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.DestroyAddOnRequest, base_url, '/add_ons/{code}', request)
        
        
        client = self._security_client
        
        http_res = client.request('DELETE', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DestroyAddOnResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.AddOn])
                res.add_on = out
        elif http_res.status_code == 401:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.APIResponseUnauthorized])
                res.api_response_unauthorized = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.APIResponseNotFound])
                res.api_response_not_found = out

        return res

    def find(self, request: operations.FindAddOnRequest) -> operations.FindAddOnResponse:
        r"""Find add-on by code
        Return a single add-on
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.FindAddOnRequest, base_url, '/add_ons/{code}', request)
        
        
        client = self._security_client
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.FindAddOnResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.AddOn])
                res.add_on = out
        elif http_res.status_code == 401:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.APIResponseUnauthorized])
                res.api_response_unauthorized = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.APIResponseNotFound])
                res.api_response_not_found = out

        return res

    def find_all(self, request: operations.FindAllAddOnsRequest) -> operations.FindAllAddOnsResponse:
        r"""Find add-ons
        Find all add-ons in certain organisation
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/add_ons'
        
        query_params = utils.get_query_params(operations.FindAllAddOnsRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.FindAllAddOnsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.AddOns])
                res.add_ons = out
        elif http_res.status_code == 401:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.APIResponseUnauthorized])
                res.api_response_unauthorized = out

        return res

    def update(self, request: operations.UpdateAddOnRequest) -> operations.UpdateAddOnResponse:
        r"""Update an existing add-on
        Update an existing add-on by code
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.UpdateAddOnRequest, base_url, '/add_ons/{code}', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "add_on_input", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._security_client
        
        http_res = client.request('PUT', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpdateAddOnResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.AddOn])
                res.add_on = out
        elif http_res.status_code == 400:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.APIResponseBadRequest])
                res.api_response_bad_request = out
        elif http_res.status_code == 401:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.APIResponseUnauthorized])
                res.api_response_unauthorized = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.APIResponseNotFound])
                res.api_response_not_found = out
        elif http_res.status_code == 422:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.APIResponseUnprocessableEntity])
                res.api_response_unprocessable_entity = out

        return res

    
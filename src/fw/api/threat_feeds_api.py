# coding: utf-8

"""
    BloxOne FW API

    BloxOne Threat Defense Cloud is an extension of the BloxOne Suite that provides visibility into infected and compromised off-premises devices, roaming users, remote sites, and branch offices. You can subscribe to BloxOne Cloud and use its functionality to mitigate and control malware as well as provide unprecedented insight into your network security posture and enable timely action. BloxOne Cloud also offers unified policy management, reporting, and threat analytics across the entire spectrum. Using automated and high-quality threat intelligence feeds and unique behavioral analytics, it automatically stops device communications with C&Cs/botnets and prevents DNS based data exfiltration.  The mission-critical DNS infrastructure can become a vulnerable component in your network when it is inadequately protected by traditional security solutions and consequently used as an attack surface. Compromised DNS services can result in catastrophic network and system failures. To fully protect your network in today’s cyber security threat environment, Infoblox sets a new DNS security standard by offering scalable, enterprise-grade, and integrated protection for your DNS infrastructure.  Through the Infoblox Cloud Services Portal, you can view the status of your subscription and threat intelligence feeds, manage your network scope and roaming end users, and learn more about threats on your networks through the Infoblox Threat Lookup tool and predefined reports. 

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictInt, StrictStr
from typing import Optional
from typing_extensions import Annotated
from fw.models.threat_feed_multi_response import ThreatFeedMultiResponse
from fw import models

from bloxone_client.api_client import ApiClient, RequestSerialized
from bloxone_client.api_response import ApiResponse
from bloxone_client.rest import RESTResponseType


class ThreatFeedsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_call
    def list_threat_feeds(
        self,
        filter: Annotated[
            Optional[StrictStr],
            Field(
                description=
                "A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and 'null'.  You can filter by following fields:  | Name               | type   | Supported Op                | | ------------------ | ------ | --------------------------- | | name               | string | !=, ==, ~, !~, >, <, <=, >= |  In addition grouping operators are supported:  | Op  | Description          | | --- | -------------------- | | and | Logical AND          | | or  | Logical OR           | | not | Logical NOT          | | ()  | Grouping Operators  |  Example: ``` ?_filter=\"((name=='AntiMalware')or(name~'FarSightNOD'))\" ``` "
            )] = None,
        fields: Annotated[
            Optional[StrictStr],
            Field(
                description=
                "  A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.        "
            )] = None,
        offset: Annotated[
            Optional[StrictInt],
            Field(
                description=
                "  The integer index (zero-origin) of the offset into a collection of resources. If omitted or null the value is assumed to be '0'.         "
            )] = None,
        limit: Annotated[
            Optional[StrictInt],
            Field(
                description=
                "  The integer number of resources to be returned in the response. The service may impose maximum value. If omitted the service may impose a default value.         "
            )] = None,
        page_token: Annotated[
            Optional[StrictStr],
            Field(
                description=
                "  The service-defined string used to identify a page of resources. A null value indicates the first page.         "
            )] = None,
        _request_timeout: Union[None, Annotated[StrictFloat,
                                                Field(gt=0)],
                                Tuple[Annotated[StrictFloat,
                                                Field(gt=0)],
                                      Annotated[StrictFloat,
                                                Field(gt=0)]]] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ThreatFeedMultiResponse:
        """List Threat Feeds.

        Use this method to retrieve information on all Threat Feed objects for the account.  BloxOne Cloud provides predefined threat intelligence feeds based on your subscription. The Plus subscription offers a few more feeds than the Standard subscription. The Advanced subscription offers a few more feeds than the Plus subscription. A threat feed subscription for RPZ updates offers protection against malicious hostnames.  

        :param filter: A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and 'null'.  You can filter by following fields:  | Name               | type   | Supported Op                | | ------------------ | ------ | --------------------------- | | name               | string | !=, ==, ~, !~, >, <, <=, >= |  In addition grouping operators are supported:  | Op  | Description          | | --- | -------------------- | | and | Logical AND          | | or  | Logical OR           | | not | Logical NOT          | | ()  | Grouping Operators  |  Example: ``` ?_filter=\"((name=='AntiMalware')or(name~'FarSightNOD'))\" ``` 
        :type filter: str
        :param fields:   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.        
        :type fields: str
        :param offset:   The integer index (zero-origin) of the offset into a collection of resources. If omitted or null the value is assumed to be '0'.         
        :type offset: int
        :param limit:   The integer number of resources to be returned in the response. The service may impose maximum value. If omitted the service may impose a default value.         
        :type limit: int
        :param page_token:   The service-defined string used to identify a page of resources. A null value indicates the first page.         
        :type page_token: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._list_threat_feeds_serialize(filter=filter,
                                                   fields=fields,
                                                   offset=offset,
                                                   limit=limit,
                                                   page_token=page_token,
                                                   _request_auth=_request_auth,
                                                   _content_type=_content_type,
                                                   _headers=_headers,
                                                   _host_index=_host_index)

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ThreatFeedMultiResponse",
            '500': "AccessCodesListAccessCodes500Response",
        }
        response_data = self.api_client.call_api(
            *_param, _request_timeout=_request_timeout)
        response_data.read()
        return self.api_client.response_deserialize(
            models=models,
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    @validate_call
    def list_threat_feeds_with_http_info(
        self,
        filter: Annotated[
            Optional[StrictStr],
            Field(
                description=
                "A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and 'null'.  You can filter by following fields:  | Name               | type   | Supported Op                | | ------------------ | ------ | --------------------------- | | name               | string | !=, ==, ~, !~, >, <, <=, >= |  In addition grouping operators are supported:  | Op  | Description          | | --- | -------------------- | | and | Logical AND          | | or  | Logical OR           | | not | Logical NOT          | | ()  | Grouping Operators  |  Example: ``` ?_filter=\"((name=='AntiMalware')or(name~'FarSightNOD'))\" ``` "
            )] = None,
        fields: Annotated[
            Optional[StrictStr],
            Field(
                description=
                "  A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.        "
            )] = None,
        offset: Annotated[
            Optional[StrictInt],
            Field(
                description=
                "  The integer index (zero-origin) of the offset into a collection of resources. If omitted or null the value is assumed to be '0'.         "
            )] = None,
        limit: Annotated[
            Optional[StrictInt],
            Field(
                description=
                "  The integer number of resources to be returned in the response. The service may impose maximum value. If omitted the service may impose a default value.         "
            )] = None,
        page_token: Annotated[
            Optional[StrictStr],
            Field(
                description=
                "  The service-defined string used to identify a page of resources. A null value indicates the first page.         "
            )] = None,
        _request_timeout: Union[None, Annotated[StrictFloat,
                                                Field(gt=0)],
                                Tuple[Annotated[StrictFloat,
                                                Field(gt=0)],
                                      Annotated[StrictFloat,
                                                Field(gt=0)]]] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ThreatFeedMultiResponse]:
        """List Threat Feeds.

        Use this method to retrieve information on all Threat Feed objects for the account.  BloxOne Cloud provides predefined threat intelligence feeds based on your subscription. The Plus subscription offers a few more feeds than the Standard subscription. The Advanced subscription offers a few more feeds than the Plus subscription. A threat feed subscription for RPZ updates offers protection against malicious hostnames.  

        :param filter: A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and 'null'.  You can filter by following fields:  | Name               | type   | Supported Op                | | ------------------ | ------ | --------------------------- | | name               | string | !=, ==, ~, !~, >, <, <=, >= |  In addition grouping operators are supported:  | Op  | Description          | | --- | -------------------- | | and | Logical AND          | | or  | Logical OR           | | not | Logical NOT          | | ()  | Grouping Operators  |  Example: ``` ?_filter=\"((name=='AntiMalware')or(name~'FarSightNOD'))\" ``` 
        :type filter: str
        :param fields:   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.        
        :type fields: str
        :param offset:   The integer index (zero-origin) of the offset into a collection of resources. If omitted or null the value is assumed to be '0'.         
        :type offset: int
        :param limit:   The integer number of resources to be returned in the response. The service may impose maximum value. If omitted the service may impose a default value.         
        :type limit: int
        :param page_token:   The service-defined string used to identify a page of resources. A null value indicates the first page.         
        :type page_token: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._list_threat_feeds_serialize(filter=filter,
                                                   fields=fields,
                                                   offset=offset,
                                                   limit=limit,
                                                   page_token=page_token,
                                                   _request_auth=_request_auth,
                                                   _content_type=_content_type,
                                                   _headers=_headers,
                                                   _host_index=_host_index)

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ThreatFeedMultiResponse",
            '500': "AccessCodesListAccessCodes500Response",
        }
        response_data = self.api_client.call_api(
            *_param, _request_timeout=_request_timeout)
        response_data.read()
        return self.api_client.response_deserialize(
            models=models,
            response_data=response_data,
            response_types_map=_response_types_map,
        )

    @validate_call
    def list_threat_feeds_without_preload_content(
        self,
        filter: Annotated[
            Optional[StrictStr],
            Field(
                description=
                "A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and 'null'.  You can filter by following fields:  | Name               | type   | Supported Op                | | ------------------ | ------ | --------------------------- | | name               | string | !=, ==, ~, !~, >, <, <=, >= |  In addition grouping operators are supported:  | Op  | Description          | | --- | -------------------- | | and | Logical AND          | | or  | Logical OR           | | not | Logical NOT          | | ()  | Grouping Operators  |  Example: ``` ?_filter=\"((name=='AntiMalware')or(name~'FarSightNOD'))\" ``` "
            )] = None,
        fields: Annotated[
            Optional[StrictStr],
            Field(
                description=
                "  A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.        "
            )] = None,
        offset: Annotated[
            Optional[StrictInt],
            Field(
                description=
                "  The integer index (zero-origin) of the offset into a collection of resources. If omitted or null the value is assumed to be '0'.         "
            )] = None,
        limit: Annotated[
            Optional[StrictInt],
            Field(
                description=
                "  The integer number of resources to be returned in the response. The service may impose maximum value. If omitted the service may impose a default value.         "
            )] = None,
        page_token: Annotated[
            Optional[StrictStr],
            Field(
                description=
                "  The service-defined string used to identify a page of resources. A null value indicates the first page.         "
            )] = None,
        _request_timeout: Union[None, Annotated[StrictFloat,
                                                Field(gt=0)],
                                Tuple[Annotated[StrictFloat,
                                                Field(gt=0)],
                                      Annotated[StrictFloat,
                                                Field(gt=0)]]] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """List Threat Feeds.

        Use this method to retrieve information on all Threat Feed objects for the account.  BloxOne Cloud provides predefined threat intelligence feeds based on your subscription. The Plus subscription offers a few more feeds than the Standard subscription. The Advanced subscription offers a few more feeds than the Plus subscription. A threat feed subscription for RPZ updates offers protection against malicious hostnames.  

        :param filter: A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and 'null'.  You can filter by following fields:  | Name               | type   | Supported Op                | | ------------------ | ------ | --------------------------- | | name               | string | !=, ==, ~, !~, >, <, <=, >= |  In addition grouping operators are supported:  | Op  | Description          | | --- | -------------------- | | and | Logical AND          | | or  | Logical OR           | | not | Logical NOT          | | ()  | Grouping Operators  |  Example: ``` ?_filter=\"((name=='AntiMalware')or(name~'FarSightNOD'))\" ``` 
        :type filter: str
        :param fields:   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.        
        :type fields: str
        :param offset:   The integer index (zero-origin) of the offset into a collection of resources. If omitted or null the value is assumed to be '0'.         
        :type offset: int
        :param limit:   The integer number of resources to be returned in the response. The service may impose maximum value. If omitted the service may impose a default value.         
        :type limit: int
        :param page_token:   The service-defined string used to identify a page of resources. A null value indicates the first page.         
        :type page_token: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._list_threat_feeds_serialize(filter=filter,
                                                   fields=fields,
                                                   offset=offset,
                                                   limit=limit,
                                                   page_token=page_token,
                                                   _request_auth=_request_auth,
                                                   _content_type=_content_type,
                                                   _headers=_headers,
                                                   _host_index=_host_index)

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ThreatFeedMultiResponse",
            '500': "AccessCodesListAccessCodes500Response",
        }
        response_data = self.api_client.call_api(
            *_param, _request_timeout=_request_timeout)
        return response_data.response

    def _list_threat_feeds_serialize(
        self,
        filter,
        fields,
        offset,
        limit,
        page_token,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {}

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if filter is not None:

            _query_params.append(('_filter', filter))

        if fields is not None:

            _query_params.append(('_fields', fields))

        if offset is not None:

            _query_params.append(('_offset', offset))

        if limit is not None:

            _query_params.append(('_limit', limit))

        if page_token is not None:

            _query_params.append(('_page_token', page_token))

        # process the header parameters
        # process the form parameters
        # process the body parameter

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # authentication setting
        _auth_settings: List[str] = []

        return self.api_client.param_serialize(
            method='GET',
            base_path='/api/atcfw/v1',
            resource_path='/threat_feeds',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth)

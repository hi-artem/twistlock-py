# coding: utf-8

"""
    Prisma Cloud Compute API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 21.04.439
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from openapi_client.api_client import ApiClient
from openapi_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class ForensicApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_v1_forensic_activities_download_get(self, **kwargs):  # noqa: E501
        """api_v1_forensic_activities_download_get  # noqa: E501

        DownloadHostActivities downloads the host activity data   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v1_forensic_activities_download_get(async_req=True)
        >>> result = thread.get()

        :param offset: Offset from the start of the list from which to retrieve documents. 
        :type offset: int
        :param limit: Number of documents to return. 
        :type limit: int
        :param search: Search term. 
        :type search: str
        :param sort: Key on which to sort. 
        :type sort: str
        :param reverse: Sort order. 
        :type reverse: bool
        :param collections: Scopes the query by collection. 
        :type collections: list[str]
        :param account_ids: Scopes the query by account ID. 
        :type account_ids: list[str]
        :param fields: List of fields to retrieve. 
        :type fields: list[str]
        :param _from: From is an optional minimum time constraints for the activity. 
        :type _from: datetime
        :param to: To is an optional maximum time constraints for the activity. 
        :type to: datetime
        :param type: Types is the activity type filter. 
        :type type: list[str]
        :param user: Users is the list of users to use for filtering. 
        :type user: list[str]
        :param hostname: Hosts is the list of hosts to use for filtering. 
        :type hostname: list[str]
        :param service: Services is the list of services to use for filtering. 
        :type service: list[str]
        :param cluster: Clusters is the cluster filter. 
        :type cluster: list[str]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        return self.api_v1_forensic_activities_download_get_with_http_info(**kwargs)  # noqa: E501

    def api_v1_forensic_activities_download_get_with_http_info(self, **kwargs):  # noqa: E501
        """api_v1_forensic_activities_download_get  # noqa: E501

        DownloadHostActivities downloads the host activity data   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v1_forensic_activities_download_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param offset: Offset from the start of the list from which to retrieve documents. 
        :type offset: int
        :param limit: Number of documents to return. 
        :type limit: int
        :param search: Search term. 
        :type search: str
        :param sort: Key on which to sort. 
        :type sort: str
        :param reverse: Sort order. 
        :type reverse: bool
        :param collections: Scopes the query by collection. 
        :type collections: list[str]
        :param account_ids: Scopes the query by account ID. 
        :type account_ids: list[str]
        :param fields: List of fields to retrieve. 
        :type fields: list[str]
        :param _from: From is an optional minimum time constraints for the activity. 
        :type _from: datetime
        :param to: To is an optional maximum time constraints for the activity. 
        :type to: datetime
        :param type: Types is the activity type filter. 
        :type type: list[str]
        :param user: Users is the list of users to use for filtering. 
        :type user: list[str]
        :param hostname: Hosts is the list of hosts to use for filtering. 
        :type hostname: list[str]
        :param service: Services is the list of services to use for filtering. 
        :type service: list[str]
        :param cluster: Clusters is the cluster filter. 
        :type cluster: list[str]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        local_var_params = locals()

        all_params = [
            'offset',
            'limit',
            'search',
            'sort',
            'reverse',
            'collections',
            'account_ids',
            'fields',
            '_from',
            'to',
            'type',
            'user',
            'hostname',
            'service',
            'cluster'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v1_forensic_activities_download_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params and local_var_params['offset'] is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'search' in local_var_params and local_var_params['search'] is not None:  # noqa: E501
            query_params.append(('search', local_var_params['search']))  # noqa: E501
        if 'sort' in local_var_params and local_var_params['sort'] is not None:  # noqa: E501
            query_params.append(('sort', local_var_params['sort']))  # noqa: E501
        if 'reverse' in local_var_params and local_var_params['reverse'] is not None:  # noqa: E501
            query_params.append(('reverse', local_var_params['reverse']))  # noqa: E501
        if 'collections' in local_var_params and local_var_params['collections'] is not None:  # noqa: E501
            query_params.append(('collections', local_var_params['collections']))  # noqa: E501
            collection_formats['collections'] = 'multi'  # noqa: E501
        if 'account_ids' in local_var_params and local_var_params['account_ids'] is not None:  # noqa: E501
            query_params.append(('accountIDs', local_var_params['account_ids']))  # noqa: E501
            collection_formats['accountIDs'] = 'multi'  # noqa: E501
        if 'fields' in local_var_params and local_var_params['fields'] is not None:  # noqa: E501
            query_params.append(('fields', local_var_params['fields']))  # noqa: E501
            collection_formats['fields'] = 'multi'  # noqa: E501
        if '_from' in local_var_params and local_var_params['_from'] is not None:  # noqa: E501
            query_params.append(('from', local_var_params['_from']))  # noqa: E501
        if 'to' in local_var_params and local_var_params['to'] is not None:  # noqa: E501
            query_params.append(('to', local_var_params['to']))  # noqa: E501
        if 'type' in local_var_params and local_var_params['type'] is not None:  # noqa: E501
            query_params.append(('type', local_var_params['type']))  # noqa: E501
            collection_formats['type'] = 'multi'  # noqa: E501
        if 'user' in local_var_params and local_var_params['user'] is not None:  # noqa: E501
            query_params.append(('user', local_var_params['user']))  # noqa: E501
            collection_formats['user'] = 'multi'  # noqa: E501
        if 'hostname' in local_var_params and local_var_params['hostname'] is not None:  # noqa: E501
            query_params.append(('hostname', local_var_params['hostname']))  # noqa: E501
            collection_formats['hostname'] = 'multi'  # noqa: E501
        if 'service' in local_var_params and local_var_params['service'] is not None:  # noqa: E501
            query_params.append(('service', local_var_params['service']))  # noqa: E501
            collection_formats['service'] = 'multi'  # noqa: E501
        if 'cluster' in local_var_params and local_var_params['cluster'] is not None:  # noqa: E501
            query_params.append(('cluster', local_var_params['cluster']))  # noqa: E501
            collection_formats['cluster'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501
        
        response_types_map = {}

        return self.api_client.call_api(
            '/api/v1/forensic/activities/download', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def api_v1_forensic_activities_get(self, **kwargs):  # noqa: E501
        """api_v1_forensic_activities_get  # noqa: E501

        HostActivities returns the host activities   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v1_forensic_activities_get(async_req=True)
        >>> result = thread.get()

        :param offset: Offset from the start of the list from which to retrieve documents. 
        :type offset: int
        :param limit: Number of documents to return. 
        :type limit: int
        :param search: Search term. 
        :type search: str
        :param sort: Key on which to sort. 
        :type sort: str
        :param reverse: Sort order. 
        :type reverse: bool
        :param collections: Scopes the query by collection. 
        :type collections: list[str]
        :param account_ids: Scopes the query by account ID. 
        :type account_ids: list[str]
        :param fields: List of fields to retrieve. 
        :type fields: list[str]
        :param _from: From is an optional minimum time constraints for the activity. 
        :type _from: datetime
        :param to: To is an optional maximum time constraints for the activity. 
        :type to: datetime
        :param type: Types is the activity type filter. 
        :type type: list[str]
        :param user: Users is the list of users to use for filtering. 
        :type user: list[str]
        :param hostname: Hosts is the list of hosts to use for filtering. 
        :type hostname: list[str]
        :param service: Services is the list of services to use for filtering. 
        :type service: list[str]
        :param cluster: Clusters is the cluster filter. 
        :type cluster: list[str]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: list[SharedHostActivity]
        """
        kwargs['_return_http_data_only'] = True
        return self.api_v1_forensic_activities_get_with_http_info(**kwargs)  # noqa: E501

    def api_v1_forensic_activities_get_with_http_info(self, **kwargs):  # noqa: E501
        """api_v1_forensic_activities_get  # noqa: E501

        HostActivities returns the host activities   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v1_forensic_activities_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param offset: Offset from the start of the list from which to retrieve documents. 
        :type offset: int
        :param limit: Number of documents to return. 
        :type limit: int
        :param search: Search term. 
        :type search: str
        :param sort: Key on which to sort. 
        :type sort: str
        :param reverse: Sort order. 
        :type reverse: bool
        :param collections: Scopes the query by collection. 
        :type collections: list[str]
        :param account_ids: Scopes the query by account ID. 
        :type account_ids: list[str]
        :param fields: List of fields to retrieve. 
        :type fields: list[str]
        :param _from: From is an optional minimum time constraints for the activity. 
        :type _from: datetime
        :param to: To is an optional maximum time constraints for the activity. 
        :type to: datetime
        :param type: Types is the activity type filter. 
        :type type: list[str]
        :param user: Users is the list of users to use for filtering. 
        :type user: list[str]
        :param hostname: Hosts is the list of hosts to use for filtering. 
        :type hostname: list[str]
        :param service: Services is the list of services to use for filtering. 
        :type service: list[str]
        :param cluster: Clusters is the cluster filter. 
        :type cluster: list[str]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(list[SharedHostActivity], status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'offset',
            'limit',
            'search',
            'sort',
            'reverse',
            'collections',
            'account_ids',
            'fields',
            '_from',
            'to',
            'type',
            'user',
            'hostname',
            'service',
            'cluster'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v1_forensic_activities_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params and local_var_params['offset'] is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'search' in local_var_params and local_var_params['search'] is not None:  # noqa: E501
            query_params.append(('search', local_var_params['search']))  # noqa: E501
        if 'sort' in local_var_params and local_var_params['sort'] is not None:  # noqa: E501
            query_params.append(('sort', local_var_params['sort']))  # noqa: E501
        if 'reverse' in local_var_params and local_var_params['reverse'] is not None:  # noqa: E501
            query_params.append(('reverse', local_var_params['reverse']))  # noqa: E501
        if 'collections' in local_var_params and local_var_params['collections'] is not None:  # noqa: E501
            query_params.append(('collections', local_var_params['collections']))  # noqa: E501
            collection_formats['collections'] = 'multi'  # noqa: E501
        if 'account_ids' in local_var_params and local_var_params['account_ids'] is not None:  # noqa: E501
            query_params.append(('accountIDs', local_var_params['account_ids']))  # noqa: E501
            collection_formats['accountIDs'] = 'multi'  # noqa: E501
        if 'fields' in local_var_params and local_var_params['fields'] is not None:  # noqa: E501
            query_params.append(('fields', local_var_params['fields']))  # noqa: E501
            collection_formats['fields'] = 'multi'  # noqa: E501
        if '_from' in local_var_params and local_var_params['_from'] is not None:  # noqa: E501
            query_params.append(('from', local_var_params['_from']))  # noqa: E501
        if 'to' in local_var_params and local_var_params['to'] is not None:  # noqa: E501
            query_params.append(('to', local_var_params['to']))  # noqa: E501
        if 'type' in local_var_params and local_var_params['type'] is not None:  # noqa: E501
            query_params.append(('type', local_var_params['type']))  # noqa: E501
            collection_formats['type'] = 'multi'  # noqa: E501
        if 'user' in local_var_params and local_var_params['user'] is not None:  # noqa: E501
            query_params.append(('user', local_var_params['user']))  # noqa: E501
            collection_formats['user'] = 'multi'  # noqa: E501
        if 'hostname' in local_var_params and local_var_params['hostname'] is not None:  # noqa: E501
            query_params.append(('hostname', local_var_params['hostname']))  # noqa: E501
            collection_formats['hostname'] = 'multi'  # noqa: E501
        if 'service' in local_var_params and local_var_params['service'] is not None:  # noqa: E501
            query_params.append(('service', local_var_params['service']))  # noqa: E501
            collection_formats['service'] = 'multi'  # noqa: E501
        if 'cluster' in local_var_params and local_var_params['cluster'] is not None:  # noqa: E501
            query_params.append(('cluster', local_var_params['cluster']))  # noqa: E501
            collection_formats['cluster'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501
        
        response_types_map = {
            200: "list[SharedHostActivity]",
        }

        return self.api_client.call_api(
            '/api/v1/forensic/activities', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

# openapi_client.CodereposCiApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_coderepos_ci_download_get**](CodereposCiApi.md#api_v1_coderepos_ci_download_get) | **GET** /api/v1/coderepos-ci/download | 
[**api_v1_coderepos_ci_evaluate_post**](CodereposCiApi.md#api_v1_coderepos_ci_evaluate_post) | **POST** /api/v1/coderepos-ci/evaluate | 
[**api_v1_coderepos_ci_get**](CodereposCiApi.md#api_v1_coderepos_ci_get) | **GET** /api/v1/coderepos-ci | 
[**api_v1_coderepos_ci_post**](CodereposCiApi.md#api_v1_coderepos_ci_post) | **POST** /api/v1/coderepos-ci | 


# **api_v1_coderepos_ci_download_get**
> api_v1_coderepos_ci_download_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, credential_id=credential_id, id=id, name=name, compact=compact, _from=_from, to=to)



DownloadCICodeRepos downloads CI code repository scan result 

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CodereposCiApi(api_client)
    offset = 56 # int | Offset from the start of the list from which to retrieve documents.  (optional)
limit = 56 # int | Number of documents to return.  (optional)
search = 'search_example' # str | Search term.  (optional)
sort = 'sort_example' # str | Key on which to sort.  (optional)
reverse = True # bool | Sort order.  (optional)
collections = ['collections_example'] # list[str] | Scopes the query by collection.  (optional)
account_ids = ['account_ids_example'] # list[str] | Scopes the query by account ID.  (optional)
fields = ['fields_example'] # list[str] | List of fields to retrieve.  (optional)
credential_id = 'credential_id_example' # str | ID of the requested credential, used for code repo scans.  (optional)
id = ['id_example'] # list[str] | Filters results by code repository ID. The ID is the repository's full name.  (optional)
name = ['name_example'] # list[str] | Filters results by full name of the code repositories.  (optional)
compact = True # bool | Indicates if only minimal image data is to be sent (i.e., vulnerabilities, compliance, and extended image metadata should be skipped) (true) or not (false).  (optional)
_from = '2013-10-20T19:20:30+01:00' # datetime | Filters results by starting datetime. Based on the last scan update time.  (optional)
to = '2013-10-20T19:20:30+01:00' # datetime | Filters results by end datetime. Based on the last scan update time.  (optional)

    try:
        api_instance.api_v1_coderepos_ci_download_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, credential_id=credential_id, id=id, name=name, compact=compact, _from=_from, to=to)
    except ApiException as e:
        print("Exception when calling CodereposCiApi->api_v1_coderepos_ci_download_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Offset from the start of the list from which to retrieve documents.  | [optional] 
 **limit** | **int**| Number of documents to return.  | [optional] 
 **search** | **str**| Search term.  | [optional] 
 **sort** | **str**| Key on which to sort.  | [optional] 
 **reverse** | **bool**| Sort order.  | [optional] 
 **collections** | [**list[str]**](str.md)| Scopes the query by collection.  | [optional] 
 **account_ids** | [**list[str]**](str.md)| Scopes the query by account ID.  | [optional] 
 **fields** | [**list[str]**](str.md)| List of fields to retrieve.  | [optional] 
 **credential_id** | **str**| ID of the requested credential, used for code repo scans.  | [optional] 
 **id** | [**list[str]**](str.md)| Filters results by code repository ID. The ID is the repository&#39;s full name.  | [optional] 
 **name** | [**list[str]**](str.md)| Filters results by full name of the code repositories.  | [optional] 
 **compact** | **bool**| Indicates if only minimal image data is to be sent (i.e., vulnerabilities, compliance, and extended image metadata should be skipped) (true) or not (false).  | [optional] 
 **_from** | **datetime**| Filters results by starting datetime. Based on the last scan update time.  | [optional] 
 **to** | **datetime**| Filters results by end datetime. Based on the last scan update time.  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_coderepos_ci_evaluate_post**
> CodereposScanResult api_v1_coderepos_ci_evaluate_post(coderepos_scan_result=coderepos_scan_result)



ResolveCodeRepos adds vulnerability data for the given code repo scan result 

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CodereposCiApi(api_client)
    coderepos_scan_result = openapi_client.CodereposScanResult() # CodereposScanResult |  (optional)

    try:
        api_response = api_instance.api_v1_coderepos_ci_evaluate_post(coderepos_scan_result=coderepos_scan_result)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CodereposCiApi->api_v1_coderepos_ci_evaluate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coderepos_scan_result** | [**CodereposScanResult**](CodereposScanResult.md)|  | [optional] 

### Return type

[**CodereposScanResult**](CodereposScanResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ScanResult holds a specific repository data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_coderepos_ci_get**
> list[CodereposScanResult] api_v1_coderepos_ci_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, credential_id=credential_id, id=id, name=name, compact=compact, _from=_from, to=to)



CICodeRepos returns CI code repositories scan results 

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CodereposCiApi(api_client)
    offset = 56 # int | Offset from the start of the list from which to retrieve documents.  (optional)
limit = 56 # int | Number of documents to return.  (optional)
search = 'search_example' # str | Search term.  (optional)
sort = 'sort_example' # str | Key on which to sort.  (optional)
reverse = True # bool | Sort order.  (optional)
collections = ['collections_example'] # list[str] | Scopes the query by collection.  (optional)
account_ids = ['account_ids_example'] # list[str] | Scopes the query by account ID.  (optional)
fields = ['fields_example'] # list[str] | List of fields to retrieve.  (optional)
credential_id = 'credential_id_example' # str | ID of the requested credential, used for code repo scans.  (optional)
id = ['id_example'] # list[str] | Filters results by code repository ID. The ID is the repository's full name.  (optional)
name = ['name_example'] # list[str] | Filters results by full name of the code repositories.  (optional)
compact = True # bool | Indicates if only minimal image data is to be sent (i.e., vulnerabilities, compliance, and extended image metadata should be skipped) (true) or not (false).  (optional)
_from = '2013-10-20T19:20:30+01:00' # datetime | Filters results by starting datetime. Based on the last scan update time.  (optional)
to = '2013-10-20T19:20:30+01:00' # datetime | Filters results by end datetime. Based on the last scan update time.  (optional)

    try:
        api_response = api_instance.api_v1_coderepos_ci_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, credential_id=credential_id, id=id, name=name, compact=compact, _from=_from, to=to)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CodereposCiApi->api_v1_coderepos_ci_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Offset from the start of the list from which to retrieve documents.  | [optional] 
 **limit** | **int**| Number of documents to return.  | [optional] 
 **search** | **str**| Search term.  | [optional] 
 **sort** | **str**| Key on which to sort.  | [optional] 
 **reverse** | **bool**| Sort order.  | [optional] 
 **collections** | [**list[str]**](str.md)| Scopes the query by collection.  | [optional] 
 **account_ids** | [**list[str]**](str.md)| Scopes the query by account ID.  | [optional] 
 **fields** | [**list[str]**](str.md)| List of fields to retrieve.  | [optional] 
 **credential_id** | **str**| ID of the requested credential, used for code repo scans.  | [optional] 
 **id** | [**list[str]**](str.md)| Filters results by code repository ID. The ID is the repository&#39;s full name.  | [optional] 
 **name** | [**list[str]**](str.md)| Filters results by full name of the code repositories.  | [optional] 
 **compact** | **bool**| Indicates if only minimal image data is to be sent (i.e., vulnerabilities, compliance, and extended image metadata should be skipped) (true) or not (false).  | [optional] 
 **_from** | **datetime**| Filters results by starting datetime. Based on the last scan update time.  | [optional] 
 **to** | **datetime**| Filters results by end datetime. Based on the last scan update time.  | [optional] 

### Return type

[**list[CodereposScanResult]**](CodereposScanResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_coderepos_ci_post**
> api_v1_coderepos_ci_post(coderepos_scan_result=coderepos_scan_result)



AddCICodeRepo adds a CI code repo scan result 

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CodereposCiApi(api_client)
    coderepos_scan_result = openapi_client.CodereposScanResult() # CodereposScanResult |  (optional)

    try:
        api_instance.api_v1_coderepos_ci_post(coderepos_scan_result=coderepos_scan_result)
    except ApiException as e:
        print("Exception when calling CodereposCiApi->api_v1_coderepos_ci_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coderepos_scan_result** | [**CodereposScanResult**](CodereposScanResult.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# openapi_client.CodereposApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_coderepos_discover_get**](CodereposApi.md#api_v1_coderepos_discover_get) | **GET** /api/v1/coderepos/discover | 
[**api_v1_coderepos_download_get**](CodereposApi.md#api_v1_coderepos_download_get) | **GET** /api/v1/coderepos/download | 
[**api_v1_coderepos_get**](CodereposApi.md#api_v1_coderepos_get) | **GET** /api/v1/coderepos | 
[**api_v1_coderepos_progress_get**](CodereposApi.md#api_v1_coderepos_progress_get) | **GET** /api/v1/coderepos/progress | 
[**api_v1_coderepos_scan_post**](CodereposApi.md#api_v1_coderepos_scan_post) | **POST** /api/v1/coderepos/scan | 
[**api_v1_coderepos_stop_post**](CodereposApi.md#api_v1_coderepos_stop_post) | **POST** /api/v1/coderepos/stop | 
[**api_v1_coderepos_webhook_post**](CodereposApi.md#api_v1_coderepos_webhook_post) | **POST** /api/v1/coderepos/webhook/ | 


# **api_v1_coderepos_discover_get**
> list[str] api_v1_coderepos_discover_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, credential_id=credential_id, id=id, name=name, compact=compact, _from=_from, to=to)



DiscoverCodeRepos discovers the available repositories for a credential according to the given credential ID 

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
    api_instance = openapi_client.CodereposApi(api_client)
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
        api_response = api_instance.api_v1_coderepos_discover_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, credential_id=credential_id, id=id, name=name, compact=compact, _from=_from, to=to)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CodereposApi->api_v1_coderepos_discover_get: %s\n" % e)
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

**list[str]**

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

# **api_v1_coderepos_download_get**
> api_v1_coderepos_download_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, credential_id=credential_id, id=id, name=name, compact=compact, _from=_from, to=to)



DownloadCodeRepos downloads code repository scan results 

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
    api_instance = openapi_client.CodereposApi(api_client)
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
        api_instance.api_v1_coderepos_download_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, credential_id=credential_id, id=id, name=name, compact=compact, _from=_from, to=to)
    except ApiException as e:
        print("Exception when calling CodereposApi->api_v1_coderepos_download_get: %s\n" % e)
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

# **api_v1_coderepos_get**
> list[CodereposScanResult] api_v1_coderepos_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, credential_id=credential_id, id=id, name=name, compact=compact, _from=_from, to=to)



CodeRepos returns code repositories scan results 

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
    api_instance = openapi_client.CodereposApi(api_client)
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
        api_response = api_instance.api_v1_coderepos_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, credential_id=credential_id, id=id, name=name, compact=compact, _from=_from, to=to)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CodereposApi->api_v1_coderepos_get: %s\n" % e)
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

# **api_v1_coderepos_progress_get**
> list[SharedProgress] api_v1_coderepos_progress_get()



CodeRepoScanProgress returns the code repositories scan progress 

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
    api_instance = openapi_client.CodereposApi(api_client)
    
    try:
        api_response = api_instance.api_v1_coderepos_progress_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CodereposApi->api_v1_coderepos_progress_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SharedProgress]**](SharedProgress.md)

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

# **api_v1_coderepos_scan_post**
> api_v1_coderepos_scan_post()



ScanCodeRepos triggers a scan for all code repositories 

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
    api_instance = openapi_client.CodereposApi(api_client)
    
    try:
        api_instance.api_v1_coderepos_scan_post()
    except ApiException as e:
        print("Exception when calling CodereposApi->api_v1_coderepos_scan_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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

# **api_v1_coderepos_stop_post**
> api_v1_coderepos_stop_post()



StopCodeReposScan stops the current active scan 

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
    api_instance = openapi_client.CodereposApi(api_client)
    
    try:
        api_instance.api_v1_coderepos_stop_post()
    except ApiException as e:
        print("Exception when calling CodereposApi->api_v1_coderepos_stop_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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

# **api_v1_coderepos_webhook_post**
> api_v1_coderepos_webhook_post()



CodeReposWebhook handles events from code repositories 

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
    api_instance = openapi_client.CodereposApi(api_client)
    
    try:
        api_instance.api_v1_coderepos_webhook_post()
    except ApiException as e:
        print("Exception when calling CodereposApi->api_v1_coderepos_webhook_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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


# openapi_client.HostsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_hosts_download_get**](HostsApi.md#api_v1_hosts_download_get) | **GET** /api/v1/hosts/download | 
[**api_v1_hosts_evaluate_post**](HostsApi.md#api_v1_hosts_evaluate_post) | **POST** /api/v1/hosts/evaluate | 
[**api_v1_hosts_get**](HostsApi.md#api_v1_hosts_get) | **GET** /api/v1/hosts | 
[**api_v1_hosts_info_get**](HostsApi.md#api_v1_hosts_info_get) | **GET** /api/v1/hosts/info | 
[**api_v1_hosts_scan_post**](HostsApi.md#api_v1_hosts_scan_post) | **POST** /api/v1/hosts/scan | 


# **api_v1_hosts_download_get**
> api_v1_hosts_download_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, hostname=hostname, distro=distro, provider=provider, compact=compact, clusters=clusters, compliance_ids=compliance_ids)



DownloadHosts downloads the hosts data 

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
    api_instance = openapi_client.HostsApi(api_client)
    offset = 56 # int | Offset from the start of the list from which to retrieve documents.  (optional)
limit = 56 # int | Number of documents to return.  (optional)
search = 'search_example' # str | Search term.  (optional)
sort = 'sort_example' # str | Key on which to sort.  (optional)
reverse = True # bool | Sort order.  (optional)
collections = ['collections_example'] # list[str] | Scopes the query by collection.  (optional)
account_ids = ['account_ids_example'] # list[str] | Scopes the query by account ID.  (optional)
fields = ['fields_example'] # list[str] | List of fields to retrieve.  (optional)
hostname = ['hostname_example'] # list[str] | Filters results by hostname.  (optional)
distro = ['distro_example'] # list[str] | Filters results by OS distro.  (optional)
provider = ['provider_example'] # list[str] | Filters results by cloud provider.  (optional)
compact = True # bool | Indicates if only minimal image data is to be sent (i.e., vulnerabilities, compliance, and extended image metadata should be skipped) (true) or not (false).  (optional)
clusters = ['clusters_example'] # list[str] | Filters results by cluster name.  (optional)
compliance_ids = [56] # list[int] | Filters results by compliance ID.  (optional)

    try:
        api_instance.api_v1_hosts_download_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, hostname=hostname, distro=distro, provider=provider, compact=compact, clusters=clusters, compliance_ids=compliance_ids)
    except ApiException as e:
        print("Exception when calling HostsApi->api_v1_hosts_download_get: %s\n" % e)
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
 **hostname** | [**list[str]**](str.md)| Filters results by hostname.  | [optional] 
 **distro** | [**list[str]**](str.md)| Filters results by OS distro.  | [optional] 
 **provider** | [**list[str]**](str.md)| Filters results by cloud provider.  | [optional] 
 **compact** | **bool**| Indicates if only minimal image data is to be sent (i.e., vulnerabilities, compliance, and extended image metadata should be skipped) (true) or not (false).  | [optional] 
 **clusters** | [**list[str]**](str.md)| Filters results by cluster name.  | [optional] 
 **compliance_ids** | [**list[int]**](int.md)| Filters results by compliance ID.  | [optional] 

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

# **api_v1_hosts_evaluate_post**
> ApiResolveImagesResp api_v1_hosts_evaluate_post(api_resolve_images_req=api_resolve_images_req)



ResolveHosts adds vulnerability data for the given host 

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
    api_instance = openapi_client.HostsApi(api_client)
    api_resolve_images_req = openapi_client.ApiResolveImagesReq() # ApiResolveImagesReq |  (optional)

    try:
        api_response = api_instance.api_v1_hosts_evaluate_post(api_resolve_images_req=api_resolve_images_req)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling HostsApi->api_v1_hosts_evaluate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_resolve_images_req** | [**ApiResolveImagesReq**](ApiResolveImagesReq.md)|  | [optional] 

### Return type

[**ApiResolveImagesResp**](ApiResolveImagesResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ResolveImagesResp represents the images resolution API output |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_hosts_get**
> list[SharedImageScanResult] api_v1_hosts_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, hostname=hostname, distro=distro, provider=provider, compact=compact, clusters=clusters, compliance_ids=compliance_ids)



Hosts returns the hosts scan result 

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
    api_instance = openapi_client.HostsApi(api_client)
    offset = 56 # int | Offset from the start of the list from which to retrieve documents.  (optional)
limit = 56 # int | Number of documents to return.  (optional)
search = 'search_example' # str | Search term.  (optional)
sort = 'sort_example' # str | Key on which to sort.  (optional)
reverse = True # bool | Sort order.  (optional)
collections = ['collections_example'] # list[str] | Scopes the query by collection.  (optional)
account_ids = ['account_ids_example'] # list[str] | Scopes the query by account ID.  (optional)
fields = ['fields_example'] # list[str] | List of fields to retrieve.  (optional)
hostname = ['hostname_example'] # list[str] | Filters results by hostname.  (optional)
distro = ['distro_example'] # list[str] | Filters results by OS distro.  (optional)
provider = ['provider_example'] # list[str] | Filters results by cloud provider.  (optional)
compact = True # bool | Indicates if only minimal image data is to be sent (i.e., vulnerabilities, compliance, and extended image metadata should be skipped) (true) or not (false).  (optional)
clusters = ['clusters_example'] # list[str] | Filters results by cluster name.  (optional)
compliance_ids = [56] # list[int] | Filters results by compliance ID.  (optional)

    try:
        api_response = api_instance.api_v1_hosts_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, hostname=hostname, distro=distro, provider=provider, compact=compact, clusters=clusters, compliance_ids=compliance_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling HostsApi->api_v1_hosts_get: %s\n" % e)
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
 **hostname** | [**list[str]**](str.md)| Filters results by hostname.  | [optional] 
 **distro** | [**list[str]**](str.md)| Filters results by OS distro.  | [optional] 
 **provider** | [**list[str]**](str.md)| Filters results by cloud provider.  | [optional] 
 **compact** | **bool**| Indicates if only minimal image data is to be sent (i.e., vulnerabilities, compliance, and extended image metadata should be skipped) (true) or not (false).  | [optional] 
 **clusters** | [**list[str]**](str.md)| Filters results by cluster name.  | [optional] 
 **compliance_ids** | [**list[int]**](int.md)| Filters results by compliance ID.  | [optional] 

### Return type

[**list[SharedImageScanResult]**](SharedImageScanResult.md)

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

# **api_v1_hosts_info_get**
> list[SharedHostInfo] api_v1_hosts_info_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, hostname=hostname, distro=distro, provider=provider, compact=compact, clusters=clusters, compliance_ids=compliance_ids)



HostsInfo returns information about all deployed hosts 

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
    api_instance = openapi_client.HostsApi(api_client)
    offset = 56 # int | Offset from the start of the list from which to retrieve documents.  (optional)
limit = 56 # int | Number of documents to return.  (optional)
search = 'search_example' # str | Search term.  (optional)
sort = 'sort_example' # str | Key on which to sort.  (optional)
reverse = True # bool | Sort order.  (optional)
collections = ['collections_example'] # list[str] | Scopes the query by collection.  (optional)
account_ids = ['account_ids_example'] # list[str] | Scopes the query by account ID.  (optional)
fields = ['fields_example'] # list[str] | List of fields to retrieve.  (optional)
hostname = ['hostname_example'] # list[str] | Filters results by hostname.  (optional)
distro = ['distro_example'] # list[str] | Filters results by OS distro.  (optional)
provider = ['provider_example'] # list[str] | Filters results by cloud provider.  (optional)
compact = True # bool | Indicates if only minimal image data is to be sent (i.e., vulnerabilities, compliance, and extended image metadata should be skipped) (true) or not (false).  (optional)
clusters = ['clusters_example'] # list[str] | Filters results by cluster name.  (optional)
compliance_ids = [56] # list[int] | Filters results by compliance ID.  (optional)

    try:
        api_response = api_instance.api_v1_hosts_info_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, hostname=hostname, distro=distro, provider=provider, compact=compact, clusters=clusters, compliance_ids=compliance_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling HostsApi->api_v1_hosts_info_get: %s\n" % e)
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
 **hostname** | [**list[str]**](str.md)| Filters results by hostname.  | [optional] 
 **distro** | [**list[str]**](str.md)| Filters results by OS distro.  | [optional] 
 **provider** | [**list[str]**](str.md)| Filters results by cloud provider.  | [optional] 
 **compact** | **bool**| Indicates if only minimal image data is to be sent (i.e., vulnerabilities, compliance, and extended image metadata should be skipped) (true) or not (false).  | [optional] 
 **clusters** | [**list[str]**](str.md)| Filters results by cluster name.  | [optional] 
 **compliance_ids** | [**list[int]**](int.md)| Filters results by compliance ID.  | [optional] 

### Return type

[**list[SharedHostInfo]**](SharedHostInfo.md)

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

# **api_v1_hosts_scan_post**
> api_v1_hosts_scan_post()



ScanHosts sends a host scan requests to all defenders 

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
    api_instance = openapi_client.HostsApi(api_client)
    
    try:
        api_instance.api_v1_hosts_scan_post()
    except ApiException as e:
        print("Exception when calling HostsApi->api_v1_hosts_scan_post: %s\n" % e)
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


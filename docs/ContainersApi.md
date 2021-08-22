# openapi_client.ContainersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_containers_count_get**](ContainersApi.md#api_v1_containers_count_get) | **GET** /api/v1/containers/count | 
[**api_v1_containers_download_get**](ContainersApi.md#api_v1_containers_download_get) | **GET** /api/v1/containers/download | 
[**api_v1_containers_get**](ContainersApi.md#api_v1_containers_get) | **GET** /api/v1/containers | 
[**api_v1_containers_names_get**](ContainersApi.md#api_v1_containers_names_get) | **GET** /api/v1/containers/names | 
[**api_v1_containers_scan_post**](ContainersApi.md#api_v1_containers_scan_post) | **POST** /api/v1/containers/scan | 


# **api_v1_containers_count_get**
> int api_v1_containers_count_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, hostname=hostname, image=image, image_id=image_id, id=id, profile_id=profile_id, namespaces=namespaces, clusters=clusters, compliance_ids=compliance_ids)



ContainerCount returns the total number of containers 

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
    api_instance = openapi_client.ContainersApi(api_client)
    offset = 56 # int | Offset from the start of the list from which to retrieve documents.  (optional)
limit = 56 # int | Number of documents to return.  (optional)
search = 'search_example' # str | Search term.  (optional)
sort = 'sort_example' # str | Key on which to sort.  (optional)
reverse = True # bool | Sort order.  (optional)
collections = ['collections_example'] # list[str] | Scopes the query by collection.  (optional)
account_ids = ['account_ids_example'] # list[str] | Scopes the query by account ID.  (optional)
fields = ['fields_example'] # list[str] | List of fields to retrieve.  (optional)
hostname = ['hostname_example'] # list[str] | Hosts is used to filter containers by host.  (optional)
image = ['image_example'] # list[str] | Images is used to filter containers by image name.  (optional)
image_id = ['image_id_example'] # list[str] | ImageIDs is used to filter containers by image ids.  (optional)
id = ['id_example'] # list[str] | IDs is used to filter container by container ID.  (optional)
profile_id = ['profile_id_example'] # list[str] | ProfileIDs is used to filter container by runtime profile ID.  (optional)
namespaces = ['namespaces_example'] # list[str] | Namespaces are the namespaces to filter.  (optional)
clusters = ['clusters_example'] # list[str] | Clusters is used to filter containers by cluster name.  (optional)
compliance_ids = [56] # list[int] | ComplianceIDs is used to filter containers by compliance IDs.  (optional)

    try:
        api_response = api_instance.api_v1_containers_count_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, hostname=hostname, image=image, image_id=image_id, id=id, profile_id=profile_id, namespaces=namespaces, clusters=clusters, compliance_ids=compliance_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContainersApi->api_v1_containers_count_get: %s\n" % e)
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
 **hostname** | [**list[str]**](str.md)| Hosts is used to filter containers by host.  | [optional] 
 **image** | [**list[str]**](str.md)| Images is used to filter containers by image name.  | [optional] 
 **image_id** | [**list[str]**](str.md)| ImageIDs is used to filter containers by image ids.  | [optional] 
 **id** | [**list[str]**](str.md)| IDs is used to filter container by container ID.  | [optional] 
 **profile_id** | [**list[str]**](str.md)| ProfileIDs is used to filter container by runtime profile ID.  | [optional] 
 **namespaces** | [**list[str]**](str.md)| Namespaces are the namespaces to filter.  | [optional] 
 **clusters** | [**list[str]**](str.md)| Clusters is used to filter containers by cluster name.  | [optional] 
 **compliance_ids** | [**list[int]**](int.md)| ComplianceIDs is used to filter containers by compliance IDs.  | [optional] 

### Return type

**int**

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

# **api_v1_containers_download_get**
> api_v1_containers_download_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, hostname=hostname, image=image, image_id=image_id, id=id, profile_id=profile_id, namespaces=namespaces, clusters=clusters, compliance_ids=compliance_ids)



DownloadContainers downloads the container scan results 

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
    api_instance = openapi_client.ContainersApi(api_client)
    offset = 56 # int | Offset from the start of the list from which to retrieve documents.  (optional)
limit = 56 # int | Number of documents to return.  (optional)
search = 'search_example' # str | Search term.  (optional)
sort = 'sort_example' # str | Key on which to sort.  (optional)
reverse = True # bool | Sort order.  (optional)
collections = ['collections_example'] # list[str] | Scopes the query by collection.  (optional)
account_ids = ['account_ids_example'] # list[str] | Scopes the query by account ID.  (optional)
fields = ['fields_example'] # list[str] | List of fields to retrieve.  (optional)
hostname = ['hostname_example'] # list[str] | Hosts is used to filter containers by host.  (optional)
image = ['image_example'] # list[str] | Images is used to filter containers by image name.  (optional)
image_id = ['image_id_example'] # list[str] | ImageIDs is used to filter containers by image ids.  (optional)
id = ['id_example'] # list[str] | IDs is used to filter container by container ID.  (optional)
profile_id = ['profile_id_example'] # list[str] | ProfileIDs is used to filter container by runtime profile ID.  (optional)
namespaces = ['namespaces_example'] # list[str] | Namespaces are the namespaces to filter.  (optional)
clusters = ['clusters_example'] # list[str] | Clusters is used to filter containers by cluster name.  (optional)
compliance_ids = [56] # list[int] | ComplianceIDs is used to filter containers by compliance IDs.  (optional)

    try:
        api_instance.api_v1_containers_download_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, hostname=hostname, image=image, image_id=image_id, id=id, profile_id=profile_id, namespaces=namespaces, clusters=clusters, compliance_ids=compliance_ids)
    except ApiException as e:
        print("Exception when calling ContainersApi->api_v1_containers_download_get: %s\n" % e)
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
 **hostname** | [**list[str]**](str.md)| Hosts is used to filter containers by host.  | [optional] 
 **image** | [**list[str]**](str.md)| Images is used to filter containers by image name.  | [optional] 
 **image_id** | [**list[str]**](str.md)| ImageIDs is used to filter containers by image ids.  | [optional] 
 **id** | [**list[str]**](str.md)| IDs is used to filter container by container ID.  | [optional] 
 **profile_id** | [**list[str]**](str.md)| ProfileIDs is used to filter container by runtime profile ID.  | [optional] 
 **namespaces** | [**list[str]**](str.md)| Namespaces are the namespaces to filter.  | [optional] 
 **clusters** | [**list[str]**](str.md)| Clusters is used to filter containers by cluster name.  | [optional] 
 **compliance_ids** | [**list[int]**](int.md)| ComplianceIDs is used to filter containers by compliance IDs.  | [optional] 

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

# **api_v1_containers_get**
> list[SharedContainerScanResult] api_v1_containers_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, hostname=hostname, image=image, image_id=image_id, id=id, profile_id=profile_id, namespaces=namespaces, clusters=clusters, compliance_ids=compliance_ids)



Containers returns the container scan results 

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
    api_instance = openapi_client.ContainersApi(api_client)
    offset = 56 # int | Offset from the start of the list from which to retrieve documents.  (optional)
limit = 56 # int | Number of documents to return.  (optional)
search = 'search_example' # str | Search term.  (optional)
sort = 'sort_example' # str | Key on which to sort.  (optional)
reverse = True # bool | Sort order.  (optional)
collections = ['collections_example'] # list[str] | Scopes the query by collection.  (optional)
account_ids = ['account_ids_example'] # list[str] | Scopes the query by account ID.  (optional)
fields = ['fields_example'] # list[str] | List of fields to retrieve.  (optional)
hostname = ['hostname_example'] # list[str] | Hosts is used to filter containers by host.  (optional)
image = ['image_example'] # list[str] | Images is used to filter containers by image name.  (optional)
image_id = ['image_id_example'] # list[str] | ImageIDs is used to filter containers by image ids.  (optional)
id = ['id_example'] # list[str] | IDs is used to filter container by container ID.  (optional)
profile_id = ['profile_id_example'] # list[str] | ProfileIDs is used to filter container by runtime profile ID.  (optional)
namespaces = ['namespaces_example'] # list[str] | Namespaces are the namespaces to filter.  (optional)
clusters = ['clusters_example'] # list[str] | Clusters is used to filter containers by cluster name.  (optional)
compliance_ids = [56] # list[int] | ComplianceIDs is used to filter containers by compliance IDs.  (optional)

    try:
        api_response = api_instance.api_v1_containers_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, hostname=hostname, image=image, image_id=image_id, id=id, profile_id=profile_id, namespaces=namespaces, clusters=clusters, compliance_ids=compliance_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContainersApi->api_v1_containers_get: %s\n" % e)
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
 **hostname** | [**list[str]**](str.md)| Hosts is used to filter containers by host.  | [optional] 
 **image** | [**list[str]**](str.md)| Images is used to filter containers by image name.  | [optional] 
 **image_id** | [**list[str]**](str.md)| ImageIDs is used to filter containers by image ids.  | [optional] 
 **id** | [**list[str]**](str.md)| IDs is used to filter container by container ID.  | [optional] 
 **profile_id** | [**list[str]**](str.md)| ProfileIDs is used to filter container by runtime profile ID.  | [optional] 
 **namespaces** | [**list[str]**](str.md)| Namespaces are the namespaces to filter.  | [optional] 
 **clusters** | [**list[str]**](str.md)| Clusters is used to filter containers by cluster name.  | [optional] 
 **compliance_ids** | [**list[int]**](int.md)| ComplianceIDs is used to filter containers by compliance IDs.  | [optional] 

### Return type

[**list[SharedContainerScanResult]**](SharedContainerScanResult.md)

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

# **api_v1_containers_names_get**
> list[str] api_v1_containers_names_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, hostname=hostname, image=image, image_id=image_id, id=id, profile_id=profile_id, namespaces=namespaces, clusters=clusters, compliance_ids=compliance_ids)



ContainerNames returns container names according to the query specification 

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
    api_instance = openapi_client.ContainersApi(api_client)
    offset = 56 # int | Offset from the start of the list from which to retrieve documents.  (optional)
limit = 56 # int | Number of documents to return.  (optional)
search = 'search_example' # str | Search term.  (optional)
sort = 'sort_example' # str | Key on which to sort.  (optional)
reverse = True # bool | Sort order.  (optional)
collections = ['collections_example'] # list[str] | Scopes the query by collection.  (optional)
account_ids = ['account_ids_example'] # list[str] | Scopes the query by account ID.  (optional)
fields = ['fields_example'] # list[str] | List of fields to retrieve.  (optional)
hostname = ['hostname_example'] # list[str] | Hosts is used to filter containers by host.  (optional)
image = ['image_example'] # list[str] | Images is used to filter containers by image name.  (optional)
image_id = ['image_id_example'] # list[str] | ImageIDs is used to filter containers by image ids.  (optional)
id = ['id_example'] # list[str] | IDs is used to filter container by container ID.  (optional)
profile_id = ['profile_id_example'] # list[str] | ProfileIDs is used to filter container by runtime profile ID.  (optional)
namespaces = ['namespaces_example'] # list[str] | Namespaces are the namespaces to filter.  (optional)
clusters = ['clusters_example'] # list[str] | Clusters is used to filter containers by cluster name.  (optional)
compliance_ids = [56] # list[int] | ComplianceIDs is used to filter containers by compliance IDs.  (optional)

    try:
        api_response = api_instance.api_v1_containers_names_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, hostname=hostname, image=image, image_id=image_id, id=id, profile_id=profile_id, namespaces=namespaces, clusters=clusters, compliance_ids=compliance_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContainersApi->api_v1_containers_names_get: %s\n" % e)
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
 **hostname** | [**list[str]**](str.md)| Hosts is used to filter containers by host.  | [optional] 
 **image** | [**list[str]**](str.md)| Images is used to filter containers by image name.  | [optional] 
 **image_id** | [**list[str]**](str.md)| ImageIDs is used to filter containers by image ids.  | [optional] 
 **id** | [**list[str]**](str.md)| IDs is used to filter container by container ID.  | [optional] 
 **profile_id** | [**list[str]**](str.md)| ProfileIDs is used to filter container by runtime profile ID.  | [optional] 
 **namespaces** | [**list[str]**](str.md)| Namespaces are the namespaces to filter.  | [optional] 
 **clusters** | [**list[str]**](str.md)| Clusters is used to filter containers by cluster name.  | [optional] 
 **compliance_ids** | [**list[int]**](int.md)| ComplianceIDs is used to filter containers by compliance IDs.  | [optional] 

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

# **api_v1_containers_scan_post**
> api_v1_containers_scan_post()



ScanContainers triggers a scan to all containers 

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
    api_instance = openapi_client.ContainersApi(api_client)
    
    try:
        api_instance.api_v1_containers_scan_post()
    except ApiException as e:
        print("Exception when calling ContainersApi->api_v1_containers_scan_post: %s\n" % e)
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


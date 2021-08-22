# openapi_client.VmsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_vms_download_get**](VmsApi.md#api_v1_vms_download_get) | **GET** /api/v1/vms/download | 
[**api_v1_vms_get**](VmsApi.md#api_v1_vms_get) | **GET** /api/v1/vms | 
[**api_v1_vms_labels_get**](VmsApi.md#api_v1_vms_labels_get) | **GET** /api/v1/vms/labels | 
[**api_v1_vms_names_get**](VmsApi.md#api_v1_vms_names_get) | **GET** /api/v1/vms/names | 
[**api_v1_vms_progress_get**](VmsApi.md#api_v1_vms_progress_get) | **GET** /api/v1/vms/progress | 
[**api_v1_vms_scan_post**](VmsApi.md#api_v1_vms_scan_post) | **POST** /api/v1/vms/scan | 
[**api_v1_vms_stop_post**](VmsApi.md#api_v1_vms_stop_post) | **POST** /api/v1/vms/stop | 


# **api_v1_vms_download_get**
> api_v1_vms_download_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, id=id, name=name, region=region, credential=credential, distro=distro)



DownloadVMs downloads the VM images data 

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
    api_instance = openapi_client.VmsApi(api_client)
    offset = 56 # int | Offset from the start of the list from which to retrieve documents.  (optional)
limit = 56 # int | Number of documents to return.  (optional)
search = 'search_example' # str | Search term.  (optional)
sort = 'sort_example' # str | Key on which to sort.  (optional)
reverse = True # bool | Sort order.  (optional)
collections = ['collections_example'] # list[str] | Scopes the query by collection.  (optional)
account_ids = ['account_ids_example'] # list[str] | Scopes the query by account ID.  (optional)
fields = ['fields_example'] # list[str] | List of fields to retrieve.  (optional)
id = ['id_example'] # list[str] | Filters results by ID of the VM.  (optional)
name = ['name_example'] # list[str] | Filters results by image name.  (optional)
region = ['region_example'] # list[str] | Filters results by region.  (optional)
credential = ['credential_example'] # list[str] | Filters results by credential.  (optional)
distro = ['distro_example'] # list[str] | Filters results by OS distro.  (optional)

    try:
        api_instance.api_v1_vms_download_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, id=id, name=name, region=region, credential=credential, distro=distro)
    except ApiException as e:
        print("Exception when calling VmsApi->api_v1_vms_download_get: %s\n" % e)
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
 **id** | [**list[str]**](str.md)| Filters results by ID of the VM.  | [optional] 
 **name** | [**list[str]**](str.md)| Filters results by image name.  | [optional] 
 **region** | [**list[str]**](str.md)| Filters results by region.  | [optional] 
 **credential** | [**list[str]**](str.md)| Filters results by credential.  | [optional] 
 **distro** | [**list[str]**](str.md)| Filters results by OS distro.  | [optional] 

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

# **api_v1_vms_get**
> list[SharedImageScanResult] api_v1_vms_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, id=id, name=name, region=region, credential=credential, distro=distro)



VMs returns images by the query specification 

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
    api_instance = openapi_client.VmsApi(api_client)
    offset = 56 # int | Offset from the start of the list from which to retrieve documents.  (optional)
limit = 56 # int | Number of documents to return.  (optional)
search = 'search_example' # str | Search term.  (optional)
sort = 'sort_example' # str | Key on which to sort.  (optional)
reverse = True # bool | Sort order.  (optional)
collections = ['collections_example'] # list[str] | Scopes the query by collection.  (optional)
account_ids = ['account_ids_example'] # list[str] | Scopes the query by account ID.  (optional)
fields = ['fields_example'] # list[str] | List of fields to retrieve.  (optional)
id = ['id_example'] # list[str] | Filters results by ID of the VM.  (optional)
name = ['name_example'] # list[str] | Filters results by image name.  (optional)
region = ['region_example'] # list[str] | Filters results by region.  (optional)
credential = ['credential_example'] # list[str] | Filters results by credential.  (optional)
distro = ['distro_example'] # list[str] | Filters results by OS distro.  (optional)

    try:
        api_response = api_instance.api_v1_vms_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, id=id, name=name, region=region, credential=credential, distro=distro)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VmsApi->api_v1_vms_get: %s\n" % e)
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
 **id** | [**list[str]**](str.md)| Filters results by ID of the VM.  | [optional] 
 **name** | [**list[str]**](str.md)| Filters results by image name.  | [optional] 
 **region** | [**list[str]**](str.md)| Filters results by region.  | [optional] 
 **credential** | [**list[str]**](str.md)| Filters results by credential.  | [optional] 
 **distro** | [**list[str]**](str.md)| Filters results by OS distro.  | [optional] 

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

# **api_v1_vms_labels_get**
> list[str] api_v1_vms_labels_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, id=id, name=name, region=region, credential=credential, distro=distro)



VMLabels returns VM labels according to the query specification 

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
    api_instance = openapi_client.VmsApi(api_client)
    offset = 56 # int | Offset from the start of the list from which to retrieve documents.  (optional)
limit = 56 # int | Number of documents to return.  (optional)
search = 'search_example' # str | Search term.  (optional)
sort = 'sort_example' # str | Key on which to sort.  (optional)
reverse = True # bool | Sort order.  (optional)
collections = ['collections_example'] # list[str] | Scopes the query by collection.  (optional)
account_ids = ['account_ids_example'] # list[str] | Scopes the query by account ID.  (optional)
fields = ['fields_example'] # list[str] | List of fields to retrieve.  (optional)
id = ['id_example'] # list[str] | Filters results by ID of the VM.  (optional)
name = ['name_example'] # list[str] | Filters results by image name.  (optional)
region = ['region_example'] # list[str] | Filters results by region.  (optional)
credential = ['credential_example'] # list[str] | Filters results by credential.  (optional)
distro = ['distro_example'] # list[str] | Filters results by OS distro.  (optional)

    try:
        api_response = api_instance.api_v1_vms_labels_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, id=id, name=name, region=region, credential=credential, distro=distro)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VmsApi->api_v1_vms_labels_get: %s\n" % e)
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
 **id** | [**list[str]**](str.md)| Filters results by ID of the VM.  | [optional] 
 **name** | [**list[str]**](str.md)| Filters results by image name.  | [optional] 
 **region** | [**list[str]**](str.md)| Filters results by region.  | [optional] 
 **credential** | [**list[str]**](str.md)| Filters results by credential.  | [optional] 
 **distro** | [**list[str]**](str.md)| Filters results by OS distro.  | [optional] 

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

# **api_v1_vms_names_get**
> list[str] api_v1_vms_names_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, id=id, name=name, region=region, credential=credential, distro=distro)



ImageNames returns image names according to the query specification 

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
    api_instance = openapi_client.VmsApi(api_client)
    offset = 56 # int | Offset from the start of the list from which to retrieve documents.  (optional)
limit = 56 # int | Number of documents to return.  (optional)
search = 'search_example' # str | Search term.  (optional)
sort = 'sort_example' # str | Key on which to sort.  (optional)
reverse = True # bool | Sort order.  (optional)
collections = ['collections_example'] # list[str] | Scopes the query by collection.  (optional)
account_ids = ['account_ids_example'] # list[str] | Scopes the query by account ID.  (optional)
fields = ['fields_example'] # list[str] | List of fields to retrieve.  (optional)
id = ['id_example'] # list[str] | Filters results by ID of the VM.  (optional)
name = ['name_example'] # list[str] | Filters results by image name.  (optional)
region = ['region_example'] # list[str] | Filters results by region.  (optional)
credential = ['credential_example'] # list[str] | Filters results by credential.  (optional)
distro = ['distro_example'] # list[str] | Filters results by OS distro.  (optional)

    try:
        api_response = api_instance.api_v1_vms_names_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, id=id, name=name, region=region, credential=credential, distro=distro)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VmsApi->api_v1_vms_names_get: %s\n" % e)
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
 **id** | [**list[str]**](str.md)| Filters results by ID of the VM.  | [optional] 
 **name** | [**list[str]**](str.md)| Filters results by image name.  | [optional] 
 **region** | [**list[str]**](str.md)| Filters results by region.  | [optional] 
 **credential** | [**list[str]**](str.md)| Filters results by credential.  | [optional] 
 **distro** | [**list[str]**](str.md)| Filters results by OS distro.  | [optional] 

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

# **api_v1_vms_progress_get**
> list[SharedProgress] api_v1_vms_progress_get()



VMScanProgress returns the VM images scan progress 

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
    api_instance = openapi_client.VmsApi(api_client)
    
    try:
        api_response = api_instance.api_v1_vms_progress_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VmsApi->api_v1_vms_progress_get: %s\n" % e)
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

# **api_v1_vms_scan_post**
> api_v1_vms_scan_post()



ScanVMs sends a VM scan request 

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
    api_instance = openapi_client.VmsApi(api_client)
    
    try:
        api_instance.api_v1_vms_scan_post()
    except ApiException as e:
        print("Exception when calling VmsApi->api_v1_vms_scan_post: %s\n" % e)
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

# **api_v1_vms_stop_post**
> api_v1_vms_stop_post()



StopVMsScan stops the currently running VMs scan 

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
    api_instance = openapi_client.VmsApi(api_client)
    
    try:
        api_instance.api_v1_vms_stop_post()
    except ApiException as e:
        print("Exception when calling VmsApi->api_v1_vms_stop_post: %s\n" % e)
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


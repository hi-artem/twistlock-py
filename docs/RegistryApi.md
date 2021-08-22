# openapi_client.RegistryApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_registry_download_get**](RegistryApi.md#api_v1_registry_download_get) | **GET** /api/v1/registry/download | 
[**api_v1_registry_get**](RegistryApi.md#api_v1_registry_get) | **GET** /api/v1/registry | 
[**api_v1_registry_names_get**](RegistryApi.md#api_v1_registry_names_get) | **GET** /api/v1/registry/names | 
[**api_v1_registry_scan_post**](RegistryApi.md#api_v1_registry_scan_post) | **POST** /api/v1/registry/scan | 
[**api_v1_registry_stop_post**](RegistryApi.md#api_v1_registry_stop_post) | **POST** /api/v1/registry/stop | 
[**api_v1_registry_webhook_webhook_delete**](RegistryApi.md#api_v1_registry_webhook_webhook_delete) | **DELETE** /api/v1/registry/webhook/webhook | 
[**api_v1_registry_webhook_webhook_post**](RegistryApi.md#api_v1_registry_webhook_webhook_post) | **POST** /api/v1/registry/webhook/webhook | 


# **api_v1_registry_download_get**
> api_v1_registry_download_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, id=id, image_id=image_id, repository=repository, registry=registry, name=name, layers=layers, compact=compact, filter_base_image=filter_base_image)



DownloadRegistryImages downloads the registry images data to CSVs 

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
    api_instance = openapi_client.RegistryApi(api_client)
    offset = 56 # int | Offset from the start of the list from which to retrieve documents.  (optional)
limit = 56 # int | Number of documents to return.  (optional)
search = 'search_example' # str | Search term.  (optional)
sort = 'sort_example' # str | Key on which to sort.  (optional)
reverse = True # bool | Sort order.  (optional)
collections = ['collections_example'] # list[str] | Scopes the query by collection.  (optional)
account_ids = ['account_ids_example'] # list[str] | Scopes the query by account ID.  (optional)
fields = ['fields_example'] # list[str] | List of fields to retrieve.  (optional)
id = ['id_example'] # list[str] | Filters results by registry image.  (optional)
image_id = ['image_id_example'] # list[str] | Filters results by image IDs (as they appear at the daemon).  (optional)
repository = ['repository_example'] # list[str] | Filters results by image repository.  (optional)
registry = ['registry_example'] # list[str] | Filters results by image registry.  (optional)
name = ['name_example'] # list[str] | Full image names on which to query.  (optional)
layers = True # bool | Indicates if CVEs are mapped to image layer (true) or not (false).  (optional)
compact = True # bool | Indicates if only minimal image data is to be returned (i.e., vulnerabilities, compliance, and extended image metadata should be skipped) (true) or not (false).  (optional)
filter_base_image = True # bool | Indicates if base image vulnerabilities are to be filtered (true) or not (false). Requires predefined base images that have already been scanned.  (optional)

    try:
        api_instance.api_v1_registry_download_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, id=id, image_id=image_id, repository=repository, registry=registry, name=name, layers=layers, compact=compact, filter_base_image=filter_base_image)
    except ApiException as e:
        print("Exception when calling RegistryApi->api_v1_registry_download_get: %s\n" % e)
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
 **id** | [**list[str]**](str.md)| Filters results by registry image.  | [optional] 
 **image_id** | [**list[str]**](str.md)| Filters results by image IDs (as they appear at the daemon).  | [optional] 
 **repository** | [**list[str]**](str.md)| Filters results by image repository.  | [optional] 
 **registry** | [**list[str]**](str.md)| Filters results by image registry.  | [optional] 
 **name** | [**list[str]**](str.md)| Full image names on which to query.  | [optional] 
 **layers** | **bool**| Indicates if CVEs are mapped to image layer (true) or not (false).  | [optional] 
 **compact** | **bool**| Indicates if only minimal image data is to be returned (i.e., vulnerabilities, compliance, and extended image metadata should be skipped) (true) or not (false).  | [optional] 
 **filter_base_image** | **bool**| Indicates if base image vulnerabilities are to be filtered (true) or not (false). Requires predefined base images that have already been scanned.  | [optional] 

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

# **api_v1_registry_get**
> list[SharedImageScanResult] api_v1_registry_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, id=id, image_id=image_id, repository=repository, registry=registry, name=name, layers=layers, compact=compact, filter_base_image=filter_base_image)



RegistryImages returns registry images 

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
    api_instance = openapi_client.RegistryApi(api_client)
    offset = 56 # int | Offset from the start of the list from which to retrieve documents.  (optional)
limit = 56 # int | Number of documents to return.  (optional)
search = 'search_example' # str | Search term.  (optional)
sort = 'sort_example' # str | Key on which to sort.  (optional)
reverse = True # bool | Sort order.  (optional)
collections = ['collections_example'] # list[str] | Scopes the query by collection.  (optional)
account_ids = ['account_ids_example'] # list[str] | Scopes the query by account ID.  (optional)
fields = ['fields_example'] # list[str] | List of fields to retrieve.  (optional)
id = ['id_example'] # list[str] | Filters results by registry image.  (optional)
image_id = ['image_id_example'] # list[str] | Filters results by image IDs (as they appear at the daemon).  (optional)
repository = ['repository_example'] # list[str] | Filters results by image repository.  (optional)
registry = ['registry_example'] # list[str] | Filters results by image registry.  (optional)
name = ['name_example'] # list[str] | Full image names on which to query.  (optional)
layers = True # bool | Indicates if CVEs are mapped to image layer (true) or not (false).  (optional)
compact = True # bool | Indicates if only minimal image data is to be returned (i.e., vulnerabilities, compliance, and extended image metadata should be skipped) (true) or not (false).  (optional)
filter_base_image = True # bool | Indicates if base image vulnerabilities are to be filtered (true) or not (false). Requires predefined base images that have already been scanned.  (optional)

    try:
        api_response = api_instance.api_v1_registry_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, id=id, image_id=image_id, repository=repository, registry=registry, name=name, layers=layers, compact=compact, filter_base_image=filter_base_image)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RegistryApi->api_v1_registry_get: %s\n" % e)
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
 **id** | [**list[str]**](str.md)| Filters results by registry image.  | [optional] 
 **image_id** | [**list[str]**](str.md)| Filters results by image IDs (as they appear at the daemon).  | [optional] 
 **repository** | [**list[str]**](str.md)| Filters results by image repository.  | [optional] 
 **registry** | [**list[str]**](str.md)| Filters results by image registry.  | [optional] 
 **name** | [**list[str]**](str.md)| Full image names on which to query.  | [optional] 
 **layers** | **bool**| Indicates if CVEs are mapped to image layer (true) or not (false).  | [optional] 
 **compact** | **bool**| Indicates if only minimal image data is to be returned (i.e., vulnerabilities, compliance, and extended image metadata should be skipped) (true) or not (false).  | [optional] 
 **filter_base_image** | **bool**| Indicates if base image vulnerabilities are to be filtered (true) or not (false). Requires predefined base images that have already been scanned.  | [optional] 

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

# **api_v1_registry_names_get**
> list[str] api_v1_registry_names_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, id=id, image_id=image_id, repository=repository, registry=registry, name=name, layers=layers, compact=compact, filter_base_image=filter_base_image)



RegistryImageNames returns registry scanned image names according to the query specification 

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
    api_instance = openapi_client.RegistryApi(api_client)
    offset = 56 # int | Offset from the start of the list from which to retrieve documents.  (optional)
limit = 56 # int | Number of documents to return.  (optional)
search = 'search_example' # str | Search term.  (optional)
sort = 'sort_example' # str | Key on which to sort.  (optional)
reverse = True # bool | Sort order.  (optional)
collections = ['collections_example'] # list[str] | Scopes the query by collection.  (optional)
account_ids = ['account_ids_example'] # list[str] | Scopes the query by account ID.  (optional)
fields = ['fields_example'] # list[str] | List of fields to retrieve.  (optional)
id = ['id_example'] # list[str] | Filters results by registry image.  (optional)
image_id = ['image_id_example'] # list[str] | Filters results by image IDs (as they appear at the daemon).  (optional)
repository = ['repository_example'] # list[str] | Filters results by image repository.  (optional)
registry = ['registry_example'] # list[str] | Filters results by image registry.  (optional)
name = ['name_example'] # list[str] | Full image names on which to query.  (optional)
layers = True # bool | Indicates if CVEs are mapped to image layer (true) or not (false).  (optional)
compact = True # bool | Indicates if only minimal image data is to be returned (i.e., vulnerabilities, compliance, and extended image metadata should be skipped) (true) or not (false).  (optional)
filter_base_image = True # bool | Indicates if base image vulnerabilities are to be filtered (true) or not (false). Requires predefined base images that have already been scanned.  (optional)

    try:
        api_response = api_instance.api_v1_registry_names_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, id=id, image_id=image_id, repository=repository, registry=registry, name=name, layers=layers, compact=compact, filter_base_image=filter_base_image)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RegistryApi->api_v1_registry_names_get: %s\n" % e)
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
 **id** | [**list[str]**](str.md)| Filters results by registry image.  | [optional] 
 **image_id** | [**list[str]**](str.md)| Filters results by image IDs (as they appear at the daemon).  | [optional] 
 **repository** | [**list[str]**](str.md)| Filters results by image repository.  | [optional] 
 **registry** | [**list[str]**](str.md)| Filters results by image registry.  | [optional] 
 **name** | [**list[str]**](str.md)| Full image names on which to query.  | [optional] 
 **layers** | **bool**| Indicates if CVEs are mapped to image layer (true) or not (false).  | [optional] 
 **compact** | **bool**| Indicates if only minimal image data is to be returned (i.e., vulnerabilities, compliance, and extended image metadata should be skipped) (true) or not (false).  | [optional] 
 **filter_base_image** | **bool**| Indicates if base image vulnerabilities are to be filtered (true) or not (false). Requires predefined base images that have already been scanned.  | [optional] 

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

# **api_v1_registry_scan_post**
> api_v1_registry_scan_post(shared_registry_scan_request=shared_registry_scan_request)



ScanRegistry sends a registry scan request to all registry scanner defenders 

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
    api_instance = openapi_client.RegistryApi(api_client)
    shared_registry_scan_request = openapi_client.SharedRegistryScanRequest() # SharedRegistryScanRequest |  (optional)

    try:
        api_instance.api_v1_registry_scan_post(shared_registry_scan_request=shared_registry_scan_request)
    except ApiException as e:
        print("Exception when calling RegistryApi->api_v1_registry_scan_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shared_registry_scan_request** | [**SharedRegistryScanRequest**](SharedRegistryScanRequest.md)|  | [optional] 

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

# **api_v1_registry_stop_post**
> api_v1_registry_stop_post()



StopRegistryScan stops the currently running registry scan 

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
    api_instance = openapi_client.RegistryApi(api_client)
    
    try:
        api_instance.api_v1_registry_stop_post()
    except ApiException as e:
        print("Exception when calling RegistryApi->api_v1_registry_stop_post: %s\n" % e)
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

# **api_v1_registry_webhook_webhook_delete**
> api_v1_registry_webhook_webhook_delete()



RegistryWebhook listen to registry updates 

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
    api_instance = openapi_client.RegistryApi(api_client)
    
    try:
        api_instance.api_v1_registry_webhook_webhook_delete()
    except ApiException as e:
        print("Exception when calling RegistryApi->api_v1_registry_webhook_webhook_delete: %s\n" % e)
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

# **api_v1_registry_webhook_webhook_post**
> api_v1_registry_webhook_webhook_post(types_registry_webhook_request=types_registry_webhook_request)



RegistryWebhook listen to registry updates 

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
    api_instance = openapi_client.RegistryApi(api_client)
    types_registry_webhook_request = openapi_client.TypesRegistryWebhookRequest() # TypesRegistryWebhookRequest |  (optional)

    try:
        api_instance.api_v1_registry_webhook_webhook_post(types_registry_webhook_request=types_registry_webhook_request)
    except ApiException as e:
        print("Exception when calling RegistryApi->api_v1_registry_webhook_webhook_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **types_registry_webhook_request** | [**TypesRegistryWebhookRequest**](TypesRegistryWebhookRequest.md)|  | [optional] 

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


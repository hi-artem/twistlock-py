# openapi_client.CollectionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_collections_get**](CollectionsApi.md#api_v1_collections_get) | **GET** /api/v1/collections | 
[**api_v1_collections_id_delete**](CollectionsApi.md#api_v1_collections_id_delete) | **DELETE** /api/v1/collections/{id} | 
[**api_v1_collections_id_put**](CollectionsApi.md#api_v1_collections_id_put) | **PUT** /api/v1/collections/{id} | 
[**api_v1_collections_id_usages_get**](CollectionsApi.md#api_v1_collections_id_usages_get) | **GET** /api/v1/collections/{id}/usages | 
[**api_v1_collections_post**](CollectionsApi.md#api_v1_collections_post) | **POST** /api/v1/collections | 


# **api_v1_collections_get**
> list[CollectionCollection] api_v1_collections_get(exclude_prisma=exclude_prisma)



Collections returns a list of references to the used collections 

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
    api_instance = openapi_client.CollectionsApi(api_client)
    exclude_prisma = True # bool | ExcludePrisma indicates to exclude Prisma collections.  (optional)

    try:
        api_response = api_instance.api_v1_collections_get(exclude_prisma=exclude_prisma)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CollectionsApi->api_v1_collections_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exclude_prisma** | **bool**| ExcludePrisma indicates to exclude Prisma collections.  | [optional] 

### Return type

[**list[CollectionCollection]**](CollectionCollection.md)

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

# **api_v1_collections_id_delete**
> api_v1_collections_id_delete(id)



DeleteCollection deletes a collection 

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
    api_instance = openapi_client.CollectionsApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.api_v1_collections_id_delete(id)
    except ApiException as e:
        print("Exception when calling CollectionsApi->api_v1_collections_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

# **api_v1_collections_id_put**
> api_v1_collections_id_put(id, collection_collection=collection_collection)



UpdateCollection updates a collection 

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
    api_instance = openapi_client.CollectionsApi(api_client)
    id = 'id_example' # str | 
collection_collection = openapi_client.CollectionCollection() # CollectionCollection |  (optional)

    try:
        api_instance.api_v1_collections_id_put(id, collection_collection=collection_collection)
    except ApiException as e:
        print("Exception when calling CollectionsApi->api_v1_collections_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **collection_collection** | [**CollectionCollection**](CollectionCollection.md)|  | [optional] 

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

# **api_v1_collections_id_usages_get**
> list[CollectionUsage] api_v1_collections_id_usages_get(id)



CollectionUsages returns all usages of the queried collection 

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
    api_instance = openapi_client.CollectionsApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.api_v1_collections_id_usages_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CollectionsApi->api_v1_collections_id_usages_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**list[CollectionUsage]**](CollectionUsage.md)

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

# **api_v1_collections_post**
> api_v1_collections_post(collection_collection=collection_collection)



AddCollection adds the given collection 

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
    api_instance = openapi_client.CollectionsApi(api_client)
    collection_collection = openapi_client.CollectionCollection() # CollectionCollection |  (optional)

    try:
        api_instance.api_v1_collections_post(collection_collection=collection_collection)
    except ApiException as e:
        print("Exception when calling CollectionsApi->api_v1_collections_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_collection** | [**CollectionCollection**](CollectionCollection.md)|  | [optional] 

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


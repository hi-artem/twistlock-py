# openapi_client.GroupsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_groups_get**](GroupsApi.md#api_v1_groups_get) | **GET** /api/v1/groups | 
[**api_v1_groups_id_delete**](GroupsApi.md#api_v1_groups_id_delete) | **DELETE** /api/v1/groups/{id} | 
[**api_v1_groups_id_put**](GroupsApi.md#api_v1_groups_id_put) | **PUT** /api/v1/groups/{id} | 
[**api_v1_groups_names_get**](GroupsApi.md#api_v1_groups_names_get) | **GET** /api/v1/groups/names | 
[**api_v1_groups_post**](GroupsApi.md#api_v1_groups_post) | **POST** /api/v1/groups | 


# **api_v1_groups_get**
> list[TypesGroup] api_v1_groups_get()



Groups returns all user groups, if request was sent from secondary project - only project's groups are returned 

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
    api_instance = openapi_client.GroupsApi(api_client)
    
    try:
        api_response = api_instance.api_v1_groups_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupsApi->api_v1_groups_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[TypesGroup]**](TypesGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Groups represents a list of groups |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_groups_id_delete**
> api_v1_groups_id_delete(id)



DeleteGroup deletes the given group name 

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
    api_instance = openapi_client.GroupsApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.api_v1_groups_id_delete(id)
    except ApiException as e:
        print("Exception when calling GroupsApi->api_v1_groups_id_delete: %s\n" % e)
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

# **api_v1_groups_id_put**
> api_v1_groups_id_put(id, types_group=types_group)



UpdateGroup adds or update a group 

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
    api_instance = openapi_client.GroupsApi(api_client)
    id = 'id_example' # str | 
types_group = openapi_client.TypesGroup() # TypesGroup |  (optional)

    try:
        api_instance.api_v1_groups_id_put(id, types_group=types_group)
    except ApiException as e:
        print("Exception when calling GroupsApi->api_v1_groups_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **types_group** | [**TypesGroup**](TypesGroup.md)|  | [optional] 

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

# **api_v1_groups_names_get**
> list[str] api_v1_groups_names_get()



GroupNames returns all group names 

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
    api_instance = openapi_client.GroupsApi(api_client)
    
    try:
        api_response = api_instance.api_v1_groups_names_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupsApi->api_v1_groups_names_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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

# **api_v1_groups_post**
> api_v1_groups_post(types_group=types_group)



UpdateGroup adds or update a group 

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
    api_instance = openapi_client.GroupsApi(api_client)
    types_group = openapi_client.TypesGroup() # TypesGroup |  (optional)

    try:
        api_instance.api_v1_groups_post(types_group=types_group)
    except ApiException as e:
        print("Exception when calling GroupsApi->api_v1_groups_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **types_group** | [**TypesGroup**](TypesGroup.md)|  | [optional] 

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


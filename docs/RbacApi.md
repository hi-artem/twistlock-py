# openapi_client.RbacApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_rbac_roles_get**](RbacApi.md#api_v1_rbac_roles_get) | **GET** /api/v1/rbac/roles | 
[**api_v1_rbac_roles_id_delete**](RbacApi.md#api_v1_rbac_roles_id_delete) | **DELETE** /api/v1/rbac/roles/{id} | 
[**api_v1_rbac_roles_post**](RbacApi.md#api_v1_rbac_roles_post) | **POST** /api/v1/rbac/roles | 
[**api_v1_rbac_roles_put**](RbacApi.md#api_v1_rbac_roles_put) | **PUT** /api/v1/rbac/roles | 


# **api_v1_rbac_roles_get**
> list[RbacRole] api_v1_rbac_roles_get()



Roles returns all roles (custom and system) 

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
    api_instance = openapi_client.RbacApi(api_client)
    
    try:
        api_response = api_instance.api_v1_rbac_roles_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RbacApi->api_v1_rbac_roles_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[RbacRole]**](RbacRole.md)

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

# **api_v1_rbac_roles_id_delete**
> api_v1_rbac_roles_id_delete(id)



DeleteRole deletes specified role by name 

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
    api_instance = openapi_client.RbacApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.api_v1_rbac_roles_id_delete(id)
    except ApiException as e:
        print("Exception when calling RbacApi->api_v1_rbac_roles_id_delete: %s\n" % e)
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

# **api_v1_rbac_roles_post**
> api_v1_rbac_roles_post(rbac_role=rbac_role)



CreateRole creates a new role 

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
    api_instance = openapi_client.RbacApi(api_client)
    rbac_role = openapi_client.RbacRole() # RbacRole |  (optional)

    try:
        api_instance.api_v1_rbac_roles_post(rbac_role=rbac_role)
    except ApiException as e:
        print("Exception when calling RbacApi->api_v1_rbac_roles_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rbac_role** | [**RbacRole**](RbacRole.md)|  | [optional] 

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

# **api_v1_rbac_roles_put**
> api_v1_rbac_roles_put(rbac_role=rbac_role)



UpdateRole updates a custom role 

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
    api_instance = openapi_client.RbacApi(api_client)
    rbac_role = openapi_client.RbacRole() # RbacRole |  (optional)

    try:
        api_instance.api_v1_rbac_roles_put(rbac_role=rbac_role)
    except ApiException as e:
        print("Exception when calling RbacApi->api_v1_rbac_roles_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rbac_role** | [**RbacRole**](RbacRole.md)|  | [optional] 

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


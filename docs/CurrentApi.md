# openapi_client.CurrentApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_current_cloud_account_ids_get**](CurrentApi.md#api_v1_current_cloud_account_ids_get) | **GET** /api/v1/current/cloud-account-ids | 
[**api_v1_current_collections_get**](CurrentApi.md#api_v1_current_collections_get) | **GET** /api/v1/current/collections | 
[**api_v1_current_preferences_get**](CurrentApi.md#api_v1_current_preferences_get) | **GET** /api/v1/current/preferences | 
[**api_v1_current_preferences_put**](CurrentApi.md#api_v1_current_preferences_put) | **PUT** /api/v1/current/preferences | 
[**api_v1_current_projects_get**](CurrentApi.md#api_v1_current_projects_get) | **GET** /api/v1/current/projects | 
[**api_v1_current_role_get**](CurrentApi.md#api_v1_current_role_get) | **GET** /api/v1/current/role | 
[**api_v1_current_token_get**](CurrentApi.md#api_v1_current_token_get) | **GET** /api/v1/current/token | 


# **api_v1_current_cloud_account_ids_get**
> list[str] api_v1_current_cloud_account_ids_get()



RoleAccountIDs returns account IDs associated with the given Prisma Cloud role 

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
    api_instance = openapi_client.CurrentApi(api_client)
    
    try:
        api_response = api_instance.api_v1_current_cloud_account_ids_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CurrentApi->api_v1_current_cloud_account_ids_get: %s\n" % e)
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

# **api_v1_current_collections_get**
> list[TypesUserCollection] api_v1_current_collections_get()



UserCollections returns collections in the current project that the user has permission to access 

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
    api_instance = openapi_client.CurrentApi(api_client)
    
    try:
        api_response = api_instance.api_v1_current_collections_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CurrentApi->api_v1_current_collections_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[TypesUserCollection]**](TypesUserCollection.md)

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

# **api_v1_current_preferences_get**
> TypesUserPreferences api_v1_current_preferences_get()



UserPreferences gets information about the given user, a user can only query its own details 

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
    api_instance = openapi_client.CurrentApi(api_client)
    
    try:
        api_response = api_instance.api_v1_current_preferences_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CurrentApi->api_v1_current_preferences_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TypesUserPreferences**](TypesUserPreferences.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UserPreferences are the user global project reference that are persistent between versions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_current_preferences_put**
> api_v1_current_preferences_put(types_user_preferences=types_user_preferences)



SetUserPreferences sets the user preference data 

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
    api_instance = openapi_client.CurrentApi(api_client)
    types_user_preferences = openapi_client.TypesUserPreferences() # TypesUserPreferences |  (optional)

    try:
        api_instance.api_v1_current_preferences_put(types_user_preferences=types_user_preferences)
    except ApiException as e:
        print("Exception when calling CurrentApi->api_v1_current_preferences_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **types_user_preferences** | [**TypesUserPreferences**](TypesUserPreferences.md)|  | [optional] 

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

# **api_v1_current_projects_get**
> list[TypesUserProject] api_v1_current_projects_get()



UserProjects gets current user projects 

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
    api_instance = openapi_client.CurrentApi(api_client)
    
    try:
        api_response = api_instance.api_v1_current_projects_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CurrentApi->api_v1_current_projects_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[TypesUserProject]**](TypesUserProject.md)

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

# **api_v1_current_role_get**
> RbacRole api_v1_current_role_get()



UserRole returns current user role 

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
    api_instance = openapi_client.CurrentApi(api_client)
    
    try:
        api_response = api_instance.api_v1_current_role_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CurrentApi->api_v1_current_role_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RbacRole**](RbacRole.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Role represents the role of a given user/group |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_current_token_get**
> TypesAuthenticationResponse api_v1_current_token_get()



UserToken gets current user token (with respect to the currently selected project) 

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
    api_instance = openapi_client.CurrentApi(api_client)
    
    try:
        api_response = api_instance.api_v1_current_token_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CurrentApi->api_v1_current_token_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TypesAuthenticationResponse**](TypesAuthenticationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AuthenticationResponse returns the result of calling the authentication endpoint |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


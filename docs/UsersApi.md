# openapi_client.UsersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_users_get**](UsersApi.md#api_v1_users_get) | **GET** /api/v1/users | 
[**api_v1_users_id_delete**](UsersApi.md#api_v1_users_id_delete) | **DELETE** /api/v1/users/{id} | 
[**api_v1_users_impersonate_get**](UsersApi.md#api_v1_users_impersonate_get) | **GET** /api/v1/users/impersonate | 
[**api_v1_users_password_put**](UsersApi.md#api_v1_users_password_put) | **PUT** /api/v1/users/password | 
[**api_v1_users_post**](UsersApi.md#api_v1_users_post) | **POST** /api/v1/users | 
[**api_v1_users_put**](UsersApi.md#api_v1_users_put) | **PUT** /api/v1/users | 


# **api_v1_users_get**
> list[ApiUser] api_v1_users_get()



Users returns all users, if request was sent from secondary project - only project's users are returned 

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
    api_instance = openapi_client.UsersApi(api_client)
    
    try:
        api_response = api_instance.api_v1_users_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->api_v1_users_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ApiUser]**](ApiUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UserList represents a list of users |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_users_id_delete**
> api_v1_users_id_delete(id)



DeleteUser deletes the given user 

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
    api_instance = openapi_client.UsersApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.api_v1_users_id_delete(id)
    except ApiException as e:
        print("Exception when calling UsersApi->api_v1_users_id_delete: %s\n" % e)
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

# **api_v1_users_impersonate_get**
> ApiImpersonatedUserResp api_v1_users_impersonate_get()



ImpersonatedUserToken fetches the token of the provided impersonated user. Should only be used by the secondary console and triggered by the master console. 

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
    api_instance = openapi_client.UsersApi(api_client)
    
    try:
        api_response = api_instance.api_v1_users_impersonate_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->api_v1_users_impersonate_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiImpersonatedUserResp**](ApiImpersonatedUserResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ImpersonatedUserResp holds the response for the impersonating request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_users_password_put**
> api_v1_users_password_put(types_user_password=types_user_password)



ReplaceUserPassword replaces the user password 

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
    api_instance = openapi_client.UsersApi(api_client)
    types_user_password = openapi_client.TypesUserPassword() # TypesUserPassword |  (optional)

    try:
        api_instance.api_v1_users_password_put(types_user_password=types_user_password)
    except ApiException as e:
        print("Exception when calling UsersApi->api_v1_users_password_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **types_user_password** | [**TypesUserPassword**](TypesUserPassword.md)|  | [optional] 

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

# **api_v1_users_post**
> api_v1_users_post(api_user=api_user)



CreateUser creates a new user 

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
    api_instance = openapi_client.UsersApi(api_client)
    api_user = openapi_client.ApiUser() # ApiUser |  (optional)

    try:
        api_instance.api_v1_users_post(api_user=api_user)
    except ApiException as e:
        print("Exception when calling UsersApi->api_v1_users_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_user** | [**ApiUser**](ApiUser.md)|  | [optional] 

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

# **api_v1_users_put**
> api_v1_users_put(api_user=api_user)



UpdateUser updates an existing user 

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
    api_instance = openapi_client.UsersApi(api_client)
    api_user = openapi_client.ApiUser() # ApiUser |  (optional)

    try:
        api_instance.api_v1_users_put(api_user=api_user)
    except ApiException as e:
        print("Exception when calling UsersApi->api_v1_users_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_user** | [**ApiUser**](ApiUser.md)|  | [optional] 

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


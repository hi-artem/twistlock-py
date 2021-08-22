# openapi_client.AuthenticateApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_authenticate_identity_redirect_url_get**](AuthenticateApi.md#api_v1_authenticate_identity_redirect_url_get) | **GET** /api/v1/authenticate/identity-redirect-url | 
[**api_v1_authenticate_post**](AuthenticateApi.md#api_v1_authenticate_post) | **POST** /api/v1/authenticate | 
[**api_v1_authenticate_renew_get**](AuthenticateApi.md#api_v1_authenticate_renew_get) | **GET** /api/v1/authenticate/renew | 


# **api_v1_authenticate_identity_redirect_url_get**
> IdentityRedirectURLResponse api_v1_authenticate_identity_redirect_url_get(type=type, redirect=redirect)



IdentityRedirectURL returns the redirect URL for the given authentication provider 

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
    api_instance = openapi_client.AuthenticateApi(api_client)
    type = 'type_example' # str | Type is the auth provider type.  (optional)
redirect = True # bool | Redirect will redirect to the specified identity provider authentication flow.  (optional)

    try:
        api_response = api_instance.api_v1_authenticate_identity_redirect_url_get(type=type, redirect=redirect)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticateApi->api_v1_authenticate_identity_redirect_url_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Type is the auth provider type.  | [optional] 
 **redirect** | **bool**| Redirect will redirect to the specified identity provider authentication flow.  | [optional] 

### Return type

[**IdentityRedirectURLResponse**](IdentityRedirectURLResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | RedirectURLResponse is the response for identity redirect endpoint |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_authenticate_post**
> TypesAuthenticationResponse api_v1_authenticate_post(api_authentication_request=api_authentication_request)



Authenticate is the authentication endpoint 

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
    api_instance = openapi_client.AuthenticateApi(api_client)
    api_authentication_request = openapi_client.ApiAuthenticationRequest() # ApiAuthenticationRequest |  (optional)

    try:
        api_response = api_instance.api_v1_authenticate_post(api_authentication_request=api_authentication_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticateApi->api_v1_authenticate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_authentication_request** | [**ApiAuthenticationRequest**](ApiAuthenticationRequest.md)|  | [optional] 

### Return type

[**TypesAuthenticationResponse**](TypesAuthenticationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AuthenticationResponse returns the result of calling the authentication endpoint |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_authenticate_renew_get**
> TypesAuthenticationResponse api_v1_authenticate_renew_get()



RenewToken renews the JWT token 

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
    api_instance = openapi_client.AuthenticateApi(api_client)
    
    try:
        api_response = api_instance.api_v1_authenticate_renew_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticateApi->api_v1_authenticate_renew_get: %s\n" % e)
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


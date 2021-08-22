# openapi_client.SignupApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_signup_post**](SignupApi.md#api_v1_signup_post) | **POST** /api/v1/signup | 


# **api_v1_signup_post**
> api_v1_signup_post(api_authentication_request=api_authentication_request)



Signup signs a new admin user 

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
    api_instance = openapi_client.SignupApi(api_client)
    api_authentication_request = openapi_client.ApiAuthenticationRequest() # ApiAuthenticationRequest |  (optional)

    try:
        api_instance.api_v1_signup_post(api_authentication_request=api_authentication_request)
    except ApiException as e:
        print("Exception when calling SignupApi->api_v1_signup_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_authentication_request** | [**ApiAuthenticationRequest**](ApiAuthenticationRequest.md)|  | [optional] 

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


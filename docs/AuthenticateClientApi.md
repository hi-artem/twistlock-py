# openapi_client.AuthenticateClientApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_authenticate_client_post**](AuthenticateClientApi.md#api_v1_authenticate_client_post) | **POST** /api/v1/authenticate-client | 


# **api_v1_authenticate_client_post**
> TypesConsoleAuthResponse api_v1_authenticate_client_post()



AuthenticateClient checks the client certificate supplied and authorizes the user according to the username passed via the certificate CN or UPN fields 

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
    api_instance = openapi_client.AuthenticateClientApi(api_client)
    
    try:
        api_response = api_instance.api_v1_authenticate_client_post()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticateClientApi->api_v1_authenticate_client_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TypesConsoleAuthResponse**](TypesConsoleAuthResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ConsoleAuthResponse represents the console certificates authentication response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


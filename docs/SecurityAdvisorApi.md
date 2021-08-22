# openapi_client.SecurityAdvisorApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_security_advisor_webhook_webhook_v1_setup_configuration_post**](SecurityAdvisorApi.md#api_v1_security_advisor_webhook_webhook_v1_setup_configuration_post) | **POST** /api/v1/security-advisor/webhook/webhook/v1/setup/configuration | 
[**api_v1_security_advisor_webhook_webhook_v1_setup_dashboard_get**](SecurityAdvisorApi.md#api_v1_security_advisor_webhook_webhook_v1_setup_dashboard_get) | **GET** /api/v1/security-advisor/webhook/webhook/v1/setup/dashboard | 
[**api_v1_security_advisor_webhook_webhook_v1_setup_get**](SecurityAdvisorApi.md#api_v1_security_advisor_webhook_webhook_v1_setup_get) | **GET** /api/v1/security-advisor/webhook/webhook/v1/setup | 
[**api_v1_security_advisor_webhook_webhook_v1_setup_metadata_get**](SecurityAdvisorApi.md#api_v1_security_advisor_webhook_webhook_v1_setup_metadata_get) | **GET** /api/v1/security-advisor/webhook/webhook/v1/setup/metadata | 
[**api_v1_security_advisor_webhook_webhook_v1_setup_test_post**](SecurityAdvisorApi.md#api_v1_security_advisor_webhook_webhook_v1_setup_test_post) | **POST** /api/v1/security-advisor/webhook/webhook/v1/setup/test | 


# **api_v1_security_advisor_webhook_webhook_v1_setup_configuration_post**
> api_v1_security_advisor_webhook_webhook_v1_setup_configuration_post(types_security_advisor_configuration=types_security_advisor_configuration)



SecurityAdvisorSetConfiguration sets the webhook configuration 

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
    api_instance = openapi_client.SecurityAdvisorApi(api_client)
    types_security_advisor_configuration = openapi_client.TypesSecurityAdvisorConfiguration() # TypesSecurityAdvisorConfiguration |  (optional)

    try:
        api_instance.api_v1_security_advisor_webhook_webhook_v1_setup_configuration_post(types_security_advisor_configuration=types_security_advisor_configuration)
    except ApiException as e:
        print("Exception when calling SecurityAdvisorApi->api_v1_security_advisor_webhook_webhook_v1_setup_configuration_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **types_security_advisor_configuration** | [**TypesSecurityAdvisorConfiguration**](TypesSecurityAdvisorConfiguration.md)|  | [optional] 

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

# **api_v1_security_advisor_webhook_webhook_v1_setup_dashboard_get**
> TypesSecurityAdvisorDashboardResp api_v1_security_advisor_webhook_webhook_v1_setup_dashboard_get()



SecurityAdvisorDashboard returns the console dashboard URL 

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
    api_instance = openapi_client.SecurityAdvisorApi(api_client)
    
    try:
        api_response = api_instance.api_v1_security_advisor_webhook_webhook_v1_setup_dashboard_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SecurityAdvisorApi->api_v1_security_advisor_webhook_webhook_v1_setup_dashboard_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TypesSecurityAdvisorDashboardResp**](TypesSecurityAdvisorDashboardResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SecurityAdvisorDashboardResp is the response to security advisor dashboard |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_security_advisor_webhook_webhook_v1_setup_get**
> api_v1_security_advisor_webhook_webhook_v1_setup_get()



SecurityAdvisorWebhookCheck checks the webhook is setup correctly 

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
    api_instance = openapi_client.SecurityAdvisorApi(api_client)
    
    try:
        api_instance.api_v1_security_advisor_webhook_webhook_v1_setup_get()
    except ApiException as e:
        print("Exception when calling SecurityAdvisorApi->api_v1_security_advisor_webhook_webhook_v1_setup_get: %s\n" % e)
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

# **api_v1_security_advisor_webhook_webhook_v1_setup_metadata_get**
> TypesSecurityAdvisorNotes api_v1_security_advisor_webhook_webhook_v1_setup_metadata_get()



SecurityAdvisorMetadata returns the webhook metadata configuration 

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
    api_instance = openapi_client.SecurityAdvisorApi(api_client)
    
    try:
        api_response = api_instance.api_v1_security_advisor_webhook_webhook_v1_setup_metadata_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SecurityAdvisorApi->api_v1_security_advisor_webhook_webhook_v1_setup_metadata_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TypesSecurityAdvisorNotes**](TypesSecurityAdvisorNotes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SecurityAdvisorNotes security advisor the security advisor finding metadata |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_security_advisor_webhook_webhook_v1_setup_test_post**
> api_v1_security_advisor_webhook_webhook_v1_setup_test_post()



SecurityAdvisorTestConfiguration tests the security advisor alert profile 

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
    api_instance = openapi_client.SecurityAdvisorApi(api_client)
    
    try:
        api_instance.api_v1_security_advisor_webhook_webhook_v1_setup_test_post()
    except ApiException as e:
        print("Exception when calling SecurityAdvisorApi->api_v1_security_advisor_webhook_webhook_v1_setup_test_post: %s\n" % e)
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


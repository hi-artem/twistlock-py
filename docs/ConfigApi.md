# openapi_client.ConfigApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_config_auditsink_get**](ConfigApi.md#api_v1_config_auditsink_get) | **GET** /api/v1/config/auditsink | 
[**api_v1_config_validating_webhook_get**](ConfigApi.md#api_v1_config_validating_webhook_get) | **GET** /api/v1/config/validating-webhook | 


# **api_v1_config_auditsink_get**
> list[int] api_v1_config_auditsink_get()



GenerateAuditSinkConfig returns the audit sink configuration for integrating k8s audit sink with the Console, based upon https://kubernetes.io/docs/tasks/debug-application-cluster/audit/ 

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
    api_instance = openapi_client.ConfigApi(api_client)
    
    try:
        api_response = api_instance.api_v1_config_auditsink_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigApi->api_v1_config_auditsink_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[int]**

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

# **api_v1_config_validating_webhook_get**
> list[int] api_v1_config_validating_webhook_get()



GenerateValidatingWebhookConfig returns a validating webhook configuration for integrating k8s admission control with a Defender 

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
    api_instance = openapi_client.ConfigApi(api_client)
    
    try:
        api_response = api_instance.api_v1_config_validating_webhook_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigApi->api_v1_config_validating_webhook_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[int]**

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


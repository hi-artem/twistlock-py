# openapi_client.KubernetesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_kubernetes_scan_post**](KubernetesApi.md#api_v1_kubernetes_scan_post) | **POST** /api/v1/kubernetes/scan | 
[**api_v1_kubernetes_webhook_post**](KubernetesApi.md#api_v1_kubernetes_webhook_post) | **POST** /api/v1/kubernetes/webhook/ | 


# **api_v1_kubernetes_scan_post**
> api_v1_kubernetes_scan_post()



ScanKubernetes triggers a k8s scan 

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
    api_instance = openapi_client.KubernetesApi(api_client)
    
    try:
        api_instance.api_v1_kubernetes_scan_post()
    except ApiException as e:
        print("Exception when calling KubernetesApi->api_v1_kubernetes_scan_post: %s\n" % e)
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

# **api_v1_kubernetes_webhook_post**
> api_v1_kubernetes_webhook_post()



KubernetesAuditWebhook listens to Kubernetes audit events 

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
    api_instance = openapi_client.KubernetesApi(api_client)
    
    try:
        api_instance.api_v1_kubernetes_webhook_post()
    except ApiException as e:
        print("Exception when calling KubernetesApi->api_v1_kubernetes_webhook_post: %s\n" % e)
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


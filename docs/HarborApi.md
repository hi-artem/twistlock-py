# openapi_client.HarborApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_harbor_api_v1_metadata_get**](HarborApi.md#api_v1_harbor_api_v1_metadata_get) | **GET** /api/v1/harbor//api/v1/metadata | 
[**api_v1_harbor_api_v1_scan_id_report_get**](HarborApi.md#api_v1_harbor_api_v1_scan_id_report_get) | **GET** /api/v1/harbor//api/v1/scan/{id}/report | 
[**api_v1_harbor_api_v1_scan_post**](HarborApi.md#api_v1_harbor_api_v1_scan_post) | **POST** /api/v1/harbor//api/v1/scan | 


# **api_v1_harbor_api_v1_metadata_get**
> api_v1_harbor_api_v1_metadata_get()



HarborScannerMetadata returns metadata of the PCC vulnerability scanner adapter for Harbor registry 

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
    api_instance = openapi_client.HarborApi(api_client)
    
    try:
        api_instance.api_v1_harbor_api_v1_metadata_get()
    except ApiException as e:
        print("Exception when calling HarborApi->api_v1_harbor_api_v1_metadata_get: %s\n" % e)
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

# **api_v1_harbor_api_v1_scan_id_report_get**
> api_v1_harbor_api_v1_scan_id_report_get(id)



HarborScannerInstanceReport returns the scan results of the requested scan via its ID 

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
    api_instance = openapi_client.HarborApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.api_v1_harbor_api_v1_scan_id_report_get(id)
    except ApiException as e:
        print("Exception when calling HarborApi->api_v1_harbor_api_v1_scan_id_report_get: %s\n" % e)
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

# **api_v1_harbor_api_v1_scan_post**
> api_v1_harbor_api_v1_scan_post()



HarborScannerScan accepts an image vulnerability scan request from Harbor registry and submits it asynchronously 

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
    api_instance = openapi_client.HarborApi(api_client)
    
    try:
        api_instance.api_v1_harbor_api_v1_scan_post()
    except ApiException as e:
        print("Exception when calling HarborApi->api_v1_harbor_api_v1_scan_post: %s\n" % e)
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


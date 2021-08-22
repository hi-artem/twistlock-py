# openapi_client.TrustApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_trust_data_get**](TrustApi.md#api_v1_trust_data_get) | **GET** /api/v1/trust/data | 
[**api_v1_trust_data_put**](TrustApi.md#api_v1_trust_data_put) | **PUT** /api/v1/trust/data | 
[**api_v1_trust_result_get**](TrustApi.md#api_v1_trust_result_get) | **GET** /api/v1/trust/result | 


# **api_v1_trust_data_get**
> TrustData api_v1_trust_data_get()



TrustData returns the trust data 

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
    api_instance = openapi_client.TrustApi(api_client)
    
    try:
        api_response = api_instance.api_v1_trust_data_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TrustApi->api_v1_trust_data_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TrustData**](TrustData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Data holds the image trust data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_trust_data_put**
> api_v1_trust_data_put(trust_data=trust_data)



SetTrustData replaces the trust policy and groups with the given trust data 

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
    api_instance = openapi_client.TrustApi(api_client)
    trust_data = openapi_client.TrustData() # TrustData |  (optional)

    try:
        api_instance.api_v1_trust_data_put(trust_data=trust_data)
    except ApiException as e:
        print("Exception when calling TrustApi->api_v1_trust_data_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trust_data** | [**TrustData**](TrustData.md)|  | [optional] 

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

# **api_v1_trust_result_get**
> TrustImageResult api_v1_trust_result_get(image_id=image_id)



TrustResult returns the trust status for a given image 

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
    api_instance = openapi_client.TrustApi(api_client)
    image_id = 'image_id_example' # str | ImageID is the image ID that should be evaluated.  (optional)

    try:
        api_response = api_instance.api_v1_trust_result_get(image_id=image_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TrustApi->api_v1_trust_result_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**| ImageID is the image ID that should be evaluated.  | [optional] 

### Return type

[**TrustImageResult**](TrustImageResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ImageResult represents an aggregated image trust result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


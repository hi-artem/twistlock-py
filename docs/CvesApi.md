# openapi_client.CvesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_cves_distribution_get**](CvesApi.md#api_v1_cves_distribution_get) | **GET** /api/v1/cves/distribution | 
[**api_v1_cves_get**](CvesApi.md#api_v1_cves_get) | **GET** /api/v1/cves | 


# **api_v1_cves_distribution_get**
> list[TypesCVEStats] api_v1_cves_distribution_get()



CVEStats returns the vulnerability distribution statistics 

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
    api_instance = openapi_client.CvesApi(api_client)
    
    try:
        api_response = api_instance.api_v1_cves_distribution_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CvesApi->api_v1_cves_distribution_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[TypesCVEStats]**](TypesCVEStats.md)

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

# **api_v1_cves_get**
> list[TypesCVEVulnerability] api_v1_cves_get(id=id)



Vulnerabilities returns all relevant vulnerability data 

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
    api_instance = openapi_client.CvesApi(api_client)
    id = 'id_example' # str | ID is the term to search.  (optional)

    try:
        api_response = api_instance.api_v1_cves_get(id=id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CvesApi->api_v1_cves_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID is the term to search.  | [optional] 

### Return type

[**list[TypesCVEVulnerability]**](TypesCVEVulnerability.md)

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


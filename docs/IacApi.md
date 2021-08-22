# openapi_client.IacApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_iac_init_post**](IacApi.md#api_v1_iac_init_post) | **POST** /api/v1/iac/init | 
[**api_v1_iac_scan_post**](IacApi.md#api_v1_iac_scan_post) | **POST** /api/v1/iac/scan | 


# **api_v1_iac_init_post**
> PrismaIaCScanInfo api_v1_iac_init_post(prisma_ia_c_scan_request=prisma_ia_c_scan_request)



IaCInitScan initializes an IaC scan and returns the required information to continue the scan process 

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
    api_instance = openapi_client.IacApi(api_client)
    prisma_ia_c_scan_request = openapi_client.PrismaIaCScanRequest() # PrismaIaCScanRequest |  (optional)

    try:
        api_response = api_instance.api_v1_iac_init_post(prisma_ia_c_scan_request=prisma_ia_c_scan_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IacApi->api_v1_iac_init_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prisma_ia_c_scan_request** | [**PrismaIaCScanRequest**](PrismaIaCScanRequest.md)|  | [optional] 

### Return type

[**PrismaIaCScanInfo**](PrismaIaCScanInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | IaCScanInfo is the IaC scan initialization response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_iac_scan_post**
> PrismaIaCJobResult api_v1_iac_scan_post(prisma_ia_c_scan_job_config=prisma_ia_c_scan_job_config)



IaCScan starts a scan and returns the results given a scan ID, assuming a successful upload of the required files 

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
    api_instance = openapi_client.IacApi(api_client)
    prisma_ia_c_scan_job_config = openapi_client.PrismaIaCScanJobConfig() # PrismaIaCScanJobConfig |  (optional)

    try:
        api_response = api_instance.api_v1_iac_scan_post(prisma_ia_c_scan_job_config=prisma_ia_c_scan_job_config)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IacApi->api_v1_iac_scan_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prisma_ia_c_scan_job_config** | [**PrismaIaCScanJobConfig**](PrismaIaCScanJobConfig.md)|  | [optional] 

### Return type

[**PrismaIaCJobResult**](PrismaIaCJobResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | IaCJobResult represents the result of a performed IaC scan job and its final status |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


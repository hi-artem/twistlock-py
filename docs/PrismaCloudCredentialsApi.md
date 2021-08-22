# openapi_client.PrismaCloudCredentialsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_prisma_cloud_credentials_get**](PrismaCloudCredentialsApi.md#api_v1_prisma_cloud_credentials_get) | **GET** /api/v1/prisma-cloud-credentials | 


# **api_v1_prisma_cloud_credentials_get**
> list[CredCredential] api_v1_prisma_cloud_credentials_get()



PrismaCloudCredentials return all cloud accounts that can be used as credentials (user can add those accounts as internal credentials). Existing accounts that were transformed to local credentials are filtered. 

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
    api_instance = openapi_client.PrismaCloudCredentialsApi(api_client)
    
    try:
        api_response = api_instance.api_v1_prisma_cloud_credentials_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PrismaCloudCredentialsApi->api_v1_prisma_cloud_credentials_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CredCredential]**](CredCredential.md)

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


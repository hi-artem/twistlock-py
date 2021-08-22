# openapi_client.CustomComplianceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_custom_compliance_get**](CustomComplianceApi.md#api_v1_custom_compliance_get) | **GET** /api/v1/custom-compliance | 
[**api_v1_custom_compliance_id_delete**](CustomComplianceApi.md#api_v1_custom_compliance_id_delete) | **DELETE** /api/v1/custom-compliance/{id} | 
[**api_v1_custom_compliance_put**](CustomComplianceApi.md#api_v1_custom_compliance_put) | **PUT** /api/v1/custom-compliance | 


# **api_v1_custom_compliance_get**
> list[SharedCustomComplianceCheck] api_v1_custom_compliance_get()



SetCustomComplianceCheck returns the applicable custom compliance checks 

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
    api_instance = openapi_client.CustomComplianceApi(api_client)
    
    try:
        api_response = api_instance.api_v1_custom_compliance_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CustomComplianceApi->api_v1_custom_compliance_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SharedCustomComplianceCheck]**](SharedCustomComplianceCheck.md)

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

# **api_v1_custom_compliance_id_delete**
> api_v1_custom_compliance_id_delete(id)



DeleteCustomComplianceCheck removes the given check from the custom compliance checks list 

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
    api_instance = openapi_client.CustomComplianceApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.api_v1_custom_compliance_id_delete(id)
    except ApiException as e:
        print("Exception when calling CustomComplianceApi->api_v1_custom_compliance_id_delete: %s\n" % e)
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

# **api_v1_custom_compliance_put**
> SharedCustomComplianceCheck api_v1_custom_compliance_put(shared_custom_compliance_check=shared_custom_compliance_check)



UpsertCustomComplianceCheck sets the custom compliance checks in the db and returns the generated check ID 

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
    api_instance = openapi_client.CustomComplianceApi(api_client)
    shared_custom_compliance_check = openapi_client.SharedCustomComplianceCheck() # SharedCustomComplianceCheck |  (optional)

    try:
        api_response = api_instance.api_v1_custom_compliance_put(shared_custom_compliance_check=shared_custom_compliance_check)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CustomComplianceApi->api_v1_custom_compliance_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shared_custom_compliance_check** | [**SharedCustomComplianceCheck**](SharedCustomComplianceCheck.md)|  | [optional] 

### Return type

[**SharedCustomComplianceCheck**](SharedCustomComplianceCheck.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CustomComplianceCheck represents a custom compliance check entry |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


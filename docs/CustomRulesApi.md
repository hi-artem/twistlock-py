# openapi_client.CustomRulesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_custom_rules_get**](CustomRulesApi.md#api_v1_custom_rules_get) | **GET** /api/v1/custom-rules | 
[**api_v1_custom_rules_id_delete**](CustomRulesApi.md#api_v1_custom_rules_id_delete) | **DELETE** /api/v1/custom-rules/{id} | 
[**api_v1_custom_rules_id_put**](CustomRulesApi.md#api_v1_custom_rules_id_put) | **PUT** /api/v1/custom-rules/{id} | 


# **api_v1_custom_rules_get**
> list[CustomrulesRule] api_v1_custom_rules_get()



CustomRules returns the custom rules 

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
    api_instance = openapi_client.CustomRulesApi(api_client)
    
    try:
        api_response = api_instance.api_v1_custom_rules_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CustomRulesApi->api_v1_custom_rules_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CustomrulesRule]**](CustomrulesRule.md)

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

# **api_v1_custom_rules_id_delete**
> api_v1_custom_rules_id_delete(id)



DeleteCustomRule deletes a custom rule 

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
    api_instance = openapi_client.CustomRulesApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.api_v1_custom_rules_id_delete(id)
    except ApiException as e:
        print("Exception when calling CustomRulesApi->api_v1_custom_rules_id_delete: %s\n" % e)
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

# **api_v1_custom_rules_id_put**
> api_v1_custom_rules_id_put(id, customrules_rule=customrules_rule)



UpdateCustomRule creates/edits a custom rule 

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
    api_instance = openapi_client.CustomRulesApi(api_client)
    id = 'id_example' # str | 
customrules_rule = openapi_client.CustomrulesRule() # CustomrulesRule |  (optional)

    try:
        api_instance.api_v1_custom_rules_id_put(id, customrules_rule=customrules_rule)
    except ApiException as e:
        print("Exception when calling CustomRulesApi->api_v1_custom_rules_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **customrules_rule** | [**CustomrulesRule**](CustomrulesRule.md)|  | [optional] 

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


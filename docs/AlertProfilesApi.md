# openapi_client.AlertProfilesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_alert_profiles_get**](AlertProfilesApi.md#api_v1_alert_profiles_get) | **GET** /api/v1/alert-profiles | 
[**api_v1_alert_profiles_id_delete**](AlertProfilesApi.md#api_v1_alert_profiles_id_delete) | **DELETE** /api/v1/alert-profiles/{id} | 
[**api_v1_alert_profiles_names_get**](AlertProfilesApi.md#api_v1_alert_profiles_names_get) | **GET** /api/v1/alert-profiles/names | 
[**api_v1_alert_profiles_post**](AlertProfilesApi.md#api_v1_alert_profiles_post) | **POST** /api/v1/alert-profiles | 
[**api_v1_alert_profiles_test_post**](AlertProfilesApi.md#api_v1_alert_profiles_test_post) | **POST** /api/v1/alert-profiles/test | 


# **api_v1_alert_profiles_get**
> list[ApiAlertProfile] api_v1_alert_profiles_get()



AlertProfiles returns the all alert profiles 

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
    api_instance = openapi_client.AlertProfilesApi(api_client)
    
    try:
        api_response = api_instance.api_v1_alert_profiles_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AlertProfilesApi->api_v1_alert_profiles_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ApiAlertProfile]**](ApiAlertProfile.md)

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

# **api_v1_alert_profiles_id_delete**
> api_v1_alert_profiles_id_delete(id)



DeleteAlertProfile deletes an alert profile 

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
    api_instance = openapi_client.AlertProfilesApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.api_v1_alert_profiles_id_delete(id)
    except ApiException as e:
        print("Exception when calling AlertProfilesApi->api_v1_alert_profiles_id_delete: %s\n" % e)
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

# **api_v1_alert_profiles_names_get**
> list[str] api_v1_alert_profiles_names_get()



AlertProfileNames returns the all alert profile names 

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
    api_instance = openapi_client.AlertProfilesApi(api_client)
    
    try:
        api_response = api_instance.api_v1_alert_profiles_names_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AlertProfilesApi->api_v1_alert_profiles_names_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

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

# **api_v1_alert_profiles_post**
> api_v1_alert_profiles_post(api_alert_profile=api_alert_profile)



UpdateAlertProfile update the alert profile 

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
    api_instance = openapi_client.AlertProfilesApi(api_client)
    api_alert_profile = openapi_client.ApiAlertProfile() # ApiAlertProfile |  (optional)

    try:
        api_instance.api_v1_alert_profiles_post(api_alert_profile=api_alert_profile)
    except ApiException as e:
        print("Exception when calling AlertProfilesApi->api_v1_alert_profiles_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_alert_profile** | [**ApiAlertProfile**](ApiAlertProfile.md)|  | [optional] 

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

# **api_v1_alert_profiles_test_post**
> api_v1_alert_profiles_test_post(api_alert_profile=api_alert_profile)



SendTestAlert verifies the alert profile by sending a test alert 

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
    api_instance = openapi_client.AlertProfilesApi(api_client)
    api_alert_profile = openapi_client.ApiAlertProfile() # ApiAlertProfile |  (optional)

    try:
        api_instance.api_v1_alert_profiles_test_post(api_alert_profile=api_alert_profile)
    except ApiException as e:
        print("Exception when calling AlertProfilesApi->api_v1_alert_profiles_test_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_alert_profile** | [**ApiAlertProfile**](ApiAlertProfile.md)|  | [optional] 

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


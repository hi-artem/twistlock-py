# openapi_client.WaasApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_waas_api_observations_details_delete**](WaasApi.md#api_v1_waas_api_observations_details_delete) | **DELETE** /api/v1/waas/api-observations/details | 
[**api_v1_waas_api_observations_details_get**](WaasApi.md#api_v1_waas_api_observations_details_get) | **GET** /api/v1/waas/api-observations/details | 
[**api_v1_waas_api_observations_download_get**](WaasApi.md#api_v1_waas_api_observations_download_get) | **GET** /api/v1/waas/api-observations/download | 
[**api_v1_waas_api_observations_get**](WaasApi.md#api_v1_waas_api_observations_get) | **GET** /api/v1/waas/api-observations | 
[**api_v1_waas_api_observations_refresh_post**](WaasApi.md#api_v1_waas_api_observations_refresh_post) | **POST** /api/v1/waas/api-observations/refresh | 


# **api_v1_waas_api_observations_details_delete**
> api_v1_waas_api_observations_details_delete(rule_id=rule_id, app_id=app_id)



DeleteAppFirewallAPIObservations deletes the given API observations 

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
    api_instance = openapi_client.WaasApi(api_client)
    rule_id = 'rule_id_example' # str | RuleID is the observation rule ID.  (optional)
app_id = 'app_id_example' # str | AppID is the observation app ID.  (optional)

    try:
        api_instance.api_v1_waas_api_observations_details_delete(rule_id=rule_id, app_id=app_id)
    except ApiException as e:
        print("Exception when calling WaasApi->api_v1_waas_api_observations_details_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| RuleID is the observation rule ID.  | [optional] 
 **app_id** | **str**| AppID is the observation app ID.  | [optional] 

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

# **api_v1_waas_api_observations_details_get**
> WaasAPIObservation api_v1_waas_api_observations_details_get(rule_id=rule_id, app_id=app_id)



AppFirewallAPIObservationDetails returns the given API observation details 

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
    api_instance = openapi_client.WaasApi(api_client)
    rule_id = 'rule_id_example' # str | RuleID is the observation rule ID.  (optional)
app_id = 'app_id_example' # str | AppID is the observation app ID.  (optional)

    try:
        api_response = api_instance.api_v1_waas_api_observations_details_get(rule_id=rule_id, app_id=app_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WaasApi->api_v1_waas_api_observations_details_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| RuleID is the observation rule ID.  | [optional] 
 **app_id** | **str**| AppID is the observation app ID.  | [optional] 

### Return type

[**WaasAPIObservation**](WaasAPIObservation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | APIObservation is the API observation deduced from the API model |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_waas_api_observations_download_get**
> api_v1_waas_api_observations_download_get(rule_id=rule_id, app_id=app_id)



DownloadAppFirewallAPIObservationSpec downloads the generated OpenAPI3 spec for a given observation 

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
    api_instance = openapi_client.WaasApi(api_client)
    rule_id = 'rule_id_example' # str | RuleID is the observation rule ID.  (optional)
app_id = 'app_id_example' # str | AppID is the observation app ID.  (optional)

    try:
        api_instance.api_v1_waas_api_observations_download_get(rule_id=rule_id, app_id=app_id)
    except ApiException as e:
        print("Exception when calling WaasApi->api_v1_waas_api_observations_download_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| RuleID is the observation rule ID.  | [optional] 
 **app_id** | **str**| AppID is the observation app ID.  | [optional] 

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

# **api_v1_waas_api_observations_get**
> list[WaasAPIModelID] api_v1_waas_api_observations_get()



AppFirewallAPIObservations returns the API observations 

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
    api_instance = openapi_client.WaasApi(api_client)
    
    try:
        api_response = api_instance.api_v1_waas_api_observations_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WaasApi->api_v1_waas_api_observations_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[WaasAPIModelID]**](WaasAPIModelID.md)

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

# **api_v1_waas_api_observations_refresh_post**
> api_v1_waas_api_observations_refresh_post()



RefreshAppFirewallAPIObservations signals the defenders to send updates on their API observations 

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
    api_instance = openapi_client.WaasApi(api_client)
    
    try:
        api_instance.api_v1_waas_api_observations_refresh_post()
    except ApiException as e:
        print("Exception when calling WaasApi->api_v1_waas_api_observations_refresh_post: %s\n" % e)
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


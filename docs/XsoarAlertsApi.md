# openapi_client.XsoarAlertsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_xsoar_alerts_get**](XsoarAlertsApi.md#api_v1_xsoar_alerts_get) | **GET** /api/v1/xsoar-alerts | 


# **api_v1_xsoar_alerts_get**
> list[str] api_v1_xsoar_alerts_get(_from=_from, to=to)



XSOARAlerts returns all alerts saved in DB REMARK: All alerts are removed from DB after calling this method 

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
    api_instance = openapi_client.XsoarAlertsApi(api_client)
    _from = '2013-10-20T19:20:30+01:00' # datetime | From is an optional minimum time constraints for the alert.  (optional)
to = '2013-10-20T19:20:30+01:00' # datetime | To is an optional maximum time constraints for the alert.  (optional)

    try:
        api_response = api_instance.api_v1_xsoar_alerts_get(_from=_from, to=to)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling XsoarAlertsApi->api_v1_xsoar_alerts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **datetime**| From is an optional minimum time constraints for the alert.  | [optional] 
 **to** | **datetime**| To is an optional maximum time constraints for the alert.  | [optional] 

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
**200** | XSOARAlerts is a list of XSOAR alerts |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# openapi_client.RuntimeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_runtime_stats_get**](RuntimeApi.md#api_v1_runtime_stats_get) | **GET** /api/v1/runtime/stats | 


# **api_v1_runtime_stats_get**
> dict(str, int) api_v1_runtime_stats_get(_from=_from, to=to, collections=collections, account_ids=account_ids)



AttackTechniqueStats returns the MITRE stats dashboard 

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
    api_instance = openapi_client.RuntimeApi(api_client)
    _from = '2013-10-20T19:20:30+01:00' # datetime | From is an optional minimum time constraints for the audit.  (optional)
to = '2013-10-20T19:20:30+01:00' # datetime | To is an optional maximum time constraints for the audit.  (optional)
collections = ['collections_example'] # list[str] | Collections are collections scoping the query.  (optional)
account_ids = ['account_ids_example'] # list[str] | AccountIDs are the account IDs scoping the query.  (optional)

    try:
        api_response = api_instance.api_v1_runtime_stats_get(_from=_from, to=to, collections=collections, account_ids=account_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RuntimeApi->api_v1_runtime_stats_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **datetime**| From is an optional minimum time constraints for the audit.  | [optional] 
 **to** | **datetime**| To is an optional maximum time constraints for the audit.  | [optional] 
 **collections** | [**list[str]**](str.md)| Collections are collections scoping the query.  | [optional] 
 **account_ids** | [**list[str]**](str.md)| AccountIDs are the account IDs scoping the query.  | [optional] 

### Return type

**dict(str, int)**

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


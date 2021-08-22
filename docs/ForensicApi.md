# openapi_client.ForensicApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_forensic_activities_download_get**](ForensicApi.md#api_v1_forensic_activities_download_get) | **GET** /api/v1/forensic/activities/download | 
[**api_v1_forensic_activities_get**](ForensicApi.md#api_v1_forensic_activities_get) | **GET** /api/v1/forensic/activities | 


# **api_v1_forensic_activities_download_get**
> api_v1_forensic_activities_download_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, _from=_from, to=to, type=type, user=user, hostname=hostname, service=service, cluster=cluster)



DownloadHostActivities downloads the host activity data 

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
    api_instance = openapi_client.ForensicApi(api_client)
    offset = 56 # int | Offset from the start of the list from which to retrieve documents.  (optional)
limit = 56 # int | Number of documents to return.  (optional)
search = 'search_example' # str | Search term.  (optional)
sort = 'sort_example' # str | Key on which to sort.  (optional)
reverse = True # bool | Sort order.  (optional)
collections = ['collections_example'] # list[str] | Scopes the query by collection.  (optional)
account_ids = ['account_ids_example'] # list[str] | Scopes the query by account ID.  (optional)
fields = ['fields_example'] # list[str] | List of fields to retrieve.  (optional)
_from = '2013-10-20T19:20:30+01:00' # datetime | From is an optional minimum time constraints for the activity.  (optional)
to = '2013-10-20T19:20:30+01:00' # datetime | To is an optional maximum time constraints for the activity.  (optional)
type = ['type_example'] # list[str] | Types is the activity type filter.  (optional)
user = ['user_example'] # list[str] | Users is the list of users to use for filtering.  (optional)
hostname = ['hostname_example'] # list[str] | Hosts is the list of hosts to use for filtering.  (optional)
service = ['service_example'] # list[str] | Services is the list of services to use for filtering.  (optional)
cluster = ['cluster_example'] # list[str] | Clusters is the cluster filter.  (optional)

    try:
        api_instance.api_v1_forensic_activities_download_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, _from=_from, to=to, type=type, user=user, hostname=hostname, service=service, cluster=cluster)
    except ApiException as e:
        print("Exception when calling ForensicApi->api_v1_forensic_activities_download_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Offset from the start of the list from which to retrieve documents.  | [optional] 
 **limit** | **int**| Number of documents to return.  | [optional] 
 **search** | **str**| Search term.  | [optional] 
 **sort** | **str**| Key on which to sort.  | [optional] 
 **reverse** | **bool**| Sort order.  | [optional] 
 **collections** | [**list[str]**](str.md)| Scopes the query by collection.  | [optional] 
 **account_ids** | [**list[str]**](str.md)| Scopes the query by account ID.  | [optional] 
 **fields** | [**list[str]**](str.md)| List of fields to retrieve.  | [optional] 
 **_from** | **datetime**| From is an optional minimum time constraints for the activity.  | [optional] 
 **to** | **datetime**| To is an optional maximum time constraints for the activity.  | [optional] 
 **type** | [**list[str]**](str.md)| Types is the activity type filter.  | [optional] 
 **user** | [**list[str]**](str.md)| Users is the list of users to use for filtering.  | [optional] 
 **hostname** | [**list[str]**](str.md)| Hosts is the list of hosts to use for filtering.  | [optional] 
 **service** | [**list[str]**](str.md)| Services is the list of services to use for filtering.  | [optional] 
 **cluster** | [**list[str]**](str.md)| Clusters is the cluster filter.  | [optional] 

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

# **api_v1_forensic_activities_get**
> list[SharedHostActivity] api_v1_forensic_activities_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, _from=_from, to=to, type=type, user=user, hostname=hostname, service=service, cluster=cluster)



HostActivities returns the host activities 

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
    api_instance = openapi_client.ForensicApi(api_client)
    offset = 56 # int | Offset from the start of the list from which to retrieve documents.  (optional)
limit = 56 # int | Number of documents to return.  (optional)
search = 'search_example' # str | Search term.  (optional)
sort = 'sort_example' # str | Key on which to sort.  (optional)
reverse = True # bool | Sort order.  (optional)
collections = ['collections_example'] # list[str] | Scopes the query by collection.  (optional)
account_ids = ['account_ids_example'] # list[str] | Scopes the query by account ID.  (optional)
fields = ['fields_example'] # list[str] | List of fields to retrieve.  (optional)
_from = '2013-10-20T19:20:30+01:00' # datetime | From is an optional minimum time constraints for the activity.  (optional)
to = '2013-10-20T19:20:30+01:00' # datetime | To is an optional maximum time constraints for the activity.  (optional)
type = ['type_example'] # list[str] | Types is the activity type filter.  (optional)
user = ['user_example'] # list[str] | Users is the list of users to use for filtering.  (optional)
hostname = ['hostname_example'] # list[str] | Hosts is the list of hosts to use for filtering.  (optional)
service = ['service_example'] # list[str] | Services is the list of services to use for filtering.  (optional)
cluster = ['cluster_example'] # list[str] | Clusters is the cluster filter.  (optional)

    try:
        api_response = api_instance.api_v1_forensic_activities_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, _from=_from, to=to, type=type, user=user, hostname=hostname, service=service, cluster=cluster)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ForensicApi->api_v1_forensic_activities_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Offset from the start of the list from which to retrieve documents.  | [optional] 
 **limit** | **int**| Number of documents to return.  | [optional] 
 **search** | **str**| Search term.  | [optional] 
 **sort** | **str**| Key on which to sort.  | [optional] 
 **reverse** | **bool**| Sort order.  | [optional] 
 **collections** | [**list[str]**](str.md)| Scopes the query by collection.  | [optional] 
 **account_ids** | [**list[str]**](str.md)| Scopes the query by account ID.  | [optional] 
 **fields** | [**list[str]**](str.md)| List of fields to retrieve.  | [optional] 
 **_from** | **datetime**| From is an optional minimum time constraints for the activity.  | [optional] 
 **to** | **datetime**| To is an optional maximum time constraints for the activity.  | [optional] 
 **type** | [**list[str]**](str.md)| Types is the activity type filter.  | [optional] 
 **user** | [**list[str]**](str.md)| Users is the list of users to use for filtering.  | [optional] 
 **hostname** | [**list[str]**](str.md)| Hosts is the list of hosts to use for filtering.  | [optional] 
 **service** | [**list[str]**](str.md)| Services is the list of services to use for filtering.  | [optional] 
 **cluster** | [**list[str]**](str.md)| Clusters is the cluster filter.  | [optional] 

### Return type

[**list[SharedHostActivity]**](SharedHostActivity.md)

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


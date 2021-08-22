# openapi_client.ProfilesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_profiles_container_download_get**](ProfilesApi.md#api_v1_profiles_container_download_get) | **GET** /api/v1/profiles/container/download | 
[**api_v1_profiles_container_get**](ProfilesApi.md#api_v1_profiles_container_get) | **GET** /api/v1/profiles/container | 
[**api_v1_profiles_container_id_forensic_bundle_get**](ProfilesApi.md#api_v1_profiles_container_id_forensic_bundle_get) | **GET** /api/v1/profiles/container/{id}/forensic/bundle | 
[**api_v1_profiles_container_id_forensic_get**](ProfilesApi.md#api_v1_profiles_container_id_forensic_get) | **GET** /api/v1/profiles/container/{id}/forensic | 
[**api_v1_profiles_container_id_hosts_get**](ProfilesApi.md#api_v1_profiles_container_id_hosts_get) | **GET** /api/v1/profiles/container/{id}/hosts | 
[**api_v1_profiles_container_id_learn_post**](ProfilesApi.md#api_v1_profiles_container_id_learn_post) | **POST** /api/v1/profiles/container/{id}/learn | 
[**api_v1_profiles_container_id_rule_get**](ProfilesApi.md#api_v1_profiles_container_id_rule_get) | **GET** /api/v1/profiles/container/{id}/rule | 
[**api_v1_profiles_container_learn_post**](ProfilesApi.md#api_v1_profiles_container_learn_post) | **POST** /api/v1/profiles/container/learn | 
[**api_v1_profiles_host_download_get**](ProfilesApi.md#api_v1_profiles_host_download_get) | **GET** /api/v1/profiles/host/download | 
[**api_v1_profiles_host_get**](ProfilesApi.md#api_v1_profiles_host_get) | **GET** /api/v1/profiles/host | 
[**api_v1_profiles_host_id_forensic_download_get**](ProfilesApi.md#api_v1_profiles_host_id_forensic_download_get) | **GET** /api/v1/profiles/host/{id}/forensic/download | 
[**api_v1_profiles_host_id_forensic_get**](ProfilesApi.md#api_v1_profiles_host_id_forensic_get) | **GET** /api/v1/profiles/host/{id}/forensic | 


# **api_v1_profiles_container_download_get**
> api_v1_profiles_container_download_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, id=id, os=os, state=state, image_id=image_id, image=image, host_name=host_name, namespace=namespace, cluster=cluster)



DownloadContainerRuntimeProfiles downloads the container runtime security profiles according to the specified query 

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
    api_instance = openapi_client.ProfilesApi(api_client)
    offset = 56 # int | Offset from the start of the list from which to retrieve documents.  (optional)
limit = 56 # int | Number of documents to return.  (optional)
search = 'search_example' # str | Search term.  (optional)
sort = 'sort_example' # str | Key on which to sort.  (optional)
reverse = True # bool | Sort order.  (optional)
collections = ['collections_example'] # list[str] | Scopes the query by collection.  (optional)
account_ids = ['account_ids_example'] # list[str] | Scopes the query by account ID.  (optional)
fields = ['fields_example'] # list[str] | List of fields to retrieve.  (optional)
id = ['id_example'] # list[str] | IDs is the runtime profile id filter.  (optional)
os = ['os_example'] # list[str] | OS is the service runtime profile OS filter.  (optional)
state = ['state_example'] # list[str] | States is the runtime profile state filter.  (optional)
image_id = ['image_id_example'] # list[str] | ImageIDs is the runtime profile image id filter.  (optional)
image = ['image_example'] # list[str] | Images is the runtime profile image filter.  (optional)
host_name = ['host_name_example'] # list[str] | Hosts is the runtime profile hostname filter.  (optional)
namespace = ['namespace_example'] # list[str] | Namespaces is the runtime profile k8s namespace filter.  (optional)
cluster = ['cluster_example'] # list[str] | Clusters is the runtime profile k8s cluster filter.  (optional)

    try:
        api_instance.api_v1_profiles_container_download_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, id=id, os=os, state=state, image_id=image_id, image=image, host_name=host_name, namespace=namespace, cluster=cluster)
    except ApiException as e:
        print("Exception when calling ProfilesApi->api_v1_profiles_container_download_get: %s\n" % e)
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
 **id** | [**list[str]**](str.md)| IDs is the runtime profile id filter.  | [optional] 
 **os** | [**list[str]**](str.md)| OS is the service runtime profile OS filter.  | [optional] 
 **state** | [**list[str]**](str.md)| States is the runtime profile state filter.  | [optional] 
 **image_id** | [**list[str]**](str.md)| ImageIDs is the runtime profile image id filter.  | [optional] 
 **image** | [**list[str]**](str.md)| Images is the runtime profile image filter.  | [optional] 
 **host_name** | [**list[str]**](str.md)| Hosts is the runtime profile hostname filter.  | [optional] 
 **namespace** | [**list[str]**](str.md)| Namespaces is the runtime profile k8s namespace filter.  | [optional] 
 **cluster** | [**list[str]**](str.md)| Clusters is the runtime profile k8s cluster filter.  | [optional] 

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

# **api_v1_profiles_container_get**
> list[SharedContainerRuntimeProfile] api_v1_profiles_container_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, id=id, os=os, state=state, image_id=image_id, image=image, host_name=host_name, namespace=namespace, cluster=cluster)



ContainerRuntimeProfiles returns container runtime profiles by the query specification 

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
    api_instance = openapi_client.ProfilesApi(api_client)
    offset = 56 # int | Offset from the start of the list from which to retrieve documents.  (optional)
limit = 56 # int | Number of documents to return.  (optional)
search = 'search_example' # str | Search term.  (optional)
sort = 'sort_example' # str | Key on which to sort.  (optional)
reverse = True # bool | Sort order.  (optional)
collections = ['collections_example'] # list[str] | Scopes the query by collection.  (optional)
account_ids = ['account_ids_example'] # list[str] | Scopes the query by account ID.  (optional)
fields = ['fields_example'] # list[str] | List of fields to retrieve.  (optional)
id = ['id_example'] # list[str] | IDs is the runtime profile id filter.  (optional)
os = ['os_example'] # list[str] | OS is the service runtime profile OS filter.  (optional)
state = ['state_example'] # list[str] | States is the runtime profile state filter.  (optional)
image_id = ['image_id_example'] # list[str] | ImageIDs is the runtime profile image id filter.  (optional)
image = ['image_example'] # list[str] | Images is the runtime profile image filter.  (optional)
host_name = ['host_name_example'] # list[str] | Hosts is the runtime profile hostname filter.  (optional)
namespace = ['namespace_example'] # list[str] | Namespaces is the runtime profile k8s namespace filter.  (optional)
cluster = ['cluster_example'] # list[str] | Clusters is the runtime profile k8s cluster filter.  (optional)

    try:
        api_response = api_instance.api_v1_profiles_container_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, id=id, os=os, state=state, image_id=image_id, image=image, host_name=host_name, namespace=namespace, cluster=cluster)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProfilesApi->api_v1_profiles_container_get: %s\n" % e)
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
 **id** | [**list[str]**](str.md)| IDs is the runtime profile id filter.  | [optional] 
 **os** | [**list[str]**](str.md)| OS is the service runtime profile OS filter.  | [optional] 
 **state** | [**list[str]**](str.md)| States is the runtime profile state filter.  | [optional] 
 **image_id** | [**list[str]**](str.md)| ImageIDs is the runtime profile image id filter.  | [optional] 
 **image** | [**list[str]**](str.md)| Images is the runtime profile image filter.  | [optional] 
 **host_name** | [**list[str]**](str.md)| Hosts is the runtime profile hostname filter.  | [optional] 
 **namespace** | [**list[str]**](str.md)| Namespaces is the runtime profile k8s namespace filter.  | [optional] 
 **cluster** | [**list[str]**](str.md)| Clusters is the runtime profile k8s cluster filter.  | [optional] 

### Return type

[**list[SharedContainerRuntimeProfile]**](SharedContainerRuntimeProfile.md)

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

# **api_v1_profiles_container_id_forensic_bundle_get**
> api_v1_profiles_container_id_forensic_bundle_get(id, collections=collections, account_ids=account_ids, event_time=event_time, hostname=hostname, limit=limit, format=format, incident_id=incident_id)



ContainerForensicBundle streams the forensic bundle archive 

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
    api_instance = openapi_client.ProfilesApi(api_client)
    id = 'id_example' # str | 
collections = ['collections_example'] # list[str] | Collections are collections scoping the query.  (optional)
account_ids = ['account_ids_example'] # list[str] | AccountIDs are the account IDs scoping the query.  (optional)
event_time = '2013-10-20T19:20:30+01:00' # datetime | EventTime is the forensic event pivot time in milliseconds (used to fetch events).  (optional)
hostname = 'hostname_example' # str | Hostname is the hostname for which data should be fetched.  (optional)
limit = 56 # int | Limit is the number of events to return.  (optional)
format = 'format_example' # str | Format is the forensic data format.  (optional)
incident_id = 'incident_id_example' # str | IncidentID is the incident ID in case the request kind is an incident.  (optional)

    try:
        api_instance.api_v1_profiles_container_id_forensic_bundle_get(id, collections=collections, account_ids=account_ids, event_time=event_time, hostname=hostname, limit=limit, format=format, incident_id=incident_id)
    except ApiException as e:
        print("Exception when calling ProfilesApi->api_v1_profiles_container_id_forensic_bundle_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **collections** | [**list[str]**](str.md)| Collections are collections scoping the query.  | [optional] 
 **account_ids** | [**list[str]**](str.md)| AccountIDs are the account IDs scoping the query.  | [optional] 
 **event_time** | **datetime**| EventTime is the forensic event pivot time in milliseconds (used to fetch events).  | [optional] 
 **hostname** | **str**| Hostname is the hostname for which data should be fetched.  | [optional] 
 **limit** | **int**| Limit is the number of events to return.  | [optional] 
 **format** | **str**| Format is the forensic data format.  | [optional] 
 **incident_id** | **str**| IncidentID is the incident ID in case the request kind is an incident.  | [optional] 

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

# **api_v1_profiles_container_id_forensic_get**
> list[ForensicContainerEvent] api_v1_profiles_container_id_forensic_get(id, collections=collections, account_ids=account_ids, event_time=event_time, hostname=hostname, limit=limit, format=format, incident_id=incident_id)



ContainerForensic fetches the forensic data for a specific profile 

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
    api_instance = openapi_client.ProfilesApi(api_client)
    id = 'id_example' # str | 
collections = ['collections_example'] # list[str] | Collections are collections scoping the query.  (optional)
account_ids = ['account_ids_example'] # list[str] | AccountIDs are the account IDs scoping the query.  (optional)
event_time = '2013-10-20T19:20:30+01:00' # datetime | EventTime is the forensic event pivot time in milliseconds (used to fetch events).  (optional)
hostname = 'hostname_example' # str | Hostname is the hostname for which data should be fetched.  (optional)
limit = 56 # int | Limit is the number of events to return.  (optional)
format = 'format_example' # str | Format is the forensic data format.  (optional)
incident_id = 'incident_id_example' # str | IncidentID is the incident ID in case the request kind is an incident.  (optional)

    try:
        api_response = api_instance.api_v1_profiles_container_id_forensic_get(id, collections=collections, account_ids=account_ids, event_time=event_time, hostname=hostname, limit=limit, format=format, incident_id=incident_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProfilesApi->api_v1_profiles_container_id_forensic_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **collections** | [**list[str]**](str.md)| Collections are collections scoping the query.  | [optional] 
 **account_ids** | [**list[str]**](str.md)| AccountIDs are the account IDs scoping the query.  | [optional] 
 **event_time** | **datetime**| EventTime is the forensic event pivot time in milliseconds (used to fetch events).  | [optional] 
 **hostname** | **str**| Hostname is the hostname for which data should be fetched.  | [optional] 
 **limit** | **int**| Limit is the number of events to return.  | [optional] 
 **format** | **str**| Format is the forensic data format.  | [optional] 
 **incident_id** | **str**| IncidentID is the incident ID in case the request kind is an incident.  | [optional] 

### Return type

[**list[ForensicContainerEvent]**](ForensicContainerEvent.md)

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

# **api_v1_profiles_container_id_hosts_get**
> list[str] api_v1_profiles_container_id_hosts_get(id, offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, id2=id2, os=os, state=state, image_id=image_id, image=image, host_name=host_name, namespace=namespace, cluster=cluster)



ContainerRuntimeProfileHosts returns all the hosts that are using the given profile ID Remark: We need to make sure the returned hostnames match the provided collection filter. We accomplish this by looking up the corresponding defenders and intersecting the results. 

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
    api_instance = openapi_client.ProfilesApi(api_client)
    id = 'id_example' # str | 
offset = 56 # int | Offset from the start of the list from which to retrieve documents.  (optional)
limit = 56 # int | Number of documents to return.  (optional)
search = 'search_example' # str | Search term.  (optional)
sort = 'sort_example' # str | Key on which to sort.  (optional)
reverse = True # bool | Sort order.  (optional)
collections = ['collections_example'] # list[str] | Scopes the query by collection.  (optional)
account_ids = ['account_ids_example'] # list[str] | Scopes the query by account ID.  (optional)
fields = ['fields_example'] # list[str] | List of fields to retrieve.  (optional)
id2 = ['id_example'] # list[str] | IDs is the runtime profile id filter.  (optional)
os = ['os_example'] # list[str] | OS is the service runtime profile OS filter.  (optional)
state = ['state_example'] # list[str] | States is the runtime profile state filter.  (optional)
image_id = ['image_id_example'] # list[str] | ImageIDs is the runtime profile image id filter.  (optional)
image = ['image_example'] # list[str] | Images is the runtime profile image filter.  (optional)
host_name = ['host_name_example'] # list[str] | Hosts is the runtime profile hostname filter.  (optional)
namespace = ['namespace_example'] # list[str] | Namespaces is the runtime profile k8s namespace filter.  (optional)
cluster = ['cluster_example'] # list[str] | Clusters is the runtime profile k8s cluster filter.  (optional)

    try:
        api_response = api_instance.api_v1_profiles_container_id_hosts_get(id, offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, id2=id2, os=os, state=state, image_id=image_id, image=image, host_name=host_name, namespace=namespace, cluster=cluster)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProfilesApi->api_v1_profiles_container_id_hosts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **offset** | **int**| Offset from the start of the list from which to retrieve documents.  | [optional] 
 **limit** | **int**| Number of documents to return.  | [optional] 
 **search** | **str**| Search term.  | [optional] 
 **sort** | **str**| Key on which to sort.  | [optional] 
 **reverse** | **bool**| Sort order.  | [optional] 
 **collections** | [**list[str]**](str.md)| Scopes the query by collection.  | [optional] 
 **account_ids** | [**list[str]**](str.md)| Scopes the query by account ID.  | [optional] 
 **fields** | [**list[str]**](str.md)| List of fields to retrieve.  | [optional] 
 **id2** | [**list[str]**](str.md)| IDs is the runtime profile id filter.  | [optional] 
 **os** | [**list[str]**](str.md)| OS is the service runtime profile OS filter.  | [optional] 
 **state** | [**list[str]**](str.md)| States is the runtime profile state filter.  | [optional] 
 **image_id** | [**list[str]**](str.md)| ImageIDs is the runtime profile image id filter.  | [optional] 
 **image** | [**list[str]**](str.md)| Images is the runtime profile image filter.  | [optional] 
 **host_name** | [**list[str]**](str.md)| Hosts is the runtime profile hostname filter.  | [optional] 
 **namespace** | [**list[str]**](str.md)| Namespaces is the runtime profile k8s namespace filter.  | [optional] 
 **cluster** | [**list[str]**](str.md)| Clusters is the runtime profile k8s cluster filter.  | [optional] 

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

# **api_v1_profiles_container_id_learn_post**
> api_v1_profiles_container_id_learn_post(id, types_profile_state_update=types_profile_state_update)



UpdateContainerRuntimeProfileState updates the container profile state. Update flow: 1. Verifies the state is of the manual learning flow (Manual Relearning, Manual learning, and Active) 2. Verifies behavioral learning is enabled 3. Verifies the flow is valid: From a Manual Learning/Relearning state, another Relearning can not be triggered 4. Updates the db 5. Updates the defender 

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
    api_instance = openapi_client.ProfilesApi(api_client)
    id = 'id_example' # str | 
types_profile_state_update = openapi_client.TypesProfileStateUpdate() # TypesProfileStateUpdate |  (optional)

    try:
        api_instance.api_v1_profiles_container_id_learn_post(id, types_profile_state_update=types_profile_state_update)
    except ApiException as e:
        print("Exception when calling ProfilesApi->api_v1_profiles_container_id_learn_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **types_profile_state_update** | [**TypesProfileStateUpdate**](TypesProfileStateUpdate.md)|  | [optional] 

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

# **api_v1_profiles_container_id_rule_get**
> RuntimeContainerPolicyRule api_v1_profiles_container_id_rule_get(id)



ContainerRuntimeProfileRule returns the runtime rule associated with the given profile 

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
    api_instance = openapi_client.ProfilesApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.api_v1_profiles_container_id_rule_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProfilesApi->api_v1_profiles_container_id_rule_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**RuntimeContainerPolicyRule**](RuntimeContainerPolicyRule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ContainerPolicyRule represents a single rule in the runtime policy |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_profiles_container_learn_post**
> api_v1_profiles_container_learn_post()



RelearnAllContainerRuntimeProfiles updates all container runtime profiles state to relearn by the following 2 steps: 1. Broadcast a request to all defenders to relearn all container runtime profiles 2. Update all container runtime profiles state to extended learning in DB 

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
    api_instance = openapi_client.ProfilesApi(api_client)
    
    try:
        api_instance.api_v1_profiles_container_learn_post()
    except ApiException as e:
        print("Exception when calling ProfilesApi->api_v1_profiles_container_learn_post: %s\n" % e)
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

# **api_v1_profiles_host_download_get**
> api_v1_profiles_host_download_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, id=id, os=os, state=state, image_id=image_id, image=image, host_name=host_name, namespace=namespace, cluster=cluster)



DownloadHostsRuntimeProfiles downloads the host runtime profiles according to the specified query 

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
    api_instance = openapi_client.ProfilesApi(api_client)
    offset = 56 # int | Offset from the start of the list from which to retrieve documents.  (optional)
limit = 56 # int | Number of documents to return.  (optional)
search = 'search_example' # str | Search term.  (optional)
sort = 'sort_example' # str | Key on which to sort.  (optional)
reverse = True # bool | Sort order.  (optional)
collections = ['collections_example'] # list[str] | Scopes the query by collection.  (optional)
account_ids = ['account_ids_example'] # list[str] | Scopes the query by account ID.  (optional)
fields = ['fields_example'] # list[str] | List of fields to retrieve.  (optional)
id = ['id_example'] # list[str] | IDs is the runtime profile id filter.  (optional)
os = ['os_example'] # list[str] | OS is the service runtime profile OS filter.  (optional)
state = ['state_example'] # list[str] | States is the runtime profile state filter.  (optional)
image_id = ['image_id_example'] # list[str] | ImageIDs is the runtime profile image id filter.  (optional)
image = ['image_example'] # list[str] | Images is the runtime profile image filter.  (optional)
host_name = ['host_name_example'] # list[str] | Hosts is the runtime profile hostname filter.  (optional)
namespace = ['namespace_example'] # list[str] | Namespaces is the runtime profile k8s namespace filter.  (optional)
cluster = ['cluster_example'] # list[str] | Clusters is the runtime profile k8s cluster filter.  (optional)

    try:
        api_instance.api_v1_profiles_host_download_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, id=id, os=os, state=state, image_id=image_id, image=image, host_name=host_name, namespace=namespace, cluster=cluster)
    except ApiException as e:
        print("Exception when calling ProfilesApi->api_v1_profiles_host_download_get: %s\n" % e)
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
 **id** | [**list[str]**](str.md)| IDs is the runtime profile id filter.  | [optional] 
 **os** | [**list[str]**](str.md)| OS is the service runtime profile OS filter.  | [optional] 
 **state** | [**list[str]**](str.md)| States is the runtime profile state filter.  | [optional] 
 **image_id** | [**list[str]**](str.md)| ImageIDs is the runtime profile image id filter.  | [optional] 
 **image** | [**list[str]**](str.md)| Images is the runtime profile image filter.  | [optional] 
 **host_name** | [**list[str]**](str.md)| Hosts is the runtime profile hostname filter.  | [optional] 
 **namespace** | [**list[str]**](str.md)| Namespaces is the runtime profile k8s namespace filter.  | [optional] 
 **cluster** | [**list[str]**](str.md)| Clusters is the runtime profile k8s cluster filter.  | [optional] 

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

# **api_v1_profiles_host_get**
> list[RuntimeHostProfile] api_v1_profiles_host_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, id=id, os=os, state=state, image_id=image_id, image=image, host_name=host_name, namespace=namespace, cluster=cluster)



HostRuntimeProfiles returns host runtime profiles by the query specification 

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
    api_instance = openapi_client.ProfilesApi(api_client)
    offset = 56 # int | Offset from the start of the list from which to retrieve documents.  (optional)
limit = 56 # int | Number of documents to return.  (optional)
search = 'search_example' # str | Search term.  (optional)
sort = 'sort_example' # str | Key on which to sort.  (optional)
reverse = True # bool | Sort order.  (optional)
collections = ['collections_example'] # list[str] | Scopes the query by collection.  (optional)
account_ids = ['account_ids_example'] # list[str] | Scopes the query by account ID.  (optional)
fields = ['fields_example'] # list[str] | List of fields to retrieve.  (optional)
id = ['id_example'] # list[str] | IDs is the runtime profile id filter.  (optional)
os = ['os_example'] # list[str] | OS is the service runtime profile OS filter.  (optional)
state = ['state_example'] # list[str] | States is the runtime profile state filter.  (optional)
image_id = ['image_id_example'] # list[str] | ImageIDs is the runtime profile image id filter.  (optional)
image = ['image_example'] # list[str] | Images is the runtime profile image filter.  (optional)
host_name = ['host_name_example'] # list[str] | Hosts is the runtime profile hostname filter.  (optional)
namespace = ['namespace_example'] # list[str] | Namespaces is the runtime profile k8s namespace filter.  (optional)
cluster = ['cluster_example'] # list[str] | Clusters is the runtime profile k8s cluster filter.  (optional)

    try:
        api_response = api_instance.api_v1_profiles_host_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, id=id, os=os, state=state, image_id=image_id, image=image, host_name=host_name, namespace=namespace, cluster=cluster)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProfilesApi->api_v1_profiles_host_get: %s\n" % e)
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
 **id** | [**list[str]**](str.md)| IDs is the runtime profile id filter.  | [optional] 
 **os** | [**list[str]**](str.md)| OS is the service runtime profile OS filter.  | [optional] 
 **state** | [**list[str]**](str.md)| States is the runtime profile state filter.  | [optional] 
 **image_id** | [**list[str]**](str.md)| ImageIDs is the runtime profile image id filter.  | [optional] 
 **image** | [**list[str]**](str.md)| Images is the runtime profile image filter.  | [optional] 
 **host_name** | [**list[str]**](str.md)| Hosts is the runtime profile hostname filter.  | [optional] 
 **namespace** | [**list[str]**](str.md)| Namespaces is the runtime profile k8s namespace filter.  | [optional] 
 **cluster** | [**list[str]**](str.md)| Clusters is the runtime profile k8s cluster filter.  | [optional] 

### Return type

[**list[RuntimeHostProfile]**](RuntimeHostProfile.md)

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

# **api_v1_profiles_host_id_forensic_download_get**
> api_v1_profiles_host_id_forensic_download_get(id, collections=collections, account_ids=account_ids, event_time=event_time, hostname=hostname, limit=limit, format=format, incident_id=incident_id)



HostForensicDownload fetches the host forensic data for a specific hostname as CSV. 

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
    api_instance = openapi_client.ProfilesApi(api_client)
    id = 'id_example' # str | 
collections = ['collections_example'] # list[str] | Collections are collections scoping the query.  (optional)
account_ids = ['account_ids_example'] # list[str] | AccountIDs are the account IDs scoping the query.  (optional)
event_time = '2013-10-20T19:20:30+01:00' # datetime | EventTime is the forensic event pivot time in milliseconds (used to fetch events).  (optional)
hostname = 'hostname_example' # str | Hostname is the hostname for which data should be fetched.  (optional)
limit = 56 # int | Limit is the number of events to return.  (optional)
format = 'format_example' # str | Format is the forensic data format.  (optional)
incident_id = 'incident_id_example' # str | IncidentID is the incident ID in case the request kind is an incident.  (optional)

    try:
        api_instance.api_v1_profiles_host_id_forensic_download_get(id, collections=collections, account_ids=account_ids, event_time=event_time, hostname=hostname, limit=limit, format=format, incident_id=incident_id)
    except ApiException as e:
        print("Exception when calling ProfilesApi->api_v1_profiles_host_id_forensic_download_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **collections** | [**list[str]**](str.md)| Collections are collections scoping the query.  | [optional] 
 **account_ids** | [**list[str]**](str.md)| AccountIDs are the account IDs scoping the query.  | [optional] 
 **event_time** | **datetime**| EventTime is the forensic event pivot time in milliseconds (used to fetch events).  | [optional] 
 **hostname** | **str**| Hostname is the hostname for which data should be fetched.  | [optional] 
 **limit** | **int**| Limit is the number of events to return.  | [optional] 
 **format** | **str**| Format is the forensic data format.  | [optional] 
 **incident_id** | **str**| IncidentID is the incident ID in case the request kind is an incident.  | [optional] 

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

# **api_v1_profiles_host_id_forensic_get**
> list[ForensicHostEvent] api_v1_profiles_host_id_forensic_get(id, collections=collections, account_ids=account_ids, event_time=event_time, hostname=hostname, limit=limit, format=format, incident_id=incident_id)



HostForensic fetches the host forensic data for a specific hostname. 

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
    api_instance = openapi_client.ProfilesApi(api_client)
    id = 'id_example' # str | 
collections = ['collections_example'] # list[str] | Collections are collections scoping the query.  (optional)
account_ids = ['account_ids_example'] # list[str] | AccountIDs are the account IDs scoping the query.  (optional)
event_time = '2013-10-20T19:20:30+01:00' # datetime | EventTime is the forensic event pivot time in milliseconds (used to fetch events).  (optional)
hostname = 'hostname_example' # str | Hostname is the hostname for which data should be fetched.  (optional)
limit = 56 # int | Limit is the number of events to return.  (optional)
format = 'format_example' # str | Format is the forensic data format.  (optional)
incident_id = 'incident_id_example' # str | IncidentID is the incident ID in case the request kind is an incident.  (optional)

    try:
        api_response = api_instance.api_v1_profiles_host_id_forensic_get(id, collections=collections, account_ids=account_ids, event_time=event_time, hostname=hostname, limit=limit, format=format, incident_id=incident_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProfilesApi->api_v1_profiles_host_id_forensic_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **collections** | [**list[str]**](str.md)| Collections are collections scoping the query.  | [optional] 
 **account_ids** | [**list[str]**](str.md)| AccountIDs are the account IDs scoping the query.  | [optional] 
 **event_time** | **datetime**| EventTime is the forensic event pivot time in milliseconds (used to fetch events).  | [optional] 
 **hostname** | **str**| Hostname is the hostname for which data should be fetched.  | [optional] 
 **limit** | **int**| Limit is the number of events to return.  | [optional] 
 **format** | **str**| Format is the forensic data format.  | [optional] 
 **incident_id** | **str**| IncidentID is the incident ID in case the request kind is an incident.  | [optional] 

### Return type

[**list[ForensicHostEvent]**](ForensicHostEvent.md)

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


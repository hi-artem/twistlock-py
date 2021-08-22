# openapi_client.RadarApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_radar_container_clusters_get**](RadarApi.md#api_v1_radar_container_clusters_get) | **GET** /api/v1/radar/container/clusters | 
[**api_v1_radar_container_get**](RadarApi.md#api_v1_radar_container_get) | **GET** /api/v1/radar/container | 
[**api_v1_radar_container_namespaces_get**](RadarApi.md#api_v1_radar_container_namespaces_get) | **GET** /api/v1/radar/container/namespaces | 
[**api_v1_radar_host_get**](RadarApi.md#api_v1_radar_host_get) | **GET** /api/v1/radar/host | 
[**api_v1_radar_serverless_get**](RadarApi.md#api_v1_radar_serverless_get) | **GET** /api/v1/radar/serverless | 
[**api_v1_radar_serverless_progress_get**](RadarApi.md#api_v1_radar_serverless_progress_get) | **GET** /api/v1/radar/serverless/progress | 
[**api_v1_radar_serverless_scan_post**](RadarApi.md#api_v1_radar_serverless_scan_post) | **POST** /api/v1/radar/serverless/scan | 
[**api_v1_radar_serverless_stop_post**](RadarApi.md#api_v1_radar_serverless_stop_post) | **POST** /api/v1/radar/serverless/stop | 


# **api_v1_radar_container_clusters_get**
> list[TypesClusterRadarInfo] api_v1_radar_container_clusters_get(collections=collections, account_ids=account_ids)



ContainerRadarClusters returns the clusters for radar filters 

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
    api_instance = openapi_client.RadarApi(api_client)
    collections = ['collections_example'] # list[str] | Collections are collections scoping the query.  (optional)
account_ids = ['account_ids_example'] # list[str] | AccountIDs are the account IDs scoping the query.  (optional)

    try:
        api_response = api_instance.api_v1_radar_container_clusters_get(collections=collections, account_ids=account_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RadarApi->api_v1_radar_container_clusters_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collections** | [**list[str]**](str.md)| Collections are collections scoping the query.  | [optional] 
 **account_ids** | [**list[str]**](str.md)| AccountIDs are the account IDs scoping the query.  | [optional] 

### Return type

[**list[TypesClusterRadarInfo]**](TypesClusterRadarInfo.md)

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

# **api_v1_radar_container_get**
> TypesContainerRadarData api_v1_radar_container_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, hostname=hostname, image=image, image_id=image_id, id=id, profile_id=profile_id, namespaces=namespaces, clusters=clusters, compliance_ids=compliance_ids)



ContainerRadarData returns the container radar data 

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
    api_instance = openapi_client.RadarApi(api_client)
    offset = 56 # int | Offset from the start of the list from which to retrieve documents.  (optional)
limit = 56 # int | Number of documents to return.  (optional)
search = 'search_example' # str | Search term.  (optional)
sort = 'sort_example' # str | Key on which to sort.  (optional)
reverse = True # bool | Sort order.  (optional)
collections = ['collections_example'] # list[str] | Scopes the query by collection.  (optional)
account_ids = ['account_ids_example'] # list[str] | Scopes the query by account ID.  (optional)
fields = ['fields_example'] # list[str] | List of fields to retrieve.  (optional)
hostname = ['hostname_example'] # list[str] | Hosts is used to filter containers by host.  (optional)
image = ['image_example'] # list[str] | Images is used to filter containers by image name.  (optional)
image_id = ['image_id_example'] # list[str] | ImageIDs is used to filter containers by image ids.  (optional)
id = ['id_example'] # list[str] | IDs is used to filter container by container ID.  (optional)
profile_id = ['profile_id_example'] # list[str] | ProfileIDs is used to filter container by runtime profile ID.  (optional)
namespaces = ['namespaces_example'] # list[str] | Namespaces are the namespaces to filter.  (optional)
clusters = ['clusters_example'] # list[str] | Clusters is used to filter containers by cluster name.  (optional)
compliance_ids = [56] # list[int] | ComplianceIDs is used to filter containers by compliance IDs.  (optional)

    try:
        api_response = api_instance.api_v1_radar_container_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, hostname=hostname, image=image, image_id=image_id, id=id, profile_id=profile_id, namespaces=namespaces, clusters=clusters, compliance_ids=compliance_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RadarApi->api_v1_radar_container_get: %s\n" % e)
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
 **hostname** | [**list[str]**](str.md)| Hosts is used to filter containers by host.  | [optional] 
 **image** | [**list[str]**](str.md)| Images is used to filter containers by image name.  | [optional] 
 **image_id** | [**list[str]**](str.md)| ImageIDs is used to filter containers by image ids.  | [optional] 
 **id** | [**list[str]**](str.md)| IDs is used to filter container by container ID.  | [optional] 
 **profile_id** | [**list[str]**](str.md)| ProfileIDs is used to filter container by runtime profile ID.  | [optional] 
 **namespaces** | [**list[str]**](str.md)| Namespaces are the namespaces to filter.  | [optional] 
 **clusters** | [**list[str]**](str.md)| Clusters is used to filter containers by cluster name.  | [optional] 
 **compliance_ids** | [**list[int]**](int.md)| ComplianceIDs is used to filter containers by compliance IDs.  | [optional] 

### Return type

[**TypesContainerRadarData**](TypesContainerRadarData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ContainerRadarData represent all data relevant to the network radar |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_radar_container_namespaces_get**
> list[str] api_v1_radar_container_namespaces_get(collections=collections, account_ids=account_ids, cluster=cluster)



ContainerRadarNamespaces returns the radar namespaces 

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
    api_instance = openapi_client.RadarApi(api_client)
    collections = ['collections_example'] # list[str] | Collections are collections scoping the query.  (optional)
account_ids = ['account_ids_example'] # list[str] | AccountIDs are the account IDs scoping the query.  (optional)
cluster = ['cluster_example'] # list[str] | Clusters is the cluster name to filter by.  (optional)

    try:
        api_response = api_instance.api_v1_radar_container_namespaces_get(collections=collections, account_ids=account_ids, cluster=cluster)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RadarApi->api_v1_radar_container_namespaces_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collections** | [**list[str]**](str.md)| Collections are collections scoping the query.  | [optional] 
 **account_ids** | [**list[str]**](str.md)| AccountIDs are the account IDs scoping the query.  | [optional] 
 **cluster** | [**list[str]**](str.md)| Clusters is the cluster name to filter by.  | [optional] 

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

# **api_v1_radar_host_get**
> TypesHostRadarData api_v1_radar_host_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, profile_id=profile_id, filter_disconnected=filter_disconnected)



HostRadarData returns the host radar data 

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
    api_instance = openapi_client.RadarApi(api_client)
    offset = 56 # int | Offset from the start of the list from which to retrieve documents.  (optional)
limit = 56 # int | Number of documents to return.  (optional)
search = 'search_example' # str | Search term.  (optional)
sort = 'sort_example' # str | Key on which to sort.  (optional)
reverse = True # bool | Sort order.  (optional)
collections = ['collections_example'] # list[str] | Scopes the query by collection.  (optional)
account_ids = ['account_ids_example'] # list[str] | Scopes the query by account ID.  (optional)
fields = ['fields_example'] # list[str] | List of fields to retrieve.  (optional)
profile_id = 'profile_id_example' # str | ProfileID is used to filter radar by service profile ID.  (optional)
filter_disconnected = True # bool | FilterDisconnected indicates if only entities with connections should be returned.  (optional)

    try:
        api_response = api_instance.api_v1_radar_host_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, profile_id=profile_id, filter_disconnected=filter_disconnected)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RadarApi->api_v1_radar_host_get: %s\n" % e)
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
 **profile_id** | **str**| ProfileID is used to filter radar by service profile ID.  | [optional] 
 **filter_disconnected** | **bool**| FilterDisconnected indicates if only entities with connections should be returned.  | [optional] 

### Return type

[**TypesHostRadarData**](TypesHostRadarData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | HostRadarData represent all data relevant to the network radar |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_radar_serverless_get**
> ServerlessRadarData api_v1_radar_serverless_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, provider=provider, region=region, credential_id=credential_id)



ServerlessRadarData returns the serverless radar data 

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
    api_instance = openapi_client.RadarApi(api_client)
    offset = 56 # int | Offset from the start of the list from which to retrieve documents.  (optional)
limit = 56 # int | Number of documents to return.  (optional)
search = 'search_example' # str | Search term.  (optional)
sort = 'sort_example' # str | Key on which to sort.  (optional)
reverse = True # bool | Sort order.  (optional)
collections = ['collections_example'] # list[str] | Scopes the query by collection.  (optional)
account_ids = ['account_ids_example'] # list[str] | Scopes the query by account ID.  (optional)
fields = ['fields_example'] # list[str] | List of fields to retrieve.  (optional)
provider = ['provider_example'] # list[str] | Provider is the provider filter.  (optional)
region = ['region_example'] # list[str] | Region is the region filter.  (optional)
credential_id = ['credential_id_example'] # list[str] | CredentialID is the account filter.  (optional)

    try:
        api_response = api_instance.api_v1_radar_serverless_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, provider=provider, region=region, credential_id=credential_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RadarApi->api_v1_radar_serverless_get: %s\n" % e)
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
 **provider** | [**list[str]**](str.md)| Provider is the provider filter.  | [optional] 
 **region** | [**list[str]**](str.md)| Region is the region filter.  | [optional] 
 **credential_id** | [**list[str]**](str.md)| CredentialID is the account filter.  | [optional] 

### Return type

[**ServerlessRadarData**](ServerlessRadarData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | RadarData represent all data relevant to the serverless radar |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_radar_serverless_progress_get**
> list[SharedProgress] api_v1_radar_serverless_progress_get()



ServerlessRadarProgress returns the serverless radar scan progress 

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
    api_instance = openapi_client.RadarApi(api_client)
    
    try:
        api_response = api_instance.api_v1_radar_serverless_progress_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RadarApi->api_v1_radar_serverless_progress_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SharedProgress]**](SharedProgress.md)

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

# **api_v1_radar_serverless_scan_post**
> api_v1_radar_serverless_scan_post()



DoServerlessRadarScan starts a new serverless radar scan 

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
    api_instance = openapi_client.RadarApi(api_client)
    
    try:
        api_instance.api_v1_radar_serverless_scan_post()
    except ApiException as e:
        print("Exception when calling RadarApi->api_v1_radar_serverless_scan_post: %s\n" % e)
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

# **api_v1_radar_serverless_stop_post**
> api_v1_radar_serverless_stop_post()



StopServerlessRadarScan stops a serverless radar scan in progress 

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
    api_instance = openapi_client.RadarApi(api_client)
    
    try:
        api_instance.api_v1_radar_serverless_stop_post()
    except ApiException as e:
        print("Exception when calling RadarApi->api_v1_radar_serverless_stop_post: %s\n" % e)
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


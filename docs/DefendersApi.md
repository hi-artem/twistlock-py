# openapi_client.DefendersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_defenders_app_embedded_post**](DefendersApi.md#api_v1_defenders_app_embedded_post) | **POST** /api/v1/defenders/app-embedded | 
[**api_v1_defenders_daemonset_yaml_post**](DefendersApi.md#api_v1_defenders_daemonset_yaml_post) | **POST** /api/v1/defenders/daemonset.yaml | 
[**api_v1_defenders_download_get**](DefendersApi.md#api_v1_defenders_download_get) | **GET** /api/v1/defenders/download | 
[**api_v1_defenders_ecs_task_json_post**](DefendersApi.md#api_v1_defenders_ecs_task_json_post) | **POST** /api/v1/defenders/ecs-task.json | 
[**api_v1_defenders_fargate_json_post**](DefendersApi.md#api_v1_defenders_fargate_json_post) | **POST** /api/v1/defenders/fargate.json | 
[**api_v1_defenders_get**](DefendersApi.md#api_v1_defenders_get) | **GET** /api/v1/defenders | 
[**api_v1_defenders_helm_twistlock_defender_helm_tar_gz_post**](DefendersApi.md#api_v1_defenders_helm_twistlock_defender_helm_tar_gz_post) | **POST** /api/v1/defenders/helm/twistlock-defender-helm.tar.gz | 
[**api_v1_defenders_id_delete**](DefendersApi.md#api_v1_defenders_id_delete) | **DELETE** /api/v1/defenders/{id} | 
[**api_v1_defenders_id_features_post**](DefendersApi.md#api_v1_defenders_id_features_post) | **POST** /api/v1/defenders/{id}/features | 
[**api_v1_defenders_id_restart_post**](DefendersApi.md#api_v1_defenders_id_restart_post) | **POST** /api/v1/defenders/{id}/restart | 
[**api_v1_defenders_id_upgrade_post**](DefendersApi.md#api_v1_defenders_id_upgrade_post) | **POST** /api/v1/defenders/{id}/upgrade | 
[**api_v1_defenders_image_name_get**](DefendersApi.md#api_v1_defenders_image_name_get) | **GET** /api/v1/defenders/image-name | 
[**api_v1_defenders_install_bundle_get**](DefendersApi.md#api_v1_defenders_install_bundle_get) | **GET** /api/v1/defenders/install-bundle | 
[**api_v1_defenders_names_get**](DefendersApi.md#api_v1_defenders_names_get) | **GET** /api/v1/defenders/names | 
[**api_v1_defenders_serverless_bundle_post**](DefendersApi.md#api_v1_defenders_serverless_bundle_post) | **POST** /api/v1/defenders/serverless/bundle | 
[**api_v1_defenders_summary_get**](DefendersApi.md#api_v1_defenders_summary_get) | **GET** /api/v1/defenders/summary | 
[**api_v1_defenders_upgrade_post**](DefendersApi.md#api_v1_defenders_upgrade_post) | **POST** /api/v1/defenders/upgrade | 


# **api_v1_defenders_app_embedded_post**
> api_v1_defenders_app_embedded_post(shared_app_embedded_embed_request=shared_app_embedded_embed_request)



EmbedAppEmbeddedDefender returns an augmented Dockerfile + embedded defender dependencies as a ZIP file 

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
    api_instance = openapi_client.DefendersApi(api_client)
    shared_app_embedded_embed_request = openapi_client.SharedAppEmbeddedEmbedRequest() # SharedAppEmbeddedEmbedRequest |  (optional)

    try:
        api_instance.api_v1_defenders_app_embedded_post(shared_app_embedded_embed_request=shared_app_embedded_embed_request)
    except ApiException as e:
        print("Exception when calling DefendersApi->api_v1_defenders_app_embedded_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shared_app_embedded_embed_request** | [**SharedAppEmbeddedEmbedRequest**](SharedAppEmbeddedEmbedRequest.md)|  | [optional] 

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

# **api_v1_defenders_daemonset_yaml_post**
> list[int] api_v1_defenders_daemonset_yaml_post(common_daemon_set_options=common_daemon_set_options)



GenerateDaemonSet generates the defender daemonset k8s yaml 

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
    api_instance = openapi_client.DefendersApi(api_client)
    common_daemon_set_options = openapi_client.CommonDaemonSetOptions() # CommonDaemonSetOptions |  (optional)

    try:
        api_response = api_instance.api_v1_defenders_daemonset_yaml_post(common_daemon_set_options=common_daemon_set_options)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefendersApi->api_v1_defenders_daemonset_yaml_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **common_daemon_set_options** | [**CommonDaemonSetOptions**](CommonDaemonSetOptions.md)|  | [optional] 

### Return type

**list[int]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_defenders_download_get**
> api_v1_defenders_download_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, hostname=hostname, role=role, connected=connected, type=type, latest=latest, cluster=cluster, tas_cluster_ids=tas_cluster_ids)



DownloadDefenders downloads all defender data 

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
    api_instance = openapi_client.DefendersApi(api_client)
    offset = 56 # int | Offset from the start of the list from which to retrieve documents.  (optional)
limit = 56 # int | Number of documents to return.  (optional)
search = 'search_example' # str | Search term.  (optional)
sort = 'sort_example' # str | Key on which to sort.  (optional)
reverse = True # bool | Sort order.  (optional)
collections = ['collections_example'] # list[str] | Scopes the query by collection.  (optional)
account_ids = ['account_ids_example'] # list[str] | Scopes the query by account ID.  (optional)
fields = ['fields_example'] # list[str] | List of fields to retrieve.  (optional)
hostname = 'hostname_example' # str | Name of a specific Defender to retrieve.  (optional)
role = ['role_example'] # list[str] | Roles are the defender api.Roles to filter.  (optional)
connected = True # bool | Indicates whether to return only connected Defenders (true) or all deployed Defenders (false).  (optional)
type = ['type_example'] # list[str] | Indicates the Defender types to return (e.g., docker, dockerWindows, cri, etc).  (optional)
latest = True # bool | Indicates whether to return a list of Defenders that are running the latest version of Prisma Cloud (true) or all Defenders regardless of version (false).  (optional)
cluster = ['cluster_example'] # list[str] | Scopes the query by cluster name.  (optional)
tas_cluster_ids = ['tas_cluster_ids_example'] # list[str] | Scopes the query by TAS cluster IDs.  (optional)

    try:
        api_instance.api_v1_defenders_download_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, hostname=hostname, role=role, connected=connected, type=type, latest=latest, cluster=cluster, tas_cluster_ids=tas_cluster_ids)
    except ApiException as e:
        print("Exception when calling DefendersApi->api_v1_defenders_download_get: %s\n" % e)
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
 **hostname** | **str**| Name of a specific Defender to retrieve.  | [optional] 
 **role** | [**list[str]**](str.md)| Roles are the defender api.Roles to filter.  | [optional] 
 **connected** | **bool**| Indicates whether to return only connected Defenders (true) or all deployed Defenders (false).  | [optional] 
 **type** | [**list[str]**](str.md)| Indicates the Defender types to return (e.g., docker, dockerWindows, cri, etc).  | [optional] 
 **latest** | **bool**| Indicates whether to return a list of Defenders that are running the latest version of Prisma Cloud (true) or all Defenders regardless of version (false).  | [optional] 
 **cluster** | [**list[str]**](str.md)| Scopes the query by cluster name.  | [optional] 
 **tas_cluster_ids** | [**list[str]**](str.md)| Scopes the query by TAS cluster IDs.  | [optional] 

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

# **api_v1_defenders_ecs_task_json_post**
> list[int] api_v1_defenders_ecs_task_json_post(types_ecs_task_definition_options=types_ecs_task_definition_options)



GenerateEcsTaskDefinition generates the defender ecs task definition json 

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
    api_instance = openapi_client.DefendersApi(api_client)
    types_ecs_task_definition_options = openapi_client.TypesEcsTaskDefinitionOptions() # TypesEcsTaskDefinitionOptions |  (optional)

    try:
        api_response = api_instance.api_v1_defenders_ecs_task_json_post(types_ecs_task_definition_options=types_ecs_task_definition_options)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefendersApi->api_v1_defenders_ecs_task_json_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **types_ecs_task_definition_options** | [**TypesEcsTaskDefinitionOptions**](TypesEcsTaskDefinitionOptions.md)|  | [optional] 

### Return type

**list[int]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_defenders_fargate_json_post**
> dict(str, str) api_v1_defenders_fargate_json_post(consoleaddr=consoleaddr, defender_type=defender_type, interpreter=interpreter, request_body=request_body)



FargateTask receives fargate task definition, augments all required data and returns new task definition 

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
    api_instance = openapi_client.DefendersApi(api_client)
    consoleaddr = 'consoleaddr_example' # str | consoleaddr is the remote console address.  (optional)
defender_type = 'defender_type_example' # str | DefenderType is the type of the defender to create the install bundle for.  (optional)
interpreter = 'interpreter_example' # str | Interpreter is a custom interpreter set by the user to run the fargate defender entrypoint script.  (optional)
request_body = {'key': 'request_body_example'} # dict(str, str) |  (optional)

    try:
        api_response = api_instance.api_v1_defenders_fargate_json_post(consoleaddr=consoleaddr, defender_type=defender_type, interpreter=interpreter, request_body=request_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefendersApi->api_v1_defenders_fargate_json_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consoleaddr** | **str**| consoleaddr is the remote console address.  | [optional] 
 **defender_type** | **str**| DefenderType is the type of the defender to create the install bundle for.  | [optional] 
 **interpreter** | **str**| Interpreter is a custom interpreter set by the user to run the fargate defender entrypoint script.  | [optional] 
 **request_body** | [**dict(str, str)**](str.md)|  | [optional] 

### Return type

**dict(str, str)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | FargateTask represents the generic fargate task AWS template |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_defenders_get**
> list[DefenderDefender] api_v1_defenders_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, hostname=hostname, role=role, connected=connected, type=type, latest=latest, cluster=cluster, tas_cluster_ids=tas_cluster_ids)



Defenders returns the defenders by the query specification 

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
    api_instance = openapi_client.DefendersApi(api_client)
    offset = 56 # int | Offset from the start of the list from which to retrieve documents.  (optional)
limit = 56 # int | Number of documents to return.  (optional)
search = 'search_example' # str | Search term.  (optional)
sort = 'sort_example' # str | Key on which to sort.  (optional)
reverse = True # bool | Sort order.  (optional)
collections = ['collections_example'] # list[str] | Scopes the query by collection.  (optional)
account_ids = ['account_ids_example'] # list[str] | Scopes the query by account ID.  (optional)
fields = ['fields_example'] # list[str] | List of fields to retrieve.  (optional)
hostname = 'hostname_example' # str | Name of a specific Defender to retrieve.  (optional)
role = ['role_example'] # list[str] | Roles are the defender api.Roles to filter.  (optional)
connected = True # bool | Indicates whether to return only connected Defenders (true) or all deployed Defenders (false).  (optional)
type = ['type_example'] # list[str] | Indicates the Defender types to return (e.g., docker, dockerWindows, cri, etc).  (optional)
latest = True # bool | Indicates whether to return a list of Defenders that are running the latest version of Prisma Cloud (true) or all Defenders regardless of version (false).  (optional)
cluster = ['cluster_example'] # list[str] | Scopes the query by cluster name.  (optional)
tas_cluster_ids = ['tas_cluster_ids_example'] # list[str] | Scopes the query by TAS cluster IDs.  (optional)

    try:
        api_response = api_instance.api_v1_defenders_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, hostname=hostname, role=role, connected=connected, type=type, latest=latest, cluster=cluster, tas_cluster_ids=tas_cluster_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefendersApi->api_v1_defenders_get: %s\n" % e)
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
 **hostname** | **str**| Name of a specific Defender to retrieve.  | [optional] 
 **role** | [**list[str]**](str.md)| Roles are the defender api.Roles to filter.  | [optional] 
 **connected** | **bool**| Indicates whether to return only connected Defenders (true) or all deployed Defenders (false).  | [optional] 
 **type** | [**list[str]**](str.md)| Indicates the Defender types to return (e.g., docker, dockerWindows, cri, etc).  | [optional] 
 **latest** | **bool**| Indicates whether to return a list of Defenders that are running the latest version of Prisma Cloud (true) or all Defenders regardless of version (false).  | [optional] 
 **cluster** | [**list[str]**](str.md)| Scopes the query by cluster name.  | [optional] 
 **tas_cluster_ids** | [**list[str]**](str.md)| Scopes the query by TAS cluster IDs.  | [optional] 

### Return type

[**list[DefenderDefender]**](DefenderDefender.md)

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

# **api_v1_defenders_helm_twistlock_defender_helm_tar_gz_post**
> api_v1_defenders_helm_twistlock_defender_helm_tar_gz_post(common_daemon_set_options=common_daemon_set_options)



DefenderHelmChart generates a defender helm chart 

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
    api_instance = openapi_client.DefendersApi(api_client)
    common_daemon_set_options = openapi_client.CommonDaemonSetOptions() # CommonDaemonSetOptions |  (optional)

    try:
        api_instance.api_v1_defenders_helm_twistlock_defender_helm_tar_gz_post(common_daemon_set_options=common_daemon_set_options)
    except ApiException as e:
        print("Exception when calling DefendersApi->api_v1_defenders_helm_twistlock_defender_helm_tar_gz_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **common_daemon_set_options** | [**CommonDaemonSetOptions**](CommonDaemonSetOptions.md)|  | [optional] 

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

# **api_v1_defenders_id_delete**
> api_v1_defenders_id_delete(id)



DeleteDefender deletes the specified defender 

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
    api_instance = openapi_client.DefendersApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.api_v1_defenders_id_delete(id)
    except ApiException as e:
        print("Exception when calling DefendersApi->api_v1_defenders_id_delete: %s\n" % e)
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

# **api_v1_defenders_id_features_post**
> DefenderDefender api_v1_defenders_id_features_post(id, defender_features=defender_features)



UpdateDefenderFeatures update the specified defender features 

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
    api_instance = openapi_client.DefendersApi(api_client)
    id = 'id_example' # str | 
defender_features = openapi_client.DefenderFeatures() # DefenderFeatures |  (optional)

    try:
        api_response = api_instance.api_v1_defenders_id_features_post(id, defender_features=defender_features)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefendersApi->api_v1_defenders_id_features_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **defender_features** | [**DefenderFeatures**](DefenderFeatures.md)|  | [optional] 

### Return type

[**DefenderDefender**](DefenderDefender.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Defender is an update about an agent starting |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_defenders_id_restart_post**
> api_v1_defenders_id_restart_post(id)



RestartDefender restarts a specific defender 

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
    api_instance = openapi_client.DefendersApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.api_v1_defenders_id_restart_post(id)
    except ApiException as e:
        print("Exception when calling DefendersApi->api_v1_defenders_id_restart_post: %s\n" % e)
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

# **api_v1_defenders_id_upgrade_post**
> api_v1_defenders_id_upgrade_post(id)



UpgradeDefender upgrades a specific defender 

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
    api_instance = openapi_client.DefendersApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.api_v1_defenders_id_upgrade_post(id)
    except ApiException as e:
        print("Exception when calling DefendersApi->api_v1_defenders_id_upgrade_post: %s\n" % e)
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

# **api_v1_defenders_image_name_get**
> str api_v1_defenders_image_name_get()



DefenderImage returns the path to the official defender image 

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
    api_instance = openapi_client.DefendersApi(api_client)
    
    try:
        api_response = api_instance.api_v1_defenders_image_name_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefendersApi->api_v1_defenders_image_name_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

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

# **api_v1_defenders_install_bundle_get**
> SharedDefenderInstallBundle api_v1_defenders_install_bundle_get(consoleaddr=consoleaddr, defender_type=defender_type, interpreter=interpreter)



DefenderInstallBundle returns the install bundle according to the provided configuration 

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
    api_instance = openapi_client.DefendersApi(api_client)
    consoleaddr = 'consoleaddr_example' # str | consoleaddr is the remote console address.  (optional)
defender_type = 'defender_type_example' # str | DefenderType is the type of the defender to create the install bundle for.  (optional)
interpreter = 'interpreter_example' # str | Interpreter is a custom interpreter set by the user to run the fargate defender entrypoint script.  (optional)

    try:
        api_response = api_instance.api_v1_defenders_install_bundle_get(consoleaddr=consoleaddr, defender_type=defender_type, interpreter=interpreter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefendersApi->api_v1_defenders_install_bundle_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consoleaddr** | **str**| consoleaddr is the remote console address.  | [optional] 
 **defender_type** | **str**| DefenderType is the type of the defender to create the install bundle for.  | [optional] 
 **interpreter** | **str**| Interpreter is a custom interpreter set by the user to run the fargate defender entrypoint script.  | [optional] 

### Return type

[**SharedDefenderInstallBundle**](SharedDefenderInstallBundle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | DefenderInstallBundle represents the install bundle for the defender |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_defenders_names_get**
> list[str] api_v1_defenders_names_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, hostname=hostname, role=role, connected=connected, type=type, latest=latest, cluster=cluster, tas_cluster_ids=tas_cluster_ids)



DefenderNames returns the defenders names by the query specification 

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
    api_instance = openapi_client.DefendersApi(api_client)
    offset = 56 # int | Offset from the start of the list from which to retrieve documents.  (optional)
limit = 56 # int | Number of documents to return.  (optional)
search = 'search_example' # str | Search term.  (optional)
sort = 'sort_example' # str | Key on which to sort.  (optional)
reverse = True # bool | Sort order.  (optional)
collections = ['collections_example'] # list[str] | Scopes the query by collection.  (optional)
account_ids = ['account_ids_example'] # list[str] | Scopes the query by account ID.  (optional)
fields = ['fields_example'] # list[str] | List of fields to retrieve.  (optional)
hostname = 'hostname_example' # str | Name of a specific Defender to retrieve.  (optional)
role = ['role_example'] # list[str] | Roles are the defender api.Roles to filter.  (optional)
connected = True # bool | Indicates whether to return only connected Defenders (true) or all deployed Defenders (false).  (optional)
type = ['type_example'] # list[str] | Indicates the Defender types to return (e.g., docker, dockerWindows, cri, etc).  (optional)
latest = True # bool | Indicates whether to return a list of Defenders that are running the latest version of Prisma Cloud (true) or all Defenders regardless of version (false).  (optional)
cluster = ['cluster_example'] # list[str] | Scopes the query by cluster name.  (optional)
tas_cluster_ids = ['tas_cluster_ids_example'] # list[str] | Scopes the query by TAS cluster IDs.  (optional)

    try:
        api_response = api_instance.api_v1_defenders_names_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, hostname=hostname, role=role, connected=connected, type=type, latest=latest, cluster=cluster, tas_cluster_ids=tas_cluster_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefendersApi->api_v1_defenders_names_get: %s\n" % e)
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
 **hostname** | **str**| Name of a specific Defender to retrieve.  | [optional] 
 **role** | [**list[str]**](str.md)| Roles are the defender api.Roles to filter.  | [optional] 
 **connected** | **bool**| Indicates whether to return only connected Defenders (true) or all deployed Defenders (false).  | [optional] 
 **type** | [**list[str]**](str.md)| Indicates the Defender types to return (e.g., docker, dockerWindows, cri, etc).  | [optional] 
 **latest** | **bool**| Indicates whether to return a list of Defenders that are running the latest version of Prisma Cloud (true) or all Defenders regardless of version (false).  | [optional] 
 **cluster** | [**list[str]**](str.md)| Scopes the query by cluster name.  | [optional] 
 **tas_cluster_ids** | [**list[str]**](str.md)| Scopes the query by TAS cluster IDs.  | [optional] 

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

# **api_v1_defenders_serverless_bundle_post**
> api_v1_defenders_serverless_bundle_post(shared_serverless_bundle_request=shared_serverless_bundle_request)



DownloadServerlessBundle returns a ZIP with serverless defender bundle 

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
    api_instance = openapi_client.DefendersApi(api_client)
    shared_serverless_bundle_request = openapi_client.SharedServerlessBundleRequest() # SharedServerlessBundleRequest |  (optional)

    try:
        api_instance.api_v1_defenders_serverless_bundle_post(shared_serverless_bundle_request=shared_serverless_bundle_request)
    except ApiException as e:
        print("Exception when calling DefendersApi->api_v1_defenders_serverless_bundle_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shared_serverless_bundle_request** | [**SharedServerlessBundleRequest**](SharedServerlessBundleRequest.md)|  | [optional] 

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

# **api_v1_defenders_summary_get**
> list[TypesDefenderSummary] api_v1_defenders_summary_get()



DefendersSummary returns the number of defenders in each defender category 

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
    api_instance = openapi_client.DefendersApi(api_client)
    
    try:
        api_response = api_instance.api_v1_defenders_summary_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefendersApi->api_v1_defenders_summary_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[TypesDefenderSummary]**](TypesDefenderSummary.md)

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

# **api_v1_defenders_upgrade_post**
> api_v1_defenders_upgrade_post()



UpgradeDefenders upgrades all linux defenders Remark: only connected defenders are updated 

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
    api_instance = openapi_client.DefendersApi(api_client)
    
    try:
        api_instance.api_v1_defenders_upgrade_post()
    except ApiException as e:
        print("Exception when calling DefendersApi->api_v1_defenders_upgrade_post: %s\n" % e)
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


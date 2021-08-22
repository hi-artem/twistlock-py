# openapi_client.DeploymentApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_deployment_daemonsets_deploy_post**](DeploymentApi.md#api_v1_deployment_daemonsets_deploy_post) | **POST** /api/v1/deployment/daemonsets/deploy | 
[**api_v1_deployment_daemonsets_get**](DeploymentApi.md#api_v1_deployment_daemonsets_get) | **GET** /api/v1/deployment/daemonsets | 
[**api_v1_deployment_host_progress_get**](DeploymentApi.md#api_v1_deployment_host_progress_get) | **GET** /api/v1/deployment/host/progress | 
[**api_v1_deployment_host_scan_post**](DeploymentApi.md#api_v1_deployment_host_scan_post) | **POST** /api/v1/deployment/host/scan | 
[**api_v1_deployment_host_stop_post**](DeploymentApi.md#api_v1_deployment_host_stop_post) | **POST** /api/v1/deployment/host/stop | 
[**api_v1_deployment_serverless_progress_get**](DeploymentApi.md#api_v1_deployment_serverless_progress_get) | **GET** /api/v1/deployment/serverless/progress | 
[**api_v1_deployment_serverless_scan_post**](DeploymentApi.md#api_v1_deployment_serverless_scan_post) | **POST** /api/v1/deployment/serverless/scan | 
[**api_v1_deployment_serverless_stop_post**](DeploymentApi.md#api_v1_deployment_serverless_stop_post) | **POST** /api/v1/deployment/serverless/stop | 


# **api_v1_deployment_daemonsets_deploy_post**
> api_v1_deployment_daemonsets_deploy_post(common_daemon_set_options=common_daemon_set_options)



DeployDaemonSet deploys the DaemonSet provided by options 

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
    api_instance = openapi_client.DeploymentApi(api_client)
    common_daemon_set_options = openapi_client.CommonDaemonSetOptions() # CommonDaemonSetOptions |  (optional)

    try:
        api_instance.api_v1_deployment_daemonsets_deploy_post(common_daemon_set_options=common_daemon_set_options)
    except ApiException as e:
        print("Exception when calling DeploymentApi->api_v1_deployment_daemonsets_deploy_post: %s\n" % e)
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

# **api_v1_deployment_daemonsets_get**
> list[DeploymentDaemonSet] api_v1_deployment_daemonsets_get(credential_id=credential_id)



DefenderDaemonSets returns deployed defender daemonset based on the provided credential 

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
    api_instance = openapi_client.DeploymentApi(api_client)
    credential_id = 'credential_id_example' # str | CredentialID is the name of the credential used.  (optional)

    try:
        api_response = api_instance.api_v1_deployment_daemonsets_get(credential_id=credential_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeploymentApi->api_v1_deployment_daemonsets_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_id** | **str**| CredentialID is the name of the credential used.  | [optional] 

### Return type

[**list[DeploymentDaemonSet]**](DeploymentDaemonSet.md)

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

# **api_v1_deployment_host_progress_get**
> list[SharedProgress] api_v1_deployment_host_progress_get()



HostAutoDeployProgress returns the host auto-deploy progress 

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
    api_instance = openapi_client.DeploymentApi(api_client)
    
    try:
        api_response = api_instance.api_v1_deployment_host_progress_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeploymentApi->api_v1_deployment_host_progress_get: %s\n" % e)
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

# **api_v1_deployment_host_scan_post**
> api_v1_deployment_host_scan_post()



StartHostAutoDeploy starts a host auto-deploy 

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
    api_instance = openapi_client.DeploymentApi(api_client)
    
    try:
        api_instance.api_v1_deployment_host_scan_post()
    except ApiException as e:
        print("Exception when calling DeploymentApi->api_v1_deployment_host_scan_post: %s\n" % e)
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

# **api_v1_deployment_host_stop_post**
> api_v1_deployment_host_stop_post()



StopHostAutoDeploy stops the host auto-deploy auto-deploy scan 

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
    api_instance = openapi_client.DeploymentApi(api_client)
    
    try:
        api_instance.api_v1_deployment_host_stop_post()
    except ApiException as e:
        print("Exception when calling DeploymentApi->api_v1_deployment_host_stop_post: %s\n" % e)
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

# **api_v1_deployment_serverless_progress_get**
> list[SharedProgress] api_v1_deployment_serverless_progress_get()



ServerlessAutoDeployProgress returns the serverless auto-deploy scan progress 

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
    api_instance = openapi_client.DeploymentApi(api_client)
    
    try:
        api_response = api_instance.api_v1_deployment_serverless_progress_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeploymentApi->api_v1_deployment_serverless_progress_get: %s\n" % e)
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

# **api_v1_deployment_serverless_scan_post**
> api_v1_deployment_serverless_scan_post()



StartServerlessAutoDeploy starts a serverless auto-deploy scan 

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
    api_instance = openapi_client.DeploymentApi(api_client)
    
    try:
        api_instance.api_v1_deployment_serverless_scan_post()
    except ApiException as e:
        print("Exception when calling DeploymentApi->api_v1_deployment_serverless_scan_post: %s\n" % e)
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

# **api_v1_deployment_serverless_stop_post**
> api_v1_deployment_serverless_stop_post()



StopServerlessAutoDeploy stops a serverless auto-deploy scan 

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
    api_instance = openapi_client.DeploymentApi(api_client)
    
    try:
        api_instance.api_v1_deployment_serverless_stop_post()
    except ApiException as e:
        print("Exception when calling DeploymentApi->api_v1_deployment_serverless_stop_post: %s\n" % e)
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


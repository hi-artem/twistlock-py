# openapi_client.StatusesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_statuses_host_auto_deploy_get**](StatusesApi.md#api_v1_statuses_host_auto_deploy_get) | **GET** /api/v1/statuses/host-auto-deploy | 
[**api_v1_statuses_intelligence_get**](StatusesApi.md#api_v1_statuses_intelligence_get) | **GET** /api/v1/statuses/intelligence | 
[**api_v1_statuses_registry_get**](StatusesApi.md#api_v1_statuses_registry_get) | **GET** /api/v1/statuses/registry | 
[**api_v1_statuses_secrets_get**](StatusesApi.md#api_v1_statuses_secrets_get) | **GET** /api/v1/statuses/secrets | 
[**api_v1_statuses_serverless_auto_deploy_get**](StatusesApi.md#api_v1_statuses_serverless_auto_deploy_get) | **GET** /api/v1/statuses/serverless-auto-deploy | 
[**api_v1_statuses_serverless_radar_get**](StatusesApi.md#api_v1_statuses_serverless_radar_get) | **GET** /api/v1/statuses/serverless-radar | 


# **api_v1_statuses_host_auto_deploy_get**
> TypesStatus api_v1_statuses_host_auto_deploy_get()



HostAutoDeployStatus returns the host auto-deploy status 

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
    api_instance = openapi_client.StatusesApi(api_client)
    
    try:
        api_response = api_instance.api_v1_statuses_host_auto_deploy_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatusesApi->api_v1_statuses_host_auto_deploy_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TypesStatus**](TypesStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status stores the status of a specific defender or for global features such as intelligence or LDAP |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_statuses_intelligence_get**
> TypesStatus api_v1_statuses_intelligence_get()



IntelligenceStatus returns the intelligence connectivity status 

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
    api_instance = openapi_client.StatusesApi(api_client)
    
    try:
        api_response = api_instance.api_v1_statuses_intelligence_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatusesApi->api_v1_statuses_intelligence_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TypesStatus**](TypesStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status stores the status of a specific defender or for global features such as intelligence or LDAP |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_statuses_registry_get**
> DefenderScanStatus api_v1_statuses_registry_get()



RegistryScanStatus returns the registry scan status 

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
    api_instance = openapi_client.StatusesApi(api_client)
    
    try:
        api_response = api_instance.api_v1_statuses_registry_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatusesApi->api_v1_statuses_registry_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DefenderScanStatus**](DefenderScanStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ScanStatus represents the status of current scan |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_statuses_secrets_get**
> TypesStatus api_v1_statuses_secrets_get()



SecretsStatus returns the secrets discovery status 

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
    api_instance = openapi_client.StatusesApi(api_client)
    
    try:
        api_response = api_instance.api_v1_statuses_secrets_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatusesApi->api_v1_statuses_secrets_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TypesStatus**](TypesStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status stores the status of a specific defender or for global features such as intelligence or LDAP |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_statuses_serverless_auto_deploy_get**
> TypesStatus api_v1_statuses_serverless_auto_deploy_get()



ServerlessAutoDeployStatus returns the serverless auto-deploy scan status 

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
    api_instance = openapi_client.StatusesApi(api_client)
    
    try:
        api_response = api_instance.api_v1_statuses_serverless_auto_deploy_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatusesApi->api_v1_statuses_serverless_auto_deploy_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TypesStatus**](TypesStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status stores the status of a specific defender or for global features such as intelligence or LDAP |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_statuses_serverless_radar_get**
> TypesStatus api_v1_statuses_serverless_radar_get()



ServerlessRadarStatus returns the serverless radar scans status 

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
    api_instance = openapi_client.StatusesApi(api_client)
    
    try:
        api_response = api_instance.api_v1_statuses_serverless_radar_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatusesApi->api_v1_statuses_serverless_radar_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TypesStatus**](TypesStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status stores the status of a specific defender or for global features such as intelligence or LDAP |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


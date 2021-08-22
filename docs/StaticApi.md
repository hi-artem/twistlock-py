# openapi_client.StaticApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_static_licenses_get**](StaticApi.md#api_v1_static_licenses_get) | **GET** /api/v1/static/licenses | 
[**api_v1_static_regions_get**](StaticApi.md#api_v1_static_regions_get) | **GET** /api/v1/static/regions | 
[**api_v1_static_serverless_runtimes_get**](StaticApi.md#api_v1_static_serverless_runtimes_get) | **GET** /api/v1/static/serverless-runtimes | 
[**api_v1_static_vulnerabilities_get**](StaticApi.md#api_v1_static_vulnerabilities_get) | **GET** /api/v1/static/vulnerabilities | 


# **api_v1_static_licenses_get**
> list[str] api_v1_static_licenses_get()



AvailableLicenses returns the list of all available package licenses 

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
    api_instance = openapi_client.StaticApi(api_client)
    
    try:
        api_response = api_instance.api_v1_static_licenses_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StaticApi->api_v1_static_licenses_get: %s\n" % e)
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

# **api_v1_static_regions_get**
> dict(str, list) api_v1_static_regions_get()



RegionsData returns the list of all available regions 

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
    api_instance = openapi_client.StaticApi(api_client)
    
    try:
        api_response = api_instance.api_v1_static_regions_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StaticApi->api_v1_static_regions_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**dict(str, list)**

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

# **api_v1_static_serverless_runtimes_get**
> list[SharedLambdaRuntimeType] api_v1_static_serverless_runtimes_get()



AvailableServerlessRuntimes returns the available serverless runtimes for auto deploy 

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
    api_instance = openapi_client.StaticApi(api_client)
    
    try:
        api_response = api_instance.api_v1_static_serverless_runtimes_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StaticApi->api_v1_static_serverless_runtimes_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SharedLambdaRuntimeType]**](SharedLambdaRuntimeType.md)

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

# **api_v1_static_vulnerabilities_get**
> TypesAvailableVulnerabilities api_v1_static_vulnerabilities_get()



AvailableVulnerabilities returns the list of all available compliance issues and vulnerabiltiies 

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
    api_instance = openapi_client.StaticApi(api_client)
    
    try:
        api_response = api_instance.api_v1_static_vulnerabilities_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StaticApi->api_v1_static_vulnerabilities_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TypesAvailableVulnerabilities**](TypesAvailableVulnerabilities.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AvailableVulnerabilities contains all available vulnerabilities types |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


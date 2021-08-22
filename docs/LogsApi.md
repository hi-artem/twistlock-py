# openapi_client.LogsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_logs_console_get**](LogsApi.md#api_v1_logs_console_get) | **GET** /api/v1/logs/console | 
[**api_v1_logs_defender_download_get**](LogsApi.md#api_v1_logs_defender_download_get) | **GET** /api/v1/logs/defender/download | 
[**api_v1_logs_defender_get**](LogsApi.md#api_v1_logs_defender_get) | **GET** /api/v1/logs/defender | 
[**api_v1_logs_defender_upload_post**](LogsApi.md#api_v1_logs_defender_upload_post) | **POST** /api/v1/logs/defender/upload | 
[**api_v1_logs_system_download_get**](LogsApi.md#api_v1_logs_system_download_get) | **GET** /api/v1/logs/system/download | 
[**api_v1_logs_system_upload_post**](LogsApi.md#api_v1_logs_system_upload_post) | **POST** /api/v1/logs/system/upload | 


# **api_v1_logs_console_get**
> list[LogLogEntry] api_v1_logs_console_get(lines=lines)



ConsoleLogs returns the last console logs 

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
    api_instance = openapi_client.LogsApi(api_client)
    lines = 56 # int | Lines is the number of lines to fetch.  (optional)

    try:
        api_response = api_instance.api_v1_logs_console_get(lines=lines)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LogsApi->api_v1_logs_console_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lines** | **int**| Lines is the number of lines to fetch.  | [optional] 

### Return type

[**list[LogLogEntry]**](LogLogEntry.md)

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

# **api_v1_logs_defender_download_get**
> api_v1_logs_defender_download_get(hostname=hostname, lines=lines)



DownloadDefenderLogs downloads all defender logs and metadata 

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
    api_instance = openapi_client.LogsApi(api_client)
    hostname = 'hostname_example' # str | Hostname is the target defender hostname.  (optional)
lines = 56 # int | Lines is the number of lines to fetch.  (optional)

    try:
        api_instance.api_v1_logs_defender_download_get(hostname=hostname, lines=lines)
    except ApiException as e:
        print("Exception when calling LogsApi->api_v1_logs_defender_download_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hostname** | **str**| Hostname is the target defender hostname.  | [optional] 
 **lines** | **int**| Lines is the number of lines to fetch.  | [optional] 

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

# **api_v1_logs_defender_get**
> list[LogLogEntry] api_v1_logs_defender_get(hostname=hostname, lines=lines)



DefenderLogs returns the last defender logs 

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
    api_instance = openapi_client.LogsApi(api_client)
    hostname = 'hostname_example' # str | Hostname is the target defender hostname.  (optional)
lines = 56 # int | Lines is the number of lines to fetch.  (optional)

    try:
        api_response = api_instance.api_v1_logs_defender_get(hostname=hostname, lines=lines)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LogsApi->api_v1_logs_defender_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hostname** | **str**| Hostname is the target defender hostname.  | [optional] 
 **lines** | **int**| Lines is the number of lines to fetch.  | [optional] 

### Return type

[**list[LogLogEntry]**](LogLogEntry.md)

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

# **api_v1_logs_defender_upload_post**
> TypesLogUploadResponse api_v1_logs_defender_upload_post(body=body)



UploadDefenderLogs uploads all defender logs and metadata to intelligence 

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
    api_instance = openapi_client.LogsApi(api_client)
    body = 'body_example' # str |  (optional)

    try:
        api_response = api_instance.api_v1_logs_defender_upload_post(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LogsApi->api_v1_logs_defender_upload_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | [optional] 

### Return type

[**TypesLogUploadResponse**](TypesLogUploadResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | LogUploadResponse returns the result of uploading a file to the intelligence |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_logs_system_download_get**
> api_v1_logs_system_download_get()



DownloadSystemLogs downloads the system dump 

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
    api_instance = openapi_client.LogsApi(api_client)
    
    try:
        api_instance.api_v1_logs_system_download_get()
    except ApiException as e:
        print("Exception when calling LogsApi->api_v1_logs_system_download_get: %s\n" % e)
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

# **api_v1_logs_system_upload_post**
> TypesLogUploadResponse api_v1_logs_system_upload_post()



UploadSystemLogs uploads a system log to intelligence 

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
    api_instance = openapi_client.LogsApi(api_client)
    
    try:
        api_response = api_instance.api_v1_logs_system_upload_post()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LogsApi->api_v1_logs_system_upload_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TypesLogUploadResponse**](TypesLogUploadResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | LogUploadResponse returns the result of uploading a file to the intelligence |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


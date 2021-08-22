# openapi_client.CertsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_certs_client_certs_sh_get**](CertsApi.md#api_v1_certs_client_certs_sh_get) | **GET** /api/v1/certs/client-certs.sh | 
[**api_v1_certs_rotate_put**](CertsApi.md#api_v1_certs_rotate_put) | **PUT** /api/v1/certs/rotate | 
[**api_v1_certs_server_certs_sh_get**](CertsApi.md#api_v1_certs_server_certs_sh_get) | **GET** /api/v1/certs/server-certs.sh | 


# **api_v1_certs_client_certs_sh_get**
> list[int] api_v1_certs_client_certs_sh_get()



ClientCerts returns a client certificate bundle 

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
    api_instance = openapi_client.CertsApi(api_client)
    
    try:
        api_response = api_instance.api_v1_certs_client_certs_sh_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CertsApi->api_v1_certs_client_certs_sh_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[int]**

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

# **api_v1_certs_rotate_put**
> api_v1_certs_rotate_put()



RotateCerts rotate the certificates in case of being close to expiration 

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
    api_instance = openapi_client.CertsApi(api_client)
    
    try:
        api_instance.api_v1_certs_rotate_put()
    except ApiException as e:
        print("Exception when calling CertsApi->api_v1_certs_rotate_put: %s\n" % e)
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

# **api_v1_certs_server_certs_sh_get**
> list[int] api_v1_certs_server_certs_sh_get(os=os, ip=ip, hostname=hostname)



ServerCerts returns the resolved defender certificate bundle 

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
    api_instance = openapi_client.CertsApi(api_client)
    os = 'os_example' # str | OS is the target os.  (optional)
ip = 'ip_example' # str | IPs is the list of addresses for which the certificates are generated.  (optional)
hostname = 'hostname_example' # str | Hostname is the target defender hostname.  (optional)

    try:
        api_response = api_instance.api_v1_certs_server_certs_sh_get(os=os, ip=ip, hostname=hostname)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CertsApi->api_v1_certs_server_certs_sh_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **os** | **str**| OS is the target os.  | [optional] 
 **ip** | **str**| IPs is the list of addresses for which the certificates are generated.  | [optional] 
 **hostname** | **str**| Hostname is the target defender hostname.  | [optional] 

### Return type

**list[int]**

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


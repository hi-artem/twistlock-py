# openapi_client.ScriptsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_scripts_defender_ps1_post**](ScriptsApi.md#api_v1_scripts_defender_ps1_post) | **POST** /api/v1/scripts/defender.ps1 | 
[**api_v1_scripts_defender_sh_post**](ScriptsApi.md#api_v1_scripts_defender_sh_post) | **POST** /api/v1/scripts/defender.sh | 


# **api_v1_scripts_defender_ps1_post**
> list[int] api_v1_scripts_defender_ps1_post(api_defender_install_script_options=api_defender_install_script_options)



DefenderScriptWindows returns the resolved defender script for windows deployment 

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
    api_instance = openapi_client.ScriptsApi(api_client)
    api_defender_install_script_options = openapi_client.ApiDefenderInstallScriptOptions() # ApiDefenderInstallScriptOptions |  (optional)

    try:
        api_response = api_instance.api_v1_scripts_defender_ps1_post(api_defender_install_script_options=api_defender_install_script_options)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScriptsApi->api_v1_scripts_defender_ps1_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_defender_install_script_options** | [**ApiDefenderInstallScriptOptions**](ApiDefenderInstallScriptOptions.md)|  | [optional] 

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

# **api_v1_scripts_defender_sh_post**
> list[int] api_v1_scripts_defender_sh_post(api_defender_install_script_options=api_defender_install_script_options)



DefenderScriptLinux returns the resolved defender script for linux deployment 

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
    api_instance = openapi_client.ScriptsApi(api_client)
    api_defender_install_script_options = openapi_client.ApiDefenderInstallScriptOptions() # ApiDefenderInstallScriptOptions |  (optional)

    try:
        api_response = api_instance.api_v1_scripts_defender_sh_post(api_defender_install_script_options=api_defender_install_script_options)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScriptsApi->api_v1_scripts_defender_sh_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_defender_install_script_options** | [**ApiDefenderInstallScriptOptions**](ApiDefenderInstallScriptOptions.md)|  | [optional] 

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


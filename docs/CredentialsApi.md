# openapi_client.CredentialsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_credentials_get**](CredentialsApi.md#api_v1_credentials_get) | **GET** /api/v1/credentials | 
[**api_v1_credentials_id_delete**](CredentialsApi.md#api_v1_credentials_id_delete) | **DELETE** /api/v1/credentials/{id} | 
[**api_v1_credentials_id_usages_get**](CredentialsApi.md#api_v1_credentials_id_usages_get) | **GET** /api/v1/credentials/{id}/usages | 
[**api_v1_credentials_post**](CredentialsApi.md#api_v1_credentials_post) | **POST** /api/v1/credentials | 


# **api_v1_credentials_get**
> list[CredCredential] api_v1_credentials_get()



Credentials returns all credentials 

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
    api_instance = openapi_client.CredentialsApi(api_client)
    
    try:
        api_response = api_instance.api_v1_credentials_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CredentialsApi->api_v1_credentials_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CredCredential]**](CredCredential.md)

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

# **api_v1_credentials_id_delete**
> api_v1_credentials_id_delete(id)



DeleteCredential deletes the specified credential 

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
    api_instance = openapi_client.CredentialsApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.api_v1_credentials_id_delete(id)
    except ApiException as e:
        print("Exception when calling CredentialsApi->api_v1_credentials_id_delete: %s\n" % e)
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

# **api_v1_credentials_id_usages_get**
> list[TypesCredentialUsage] api_v1_credentials_id_usages_get(id)



CredentialUsages returns the given credential usages across the product 

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
    api_instance = openapi_client.CredentialsApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.api_v1_credentials_id_usages_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CredentialsApi->api_v1_credentials_id_usages_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**list[TypesCredentialUsage]**](TypesCredentialUsage.md)

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

# **api_v1_credentials_post**
> api_v1_credentials_post(cred_credential=cred_credential)



UpdateCredential adds or updates a credential 

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
    api_instance = openapi_client.CredentialsApi(api_client)
    cred_credential = openapi_client.CredCredential() # CredCredential |  (optional)

    try:
        api_instance.api_v1_credentials_post(cred_credential=cred_credential)
    except ApiException as e:
        print("Exception when calling CredentialsApi->api_v1_credentials_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cred_credential** | [**CredCredential**](CredCredential.md)|  | [optional] 

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


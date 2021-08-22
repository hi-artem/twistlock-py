# openapi_client.TagsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_tags_get**](TagsApi.md#api_v1_tags_get) | **GET** /api/v1/tags | 
[**api_v1_tags_id_delete**](TagsApi.md#api_v1_tags_id_delete) | **DELETE** /api/v1/tags/{id} | 
[**api_v1_tags_id_put**](TagsApi.md#api_v1_tags_id_put) | **PUT** /api/v1/tags/{id} | 
[**api_v1_tags_id_vuln_delete**](TagsApi.md#api_v1_tags_id_vuln_delete) | **DELETE** /api/v1/tags/{id}/vuln | 
[**api_v1_tags_id_vuln_post**](TagsApi.md#api_v1_tags_id_vuln_post) | **POST** /api/v1/tags/{id}/vuln | 
[**api_v1_tags_post**](TagsApi.md#api_v1_tags_post) | **POST** /api/v1/tags | 


# **api_v1_tags_get**
> list[SharedTag] api_v1_tags_get()



Tags returns all the tags 

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
    api_instance = openapi_client.TagsApi(api_client)
    
    try:
        api_response = api_instance.api_v1_tags_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TagsApi->api_v1_tags_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SharedTag]**](SharedTag.md)

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

# **api_v1_tags_id_delete**
> api_v1_tags_id_delete(id)



DeleteTag deletes a tag by its name 

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
    api_instance = openapi_client.TagsApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.api_v1_tags_id_delete(id)
    except ApiException as e:
        print("Exception when calling TagsApi->api_v1_tags_id_delete: %s\n" % e)
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

# **api_v1_tags_id_put**
> api_v1_tags_id_put(id, shared_tag=shared_tag)



UpdateTag updates a tag 

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
    api_instance = openapi_client.TagsApi(api_client)
    id = 'id_example' # str | 
shared_tag = openapi_client.SharedTag() # SharedTag |  (optional)

    try:
        api_instance.api_v1_tags_id_put(id, shared_tag=shared_tag)
    except ApiException as e:
        print("Exception when calling TagsApi->api_v1_tags_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **shared_tag** | [**SharedTag**](SharedTag.md)|  | [optional] 

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

# **api_v1_tags_id_vuln_delete**
> api_v1_tags_id_vuln_delete(id)



DeleteTagVulnMetadata deletes the tag vulnerability metadata 

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
    api_instance = openapi_client.TagsApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.api_v1_tags_id_vuln_delete(id)
    except ApiException as e:
        print("Exception when calling TagsApi->api_v1_tags_id_vuln_delete: %s\n" % e)
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

# **api_v1_tags_id_vuln_post**
> api_v1_tags_id_vuln_post(id, shared_tag_vuln_metadata=shared_tag_vuln_metadata)



UpdateTagVulnMetadata update the tag vulnerability metadata 

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
    api_instance = openapi_client.TagsApi(api_client)
    id = 'id_example' # str | 
shared_tag_vuln_metadata = openapi_client.SharedTagVulnMetadata() # SharedTagVulnMetadata |  (optional)

    try:
        api_instance.api_v1_tags_id_vuln_post(id, shared_tag_vuln_metadata=shared_tag_vuln_metadata)
    except ApiException as e:
        print("Exception when calling TagsApi->api_v1_tags_id_vuln_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **shared_tag_vuln_metadata** | [**SharedTagVulnMetadata**](SharedTagVulnMetadata.md)|  | [optional] 

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

# **api_v1_tags_post**
> api_v1_tags_post(shared_tag=shared_tag)



AddTag adds a new tag 

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
    api_instance = openapi_client.TagsApi(api_client)
    shared_tag = openapi_client.SharedTag() # SharedTag |  (optional)

    try:
        api_instance.api_v1_tags_post(shared_tag=shared_tag)
    except ApiException as e:
        print("Exception when calling TagsApi->api_v1_tags_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shared_tag** | [**SharedTag**](SharedTag.md)|  | [optional] 

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


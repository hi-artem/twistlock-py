# openapi_client.ProjectsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_projects_get**](ProjectsApi.md#api_v1_projects_get) | **GET** /api/v1/projects | 
[**api_v1_projects_id_delete**](ProjectsApi.md#api_v1_projects_id_delete) | **DELETE** /api/v1/projects/{id} | 
[**api_v1_projects_id_put**](ProjectsApi.md#api_v1_projects_id_put) | **PUT** /api/v1/projects/{id} | 
[**api_v1_projects_post**](ProjectsApi.md#api_v1_projects_post) | **POST** /api/v1/projects | 


# **api_v1_projects_get**
> list[TypesProject] api_v1_projects_get()



Projects returns the project list that are viewable by the given user 

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
    api_instance = openapi_client.ProjectsApi(api_client)
    
    try:
        api_response = api_instance.api_v1_projects_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->api_v1_projects_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[TypesProject]**](TypesProject.md)

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

# **api_v1_projects_id_delete**
> TypesProjectCredentials api_v1_projects_id_delete(id)



DeleteProject deletes the specified project 

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
    api_instance = openapi_client.ProjectsApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.api_v1_projects_id_delete(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->api_v1_projects_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**TypesProjectCredentials**](TypesProjectCredentials.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ProjectCredentials are the supervisor project credentials |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_projects_id_put**
> TypesProject api_v1_projects_id_put(id, types_project=types_project)



UpdateProject updates the specified project 

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
    api_instance = openapi_client.ProjectsApi(api_client)
    id = 'id_example' # str | 
types_project = openapi_client.TypesProject() # TypesProject |  (optional)

    try:
        api_response = api_instance.api_v1_projects_id_put(id, types_project=types_project)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->api_v1_projects_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **types_project** | [**TypesProject**](TypesProject.md)|  | [optional] 

### Return type

[**TypesProject**](TypesProject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project represent the project details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_projects_post**
> TypesProject api_v1_projects_post(types_project=types_project)



UpdateProject updates the specified project 

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
    api_instance = openapi_client.ProjectsApi(api_client)
    types_project = openapi_client.TypesProject() # TypesProject |  (optional)

    try:
        api_response = api_instance.api_v1_projects_post(types_project=types_project)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->api_v1_projects_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **types_project** | [**TypesProject**](TypesProject.md)|  | [optional] 

### Return type

[**TypesProject**](TypesProject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project represent the project details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


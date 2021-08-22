# openapi_client.ImagesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_images_download_get**](ImagesApi.md#api_v1_images_download_get) | **GET** /api/v1/images/download | 
[**api_v1_images_evaluate_post**](ImagesApi.md#api_v1_images_evaluate_post) | **POST** /api/v1/images/evaluate | 
[**api_v1_images_get**](ImagesApi.md#api_v1_images_get) | **GET** /api/v1/images | 
[**api_v1_images_names_get**](ImagesApi.md#api_v1_images_names_get) | **GET** /api/v1/images/names | 
[**api_v1_images_progress_get**](ImagesApi.md#api_v1_images_progress_get) | **GET** /api/v1/images/progress | 
[**api_v1_images_scan_post**](ImagesApi.md#api_v1_images_scan_post) | **POST** /api/v1/images/scan | 
[**api_v1_images_twistlock_defender_app_embedded_tar_gz_get**](ImagesApi.md#api_v1_images_twistlock_defender_app_embedded_tar_gz_get) | **GET** /api/v1/images/twistlock_defender_app_embedded.tar.gz | 
[**api_v1_images_twistlock_defender_layer_zip_post**](ImagesApi.md#api_v1_images_twistlock_defender_layer_zip_post) | **POST** /api/v1/images/twistlock_defender_layer.zip | 


# **api_v1_images_download_get**
> api_v1_images_download_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, id=id, hostname=hostname, repository=repository, registry=registry, name=name, layers=layers, filter_base_image=filter_base_image, compact=compact, trust_statuses=trust_statuses, clusters=clusters, compliance_ids=compliance_ids, app_embedded=app_embedded)



DownloadImages downloads the image data 

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
    api_instance = openapi_client.ImagesApi(api_client)
    offset = 56 # int | Offset from the start of the list from which to retrieve documents.  (optional)
limit = 56 # int | Number of documents to return.  (optional)
search = 'search_example' # str | Search term.  (optional)
sort = 'sort_example' # str | Key on which to sort.  (optional)
reverse = True # bool | Sort order.  (optional)
collections = ['collections_example'] # list[str] | Scopes the query by collection.  (optional)
account_ids = ['account_ids_example'] # list[str] | Scopes the query by account ID.  (optional)
fields = ['fields_example'] # list[str] | List of fields to retrieve.  (optional)
id = ['id_example'] # list[str] | Filters the results by image ID.  (optional)
hostname = ['hostname_example'] # list[str] | Filters results by hostname.  (optional)
repository = ['repository_example'] # list[str] | Filters results by image repository.  (optional)
registry = ['registry_example'] # list[str] | Filters results by image registry.  (optional)
name = ['name_example'] # list[str] | Filters results by image name.  (optional)
layers = True # bool | Indicates if CVEs are mapped to image layer (true) or not (false).  (optional)
filter_base_image = True # bool | Indicates if base image vulnerabilities are to be filtered (true) or not (false). Requires predefined base images that have already been scanned.  (optional)
compact = True # bool | Indicates if only minimal image data is to be returned (i.e., skip vulnerabilities, compliance, and extended image metadata) (true) or not (false).  (optional)
trust_statuses = ['trust_statuses_example'] # list[str] | Filters results according to whether an image is considered trusted or untrusted by your trusted images policy.  (optional)
clusters = ['clusters_example'] # list[str] | Filters results by cluster name.  (optional)
compliance_ids = [56] # list[int] | Filters results by compliance IDs.  (optional)
app_embedded = True # bool | Filters images that were scanned by App-Embedded Defenders.  (optional)

    try:
        api_instance.api_v1_images_download_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, id=id, hostname=hostname, repository=repository, registry=registry, name=name, layers=layers, filter_base_image=filter_base_image, compact=compact, trust_statuses=trust_statuses, clusters=clusters, compliance_ids=compliance_ids, app_embedded=app_embedded)
    except ApiException as e:
        print("Exception when calling ImagesApi->api_v1_images_download_get: %s\n" % e)
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
 **id** | [**list[str]**](str.md)| Filters the results by image ID.  | [optional] 
 **hostname** | [**list[str]**](str.md)| Filters results by hostname.  | [optional] 
 **repository** | [**list[str]**](str.md)| Filters results by image repository.  | [optional] 
 **registry** | [**list[str]**](str.md)| Filters results by image registry.  | [optional] 
 **name** | [**list[str]**](str.md)| Filters results by image name.  | [optional] 
 **layers** | **bool**| Indicates if CVEs are mapped to image layer (true) or not (false).  | [optional] 
 **filter_base_image** | **bool**| Indicates if base image vulnerabilities are to be filtered (true) or not (false). Requires predefined base images that have already been scanned.  | [optional] 
 **compact** | **bool**| Indicates if only minimal image data is to be returned (i.e., skip vulnerabilities, compliance, and extended image metadata) (true) or not (false).  | [optional] 
 **trust_statuses** | [**list[str]**](str.md)| Filters results according to whether an image is considered trusted or untrusted by your trusted images policy.  | [optional] 
 **clusters** | [**list[str]**](str.md)| Filters results by cluster name.  | [optional] 
 **compliance_ids** | [**list[int]**](int.md)| Filters results by compliance IDs.  | [optional] 
 **app_embedded** | **bool**| Filters images that were scanned by App-Embedded Defenders.  | [optional] 

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

# **api_v1_images_evaluate_post**
> ApiResolveImagesResp api_v1_images_evaluate_post(api_resolve_images_req=api_resolve_images_req)



ResolveImages adds vulnerability data for the given images 

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
    api_instance = openapi_client.ImagesApi(api_client)
    api_resolve_images_req = openapi_client.ApiResolveImagesReq() # ApiResolveImagesReq |  (optional)

    try:
        api_response = api_instance.api_v1_images_evaluate_post(api_resolve_images_req=api_resolve_images_req)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImagesApi->api_v1_images_evaluate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_resolve_images_req** | [**ApiResolveImagesReq**](ApiResolveImagesReq.md)|  | [optional] 

### Return type

[**ApiResolveImagesResp**](ApiResolveImagesResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ResolveImagesResp represents the images resolution API output |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_images_get**
> list[SharedImageScanResult] api_v1_images_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, id=id, hostname=hostname, repository=repository, registry=registry, name=name, layers=layers, filter_base_image=filter_base_image, compact=compact, trust_statuses=trust_statuses, clusters=clusters, compliance_ids=compliance_ids, app_embedded=app_embedded)



Images returns images by the query specification 

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
    api_instance = openapi_client.ImagesApi(api_client)
    offset = 56 # int | Offset from the start of the list from which to retrieve documents.  (optional)
limit = 56 # int | Number of documents to return.  (optional)
search = 'search_example' # str | Search term.  (optional)
sort = 'sort_example' # str | Key on which to sort.  (optional)
reverse = True # bool | Sort order.  (optional)
collections = ['collections_example'] # list[str] | Scopes the query by collection.  (optional)
account_ids = ['account_ids_example'] # list[str] | Scopes the query by account ID.  (optional)
fields = ['fields_example'] # list[str] | List of fields to retrieve.  (optional)
id = ['id_example'] # list[str] | Filters the results by image ID.  (optional)
hostname = ['hostname_example'] # list[str] | Filters results by hostname.  (optional)
repository = ['repository_example'] # list[str] | Filters results by image repository.  (optional)
registry = ['registry_example'] # list[str] | Filters results by image registry.  (optional)
name = ['name_example'] # list[str] | Filters results by image name.  (optional)
layers = True # bool | Indicates if CVEs are mapped to image layer (true) or not (false).  (optional)
filter_base_image = True # bool | Indicates if base image vulnerabilities are to be filtered (true) or not (false). Requires predefined base images that have already been scanned.  (optional)
compact = True # bool | Indicates if only minimal image data is to be returned (i.e., skip vulnerabilities, compliance, and extended image metadata) (true) or not (false).  (optional)
trust_statuses = ['trust_statuses_example'] # list[str] | Filters results according to whether an image is considered trusted or untrusted by your trusted images policy.  (optional)
clusters = ['clusters_example'] # list[str] | Filters results by cluster name.  (optional)
compliance_ids = [56] # list[int] | Filters results by compliance IDs.  (optional)
app_embedded = True # bool | Filters images that were scanned by App-Embedded Defenders.  (optional)

    try:
        api_response = api_instance.api_v1_images_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, id=id, hostname=hostname, repository=repository, registry=registry, name=name, layers=layers, filter_base_image=filter_base_image, compact=compact, trust_statuses=trust_statuses, clusters=clusters, compliance_ids=compliance_ids, app_embedded=app_embedded)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImagesApi->api_v1_images_get: %s\n" % e)
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
 **id** | [**list[str]**](str.md)| Filters the results by image ID.  | [optional] 
 **hostname** | [**list[str]**](str.md)| Filters results by hostname.  | [optional] 
 **repository** | [**list[str]**](str.md)| Filters results by image repository.  | [optional] 
 **registry** | [**list[str]**](str.md)| Filters results by image registry.  | [optional] 
 **name** | [**list[str]**](str.md)| Filters results by image name.  | [optional] 
 **layers** | **bool**| Indicates if CVEs are mapped to image layer (true) or not (false).  | [optional] 
 **filter_base_image** | **bool**| Indicates if base image vulnerabilities are to be filtered (true) or not (false). Requires predefined base images that have already been scanned.  | [optional] 
 **compact** | **bool**| Indicates if only minimal image data is to be returned (i.e., skip vulnerabilities, compliance, and extended image metadata) (true) or not (false).  | [optional] 
 **trust_statuses** | [**list[str]**](str.md)| Filters results according to whether an image is considered trusted or untrusted by your trusted images policy.  | [optional] 
 **clusters** | [**list[str]**](str.md)| Filters results by cluster name.  | [optional] 
 **compliance_ids** | [**list[int]**](int.md)| Filters results by compliance IDs.  | [optional] 
 **app_embedded** | **bool**| Filters images that were scanned by App-Embedded Defenders.  | [optional] 

### Return type

[**list[SharedImageScanResult]**](SharedImageScanResult.md)

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

# **api_v1_images_names_get**
> list[str] api_v1_images_names_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, id=id, hostname=hostname, repository=repository, registry=registry, name=name, layers=layers, filter_base_image=filter_base_image, compact=compact, trust_statuses=trust_statuses, clusters=clusters, compliance_ids=compliance_ids, app_embedded=app_embedded)



ImageNames returns image names according to the query specification 

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
    api_instance = openapi_client.ImagesApi(api_client)
    offset = 56 # int | Offset from the start of the list from which to retrieve documents.  (optional)
limit = 56 # int | Number of documents to return.  (optional)
search = 'search_example' # str | Search term.  (optional)
sort = 'sort_example' # str | Key on which to sort.  (optional)
reverse = True # bool | Sort order.  (optional)
collections = ['collections_example'] # list[str] | Scopes the query by collection.  (optional)
account_ids = ['account_ids_example'] # list[str] | Scopes the query by account ID.  (optional)
fields = ['fields_example'] # list[str] | List of fields to retrieve.  (optional)
id = ['id_example'] # list[str] | Filters the results by image ID.  (optional)
hostname = ['hostname_example'] # list[str] | Filters results by hostname.  (optional)
repository = ['repository_example'] # list[str] | Filters results by image repository.  (optional)
registry = ['registry_example'] # list[str] | Filters results by image registry.  (optional)
name = ['name_example'] # list[str] | Filters results by image name.  (optional)
layers = True # bool | Indicates if CVEs are mapped to image layer (true) or not (false).  (optional)
filter_base_image = True # bool | Indicates if base image vulnerabilities are to be filtered (true) or not (false). Requires predefined base images that have already been scanned.  (optional)
compact = True # bool | Indicates if only minimal image data is to be returned (i.e., skip vulnerabilities, compliance, and extended image metadata) (true) or not (false).  (optional)
trust_statuses = ['trust_statuses_example'] # list[str] | Filters results according to whether an image is considered trusted or untrusted by your trusted images policy.  (optional)
clusters = ['clusters_example'] # list[str] | Filters results by cluster name.  (optional)
compliance_ids = [56] # list[int] | Filters results by compliance IDs.  (optional)
app_embedded = True # bool | Filters images that were scanned by App-Embedded Defenders.  (optional)

    try:
        api_response = api_instance.api_v1_images_names_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, id=id, hostname=hostname, repository=repository, registry=registry, name=name, layers=layers, filter_base_image=filter_base_image, compact=compact, trust_statuses=trust_statuses, clusters=clusters, compliance_ids=compliance_ids, app_embedded=app_embedded)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImagesApi->api_v1_images_names_get: %s\n" % e)
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
 **id** | [**list[str]**](str.md)| Filters the results by image ID.  | [optional] 
 **hostname** | [**list[str]**](str.md)| Filters results by hostname.  | [optional] 
 **repository** | [**list[str]**](str.md)| Filters results by image repository.  | [optional] 
 **registry** | [**list[str]**](str.md)| Filters results by image registry.  | [optional] 
 **name** | [**list[str]**](str.md)| Filters results by image name.  | [optional] 
 **layers** | **bool**| Indicates if CVEs are mapped to image layer (true) or not (false).  | [optional] 
 **filter_base_image** | **bool**| Indicates if base image vulnerabilities are to be filtered (true) or not (false). Requires predefined base images that have already been scanned.  | [optional] 
 **compact** | **bool**| Indicates if only minimal image data is to be returned (i.e., skip vulnerabilities, compliance, and extended image metadata) (true) or not (false).  | [optional] 
 **trust_statuses** | [**list[str]**](str.md)| Filters results according to whether an image is considered trusted or untrusted by your trusted images policy.  | [optional] 
 **clusters** | [**list[str]**](str.md)| Filters results by cluster name.  | [optional] 
 **compliance_ids** | [**list[int]**](int.md)| Filters results by compliance IDs.  | [optional] 
 **app_embedded** | **bool**| Filters images that were scanned by App-Embedded Defenders.  | [optional] 

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

# **api_v1_images_progress_get**
> list[SharedProgress] api_v1_images_progress_get()



ImageScanProgress returns the image scan progress 

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
    api_instance = openapi_client.ImagesApi(api_client)
    
    try:
        api_response = api_instance.api_v1_images_progress_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImagesApi->api_v1_images_progress_get: %s\n" % e)
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

# **api_v1_images_scan_post**
> api_v1_images_scan_post(types_image_scan_options=types_image_scan_options)



ScanImages sends an image scan requests to all defenders 

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
    api_instance = openapi_client.ImagesApi(api_client)
    types_image_scan_options = openapi_client.TypesImageScanOptions() # TypesImageScanOptions |  (optional)

    try:
        api_instance.api_v1_images_scan_post(types_image_scan_options=types_image_scan_options)
    except ApiException as e:
        print("Exception when calling ImagesApi->api_v1_images_scan_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **types_image_scan_options** | [**TypesImageScanOptions**](TypesImageScanOptions.md)|  | [optional] 

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

# **api_v1_images_twistlock_defender_app_embedded_tar_gz_get**
> api_v1_images_twistlock_defender_app_embedded_tar_gz_get()



DownloadAppEmbeddedDefender generates the embedded defender bundle and serves it to the user 

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
    api_instance = openapi_client.ImagesApi(api_client)
    
    try:
        api_instance.api_v1_images_twistlock_defender_app_embedded_tar_gz_get()
    except ApiException as e:
        print("Exception when calling ImagesApi->api_v1_images_twistlock_defender_app_embedded_tar_gz_get: %s\n" % e)
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

# **api_v1_images_twistlock_defender_layer_zip_post**
> api_v1_images_twistlock_defender_layer_zip_post(shared_serverless_bundle_request=shared_serverless_bundle_request)



DownloadServerlessLayerBundle returns a ZIP file with a Lambda layer containing the Defender runtime 

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
    api_instance = openapi_client.ImagesApi(api_client)
    shared_serverless_bundle_request = openapi_client.SharedServerlessBundleRequest() # SharedServerlessBundleRequest |  (optional)

    try:
        api_instance.api_v1_images_twistlock_defender_layer_zip_post(shared_serverless_bundle_request=shared_serverless_bundle_request)
    except ApiException as e:
        print("Exception when calling ImagesApi->api_v1_images_twistlock_defender_layer_zip_post: %s\n" % e)
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


# openapi_client.ScansApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_scans_download_get**](ScansApi.md#api_v1_scans_download_get) | **GET** /api/v1/scans/download | 
[**api_v1_scans_get**](ScansApi.md#api_v1_scans_get) | **GET** /api/v1/scans | 
[**api_v1_scans_id_get**](ScansApi.md#api_v1_scans_id_get) | **GET** /api/v1/scans/{id} | 
[**api_v1_scans_post**](ScansApi.md#api_v1_scans_post) | **POST** /api/v1/scans | 
[**api_v1_scans_sonatype_post**](ScansApi.md#api_v1_scans_sonatype_post) | **POST** /api/v1/scans/sonatype | 
[**api_v1_scans_vms_post**](ScansApi.md#api_v1_scans_vms_post) | **POST** /api/v1/scans/vms | 


# **api_v1_scans_download_get**
> api_v1_scans_download_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, id=id, job_name=job_name, type=type, _pass=_pass, build=build, image_id=image_id, layers=layers, _from=_from, to=to, filter_base_image=filter_base_image)



DownloadCLIScanResults downloads the cli scans data to CSV 

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
    api_instance = openapi_client.ScansApi(api_client)
    offset = 56 # int | Offset from the start of the list from which to retrieve documents.  (optional)
limit = 56 # int | Number of documents to return.  (optional)
search = 'search_example' # str | Search term.  (optional)
sort = 'sort_example' # str | Key on which to sort.  (optional)
reverse = True # bool | Sort order.  (optional)
collections = ['collections_example'] # list[str] | Scopes the query by collection.  (optional)
account_ids = ['account_ids_example'] # list[str] | Scopes the query by account ID.  (optional)
fields = ['fields_example'] # list[str] | List of fields to retrieve.  (optional)
id = 'id_example' # str | Scan ID used in the image layers fetch.  (optional)
job_name = ['job_name_example'] # list[str] | Jenkins job name.  (optional)
type = 'type_example' # str | Scan type.  (optional)
_pass = True # bool | Indicates whether to filter on passed scans (true) or not (false).  (optional)
build = 'build_example' # str | Build number.  (optional)
image_id = 'image_id_example' # str | Image ID of scanned image.  (optional)
layers = True # bool | Indicates if CVEs are mapped to image layer (true) or not (false).  (optional)
_from = '2013-10-20T19:20:30+01:00' # datetime | Filters results by start datetime. Based on scan time.  (optional)
to = '2013-10-20T19:20:30+01:00' # datetime | Filters results by end datetime. Based on scan time.  (optional)
filter_base_image = True # bool | Indicates if base image vulnerabilities are to be filtered (true) or not (false). Requires predefined base images that have already been scanned.  (optional)

    try:
        api_instance.api_v1_scans_download_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, id=id, job_name=job_name, type=type, _pass=_pass, build=build, image_id=image_id, layers=layers, _from=_from, to=to, filter_base_image=filter_base_image)
    except ApiException as e:
        print("Exception when calling ScansApi->api_v1_scans_download_get: %s\n" % e)
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
 **id** | **str**| Scan ID used in the image layers fetch.  | [optional] 
 **job_name** | [**list[str]**](str.md)| Jenkins job name.  | [optional] 
 **type** | **str**| Scan type.  | [optional] 
 **_pass** | **bool**| Indicates whether to filter on passed scans (true) or not (false).  | [optional] 
 **build** | **str**| Build number.  | [optional] 
 **image_id** | **str**| Image ID of scanned image.  | [optional] 
 **layers** | **bool**| Indicates if CVEs are mapped to image layer (true) or not (false).  | [optional] 
 **_from** | **datetime**| Filters results by start datetime. Based on scan time.  | [optional] 
 **to** | **datetime**| Filters results by end datetime. Based on scan time.  | [optional] 
 **filter_base_image** | **bool**| Indicates if base image vulnerabilities are to be filtered (true) or not (false). Requires predefined base images that have already been scanned.  | [optional] 

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

# **api_v1_scans_get**
> list[SharedCLIScanResult] api_v1_scans_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, id=id, job_name=job_name, type=type, _pass=_pass, build=build, image_id=image_id, layers=layers, _from=_from, to=to, filter_base_image=filter_base_image)



CLIScanResults fetches all CLI scan results 

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
    api_instance = openapi_client.ScansApi(api_client)
    offset = 56 # int | Offset from the start of the list from which to retrieve documents.  (optional)
limit = 56 # int | Number of documents to return.  (optional)
search = 'search_example' # str | Search term.  (optional)
sort = 'sort_example' # str | Key on which to sort.  (optional)
reverse = True # bool | Sort order.  (optional)
collections = ['collections_example'] # list[str] | Scopes the query by collection.  (optional)
account_ids = ['account_ids_example'] # list[str] | Scopes the query by account ID.  (optional)
fields = ['fields_example'] # list[str] | List of fields to retrieve.  (optional)
id = 'id_example' # str | Scan ID used in the image layers fetch.  (optional)
job_name = ['job_name_example'] # list[str] | Jenkins job name.  (optional)
type = 'type_example' # str | Scan type.  (optional)
_pass = True # bool | Indicates whether to filter on passed scans (true) or not (false).  (optional)
build = 'build_example' # str | Build number.  (optional)
image_id = 'image_id_example' # str | Image ID of scanned image.  (optional)
layers = True # bool | Indicates if CVEs are mapped to image layer (true) or not (false).  (optional)
_from = '2013-10-20T19:20:30+01:00' # datetime | Filters results by start datetime. Based on scan time.  (optional)
to = '2013-10-20T19:20:30+01:00' # datetime | Filters results by end datetime. Based on scan time.  (optional)
filter_base_image = True # bool | Indicates if base image vulnerabilities are to be filtered (true) or not (false). Requires predefined base images that have already been scanned.  (optional)

    try:
        api_response = api_instance.api_v1_scans_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, id=id, job_name=job_name, type=type, _pass=_pass, build=build, image_id=image_id, layers=layers, _from=_from, to=to, filter_base_image=filter_base_image)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScansApi->api_v1_scans_get: %s\n" % e)
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
 **id** | **str**| Scan ID used in the image layers fetch.  | [optional] 
 **job_name** | [**list[str]**](str.md)| Jenkins job name.  | [optional] 
 **type** | **str**| Scan type.  | [optional] 
 **_pass** | **bool**| Indicates whether to filter on passed scans (true) or not (false).  | [optional] 
 **build** | **str**| Build number.  | [optional] 
 **image_id** | **str**| Image ID of scanned image.  | [optional] 
 **layers** | **bool**| Indicates if CVEs are mapped to image layer (true) or not (false).  | [optional] 
 **_from** | **datetime**| Filters results by start datetime. Based on scan time.  | [optional] 
 **to** | **datetime**| Filters results by end datetime. Based on scan time.  | [optional] 
 **filter_base_image** | **bool**| Indicates if base image vulnerabilities are to be filtered (true) or not (false). Requires predefined base images that have already been scanned.  | [optional] 

### Return type

[**list[SharedCLIScanResult]**](SharedCLIScanResult.md)

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

# **api_v1_scans_id_get**
> api_v1_scans_id_get(id)



ScanResult returns the scan result for the given image 

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
    api_instance = openapi_client.ScansApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.api_v1_scans_id_get(id)
    except ApiException as e:
        print("Exception when calling ScansApi->api_v1_scans_id_get: %s\n" % e)
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

# **api_v1_scans_post**
> api_v1_scans_post(shared_cli_scan_result=shared_cli_scan_result)



AddCLIScanResult adds a CLI scan result 

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
    api_instance = openapi_client.ScansApi(api_client)
    shared_cli_scan_result = openapi_client.SharedCLIScanResult() # SharedCLIScanResult |  (optional)

    try:
        api_instance.api_v1_scans_post(shared_cli_scan_result=shared_cli_scan_result)
    except ApiException as e:
        print("Exception when calling ScansApi->api_v1_scans_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shared_cli_scan_result** | [**SharedCLIScanResult**](SharedCLIScanResult.md)|  | [optional] 

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

# **api_v1_scans_sonatype_post**
> SharedUploadScanResult api_v1_scans_sonatype_post()



UploadScanResult saves the image scan results, it also scavenge historical images 

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
    api_instance = openapi_client.ScansApi(api_client)
    
    try:
        api_response = api_instance.api_v1_scans_sonatype_post()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScansApi->api_v1_scans_sonatype_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SharedUploadScanResult**](SharedUploadScanResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UploadScanResult is the result uploading the scanning result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_scans_vms_post**
> api_v1_scans_vms_post(shared_image_scan_result=shared_image_scan_result)



AddVMScanResult adds a VM scan result 

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
    api_instance = openapi_client.ScansApi(api_client)
    shared_image_scan_result = openapi_client.SharedImageScanResult() # SharedImageScanResult |  (optional)

    try:
        api_instance.api_v1_scans_vms_post(shared_image_scan_result=shared_image_scan_result)
    except ApiException as e:
        print("Exception when calling ScansApi->api_v1_scans_vms_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shared_image_scan_result** | [**SharedImageScanResult**](SharedImageScanResult.md)|  | [optional] 

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


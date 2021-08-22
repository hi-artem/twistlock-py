# openapi_client.TasDropletsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_tas_droplets_addresses_get**](TasDropletsApi.md#api_v1_tas_droplets_addresses_get) | **GET** /api/v1/tas-droplets/addresses | 
[**api_v1_tas_droplets_download_get**](TasDropletsApi.md#api_v1_tas_droplets_download_get) | **GET** /api/v1/tas-droplets/download | 
[**api_v1_tas_droplets_get**](TasDropletsApi.md#api_v1_tas_droplets_get) | **GET** /api/v1/tas-droplets | 
[**api_v1_tas_droplets_progress_get**](TasDropletsApi.md#api_v1_tas_droplets_progress_get) | **GET** /api/v1/tas-droplets/progress | 
[**api_v1_tas_droplets_scan_post**](TasDropletsApi.md#api_v1_tas_droplets_scan_post) | **POST** /api/v1/tas-droplets/scan | 
[**api_v1_tas_droplets_stop_post**](TasDropletsApi.md#api_v1_tas_droplets_stop_post) | **POST** /api/v1/tas-droplets/stop | 


# **api_v1_tas_droplets_addresses_get**
> list[str] api_v1_tas_droplets_addresses_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, id=id, cloud_controller_addresses=cloud_controller_addresses, provider=provider, region=region, runtime=runtime, version=version, function_layers=function_layers, defended=defended, compliance_ids=compliance_ids)



TASCloudControllerAddresses returns Cloud Controllers addresses of scanned droplets 

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
    api_instance = openapi_client.TasDropletsApi(api_client)
    offset = 56 # int | Offset from the start of the list from which to retrieve documents.  (optional)
limit = 56 # int | Number of documents to return.  (optional)
search = 'search_example' # str | Search term.  (optional)
sort = 'sort_example' # str | Key on which to sort.  (optional)
reverse = True # bool | Sort order.  (optional)
collections = ['collections_example'] # list[str] | Scopes the query by collection.  (optional)
account_ids = ['account_ids_example'] # list[str] | Scopes the query by account ID.  (optional)
fields = ['fields_example'] # list[str] | List of fields to retrieve.  (optional)
id = ['id_example'] # list[str] | List of function IDs.  (optional)
cloud_controller_addresses = ['cloud_controller_addresses_example'] # list[str] | List of cloud controller addresses which hold the functions.  (optional)
provider = ['provider_example'] # list[str] | Filters results by provider.  (optional)
region = ['region_example'] # list[str] | Filters results by region.  (optional)
runtime = ['runtime_example'] # list[str] | Filters results by runtime.  (optional)
version = ['version_example'] # list[str] | Filters results by function version.  (optional)
function_layers = ['function_layers_example'] # list[str] | Filters results by function layers.  (optional)
defended = True # bool | Filters results by functions which are defended by a Defender and are connected to Console (true) or not (false).  (optional)
compliance_ids = [56] # list[int] | Filters results by compliance ID.  (optional)

    try:
        api_response = api_instance.api_v1_tas_droplets_addresses_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, id=id, cloud_controller_addresses=cloud_controller_addresses, provider=provider, region=region, runtime=runtime, version=version, function_layers=function_layers, defended=defended, compliance_ids=compliance_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasDropletsApi->api_v1_tas_droplets_addresses_get: %s\n" % e)
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
 **id** | [**list[str]**](str.md)| List of function IDs.  | [optional] 
 **cloud_controller_addresses** | [**list[str]**](str.md)| List of cloud controller addresses which hold the functions.  | [optional] 
 **provider** | [**list[str]**](str.md)| Filters results by provider.  | [optional] 
 **region** | [**list[str]**](str.md)| Filters results by region.  | [optional] 
 **runtime** | [**list[str]**](str.md)| Filters results by runtime.  | [optional] 
 **version** | [**list[str]**](str.md)| Filters results by function version.  | [optional] 
 **function_layers** | [**list[str]**](str.md)| Filters results by function layers.  | [optional] 
 **defended** | **bool**| Filters results by functions which are defended by a Defender and are connected to Console (true) or not (false).  | [optional] 
 **compliance_ids** | [**list[int]**](int.md)| Filters results by compliance ID.  | [optional] 

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

# **api_v1_tas_droplets_download_get**
> api_v1_tas_droplets_download_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, id=id, cloud_controller_addresses=cloud_controller_addresses, provider=provider, region=region, runtime=runtime, version=version, function_layers=function_layers, defended=defended, compliance_ids=compliance_ids)



DownloadTASDroplets downloads the TAS droplets data to CSVs 

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
    api_instance = openapi_client.TasDropletsApi(api_client)
    offset = 56 # int | Offset from the start of the list from which to retrieve documents.  (optional)
limit = 56 # int | Number of documents to return.  (optional)
search = 'search_example' # str | Search term.  (optional)
sort = 'sort_example' # str | Key on which to sort.  (optional)
reverse = True # bool | Sort order.  (optional)
collections = ['collections_example'] # list[str] | Scopes the query by collection.  (optional)
account_ids = ['account_ids_example'] # list[str] | Scopes the query by account ID.  (optional)
fields = ['fields_example'] # list[str] | List of fields to retrieve.  (optional)
id = ['id_example'] # list[str] | List of function IDs.  (optional)
cloud_controller_addresses = ['cloud_controller_addresses_example'] # list[str] | List of cloud controller addresses which hold the functions.  (optional)
provider = ['provider_example'] # list[str] | Filters results by provider.  (optional)
region = ['region_example'] # list[str] | Filters results by region.  (optional)
runtime = ['runtime_example'] # list[str] | Filters results by runtime.  (optional)
version = ['version_example'] # list[str] | Filters results by function version.  (optional)
function_layers = ['function_layers_example'] # list[str] | Filters results by function layers.  (optional)
defended = True # bool | Filters results by functions which are defended by a Defender and are connected to Console (true) or not (false).  (optional)
compliance_ids = [56] # list[int] | Filters results by compliance ID.  (optional)

    try:
        api_instance.api_v1_tas_droplets_download_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, id=id, cloud_controller_addresses=cloud_controller_addresses, provider=provider, region=region, runtime=runtime, version=version, function_layers=function_layers, defended=defended, compliance_ids=compliance_ids)
    except ApiException as e:
        print("Exception when calling TasDropletsApi->api_v1_tas_droplets_download_get: %s\n" % e)
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
 **id** | [**list[str]**](str.md)| List of function IDs.  | [optional] 
 **cloud_controller_addresses** | [**list[str]**](str.md)| List of cloud controller addresses which hold the functions.  | [optional] 
 **provider** | [**list[str]**](str.md)| Filters results by provider.  | [optional] 
 **region** | [**list[str]**](str.md)| Filters results by region.  | [optional] 
 **runtime** | [**list[str]**](str.md)| Filters results by runtime.  | [optional] 
 **version** | [**list[str]**](str.md)| Filters results by function version.  | [optional] 
 **function_layers** | [**list[str]**](str.md)| Filters results by function layers.  | [optional] 
 **defended** | **bool**| Filters results by functions which are defended by a Defender and are connected to Console (true) or not (false).  | [optional] 
 **compliance_ids** | [**list[int]**](int.md)| Filters results by compliance ID.  | [optional] 

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

# **api_v1_tas_droplets_get**
> list[ServerlessFunctionInfo] api_v1_tas_droplets_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, id=id, cloud_controller_addresses=cloud_controller_addresses, provider=provider, region=region, runtime=runtime, version=version, function_layers=function_layers, defended=defended, compliance_ids=compliance_ids)



TASDroplets returns TAS droplets 

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
    api_instance = openapi_client.TasDropletsApi(api_client)
    offset = 56 # int | Offset from the start of the list from which to retrieve documents.  (optional)
limit = 56 # int | Number of documents to return.  (optional)
search = 'search_example' # str | Search term.  (optional)
sort = 'sort_example' # str | Key on which to sort.  (optional)
reverse = True # bool | Sort order.  (optional)
collections = ['collections_example'] # list[str] | Scopes the query by collection.  (optional)
account_ids = ['account_ids_example'] # list[str] | Scopes the query by account ID.  (optional)
fields = ['fields_example'] # list[str] | List of fields to retrieve.  (optional)
id = ['id_example'] # list[str] | List of function IDs.  (optional)
cloud_controller_addresses = ['cloud_controller_addresses_example'] # list[str] | List of cloud controller addresses which hold the functions.  (optional)
provider = ['provider_example'] # list[str] | Filters results by provider.  (optional)
region = ['region_example'] # list[str] | Filters results by region.  (optional)
runtime = ['runtime_example'] # list[str] | Filters results by runtime.  (optional)
version = ['version_example'] # list[str] | Filters results by function version.  (optional)
function_layers = ['function_layers_example'] # list[str] | Filters results by function layers.  (optional)
defended = True # bool | Filters results by functions which are defended by a Defender and are connected to Console (true) or not (false).  (optional)
compliance_ids = [56] # list[int] | Filters results by compliance ID.  (optional)

    try:
        api_response = api_instance.api_v1_tas_droplets_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, id=id, cloud_controller_addresses=cloud_controller_addresses, provider=provider, region=region, runtime=runtime, version=version, function_layers=function_layers, defended=defended, compliance_ids=compliance_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasDropletsApi->api_v1_tas_droplets_get: %s\n" % e)
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
 **id** | [**list[str]**](str.md)| List of function IDs.  | [optional] 
 **cloud_controller_addresses** | [**list[str]**](str.md)| List of cloud controller addresses which hold the functions.  | [optional] 
 **provider** | [**list[str]**](str.md)| Filters results by provider.  | [optional] 
 **region** | [**list[str]**](str.md)| Filters results by region.  | [optional] 
 **runtime** | [**list[str]**](str.md)| Filters results by runtime.  | [optional] 
 **version** | [**list[str]**](str.md)| Filters results by function version.  | [optional] 
 **function_layers** | [**list[str]**](str.md)| Filters results by function layers.  | [optional] 
 **defended** | **bool**| Filters results by functions which are defended by a Defender and are connected to Console (true) or not (false).  | [optional] 
 **compliance_ids** | [**list[int]**](int.md)| Filters results by compliance ID.  | [optional] 

### Return type

[**list[ServerlessFunctionInfo]**](ServerlessFunctionInfo.md)

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

# **api_v1_tas_droplets_progress_get**
> list[SharedProgress] api_v1_tas_droplets_progress_get()



TASDropletsProgress returns the TAS droplets scan progress 

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
    api_instance = openapi_client.TasDropletsApi(api_client)
    
    try:
        api_response = api_instance.api_v1_tas_droplets_progress_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasDropletsApi->api_v1_tas_droplets_progress_get: %s\n" % e)
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

# **api_v1_tas_droplets_scan_post**
> api_v1_tas_droplets_scan_post()



ScanTASDroplets sends a TAS droplets scan request to all serverless scanner defenders 

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
    api_instance = openapi_client.TasDropletsApi(api_client)
    
    try:
        api_instance.api_v1_tas_droplets_scan_post()
    except ApiException as e:
        print("Exception when calling TasDropletsApi->api_v1_tas_droplets_scan_post: %s\n" % e)
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

# **api_v1_tas_droplets_stop_post**
> api_v1_tas_droplets_stop_post()



StopTASDropletsScan stops the current TAS droplets scan 

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
    api_instance = openapi_client.TasDropletsApi(api_client)
    
    try:
        api_instance.api_v1_tas_droplets_stop_post()
    except ApiException as e:
        print("Exception when calling TasDropletsApi->api_v1_tas_droplets_stop_post: %s\n" % e)
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


# openapi_client.FeedsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_feeds_bundle_get**](FeedsApi.md#api_v1_feeds_bundle_get) | **GET** /api/v1/feeds/bundle | 
[**api_v1_feeds_bundle_put**](FeedsApi.md#api_v1_feeds_bundle_put) | **PUT** /api/v1/feeds/bundle | 
[**api_v1_feeds_custom_custom_vulnerabilities_digest_get**](FeedsApi.md#api_v1_feeds_custom_custom_vulnerabilities_digest_get) | **GET** /api/v1/feeds/custom/custom-vulnerabilities/digest | 
[**api_v1_feeds_custom_custom_vulnerabilities_get**](FeedsApi.md#api_v1_feeds_custom_custom_vulnerabilities_get) | **GET** /api/v1/feeds/custom/custom-vulnerabilities | 
[**api_v1_feeds_custom_custom_vulnerabilities_put**](FeedsApi.md#api_v1_feeds_custom_custom_vulnerabilities_put) | **PUT** /api/v1/feeds/custom/custom-vulnerabilities | 
[**api_v1_feeds_custom_cve_allow_list_digest_get**](FeedsApi.md#api_v1_feeds_custom_cve_allow_list_digest_get) | **GET** /api/v1/feeds/custom/cve-allow-list/digest | 
[**api_v1_feeds_custom_cve_allow_list_get**](FeedsApi.md#api_v1_feeds_custom_cve_allow_list_get) | **GET** /api/v1/feeds/custom/cve-allow-list | 
[**api_v1_feeds_custom_cve_allow_list_put**](FeedsApi.md#api_v1_feeds_custom_cve_allow_list_put) | **PUT** /api/v1/feeds/custom/cve-allow-list | 
[**api_v1_feeds_custom_ips_digest_get**](FeedsApi.md#api_v1_feeds_custom_ips_digest_get) | **GET** /api/v1/feeds/custom/ips/digest | 
[**api_v1_feeds_custom_ips_get**](FeedsApi.md#api_v1_feeds_custom_ips_get) | **GET** /api/v1/feeds/custom/ips | 
[**api_v1_feeds_custom_ips_put**](FeedsApi.md#api_v1_feeds_custom_ips_put) | **PUT** /api/v1/feeds/custom/ips | 
[**api_v1_feeds_custom_malware_digest_get**](FeedsApi.md#api_v1_feeds_custom_malware_digest_get) | **GET** /api/v1/feeds/custom/malware/digest | 
[**api_v1_feeds_custom_malware_get**](FeedsApi.md#api_v1_feeds_custom_malware_get) | **GET** /api/v1/feeds/custom/malware | 
[**api_v1_feeds_custom_malware_put**](FeedsApi.md#api_v1_feeds_custom_malware_put) | **PUT** /api/v1/feeds/custom/malware | 
[**api_v1_feeds_force_refresh_put**](FeedsApi.md#api_v1_feeds_force_refresh_put) | **PUT** /api/v1/feeds/force-refresh | 


# **api_v1_feeds_bundle_get**
> api_v1_feeds_bundle_get()



DownloadFeedsBundle creates and serves the intelligence feeds bundle 

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
    api_instance = openapi_client.FeedsApi(api_client)
    
    try:
        api_instance.api_v1_feeds_bundle_get()
    except ApiException as e:
        print("Exception when calling FeedsApi->api_v1_feeds_bundle_get: %s\n" % e)
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

# **api_v1_feeds_bundle_put**
> api_v1_feeds_bundle_put()



UploadOfflineIntelligenceFeeds uploads the offline intelligence feeds bundle 

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
    api_instance = openapi_client.FeedsApi(api_client)
    
    try:
        api_instance.api_v1_feeds_bundle_put()
    except ApiException as e:
        print("Exception when calling FeedsApi->api_v1_feeds_bundle_put: %s\n" % e)
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

# **api_v1_feeds_custom_custom_vulnerabilities_digest_get**
> str api_v1_feeds_custom_custom_vulnerabilities_digest_get()



CustomVulnerabilitiesDigest returns the custom vulnerabilities feed digest 

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
    api_instance = openapi_client.FeedsApi(api_client)
    
    try:
        api_response = api_instance.api_v1_feeds_custom_custom_vulnerabilities_digest_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FeedsApi->api_v1_feeds_custom_custom_vulnerabilities_digest_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

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

# **api_v1_feeds_custom_custom_vulnerabilities_get**
> VulnCustomVulnerabilities api_v1_feeds_custom_custom_vulnerabilities_get()



CustomVulnerabilities returns the custom vulnerabilities feed 

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
    api_instance = openapi_client.FeedsApi(api_client)
    
    try:
        api_response = api_instance.api_v1_feeds_custom_custom_vulnerabilities_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FeedsApi->api_v1_feeds_custom_custom_vulnerabilities_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**VulnCustomVulnerabilities**](VulnCustomVulnerabilities.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CustomVulnerabilities is a collection of custom vulnerabilities TBD: this storage usage is not best practice, should be migrate to a 1 document per vulnerability |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_feeds_custom_custom_vulnerabilities_put**
> api_v1_feeds_custom_custom_vulnerabilities_put(vuln_custom_vulnerabilities=vuln_custom_vulnerabilities)



SetCustomVulnerabilities sets the custom vulnerabilities feed 

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
    api_instance = openapi_client.FeedsApi(api_client)
    vuln_custom_vulnerabilities = openapi_client.VulnCustomVulnerabilities() # VulnCustomVulnerabilities |  (optional)

    try:
        api_instance.api_v1_feeds_custom_custom_vulnerabilities_put(vuln_custom_vulnerabilities=vuln_custom_vulnerabilities)
    except ApiException as e:
        print("Exception when calling FeedsApi->api_v1_feeds_custom_custom_vulnerabilities_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vuln_custom_vulnerabilities** | [**VulnCustomVulnerabilities**](VulnCustomVulnerabilities.md)|  | [optional] 

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

# **api_v1_feeds_custom_cve_allow_list_digest_get**
> str api_v1_feeds_custom_cve_allow_list_digest_get()



CVEAllowListDigest returns the CVE allow list digest 

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
    api_instance = openapi_client.FeedsApi(api_client)
    
    try:
        api_response = api_instance.api_v1_feeds_custom_cve_allow_list_digest_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FeedsApi->api_v1_feeds_custom_cve_allow_list_digest_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

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

# **api_v1_feeds_custom_cve_allow_list_get**
> SharedCVEAllowList api_v1_feeds_custom_cve_allow_list_get()



CVEAllowList returns the list of allowed CVEs 

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
    api_instance = openapi_client.FeedsApi(api_client)
    
    try:
        api_response = api_instance.api_v1_feeds_custom_cve_allow_list_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FeedsApi->api_v1_feeds_custom_cve_allow_list_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SharedCVEAllowList**](SharedCVEAllowList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CVEAllowList is a collection of allowed CVE&#39;s |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_feeds_custom_cve_allow_list_put**
> api_v1_feeds_custom_cve_allow_list_put(shared_cve_allow_list=shared_cve_allow_list)



SetCVEAllowList adds the given CVE allow list entries 

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
    api_instance = openapi_client.FeedsApi(api_client)
    shared_cve_allow_list = openapi_client.SharedCVEAllowList() # SharedCVEAllowList |  (optional)

    try:
        api_instance.api_v1_feeds_custom_cve_allow_list_put(shared_cve_allow_list=shared_cve_allow_list)
    except ApiException as e:
        print("Exception when calling FeedsApi->api_v1_feeds_custom_cve_allow_list_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shared_cve_allow_list** | [**SharedCVEAllowList**](SharedCVEAllowList.md)|  | [optional] 

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

# **api_v1_feeds_custom_ips_digest_get**
> str api_v1_feeds_custom_ips_digest_get()



CustomIPFeedDigest returns the custom ip feed digest 

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
    api_instance = openapi_client.FeedsApi(api_client)
    
    try:
        api_response = api_instance.api_v1_feeds_custom_ips_digest_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FeedsApi->api_v1_feeds_custom_ips_digest_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

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

# **api_v1_feeds_custom_ips_get**
> SharedCustomIPFeed api_v1_feeds_custom_ips_get()



CustomIPFeed returns the custom ip feed 

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
    api_instance = openapi_client.FeedsApi(api_client)
    
    try:
        api_response = api_instance.api_v1_feeds_custom_ips_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FeedsApi->api_v1_feeds_custom_ips_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SharedCustomIPFeed**](SharedCustomIPFeed.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CustomIPFeed represent the custom IP feed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_feeds_custom_ips_put**
> api_v1_feeds_custom_ips_put(shared_custom_ip_feed=shared_custom_ip_feed)



SetCustomIPFeed sets the custom IP feed 

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
    api_instance = openapi_client.FeedsApi(api_client)
    shared_custom_ip_feed = openapi_client.SharedCustomIPFeed() # SharedCustomIPFeed |  (optional)

    try:
        api_instance.api_v1_feeds_custom_ips_put(shared_custom_ip_feed=shared_custom_ip_feed)
    except ApiException as e:
        print("Exception when calling FeedsApi->api_v1_feeds_custom_ips_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shared_custom_ip_feed** | [**SharedCustomIPFeed**](SharedCustomIPFeed.md)|  | [optional] 

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

# **api_v1_feeds_custom_malware_digest_get**
> str api_v1_feeds_custom_malware_digest_get()



CustomMalwareFeedDigest returns the custom malware feed digest 

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
    api_instance = openapi_client.FeedsApi(api_client)
    
    try:
        api_response = api_instance.api_v1_feeds_custom_malware_digest_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FeedsApi->api_v1_feeds_custom_malware_digest_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

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

# **api_v1_feeds_custom_malware_get**
> SharedCustomMalwareFeed api_v1_feeds_custom_malware_get()



CustomMalwareFeed returns the custom malware feed 

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
    api_instance = openapi_client.FeedsApi(api_client)
    
    try:
        api_response = api_instance.api_v1_feeds_custom_malware_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FeedsApi->api_v1_feeds_custom_malware_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SharedCustomMalwareFeed**](SharedCustomMalwareFeed.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CustomMalwareFeed represent the custom malware |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_feeds_custom_malware_put**
> api_v1_feeds_custom_malware_put(shared_custom_malware_feed=shared_custom_malware_feed)



SetCustomMalwareFeed sets the custom malware feed 

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
    api_instance = openapi_client.FeedsApi(api_client)
    shared_custom_malware_feed = openapi_client.SharedCustomMalwareFeed() # SharedCustomMalwareFeed |  (optional)

    try:
        api_instance.api_v1_feeds_custom_malware_put(shared_custom_malware_feed=shared_custom_malware_feed)
    except ApiException as e:
        print("Exception when calling FeedsApi->api_v1_feeds_custom_malware_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shared_custom_malware_feed** | [**SharedCustomMalwareFeed**](SharedCustomMalwareFeed.md)|  | [optional] 

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

# **api_v1_feeds_force_refresh_put**
> api_v1_feeds_force_refresh_put()



ForceIntelligenceUpdate performs pushing/polling of intelligence feeds on demand 

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
    api_instance = openapi_client.FeedsApi(api_client)
    
    try:
        api_instance.api_v1_feeds_force_refresh_put()
    except ApiException as e:
        print("Exception when calling FeedsApi->api_v1_feeds_force_refresh_put: %s\n" % e)
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


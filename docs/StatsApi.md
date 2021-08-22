# openapi_client.StatsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_stats_app_firewall_count_get**](StatsApi.md#api_v1_stats_app_firewall_count_get) | **GET** /api/v1/stats/app-firewall/count | 
[**api_v1_stats_compliance_download_get**](StatsApi.md#api_v1_stats_compliance_download_get) | **GET** /api/v1/stats/compliance/download | 
[**api_v1_stats_compliance_get**](StatsApi.md#api_v1_stats_compliance_get) | **GET** /api/v1/stats/compliance | 
[**api_v1_stats_compliance_refresh_post**](StatsApi.md#api_v1_stats_compliance_refresh_post) | **POST** /api/v1/stats/compliance/refresh | 
[**api_v1_stats_daily_get**](StatsApi.md#api_v1_stats_daily_get) | **GET** /api/v1/stats/daily | 
[**api_v1_stats_dashboard_get**](StatsApi.md#api_v1_stats_dashboard_get) | **GET** /api/v1/stats/dashboard | 
[**api_v1_stats_events_get**](StatsApi.md#api_v1_stats_events_get) | **GET** /api/v1/stats/events | 
[**api_v1_stats_license_download_get**](StatsApi.md#api_v1_stats_license_download_get) | **GET** /api/v1/stats/license/download | 
[**api_v1_stats_license_get**](StatsApi.md#api_v1_stats_license_get) | **GET** /api/v1/stats/license | 
[**api_v1_stats_vulnerabilities_get**](StatsApi.md#api_v1_stats_vulnerabilities_get) | **GET** /api/v1/stats/vulnerabilities | 
[**api_v1_stats_vulnerabilities_impacted_resources_get**](StatsApi.md#api_v1_stats_vulnerabilities_impacted_resources_get) | **GET** /api/v1/stats/vulnerabilities/impacted-resources | 
[**api_v1_stats_vulnerabilities_refresh_post**](StatsApi.md#api_v1_stats_vulnerabilities_refresh_post) | **POST** /api/v1/stats/vulnerabilities/refresh | 


# **api_v1_stats_app_firewall_count_get**
> int api_v1_stats_app_firewall_count_get()



AppFirewallCount returns the number of app firewalls in use 

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
    api_instance = openapi_client.StatsApi(api_client)
    
    try:
        api_response = api_instance.api_v1_stats_app_firewall_count_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatsApi->api_v1_stats_app_firewall_count_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**int**

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

# **api_v1_stats_compliance_download_get**
> api_v1_stats_compliance_download_get(collections=collections, account_ids=account_ids, rule_name=rule_name, policy_type=policy_type, category=category, template=template)



DownloadComplianceStats downloads the compliance stats 

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
    api_instance = openapi_client.StatsApi(api_client)
    collections = ['collections_example'] # list[str] | Scopes query by collection.  (optional)
account_ids = ['account_ids_example'] # list[str] | Scopes query by account ID.  (optional)
rule_name = 'rule_name_example' # str | Filters results by rule name.  (optional)
policy_type = 'policy_type_example' # str | Filters results by policy type. Used to further scope queries because rule names do not need to be unique between policies.  (optional)
category = 'category_example' # str | Filters results by category. For example, a benchmark or resource type.  (optional)
template = 'template_example' # str | Filters results by compliance template.  (optional)

    try:
        api_instance.api_v1_stats_compliance_download_get(collections=collections, account_ids=account_ids, rule_name=rule_name, policy_type=policy_type, category=category, template=template)
    except ApiException as e:
        print("Exception when calling StatsApi->api_v1_stats_compliance_download_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collections** | [**list[str]**](str.md)| Scopes query by collection.  | [optional] 
 **account_ids** | [**list[str]**](str.md)| Scopes query by account ID.  | [optional] 
 **rule_name** | **str**| Filters results by rule name.  | [optional] 
 **policy_type** | **str**| Filters results by policy type. Used to further scope queries because rule names do not need to be unique between policies.  | [optional] 
 **category** | **str**| Filters results by category. For example, a benchmark or resource type.  | [optional] 
 **template** | **str**| Filters results by compliance template.  | [optional] 

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

# **api_v1_stats_compliance_get**
> TypesComplianceStats api_v1_stats_compliance_get(collections=collections, account_ids=account_ids, rule_name=rule_name, policy_type=policy_type, category=category, template=template)



ComplianceStats returns compliance stats that match the specified query options 

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
    api_instance = openapi_client.StatsApi(api_client)
    collections = ['collections_example'] # list[str] | Scopes query by collection.  (optional)
account_ids = ['account_ids_example'] # list[str] | Scopes query by account ID.  (optional)
rule_name = 'rule_name_example' # str | Filters results by rule name.  (optional)
policy_type = 'policy_type_example' # str | Filters results by policy type. Used to further scope queries because rule names do not need to be unique between policies.  (optional)
category = 'category_example' # str | Filters results by category. For example, a benchmark or resource type.  (optional)
template = 'template_example' # str | Filters results by compliance template.  (optional)

    try:
        api_response = api_instance.api_v1_stats_compliance_get(collections=collections, account_ids=account_ids, rule_name=rule_name, policy_type=policy_type, category=category, template=template)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatsApi->api_v1_stats_compliance_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collections** | [**list[str]**](str.md)| Scopes query by collection.  | [optional] 
 **account_ids** | [**list[str]**](str.md)| Scopes query by account ID.  | [optional] 
 **rule_name** | **str**| Filters results by rule name.  | [optional] 
 **policy_type** | **str**| Filters results by policy type. Used to further scope queries because rule names do not need to be unique between policies.  | [optional] 
 **category** | **str**| Filters results by category. For example, a benchmark or resource type.  | [optional] 
 **template** | **str**| Filters results by compliance template.  | [optional] 

### Return type

[**TypesComplianceStats**](TypesComplianceStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ComplianceStats holds compliance data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_stats_compliance_refresh_post**
> TypesComplianceStats api_v1_stats_compliance_refresh_post(collections=collections, account_ids=account_ids, rule_name=rule_name, policy_type=policy_type, category=category, template=template)



RefreshComplianceStats collects compliance stats and returns the collected stats 

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
    api_instance = openapi_client.StatsApi(api_client)
    collections = ['collections_example'] # list[str] | Scopes query by collection.  (optional)
account_ids = ['account_ids_example'] # list[str] | Scopes query by account ID.  (optional)
rule_name = 'rule_name_example' # str | Filters results by rule name.  (optional)
policy_type = 'policy_type_example' # str | Filters results by policy type. Used to further scope queries because rule names do not need to be unique between policies.  (optional)
category = 'category_example' # str | Filters results by category. For example, a benchmark or resource type.  (optional)
template = 'template_example' # str | Filters results by compliance template.  (optional)

    try:
        api_response = api_instance.api_v1_stats_compliance_refresh_post(collections=collections, account_ids=account_ids, rule_name=rule_name, policy_type=policy_type, category=category, template=template)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatsApi->api_v1_stats_compliance_refresh_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collections** | [**list[str]**](str.md)| Scopes query by collection.  | [optional] 
 **account_ids** | [**list[str]**](str.md)| Scopes query by account ID.  | [optional] 
 **rule_name** | **str**| Filters results by rule name.  | [optional] 
 **policy_type** | **str**| Filters results by policy type. Used to further scope queries because rule names do not need to be unique between policies.  | [optional] 
 **category** | **str**| Filters results by category. For example, a benchmark or resource type.  | [optional] 
 **template** | **str**| Filters results by compliance template.  | [optional] 

### Return type

[**TypesComplianceStats**](TypesComplianceStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ComplianceStats holds compliance data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_stats_daily_get**
> list[TypesStats] api_v1_stats_daily_get()



Stats returns the system stats 

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
    api_instance = openapi_client.StatsApi(api_client)
    
    try:
        api_response = api_instance.api_v1_stats_daily_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatsApi->api_v1_stats_daily_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[TypesStats]**](TypesStats.md)

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

# **api_v1_stats_dashboard_get**
> TypesTrends api_v1_stats_dashboard_get()



Trends returns the current system trends 

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
    api_instance = openapi_client.StatsApi(api_client)
    
    try:
        api_response = api_instance.api_v1_stats_dashboard_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatsApi->api_v1_stats_dashboard_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TypesTrends**](TypesTrends.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Trends contains data on global trends in the system |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_stats_events_get**
> TypesEventStats api_v1_stats_events_get(collections=collections, account_ids=account_ids, _from=_from, to=to, attack_techniques=attack_techniques)



EventsStats returns events statistics 

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
    api_instance = openapi_client.StatsApi(api_client)
    collections = ['collections_example'] # list[str] | Collections are collections scoping the query.  (optional)
account_ids = ['account_ids_example'] # list[str] | AccountIDs are the account IDs scoping the query.  (optional)
_from = '2013-10-20T19:20:30+01:00' # datetime | From is an optional minimum time constraints for the audit.  (optional)
to = '2013-10-20T19:20:30+01:00' # datetime | To is an optional maximum time constraints for the audit.  (optional)
attack_techniques = ['attack_techniques_example'] # list[str] | AttackTechniques are the MITRE attack techniques.  (optional)

    try:
        api_response = api_instance.api_v1_stats_events_get(collections=collections, account_ids=account_ids, _from=_from, to=to, attack_techniques=attack_techniques)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatsApi->api_v1_stats_events_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collections** | [**list[str]**](str.md)| Collections are collections scoping the query.  | [optional] 
 **account_ids** | [**list[str]**](str.md)| AccountIDs are the account IDs scoping the query.  | [optional] 
 **_from** | **datetime**| From is an optional minimum time constraints for the audit.  | [optional] 
 **to** | **datetime**| To is an optional maximum time constraints for the audit.  | [optional] 
 **attack_techniques** | [**list[str]**](str.md)| AttackTechniques are the MITRE attack techniques.  | [optional] 

### Return type

[**TypesEventStats**](TypesEventStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | EventStats holds counters for all event types |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_stats_license_download_get**
> api_v1_stats_license_download_get()



DownloadLicenseStats downloads the license usage 

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
    api_instance = openapi_client.StatsApi(api_client)
    
    try:
        api_instance.api_v1_stats_license_download_get()
    except ApiException as e:
        print("Exception when calling StatsApi->api_v1_stats_license_download_get: %s\n" % e)
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

# **api_v1_stats_license_get**
> TypesLicenseStats api_v1_stats_license_get()



LicenseStats returns the license stats including the credit per defender 

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
    api_instance = openapi_client.StatsApi(api_client)
    
    try:
        api_response = api_instance.api_v1_stats_license_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatsApi->api_v1_stats_license_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TypesLicenseStats**](TypesLicenseStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | LicenseStats holds the console license stats |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_stats_vulnerabilities_get**
> list[TypesVulnerabilityStats] api_v1_stats_vulnerabilities_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields)



VulnerabilityStats returns most critical vulnerability stats or search result stats 

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
    api_instance = openapi_client.StatsApi(api_client)
    offset = 56 # int | Offset from the start of the list from which to retrieve documents.  (optional)
limit = 56 # int | Number of documents to return.  (optional)
search = 'search_example' # str | Search term.  (optional)
sort = 'sort_example' # str | Key on which to sort.  (optional)
reverse = True # bool | Sort order.  (optional)
collections = ['collections_example'] # list[str] | Scopes the query by collection.  (optional)
account_ids = ['account_ids_example'] # list[str] | Scopes the query by account ID.  (optional)
fields = ['fields_example'] # list[str] | List of fields to retrieve.  (optional)

    try:
        api_response = api_instance.api_v1_stats_vulnerabilities_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatsApi->api_v1_stats_vulnerabilities_get: %s\n" % e)
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

### Return type

[**list[TypesVulnerabilityStats]**](TypesVulnerabilityStats.md)

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

# **api_v1_stats_vulnerabilities_impacted_resources_get**
> TypesVulnImpactedResources api_v1_stats_vulnerabilities_impacted_resources_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, cve=cve)



VulnerabilityImpactedResources returns the impacted resources of a given CVE 

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
    api_instance = openapi_client.StatsApi(api_client)
    offset = 56 # int | Offset from the start of the list from which to retrieve documents.  (optional)
limit = 56 # int | Number of documents to return.  (optional)
search = 'search_example' # str | Search term.  (optional)
sort = 'sort_example' # str | Key on which to sort.  (optional)
reverse = True # bool | Sort order.  (optional)
collections = ['collections_example'] # list[str] | Scopes the query by collection.  (optional)
account_ids = ['account_ids_example'] # list[str] | Scopes the query by account ID.  (optional)
fields = ['fields_example'] # list[str] | List of fields to retrieve.  (optional)
cve = 'cve_example' # str | CVE is used to as a pivot for the impacted resource search.  (optional)

    try:
        api_response = api_instance.api_v1_stats_vulnerabilities_impacted_resources_get(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields, cve=cve)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatsApi->api_v1_stats_vulnerabilities_impacted_resources_get: %s\n" % e)
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
 **cve** | **str**| CVE is used to as a pivot for the impacted resource search.  | [optional] 

### Return type

[**TypesVulnImpactedResources**](TypesVulnImpactedResources.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | VulnImpactedResources holds details about the resources impacted by vulnerability |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_stats_vulnerabilities_refresh_post**
> list[TypesVulnerabilityStats] api_v1_stats_vulnerabilities_refresh_post(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields)



RefreshVulnerabilityStats collects vulnerability stats and returns the collected stats 

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
    api_instance = openapi_client.StatsApi(api_client)
    offset = 56 # int | Offset from the start of the list from which to retrieve documents.  (optional)
limit = 56 # int | Number of documents to return.  (optional)
search = 'search_example' # str | Search term.  (optional)
sort = 'sort_example' # str | Key on which to sort.  (optional)
reverse = True # bool | Sort order.  (optional)
collections = ['collections_example'] # list[str] | Scopes the query by collection.  (optional)
account_ids = ['account_ids_example'] # list[str] | Scopes the query by account ID.  (optional)
fields = ['fields_example'] # list[str] | List of fields to retrieve.  (optional)

    try:
        api_response = api_instance.api_v1_stats_vulnerabilities_refresh_post(offset=offset, limit=limit, search=search, sort=sort, reverse=reverse, collections=collections, account_ids=account_ids, fields=fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatsApi->api_v1_stats_vulnerabilities_refresh_post: %s\n" % e)
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

### Return type

[**list[TypesVulnerabilityStats]**](TypesVulnerabilityStats.md)

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


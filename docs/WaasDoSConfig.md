# WaasDoSConfig

DoSConfig is a dos policy specification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert** | [**WaasDoSRates**](WaasDoSRates.md) |  | [optional] 
**ban** | [**WaasDoSRates**](WaasDoSRates.md) |  | [optional] 
**enabled** | **bool** | Enabled indicates if dos protection is enabled.  | [optional] 
**excluded_network_lists** | **list[str]** | Network IPs to exclude from DoS tracking.  | [optional] 
**match_conditions** | [**list[WaasDoSMatchCondition]**](WaasDoSMatchCondition.md) | Conditions on which to match to track a request. The conditions are \\\&quot;OR\\\&quot;&#39;d together during the check.  | [optional] 
**track_session** | **bool** | Indicates if the custom session ID generated during bot protection flow is tracked (true) or not (false).  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



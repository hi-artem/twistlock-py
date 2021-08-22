# WaasAccessControls

AccessControls contains the access controls config (e.g., denied/allowed sources)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert** | **list[str]** | Alert are the denied sources for which we alert.  | [optional] 
**allow** | **list[str]** | Allow are the allowed sources for which we don&#39;t alert or prevent.  | [optional] 
**allow_mode** | **bool** | AllowMode indicates allowlist (true) or denylist (false) mode.  | [optional] 
**enabled** | **bool** | Enabled indicates if access controls protection is enabled.  | [optional] 
**fallback_effect** | [**WaasEffect**](WaasEffect.md) |  | [optional] 
**prevent** | **list[str]** | Prevent are the denied sources.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



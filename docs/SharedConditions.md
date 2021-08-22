# SharedConditions

Conditions contains rule conditions. Conditions apply only for their respective policy type

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | Allowed volume host device (wildcard). If a \&quot;container create\&quot; command specifies a non matching host device, th action is blocked. Only applies to rules in certain policy types.  | [optional] 
**readonly** | **bool** | Indicates if the condition applies only to read-only commands (i.e., HTTP GET requests) (true) or not (false).  | [optional] 
**vulnerabilities** | [**list[VulnCondition]**](VulnCondition.md) | Block and scan severity-based vulnerabilities conditions.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



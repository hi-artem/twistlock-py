# SharedCloudScanPolicy

CloudScanPolicy holds policies for cloud scan

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID is the cloud policy id.  | [optional] 
**disabled** | **bool** | Indicates if the rule is currently disabled (true) or not (false).  | [optional] 
**modified** | **datetime** | Datetime when the rule was last modified.  | [optional] 
**name** | **str** | Name of the rule.  | [optional] 
**notes** | **str** | Free-form text.  | [optional] 
**owner** | **str** | User who created or last modified the rule.  | [optional] 
**previous_name** | **str** | Previous name of the rule. Required for rule renaming.  | [optional] 
**rules** | [**list[SharedCloudScanRule]**](SharedCloudScanRule.md) | Rules are the rules for cloud scan.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



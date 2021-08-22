# AdmissionRule

Rule represents an admission rule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attack_techniques** | [**list[MitreTechnique]**](MitreTechnique.md) | AttackTechniques are the MITRE attack techniques.  | [optional] 
**description** | **str** | Description is the rule description.  | [optional] 
**disabled** | **bool** | Indicates if the rule is currently disabled (true) or not (false).  | [optional] 
**effect** | [**CommonPolicyEffect**](CommonPolicyEffect.md) |  | [optional] 
**modified** | **datetime** | Datetime when the rule was last modified.  | [optional] 
**name** | **str** | Name of the rule.  | [optional] 
**notes** | **str** | Free-form text.  | [optional] 
**owner** | **str** | User who created or last modified the rule.  | [optional] 
**previous_name** | **str** | Previous name of the rule. Required for rule renaming.  | [optional] 
**script** | **str** | Script is the Rego script.  | [optional] 
**skip_raw_req** | **bool** | SkipRawReq signals to exclude raw review request in a resulting admission audit.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



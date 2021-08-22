# RuntimeHostPolicyRule

HostPolicyRule represents a single rule in the runtime policy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anti_malware** | [**RuntimeAntiMalwareRule**](RuntimeAntiMalwareRule.md) |  | [optional] 
**collections** | [**list[CollectionCollection]**](CollectionCollection.md) | Collections is a list of collections the rule applies to.  | [optional] 
**custom_rules** | [**list[CustomrulesRef]**](CustomrulesRef.md) | CustomRules is a list of custom rules associated with the container runtime policy.  | [optional] 
**disabled** | **bool** | Indicates if the rule is currently disabled (true) or not (false).  | [optional] 
**dns** | [**RuntimeHostDNSRule**](RuntimeHostDNSRule.md) |  | [optional] 
**file_integrity_rules** | [**list[RuntimeFileIntegrityRule]**](RuntimeFileIntegrityRule.md) | FileIntegrityRules are the file integrity monitoring rules.  | [optional] 
**forensic** | [**CommonHostForensicSettings**](CommonHostForensicSettings.md) |  | [optional] 
**log_inspection_rules** | [**list[RuntimeLogInspectionRule]**](RuntimeLogInspectionRule.md) | LogInspectionRules is a list of log inspection rules.  | [optional] 
**modified** | **datetime** | Datetime when the rule was last modified.  | [optional] 
**name** | **str** | Name of the rule.  | [optional] 
**network** | [**RuntimeHostNetworkRule**](RuntimeHostNetworkRule.md) |  | [optional] 
**notes** | **str** | Free-form text.  | [optional] 
**owner** | **str** | User who created or last modified the rule.  | [optional] 
**previous_name** | **str** | Previous name of the rule. Required for rule renaming.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



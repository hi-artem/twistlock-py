# SharedPolicyRule

PolicyRule is a single rule in the policy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **list[str]** | Action to take.  | [optional] 
**alert_threshold** | [**SharedAlertThreshold**](SharedAlertThreshold.md) |  | [optional] 
**all_compliance** | **bool** | Reports the results of all compliance checks (both passed and failed) (true).  | [optional] 
**audit_allowed** | **bool** | Specifies if Prisma Cloud audits successful transactions.  | [optional] 
**block_msg** | **str** | PolicyBlockMsg represent the block message in a Policy | [optional] 
**block_threshold** | [**SharedBlockThreshold**](SharedBlockThreshold.md) |  | [optional] 
**collections** | [**list[CollectionCollection]**](CollectionCollection.md) | List of collections. Used to scope the rule.  | [optional] 
**condition** | [**SharedConditions**](SharedConditions.md) |  | [optional] 
**cve_rules** | [**list[SharedCVERule]**](SharedCVERule.md) | List of CVE IDs classified for special handling (also known as exceptions).  | [optional] 
**disabled** | **bool** | Indicates if the rule is currently disabled (true) or not (false).  | [optional] 
**effect** | [**CommonPolicyEffect**](CommonPolicyEffect.md) |  | [optional] 
**grace_days** | **int** | Number of days to suppress the rule&#39;s block effect. Measured from date the vuln was fixed. If there&#39;s no fix, measured from the date the vuln was published.  | [optional] 
**group** | **list[str]** | Applicable groups.  | [optional] 
**license** | [**SharedLicenseConfig**](SharedLicenseConfig.md) |  | [optional] 
**modified** | **datetime** | Datetime when the rule was last modified.  | [optional] 
**name** | **str** | Name of the rule.  | [optional] 
**notes** | **str** | Free-form text.  | [optional] 
**only_fixed** | **bool** | Applies rule only when vendor fixes are available (true).  | [optional] 
**owner** | **str** | User who created or last modified the rule.  | [optional] 
**previous_name** | **str** | Previous name of the rule. Required for rule renaming.  | [optional] 
**principal** | **list[str]** | Applicable users.  | [optional] 
**tags** | [**list[SharedTagRule]**](SharedTagRule.md) | List of tags classified for special handling (also known as exceptions).  | [optional] 
**verbose** | **bool** | Displays a detailed message when an operation is blocked (true).  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



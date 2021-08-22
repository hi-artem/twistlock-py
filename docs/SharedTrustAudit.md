# SharedTrustAudit

TrustAudit represents a trust audit

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID is the registry-repo of the created container.  | [optional] 
**account_id** | **str** | AccountID is the cloud account ID where the audit was generated.  | [optional] 
**cluster** | **str** | Cluster is the cluster where the audit was generated.  | [optional] 
**count** | **int** | Count is the number of times this audit occurred.  | [optional] 
**effect** | [**VulnEffect**](VulnEffect.md) |  | [optional] 
**image_id** | **str** | ImageID is the container image id.  | [optional] 
**image_name** | **str** | ImageName is the container image name.  | [optional] 
**msg** | **str** | Message is the blocking message text.  | [optional] 
**rule_name** | **str** | If blocked, contains the name of the rule that was applied.  | [optional] 
**time** | **datetime** | Time is the UTC time of the audit event.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



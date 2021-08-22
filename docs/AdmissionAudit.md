# AdmissionAudit

Audit represents an admission audit

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | AccountID is the cloud account ID.  | [optional] 
**attack_techniques** | [**list[MitreTechnique]**](MitreTechnique.md) | AttackTechniques are the MITRE attack techniques.  | [optional] 
**cluster** | **str** | Cluster is the cluster where the audit took place.  | [optional] 
**collections** | **list[str]** | Collections are collections to which this audit applies.  | [optional] 
**effect** | **str** | Effect is the rule effect which was applied to the review which led to this audit.  | [optional] 
**kind** | **str** | Kind is the type of object being manipulated. For example: Pod.  | [optional] 
**message** | **str** | Message is the rule user defined message which appears on audit.  | [optional] 
**namespace** | **str** | Namespace is the namespace associated with the request (if any).  | [optional] 
**operation** | **str** | Operation is the operation being performed.  | [optional] 
**raw_request** | **str** | RawRequest is the original review request that caused this audit.  | [optional] 
**resource** | **str** | Resource is the name of the resource being requested.  This is not the kind.  For example: pods.  | [optional] 
**rule_name** | **str** | RuleName is the name of the rule which issued this audit.  | [optional] 
**time** | **datetime** | Time is the time at which the audit was generated.  | [optional] 
**user_groups** | **str** | UserGroups is the names of groups this user is a part of.  | [optional] 
**user_uid** | **str** | UserUID is a unique value that identifies this user across time. If this user is deleted and another user by the same name is added, they will have different UIDs.  | [optional] 
**username** | **str** | Username is the name that uniquely identifies this user among all active users.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



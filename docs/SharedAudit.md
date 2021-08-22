# SharedAudit

Audit represents an event in the system

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | AccountID is the cloud account ID where the audit was created.  | [optional] 
**allow** | **bool** | Allow indicates whether the command was allowe or denied.  | [optional] 
**api** | **str** | API is the api that is being audited.  | [optional] 
**cluster** | **str** | Cluster is the cluster from which the audit originated.  | [optional] 
**collections** | **list[str]** | Collections are collections to which this audit applies.  | [optional] 
**container_name** | **str** | ContainerName is the name of the container.  | [optional] 
**fqdn** | **str** | FQDN is the fully qualified domain name from which the audit originated.  | [optional] 
**hostname** | **str** | Hostname is the hostname from which the audit originated.  | [optional] 
**image_name** | **str** | ImageName is the name of the image.  | [optional] 
**labels** | **dict(str, str)** | Labels are the labels associated with the target audit (for containers/images).  | [optional] 
**msg** | **str** | Msg is the message explaining the audit.  | [optional] 
**rule_name** | **str** | RulesName is contains the name of the rule that was applied, when blocked.  | [optional] 
**source_ip** | **str** | SourceIP is the remote agent&#39;s source IP.  | [optional] 
**time** | **datetime** | Time is the UTC time of the audit event.  | [optional] 
**type** | **str** | Type is the audit type.  | [optional] 
**user** | **str** | User is the user that run the command.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# SharedContainerNetworkFirewallProfileAudits

ContainerNetworkFirewallProfileAudits represents the container network firewall profile audits

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ProfileID is the runtime profile ID.  | [optional] 
**audits** | [**dict(str, SharedContainerNetworkFirewallSubtypeAudits)**](SharedContainerNetworkFirewallSubtypeAudits.md) | Audits is a map from the audit sub-type to the audit events list.  | [optional] 
**cluster** | **str** | Cluster is the cluster from which the audit originated.  | [optional] 
**collections** | **list[str]** | Collections are collections to which this audit applies.  | [optional] 
**image_name** | **str** | ImageName is the container image name.  | [optional] 
**label** | **str** | Label represents the container deployment label.  | [optional] 
**os** | **str** | OS is the operating system distribution.  | [optional] 
**resource** | [**CommonRuntimeResource**](CommonRuntimeResource.md) |  | [optional] 
**time** | **datetime** | Time is the UTC time of the last audit event.  | [optional] 
**total** | **int** | Total is the total count of audits per runtime profile.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CnnfContainerAudit

ContainerAudit represents a network firewall audit event

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block** | **bool** | Block indicates whether the connection was blocked.  | [optional] 
**count** | **int** | Count is the event occurrences count.  | [optional] 
**dst_container_name** | **str** | DstContainerName is the destination container name.  | [optional] 
**dst_domain** | **str** | DstDomain is the destination domain that was queried.  | [optional] 
**dst_image_name** | **str** | DstImage is the destination image name.  | [optional] 
**dst_port** | **int** | DstPort is the connection destination port.  | [optional] 
**dst_profile_hash** | **int** | ProfileHash represents the profile hash It is allowed to contain up to uint32 numbers, and represented by int64 since mongodb does not support unsigned data types | [optional] 
**dst_profile_id** | **str** | DstProfileID is the destination profile ID.  | [optional] 
**dst_subnet** | **str** | DstSubnet is the destination subnet.  | [optional] 
**labels** | **dict(str, str)** | Labels are the custom labels associated with the target container.  | [optional] 
**msg** | **str** | Message is the event message.  | [optional] 
**rule_id** | **int** | RuleID represents the ID of each container network firewall policy rule | [optional] 
**src_container_name** | **str** | SrcContainerName is the source container name.  | [optional] 
**src_image_name** | **str** | SrcImage is the source image name.  | [optional] 
**src_profile_hash** | **int** | ProfileHash represents the profile hash It is allowed to contain up to uint32 numbers, and represented by int64 since mongodb does not support unsigned data types | [optional] 
**src_profile_id** | **str** | SrcProfileID is the source profile ID.  | [optional] 
**time** | **datetime** | Time is the UTC time of the audit event.  | [optional] 
**type** | [**CnnfNetworkFirewallAttackType**](CnnfNetworkFirewallAttackType.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CnnfHostAudit

HostAudit represents a host network firewall audit event

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | AccountID is the host account ID.  | [optional] 
**block** | **bool** | Block indicates whether the connection was blocked.  | [optional] 
**cluster** | **str** | Cluster is the cluster from which the audit originated.  | [optional] 
**count** | **int** | Count is the event occurrences count.  | [optional] 
**dst_hostname** | **str** | DstHostname is the destination hostname.  | [optional] 
**dst_port** | **int** | DstPort is the connection destination port.  | [optional] 
**dst_subnet** | **str** | DstSubnet is the destination subnet.  | [optional] 
**msg** | **str** | Message is the event message.  | [optional] 
**rule_id** | **int** | RuleID represents the ID of each container network firewall policy rule | [optional] 
**src_hash** | **int** | ProfileHash represents the profile hash It is allowed to contain up to uint32 numbers, and represented by int64 since mongodb does not support unsigned data types | [optional] 
**src_hostname** | **str** | SrcHostname is the source hostname.  | [optional] 
**src_subnet** | **str** | SrcSubnet is the source subnet.  | [optional] 
**time** | **datetime** | Time is the UTC time of the audit event.  | [optional] 
**type** | [**CnnfNetworkFirewallAttackType**](CnnfNetworkFirewallAttackType.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



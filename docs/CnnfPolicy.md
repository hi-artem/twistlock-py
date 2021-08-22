# CnnfPolicy

Policy holds the data for firewall policies (host and container)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | .  | [optional] 
**container_enabled** | **bool** | ContainerEnabled indicates whether container network firewall feature is enabled.  | [optional] 
**container_rules** | [**list[CnnfRule]**](CnnfRule.md) | ContainerRules holds the container firewall rules.  | [optional] 
**host_enabled** | **bool** | HostEnabled indicates whether host network firewall feature is enabled.  | [optional] 
**host_rules** | [**list[CnnfRule]**](CnnfRule.md) | HostRules holds the host firewall rules.  | [optional] 
**modified** | **datetime** | .  | [optional] 
**network_entities** | [**list[CnnfNetworkEntity]**](CnnfNetworkEntity.md) | NetworkEntities represents a list of network firewall entities | [optional] 
**owner** | **str** | .  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



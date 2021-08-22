# CnnfNetworkEntity

NetworkEntity represents a network firewall entity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | EntityID represents the ID of each network firewall entity. 20 bits are used. Max legal value: 2^20-1 | [optional] 
**allow_all** | [**CnnfAllowAllConnections**](CnnfAllowAllConnections.md) |  | [optional] 
**collections** | [**list[CollectionCollection]**](CollectionCollection.md) | Collections indicate the collection the entity is part of.  | [optional] 
**domains** | **list[str]** | Domains is a list of domains.  | [optional] 
**name** | **str** | Name is the entity name.  | [optional] 
**subnets** | [**list[CnnfSubnet]**](CnnfSubnet.md) | Subnets are the CIDR format network.  | [optional] 
**type** | [**CnnfRuleEntityType**](CnnfRuleEntityType.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



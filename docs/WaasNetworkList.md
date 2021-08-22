# WaasNetworkList

NetworkList represent network list of IP/CIDR in waas

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID.  | [optional] 
**description** | **str** | Description of the network list.  | [optional] 
**disabled** | **bool** | Indicates if the rule is currently disabled (true) or not (false).  | [optional] 
**modified** | **datetime** | Datetime when the rule was last modified.  | [optional] 
**name** | **str** | Name of the rule.  | [optional] 
**notes** | **str** | Free-form text.  | [optional] 
**owner** | **str** | User who created or last modified the rule.  | [optional] 
**previous_name** | **str** | Previous name of the rule. Required for rule renaming.  | [optional] 
**subnets** | **list[str]** | List of the IPv4 addresses and IP CIDR blocks.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



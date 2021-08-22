# RuntimeContainerNetworkRule

ContainerNetworkRule represents the restrictions/suppression for networking

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blacklist_ips** | **list[str]** | Deny-listed IP addresses.  | [optional] 
**blacklist_listening_ports** | [**list[CommonPortRange]**](CommonPortRange.md) | Deny-listed listening ports.  | [optional] 
**blacklist_outbound_ports** | [**list[CommonPortRange]**](CommonPortRange.md) | Deny-listed outbound ports.  | [optional] 
**detect_port_scan** | **bool** | Specifies whether port scanning detection is enabled (true) or not (false).  | [optional] 
**effect** | [**RuntimeRuleEffect**](RuntimeRuleEffect.md) |  | [optional] 
**skip_modified_proc** | **bool** | Specifies whether Prisma Cloud detects when modified processes perform malicious networking activity.  | [optional] 
**skip_raw_sockets** | **bool** | Specifies whether raw socket detection should be skipped (true) or not (false).  | [optional] 
**whitelist_ips** | **list[str]** | Allow-listed IP addresses.  | [optional] 
**whitelist_listening_ports** | [**list[CommonPortRange]**](CommonPortRange.md) | Allow-listed listening ports.  | [optional] 
**whitelist_outbound_ports** | [**list[CommonPortRange]**](CommonPortRange.md) | Allow-listed outbound ports.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



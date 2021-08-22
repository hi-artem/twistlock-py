# RuntimeHostNetworkRule

HostNetworkRule represents the restrictions/suppression for host networking

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_outbound_ips** | **list[str]** | AllowedOutboundIPs is a list of IPs to skip checks for.  | [optional] 
**custom_feed** | [**RuntimeRuleEffect**](RuntimeRuleEffect.md) |  | [optional] 
**denied_listening_ports** | [**list[CommonPortRange]**](CommonPortRange.md) | DeniedListeningPorts is a list of listening ports to deny.  | [optional] 
**denied_outbound_ips** | **list[str]** | DeniedOutboundIPs is a list of outbound IPs to deny.  | [optional] 
**denied_outbound_ports** | [**list[CommonPortRange]**](CommonPortRange.md) | DeniedOutboundPorts is a list of outbound ports to deny.  | [optional] 
**deny_list_effect** | [**RuntimeRuleEffect**](RuntimeRuleEffect.md) |  | [optional] 
**intelligence_feed** | [**RuntimeRuleEffect**](RuntimeRuleEffect.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



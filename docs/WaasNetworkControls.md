# WaasNetworkControls

NetworkControls contains the network controls config (e.g., access controls for IPs and countries)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advanced_protection_effect** | [**WaasEffect**](WaasEffect.md) |  | [optional] 
**countries** | [**WaasAccessControls**](WaasAccessControls.md) |  | [optional] 
**exception_subnets** | **list[str]** | Network lists for which requests completely bypass WAAS checks and protections.  | [optional] 
**subnets** | [**WaasAccessControls**](WaasAccessControls.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# SharedContainerScanResult

ContainerScanResult contains the result of a scanning a container

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id is the container id.  | [optional] 
**collections** | **list[str]** | Collections are collections to which this container applies.  | [optional] 
**firewall_protection** | [**WaasProtectionStatus**](WaasProtectionStatus.md) |  | [optional] 
**hostname** | **str** | Hostname is the hostname on which the container is deployed.  | [optional] 
**info** | [**SharedContainerInfo**](SharedContainerInfo.md) |  | [optional] 
**scan_time** | **datetime** | ScanTime is the container scan time.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



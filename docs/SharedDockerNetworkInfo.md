# SharedDockerNetworkInfo

DockerNetworkInfo contains network-related information about a container

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_address** | **str** | IPAddress is the container IP.  | [optional] 
**mac_address** | **str** | MacAddress is the container MAC.  | [optional] 
**networks** | [**list[SharedNetworkInfo]**](SharedNetworkInfo.md) | Networks are the networks the container is connected to.  | [optional] 
**ports** | [**list[SharedPort]**](SharedPort.md) | Ports are the container network binding that are externally mapped.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



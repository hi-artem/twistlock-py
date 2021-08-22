# DefenderDefender

Defender is an update about an agent starting

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | [**DefenderCategory**](DefenderCategory.md) |  | [optional] 
**certificate_expiration** | **datetime** | Client certificate expiration time.  | [optional] 
**cloud_metadata** | [**CommonCloudMetadata**](CommonCloudMetadata.md) |  | [optional] 
**cluster** | **str** | Cluster name (fallback is internal IP).  | [optional] 
**cluster_id** | **str** | Unique ID generated for each DaemonSet. Used to group Defenders by clusters. Note: Kubernetes does not provide a cluster name as part of its API.  | [optional] 
**collections** | **list[str]** | Collections to which this Defender belongs.  | [optional] 
**compatible_version** | **bool** | Indicates if Defender has a compatible version for communication (e.g., request logs) (true) or not (false).  | [optional] 
**connected** | **bool** | Indicates whether Defender is connected (true) or not (false).  | [optional] 
**features** | [**DefenderFeatures**](DefenderFeatures.md) |  | [optional] 
**firewall_protection** | [**WaasProtectionStatus**](WaasProtectionStatus.md) |  | [optional] 
**fqdn** | **str** | Full domain name of the host. Used in audit alerts to identify specific hosts.  | [optional] 
**hostname** | **str** | Name of host where Defender is deployed.  | [optional] 
**last_modified** | **datetime** | Datetime when the Defender&#39;s connectivity status last changed.  | [optional] 
**port** | **int** | Port that Defender uses to connect to Console.  | [optional] 
**proxy** | [**CommonProxySettings**](CommonProxySettings.md) |  | [optional] 
**remote_logging_supported** | **bool** | Indicates if Defender logs can be retrieved remotely (true) or not (false).  | [optional] 
**remote_mgmt_supported** | **bool** | Indicates if Defender can be remotely managed (upgraded, restarted) (true) or not (false).  | [optional] 
**status** | [**DefenderStatus**](DefenderStatus.md) |  | [optional] 
**system_info** | [**DefenderSystemInfo**](DefenderSystemInfo.md) |  | [optional] 
**tas_cluster_id** | **str** | TAS cluster ID where Defender runs. This is typically set to the Cloud controller&#39;s API address.  | [optional] 
**type** | [**DefenderType**](DefenderType.md) |  | [optional] 
**version** | **str** | Defender version.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



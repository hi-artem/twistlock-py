# SharedForensicSettings

ForensicSettings are settings for the forensic data collection

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collect_network_firewall** | **bool** | CollectNetworkFirewall indicates whether network firewall collection is enabled.  | [optional] 
**collect_network_snapshot** | **bool** | CollectNetworkSnapshot indicates whether network snapshot collection is enabled.  | [optional] 
**container_disk_usage_mb** | **int** | ContainerDiskUsageMb is the maximum amount of disk space used to store the container historical forensic events.  | [optional] 
**enabled** | **bool** | Enabled indicates whether host and container forensic data collection is enabled.  | [optional] 
**host_disk_usage_mb** | **int** | HostDiskUsageMb is the maximum amount of disk space used to store the host historical forensic events.  | [optional] 
**incident_snapshots_cap** | **int** | IncidentSnapshotCap is the maximum amount of incident snapshots we store.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TypesHostRadarEntity

HostRadarEntity is the extended host radar entity (include presentation metadata)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**os_distro** | **str** | OSDistro is the OS distro name (e.g., ubuntu).  | [optional] 
**id** | **str** | ID is the host name.  | [optional] 
**activities_count** | **int** | ActivitiesCount is the number of activities detected in the host.  | [optional] 
**allow_all** | [**CnnfAllowAllConnections**](CnnfAllowAllConnections.md) |  | [optional] 
**app_firewall_attack_counts** | [**list[TypesAppFirewallAttackCount]**](TypesAppFirewallAttackCount.md) | AppFirewallAttackCounts is the counts for the app firewall attacks.  | [optional] 
**cloud_metadata** | [**CommonCloudMetadata**](CommonCloudMetadata.md) |  | [optional] 
**cluster** | **str** | Cluster is the cluster the host is deployed on.  | [optional] 
**compliance_distribution** | [**VulnDistribution**](VulnDistribution.md) |  | [optional] 
**created** | **datetime** | Created is the profile creation time.  | [optional] 
**file_integrity_count** | **int** | FileIntegrityCount is the number of file integrity events detected in the host.  | [optional] 
**filesystem_count** | **int** | FilesystemCount is number of filesystem events triggered by the entity.  | [optional] 
**firewall_protection** | [**WaasProtectionStatus**](WaasProtectionStatus.md) |  | [optional] 
**geoip** | [**RuntimeProfileNetworkGeoIP**](RuntimeProfileNetworkGeoIP.md) |  | [optional] 
**incident_count** | **int** | IncidentCount is the number of incidents triggered by the entity.  | [optional] 
**incoming** | [**list[SharedHostRadarIncomingConnection]**](SharedHostRadarIncomingConnection.md) | Incoming are the incoming connections from the host.  | [optional] 
**internet** | [**SharedInternetConnections**](SharedInternetConnections.md) |  | [optional] 
**labels** | **list[str]** | Labels are the labels associated with the profile.  | [optional] 
**listening_ports** | [**CommonProfilePortData**](CommonProfilePortData.md) |  | [optional] 
**log_inspection_count** | **int** | LogInspectionCount is the number of log inspection events detected in the host.  | [optional] 
**network_count** | **int** | NetworkCount is number of network events triggered by the entity.  | [optional] 
**outbound_ports** | [**CommonProfilePortData**](CommonProfilePortData.md) |  | [optional] 
**processes_count** | **int** | ProcessesCount is the number of processes events triggered by the entity.  | [optional] 
**profile_hash** | **int** | ProfileHash represents the profile hash It is allowed to contain up to uint32 numbers, and represented by int64 since mongodb does not support unsigned data types | [optional] 
**subnet_connections** | [**SharedSubnetConnections**](SharedSubnetConnections.md) |  | [optional] 
**vulnerability_distribution** | [**VulnDistribution**](VulnDistribution.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



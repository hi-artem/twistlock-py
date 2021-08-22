# TypesContainerRadarEntity

ContainerRadarEntity is the extended container radar entity (include presentation metadata)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | .  | [optional] 
**allow_all** | [**CnnfAllowAllConnections**](CnnfAllowAllConnections.md) |  | [optional] 
**app_firewall_attack_counts** | [**list[TypesAppFirewallAttackCount]**](TypesAppFirewallAttackCount.md) | AppFirewallAttackCounts is the counts for the app firewall attacks.  | [optional] 
**cluster** | **str** | Cluster is the provided cluster name.  | [optional] 
**compliance_distribution** | [**VulnDistribution**](VulnDistribution.md) |  | [optional] 
**consul** | **bool** | Consul states whether it is a consul container.  | [optional] 
**container_count** | **int** | ContainerCount is the amount of containers per entity.  | [optional] 
**distro** | **str** | .  | [optional] 
**dns** | **bool** | DNS states whether this is a DNS node.  | [optional] 
**filesystem_count** | **int** | .  | [optional] 
**firewall_protection** | [**WaasProtectionStatus**](WaasProtectionStatus.md) |  | [optional] 
**geoip** | [**RuntimeProfileNetworkGeoIP**](RuntimeProfileNetworkGeoIP.md) |  | [optional] 
**has_dns_connection** | **bool** | HasDNSConnection states whether the node has DNS connection.  | [optional] 
**host_count** | **int** | .  | [optional] 
**hostname** | **str** | .  | [optional] 
**image_id** | **str** | ImageID is the entity&#39;s image ID.  | [optional] 
**image_name** | **str** | ImageName is the entity&#39;s image name.  | [optional] 
**image_names** | **list[str]** | ImageNames are the names of the image associated with the radar entity.  | [optional] 
**incident_count** | **int** | IncidentCount is the number of incidents.  | [optional] 
**incoming_connections** | [**list[SharedContainerRadarIncomingConnection]**](SharedContainerRadarIncomingConnection.md) | IncomingConnections are the radar entity incoming connections.  | [optional] 
**internet** | [**SharedInternetConnections**](SharedInternetConnections.md) |  | [optional] 
**istio** | **bool** | Istio states whether it is an istio-monitored entity.  | [optional] 
**istio_authorization_policies** | [**list[IstioAuthorizationPolicy]**](IstioAuthorizationPolicy.md) | IstioAuthorizationPolicies are the Istio authorization policies.  | [optional] 
**k8s** | [**SharedProfileKubernetesData**](SharedProfileKubernetesData.md) |  | [optional] 
**label** | **str** | Label is the entity&#39;s label.  | [optional] 
**labels** | **list[str]** | Labels are the radar entity labels.  | [optional] 
**learning** | **bool** | Learning indicates whether the runtime profile associated with the entity is in learning state.  | [optional] 
**namespace** | **str** | Namespace is the kubernetes namespace the entity belongs to (for kubernetes type).  | [optional] 
**network_count** | **int** | .  | [optional] 
**processes_count** | **int** | .  | [optional] 
**profile_hash** | **int** | ProfileHash represents the profile hash It is allowed to contain up to uint32 numbers, and represented by int64 since mongodb does not support unsigned data types | [optional] 
**region** | **str** | Region is the cloud provider region.  | [optional] 
**resolved** | **bool** | Resolved indicates if the entity has all data resolved or just contains the ID and hash, used to indicate if the console should be updated on entity resolving.  | [optional] 
**service_ip** | **str** | ServiceIP the ip of the kubernetes service (for kubernetes type).  | [optional] 
**service_name** | **str** | ServiceName is kubernetes service the entity belongs to (for kubernetes type).  | [optional] 
**service_ports** | **list[int]** | ServicePorts are the ports the kubernetes service exposes (for kubernetes type).  | [optional] 
**subnet_connections** | [**SharedSubnetConnections**](SharedSubnetConnections.md) |  | [optional] 
**type** | [**SharedEntityType**](SharedEntityType.md) |  | [optional] 
**vulnerability_distribution** | [**VulnDistribution**](VulnDistribution.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



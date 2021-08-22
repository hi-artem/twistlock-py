# SharedContainerInfo

ContainerInfo contains all information gathered on a specific container

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_compliance** | [**VulnAllCompliance**](VulnAllCompliance.md) |  | [optional] 
**app** | **str** | App is the app that is hosted in the container.  | [optional] 
**cloud_metadata** | [**CommonCloudMetadata**](CommonCloudMetadata.md) |  | [optional] 
**cluster** | **str** | Cluster is the provided cluster name.  | [optional] 
**compliance_distribution** | [**VulnDistribution**](VulnDistribution.md) |  | [optional] 
**compliance_issues** | [**list[VulnVulnerability]**](VulnVulnerability.md) | ComplianceIssues are all the container compliance issues.  | [optional] 
**compliance_issues_count** | **int** | .  | [optional] 
**compliance_risk_score** | **float** | ComplianceRiskScore is the container&#39;s compliance risk score.  | [optional] 
**external_labels** | [**list[CommonExternalLabel]**](CommonExternalLabel.md) | ExternalLabels is the external labels e.g., kubernetes namespace labels.  | [optional] 
**id** | **str** | Id is the container id.  | [optional] 
**image** | **str** | Image is the canonical image name.  | [optional] 
**image_id** | **str** | ImageId is the image id.  | [optional] 
**image_name** | **str** | Deprecated: The image name as stated in the docker run command.  | [optional] 
**infra** | **bool** | Infra represents any container that belongs to the infrastructure.  | [optional] 
**installed_products** | [**SharedInstalledProducts**](SharedInstalledProducts.md) |  | [optional] 
**labels** | **list[str]** | Labels are the container labels (https://docs.docker.com/engine/userguide/labels-custom-metadata/).  | [optional] 
**name** | **str** | Name is the container name.  | [optional] 
**namespace** | **str** | Namespace is the k8s deployment namespace.  | [optional] 
**network** | [**SharedContainerNetwork**](SharedContainerNetwork.md) |  | [optional] 
**network_settings** | [**SharedDockerNetworkInfo**](SharedDockerNetworkInfo.md) |  | [optional] 
**processes** | [**list[SharedContainerProcess]**](SharedContainerProcess.md) | Processes are the processes that are running inside the container.  | [optional] 
**profile_id** | **str** | ProfileID is the container profile id.  | [optional] 
**size_bytes** | **int** | .  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



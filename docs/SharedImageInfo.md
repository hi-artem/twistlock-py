# SharedImageInfo

ImageInfo contains image information collected during image scan

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_compliance** | [**VulnAllCompliance**](VulnAllCompliance.md) |  | [optional] 
**applications** | [**list[VulnApplication]**](VulnApplication.md) | Products in the image.  | [optional] 
**base_image** | **str** | Image’s base image name. Used when filtering the vulnerabilities by base images.  | [optional] 
**binaries** | [**list[SharedBinary]**](SharedBinary.md) | Binaries in the image.  | [optional] 
**cloud_metadata** | [**CommonCloudMetadata**](CommonCloudMetadata.md) |  | [optional] 
**clusters** | **list[str]** | Cluster names.  | [optional] 
**compliance_distribution** | [**VulnDistribution**](VulnDistribution.md) |  | [optional] 
**compliance_issues** | [**list[VulnVulnerability]**](VulnVulnerability.md) | All the compliance issues.  | [optional] 
**compliance_issues_count** | **int** | Number of compliance issues.  | [optional] 
**compliance_risk_score** | **float** | Compliance risk score for the image.  | [optional] 
**creation_time** | **datetime** | Date/time when the image was created.  | [optional] 
**distro** | **str** | Full name of the distribution.  | [optional] 
**ecs_cluster_name** | **str** | ECS cluster name.  | [optional] 
**external_labels** | [**list[CommonExternalLabel]**](CommonExternalLabel.md) | Kubernetes external labels of all containers running this image.  | [optional] 
**files** | [**list[SharedFileDetails]**](SharedFileDetails.md) | Files in the container.  | [optional] 
**first_scan_time** | **datetime** | Date/time when this image was first scanned (preserved during version updates).  | [optional] 
**history** | [**list[SharedImageHistory]**](SharedImageHistory.md) | Docker image history.  | [optional] 
**host_devices** | [**list[CommonNetworkDeviceIP]**](CommonNetworkDeviceIP.md) | Map from host network device name to IP address.  | [optional] 
**id** | **str** | Image ID.  | [optional] 
**image** | [**SharedImage**](SharedImage.md) |  | [optional] 
**installed_products** | [**SharedInstalledProducts**](SharedInstalledProducts.md) |  | [optional] 
**k8s_cluster_addr** | **str** | Endpoint of the Kubernetes API server.  | [optional] 
**labels** | **list[str]** | Image labels.  | [optional] 
**layers** | **list[str]** | Image&#39;s filesystem layers. Each layer is a SHA256 digest of the filesystem diff See: https://windsock.io/explaining-docker-image-ids/.  | [optional] 
**missing_distro_vuln_coverage** | **bool** | Indicates if the image OS is covered in the IS (true) or not (false).  | [optional] 
**namespaces** | **list[str]** | k8s namespaces of all the containers running this image.  | [optional] 
**os_distro** | **str** | Name of the OS distribution.  | [optional] 
**os_distro_release** | **str** | OS distribution release.  | [optional] 
**os_distro_version** | **str** | OS distribution version.  | [optional] 
**package_manager** | **bool** | Indicates if the package manager is installed for the OS.  | [optional] 
**packages** | [**list[SharedPackages]**](SharedPackages.md) | Packages which exist in the image.  | [optional] 
**registry_namespace** | **str** | IBM cloud namespace to which the image belongs.  | [optional] 
**repo_digests** | **list[str]** | Digests of the image. Used for content trust (notary). Has one digest per tag.  | [optional] 
**repo_tag** | [**SharedImageTag**](SharedImageTag.md) |  | [optional] 
**risk_factors** | **dict(str, str)** | RiskFactors maps the existence of vulnerability risk factors | [optional] 
**scan_version** | **str** | Defender version that published the image.  | [optional] 
**startup_binaries** | [**list[SharedBinary]**](SharedBinary.md) | Binaries which are expected to run when the container is created from this image.  | [optional] 
**tags** | [**list[SharedImageTag]**](SharedImageTag.md) | Tags associated with the given image.  | [optional] 
**top_layer** | **str** | SHA256 of the image&#39;s last layer that is the last element of the Layers field.  | [optional] 
**twistlock_image** | **bool** | Indicates if the image is a Twistlock image (true) or not (false).  | [optional] 
**vulnerabilities** | [**list[VulnVulnerability]**](VulnVulnerability.md) | CVE vulnerabilities of the image.  | [optional] 
**vulnerabilities_count** | **int** | Total number of vulnerabilities.  | [optional] 
**vulnerability_distribution** | [**VulnDistribution**](VulnDistribution.md) |  | [optional] 
**vulnerability_risk_score** | **float** | Image&#39;s CVE risk score.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



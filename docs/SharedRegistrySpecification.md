# SharedRegistrySpecification

RegistrySpecification contains information for connecting to local/remote registry

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cap** | **int** | Specifies the maximum number of images from each repo to fetch and scan, sorted by most recently modified.  | [optional] 
**collections** | **list[str]** | Specifies the set of Defenders in-scope for working on a scan job.  | [optional] 
**credential** | [**CredCredential**](CredCredential.md) |  | [optional] 
**credential_id** | **str** | ID of the credentials in the credentials store to use for authenticating with the registry.  | [optional] 
**excluded_repositories** | **list[str]** | Repositories to exclude from scanning.  | [optional] 
**excluded_tags** | **list[str]** | Tags to exclude from scanning.  | [optional] 
**jfrog_repo_types** | [**list[SharedJFrogRepoType]**](SharedJFrogRepoType.md) | JFrog Artifactory repository types to scan.  | [optional] 
**namespace** | **str** | IBM Bluemix namespace https://console.bluemix.net/docs/services/Registry/registry_overview.html#registry_planning.  | [optional] 
**os** | [**SharedRegistryOSType**](SharedRegistryOSType.md) |  | [optional] 
**registry** | **str** | Registry address (e.g., https://gcr.io).  | [optional] 
**repository** | **str** | Repositories to scan.  | [optional] 
**scanners** | **int** | Number of Defenders that can be utilized for each scan job.  | [optional] 
**tag** | **str** | Tags to scan.  | [optional] 
**version** | **str** | Registry type. Determines the protocol Prisma Cloud uses to communicate with the registry.  | [optional] 
**version_pattern** | **str** | Pattern heuristic for quickly filtering images by tags without having to query all images for modification dates.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



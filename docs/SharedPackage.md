# SharedPackage

Package stores relevant package information

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binary_idx** | **list[int]** | Indexes of the top binaries which use the package.  | [optional] 
**binary_pkgs** | **list[str]** | Names of the distro binary packages (packages which are built on the source of the package).  | [optional] 
**cve_count** | **int** | Total number of CVEs for this specific package.  | [optional] 
**files** | [**list[SharedFileDetails]**](SharedFileDetails.md) | List of package-related files and their hashes. Only included when the appropriate scan option is set.  | [optional] 
**function_layer** | **str** | ID of the serverless layer in which the package was discovered.  | [optional] 
**layer_time** | **int** | Image layer to which the package belongs (layer creation time).  | [optional] 
**license** | **str** | License information for the package.  | [optional] 
**name** | **str** | Name of the package.  | [optional] 
**path** | **str** | Full package path (e.g., JAR or Node.js package path).  | [optional] 
**version** | **str** | Package version.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



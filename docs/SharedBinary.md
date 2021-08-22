# SharedBinary

Binary represents a detected binary file (ELF)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**altered** | **bool** | Indicates if the binary was installed from a package manager and modified/replaced (true) or not (false).  | [optional] 
**cve_count** | **int** | Total number of CVEs for this specific binary.  | [optional] 
**deps** | **list[str]** | Third-party package files which are used by the binary.  | [optional] 
**function_layer** | **str** | ID of the serverless layer in which the package was discovered.  | [optional] 
**md5** | **str** | Md5 hashset of the binary.  | [optional] 
**missing_pkg** | **bool** | Indicates if this binary is not related to any package (true) or not (false).  | [optional] 
**name** | **str** | Name of the binary.  | [optional] 
**path** | **str** | Relative path of the binary inside the container.  | [optional] 
**pkg_root_dir** | **str** | Path for searching packages used by the binary.  | [optional] 
**services** | **list[str]** | Name of services which use the binary.  | [optional] 
**version** | **str** | Version of the binary.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



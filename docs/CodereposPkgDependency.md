# CodereposPkgDependency

PkgDependency represents a required package

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dev_dependency** | **bool** | Indicates if this dependency is used only for the development of the package (true) or not (false).  | [optional] 
**last_resolved** | **datetime** | Date/time of the last version resolution. If the value is zero, it means the version is explicit and does not require resolving.  | [optional] 
**license_severity** | **str** | Maximum severity of the detected licenses according to the compliance policy.  | [optional] 
**licenses** | [**list[LicenseSPDXLicense]**](LicenseSPDXLicense.md) | Detected licenses of the dependant package.  | [optional] 
**name** | **str** | Package name that the dependency refers to.  | [optional] 
**raw_requirement** | **str** | Line in which the package is declared.  | [optional] 
**unsupported** | **bool** | Indicates if this package is unsupported by the remote package manager DB (e.g., due to a bad name or private package) (true) or not (false).  | [optional] 
**version** | **str** | Package version, either explicitly specified in a manifest or resolved by the scanner.  | [optional] 
**vulnerabilities** | [**list[VulnVulnerability]**](VulnVulnerability.md) | Vulnerabilities in the package.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# SharedScanSettings

ScanSettings are global settings for image/host/container and registry scanning

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_platforms_scan_period_ms** | **int** | CloudPlatformsScanPeriodMS is the cloud platforms scan period in ms - validated for minimum 1 hour or disabled with zero.  | [optional] 
**code_repos_scan_period_ms** | **int** | CodeReposScanPeriodMS is the code repository scan period in ms - validated for minimum 1 hour or disabled with zero.  | [optional] 
**containers_scan_period_ms** | **int** | ContainersScanPeriodMS is the container scan period in ms - validated for minimum 1 hour or disabled with zero.  | [optional] 
**extract_archive** | **bool** | ExtractArchive indicates whether to search within archive during scan is enabled.  | [optional] 
**images_scan_period_ms** | **int** | ImageScanPeriodMS is the image scan period in ms - validated for minimum 1 hour or disabled with zero.  | [optional] 
**include_js_dependencies** | **bool** | IncludeJsDependencies indicates whether to include packages from the \&quot;dependencies\&quot;.  | [optional] 
**registry_scan_period_ms** | **int** | RegistryScanPeriodMS is the registry scan period in ms - validated for minimum 1 hour or disabled with zero.  | [optional] 
**registry_scan_retention_days** | **int** | RegistryScanRetentionDays is the number of days to keep deleted registry images.  | [optional] 
**scan_running_images** | **bool** | ScanRunningImages indicates only images that are used by containers should be used.  | [optional] 
**serverless_scan_period_ms** | **int** | ServerlessScanPeriodMS is the serverless vulnerability scan period in ms - validated for minimum 1 hour or disabled with zero.  | [optional] 
**show_infra_containers** | **bool** | ShowInfraContainers indicates infra containers should be shown.  | [optional] 
**show_negligible_vulnerabilities** | **bool** | ShowNegligibleVulnerabilities indicates whether to display negligible vulnerabilities (low severity).  | [optional] 
**system_scan_period_ms** | **int** | SystemScanPeriodMS is the host scan period in ms - validated for minimum 1 hour or disabled with zero.  | [optional] 
**tas_droplets_scan_period_ms** | **int** | TASDropletsScanPeriodMS is the TAS scan period in ms - validated for minimum 1 hour or disabled with zero.  | [optional] 
**vm_scan_period_ms** | **int** | VMScanPeriodMS is the VM image scan period in ms - validated for minimum 1 hour or disabled with zero.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



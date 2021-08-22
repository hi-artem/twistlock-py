# TypesStatus

Status stores the status of a specific defender or for global features such as intelligence or LDAP

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id is the defender identifier if the status is per defender or the type for global statuses.  | [optional] 
**app_firewall** | [**DefenderFeatureStatus**](DefenderFeatureStatus.md) |  | [optional] 
**container** | [**DefenderScanStatus**](DefenderScanStatus.md) |  | [optional] 
**container_network_firewall** | [**DefenderFeatureStatus**](DefenderFeatureStatus.md) |  | [optional] 
**features** | [**DefenderFeatureStatus**](DefenderFeatureStatus.md) |  | [optional] 
**filesystem** | [**DefenderFeatureStatus**](DefenderFeatureStatus.md) |  | [optional] 
**host_auto_deploy** | [**TypesHostAutoDeployStatus**](TypesHostAutoDeployStatus.md) |  | [optional] 
**host_custom_compliance** | [**DefenderFeatureStatus**](DefenderFeatureStatus.md) |  | [optional] 
**host_network_firewall** | [**DefenderFeatureStatus**](DefenderFeatureStatus.md) |  | [optional] 
**image** | [**DefenderScanStatus**](DefenderScanStatus.md) |  | [optional] 
**intelligence** | [**TypesIntelligenceStatus**](TypesIntelligenceStatus.md) |  | [optional] 
**last_modified** | **datetime** | Datetime the status was last modified.  | [optional] 
**network** | [**DefenderFeatureStatus**](DefenderFeatureStatus.md) |  | [optional] 
**process** | [**DefenderFeatureStatus**](DefenderFeatureStatus.md) |  | [optional] 
**registry** | [**DefenderScanStatus**](DefenderScanStatus.md) |  | [optional] 
**runc** | [**DefenderFeatureStatus**](DefenderFeatureStatus.md) |  | [optional] 
**runtime** | [**DefenderFeatureStatus**](DefenderFeatureStatus.md) |  | [optional] 
**secrets** | [**TypesSecretsStatus**](TypesSecretsStatus.md) |  | [optional] 
**serverless_auto_deploy** | [**TypesServerlessAutoDeployStatus**](TypesServerlessAutoDeployStatus.md) |  | [optional] 
**serverless_radar** | [**TypesServerlessRadarStatus**](TypesServerlessRadarStatus.md) |  | [optional] 
**tas_droplets** | [**DefenderScanStatus**](DefenderScanStatus.md) |  | [optional] 
**type** | [**TypesStatusType**](TypesStatusType.md) |  | [optional] 
**upgrade** | [**DefenderUpgradeStatus**](DefenderUpgradeStatus.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TypesStats

Stats represents the status model that is stored in the DB

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id is the metric type.  | [optional] 
**access** | [**TypesAccessStats**](TypesAccessStats.md) |  | [optional] 
**app_embedded_app_firewall** | **dict(str, int)** | AppFirewallStats are the daily stats for app firewall audits TODO #20802 - replace string key with WAAS attack type type when mongo changed to avoid encoding map keys without stringer | [optional] 
**container** | [**TypesRuntimeStats**](TypesRuntimeStats.md) |  | [optional] 
**container_app_firewall** | **dict(str, int)** | AppFirewallStats are the daily stats for app firewall audits TODO #20802 - replace string key with WAAS attack type type when mongo changed to avoid encoding map keys without stringer | [optional] 
**container_network_firewall** | [**TypesNetworkFirewallStats**](TypesNetworkFirewallStats.md) |  | [optional] 
**host** | [**TypesRuntimeStats**](TypesRuntimeStats.md) |  | [optional] 
**host_app_firewall** | **dict(str, int)** | AppFirewallStats are the daily stats for app firewall audits TODO #20802 - replace string key with WAAS attack type type when mongo changed to avoid encoding map keys without stringer | [optional] 
**host_compliance_count** | **int** | HostComplianceCount is the host compliance count.  | [optional] 
**host_network_firewall** | [**TypesNetworkFirewallStats**](TypesNetworkFirewallStats.md) |  | [optional] 
**incidents_count** | **int** | IncidentsCount is the incidents count.  | [optional] 
**serverless** | [**TypesRuntimeStats**](TypesRuntimeStats.md) |  | [optional] 
**serverless_app_firewall** | **dict(str, int)** | AppFirewallStats are the daily stats for app firewall audits TODO #20802 - replace string key with WAAS attack type type when mongo changed to avoid encoding map keys without stringer | [optional] 
**time** | **int** | UnixTimestamp is the unix timestamp.  | [optional] 
**vulnerabilities** | [**TypesVulnerabilitiesStats**](TypesVulnerabilitiesStats.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



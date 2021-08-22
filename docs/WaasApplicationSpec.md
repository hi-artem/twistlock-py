# WaasApplicationSpec

ApplicationSpec is an application of a firewall instance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_spec** | [**WaasAPISpec**](WaasAPISpec.md) |  | [optional] 
**app_id** | **str** | Unique ID for the app.  | [optional] 
**attack_tools** | [**WaasProtectionConfig**](WaasProtectionConfig.md) |  | [optional] 
**ban_duration_minutes** | **int** | Ban duration, in minutes.  | [optional] 
**body** | [**WaasBodyConfig**](WaasBodyConfig.md) |  | [optional] 
**bot_protection_spec** | [**WaasBotProtectionSpec**](WaasBotProtectionSpec.md) |  | [optional] 
**certificate** | [**CommonSecret**](CommonSecret.md) |  | [optional] 
**clickjacking_enabled** | **bool** | Indicates whether clickjacking protection is enabled (true) or not (false).  | [optional] 
**cmdi** | [**WaasProtectionConfig**](WaasProtectionConfig.md) |  | [optional] 
**code_injection** | [**WaasProtectionConfig**](WaasProtectionConfig.md) |  | [optional] 
**csrf_enabled** | **bool** | Indicates whether Cross-Site Request Forgery (CSRF) protection is enabled (true) or not (false).  | [optional] 
**custom_block_response** | [**WaasCustomBlockResponseConfig**](WaasCustomBlockResponseConfig.md) |  | [optional] 
**custom_rules** | [**list[CustomrulesRef]**](CustomrulesRef.md) | List of custom runtime rules.  | [optional] 
**dos_config** | [**WaasDoSConfig**](WaasDoSConfig.md) |  | [optional] 
**header_specs** | [**list[WaasHeaderSpec]**](WaasHeaderSpec.md) | Configuration for inspecting HTTP headers.  | [optional] 
**intel_gathering** | [**WaasIntelGatheringConfig**](WaasIntelGatheringConfig.md) |  | [optional] 
**lfi** | [**WaasProtectionConfig**](WaasProtectionConfig.md) |  | [optional] 
**malformed_req** | [**WaasProtectionConfig**](WaasProtectionConfig.md) |  | [optional] 
**malicious_upload** | [**WaasMaliciousUploadConfig**](WaasMaliciousUploadConfig.md) |  | [optional] 
**network_controls** | [**WaasNetworkControls**](WaasNetworkControls.md) |  | [optional] 
**remote_host_forwarding** | [**WaasRemoteHostForwardingConfig**](WaasRemoteHostForwardingConfig.md) |  | [optional] 
**session_cookie_ban** | **bool** | Indicates if bans in this app are made by session cookie ID (true) or false (not).  | [optional] 
**session_cookie_enabled** | **bool** | Indicates if session cookies are enabled (true) or not (false).  | [optional] 
**shellshock** | [**WaasProtectionConfig**](WaasProtectionConfig.md) |  | [optional] 
**sqli** | [**WaasProtectionConfig**](WaasProtectionConfig.md) |  | [optional] 
**xss** | [**WaasProtectionConfig**](WaasProtectionConfig.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



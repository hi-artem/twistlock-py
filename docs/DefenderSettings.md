# DefenderSettings

Settings is an update request of the defender proxy settings.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admission_control_enabled** | **bool** | Indicates if the admission controller is enabled (true) or not (false).  | [optional] 
**admission_control_webhook_suffix** | **str** | Relative path to the admission control webhook HTTP endpoint.  | [optional] 
**automatic_upgrade** | **bool** | Indicates if Defenders should be automatically upgraded to the latest version (true) or not (false).  | [optional] 
**disconnect_period_days** | **int** | Number of consecutive days a Defender must remain disconnected for it to be considered decommissioned.  | [optional] 
**host_custom_compliance_enabled** | **bool** | Indicates if Defenders support host custom compliance checks (true) or not (false).  | [optional] 
**listening_port** | **int** | Port on which Defenders listen.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



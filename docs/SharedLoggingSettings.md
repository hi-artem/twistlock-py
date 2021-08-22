# SharedLoggingSettings

LoggingSettings are the logging settings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**console_address** | **str** | ConsoleAddress is the console address used by the admin to access the console, used for creating links for runtime events.  | [optional] 
**enable_metrics_collection** | **bool** | EnableMetricsCollection indicates whether metric collections feature is enabled.  | [optional] 
**include_runtime_link** | **bool** | IncludeRuntimeLink indicates whether link to forensic event should be included in the output.  | [optional] 
**stdout** | [**SharedLoggerSetting**](SharedLoggerSetting.md) |  | [optional] 
**syslog** | [**SharedSyslogSettings**](SharedSyslogSettings.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



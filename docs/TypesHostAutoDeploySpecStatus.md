# TypesHostAutoDeploySpecStatus

HostAutoDeploySpecStatus contains the discovery and deployment status for a particular host auto-deploy spec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**defended** | **int** | Defended is the number of already defended VMs.  | [optional] 
**discovered** | **int** | Discovered is the number of discovered unprodected VMs.  | [optional] 
**error** | **str** | Error is an error logged during the the auto-deploy scan (if occurred).  | [optional] 
**errors** | [**list[DeploymentCommandError]**](DeploymentCommandError.md) | Errors are the errors occurred in the command invocations.  | [optional] 
**failed** | **int** | Failed is the number of instances where deployment failed.  | [optional] 
**missing_permissions** | **int** | MissingPermissions is the number of instances in regions that the credential don&#39;t have permissions to them.  | [optional] 
**name** | **str** | Name is the spec name.  | [optional] 
**unsupported** | **int** | Unsupported is the number of instances with missing prerequisites.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



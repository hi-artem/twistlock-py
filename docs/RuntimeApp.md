# RuntimeApp

App represents the applications runtime data

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**listening_ports** | [**list[RuntimeHostProfileListeningPort]**](RuntimeHostProfileListeningPort.md) | ListeningPorts represents the applications listening ports.  | [optional] 
**name** | **str** | Name is the app name.  | [optional] 
**outgoing_ports** | [**list[RuntimeHostProfileOutgoingPort]**](RuntimeHostProfileOutgoingPort.md) | OutgoingPorts represents the applications outgoing ports.  | [optional] 
**processes** | [**list[RuntimeProfileProcess]**](RuntimeProfileProcess.md) | Processes is a list of the app&#39;s descendant processes.  | [optional] 
**startup_process** | [**RuntimeProfileProcess**](RuntimeProfileProcess.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



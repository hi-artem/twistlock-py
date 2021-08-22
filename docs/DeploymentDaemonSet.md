# DeploymentDaemonSet

DaemonSet holds information about deployed defender DaemonSet TODO #12377 - Implement Resource interface for collections filtering, after retrieving correct value to Cluster field

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Address is the kubernetes cluster address.  | [optional] 
**cluster** | **str** | Cluster is the kubernetes cluster name.  | [optional] 
**credential_id** | **str** | CredentialID is the name of the credential used.  | [optional] 
**defenders_version** | **str** | DefendersVersion is the version of the defenders deployed.  | [optional] 
**desired_defenders** | **int** | DesiredDefenders is the number of desired defenders.  | [optional] 
**error** | **str** | Error indicates any related errors found.  | [optional] 
**has_defender** | **bool** | HasDefender indicates if the cluster has at least one running defender.  | [optional] 
**region** | **str** | Region is the kubernetes cluster location region.  | [optional] 
**running_defenders** | **int** | RunningDefenders is the number of defenders running.  | [optional] 
**upgradable** | **bool** | Upgradable indicates if the cluster is upgradable.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



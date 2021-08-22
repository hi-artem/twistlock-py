# TypesDiscoveredVM

DiscoveredVM represents the information about the instance, fetched from the cloud compute interface

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID is the instance id. E.g. \&quot;i-5cd23551\&quot;.  | [optional] 
**account_id** | **str** | AccountID is the cloud provider account ID.  | [optional] 
**architecture** | **str** | Architecture is the architecture of the image.  | [optional] 
**arn** | **str** | The Amazon Resource Name (ARN) assigned to the instance.  | [optional] 
**collections** | **list[str]** | Collections is a list of the matched collections.  | [optional] 
**created_at** | **datetime** | CreatedAt is the time when the instance was launched.  | [optional] 
**fqdn** | **str** | FQDN is the host&#39;s fully qualified domain name . E.g. \&quot;ip-192-0-2-0.us-east-2.compute.internal\&quot;.  | [optional] 
**has_defender** | **bool** | HasDefender indicates that the instance has a defender installed on it.  | [optional] 
**hostname** | **str** | Hostname is the hostname. E.g. \&quot;ip-192-0-2-0\&quot; or \&quot;custom\&quot;.  | [optional] 
**image_id** | **str** | ImageID is the the ID of the AMI used to launch the instance. E.g. \&quot;ami-35501205\&quot;.  | [optional] 
**image_nameomitempty_name** | **str** | ImageName is the the name of the AMI used to launch the instance.  | [optional] 
**name** | **str** | Name is the instance name.  | [optional] 
**os** | **str** | OS is the Operating System installed on the instance.  | [optional] 
**provider** | [**CommonCloudProvider**](CommonCloudProvider.md) |  | [optional] 
**region** | **str** | Region is the region the VM is located at.  | [optional] 
**tags** | [**list[CommonExternalLabel]**](CommonExternalLabel.md) | Tags are the tags of the VM instance.  | [optional] 
**timestamp** | **datetime** | Timestamp is the time in which the instance info was fetched.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



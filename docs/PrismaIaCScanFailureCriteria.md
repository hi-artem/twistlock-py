# PrismaIaCScanFailureCriteria

IaCScanFailureCriteria is the IaC scan failure criteria in prisma convention See async scan POST section in https://redlock.atlassian.net/wiki/spaces/PSA/pages/1796736090/All-in-one+IaC+Service+2.0+MVP

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**high** | **int** | High is the minimal number of high compliance issues that would fail the scan.  | [optional] 
**low** | **int** | Low is the minimal number of low compliance issues that would fail the scan.  | [optional] 
**medium** | **int** | Medium is the minimal number of medium compliance issues that would fail the scan.  | [optional] 
**operator** | **str** | Operator is the logical operator (and/or) for defining when the scan should fail given the above numbers.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



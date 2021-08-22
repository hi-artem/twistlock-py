# WaasAPIRequest

APIRequest represents a single API request and its data

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** | AppID is the application ID to which this request belongs.  | [optional] 
**content_type** | **str** | ContentType is the request content type.  | [optional] 
**method** | **str** | Method is the HTTP Method of the API request.  | [optional] 
**path** | **str** | Path is the path of the API request.  | [optional] 
**query_parameters** | **list[str]** | QueryParameters are the query parameters of the API request.  | [optional] 
**response_content_type** | **str** | ResponseContentType is the response content type.  | [optional] 
**server** | **str** | Server is the destination Server (including port and schema) of the API request.  | [optional] 
**source_ip** | **str** | SourceIP is the source IP of the API request.  | [optional] 
**status_code** | **int** | StatusCode is the response status code.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



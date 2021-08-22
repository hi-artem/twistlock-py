# WaasEndpoint

Endpoint is an application endpoint

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_path** | **str** | Base path for the endpoint.  | [optional] 
**exposed_port** | **int** | Exposed port that the proxy is listening on.  | [optional] 
**host** | **str** | URL address (name or IP) of the endpoint&#39;s API specification (e.g., petstore.swagger.io). The address can be prefixed with a wildcard (e.g., *.swagger.io).  | [optional] 
**http2** | **bool** | Indicates if the proxy supports HTTP/2 (true) or not (false).  | [optional] 
**internal_port** | **int** | Internal port that the application is listening on.  | [optional] 
**tls** | **bool** | Indicates if the connection is secured (true) or not (false).  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



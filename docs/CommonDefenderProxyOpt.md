# CommonDefenderProxyOpt

DefenderProxyOpt holds options for defender proxy configuration It embeds ProxySettings but override it's Password field with a simple string This is needed in order to avoid Secret's MarshalJSON method, which depends on existence of master key file

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca** | **str** | Proxy&#39;s CA for Defender to trust. Required when using TLS intercept proxies.  | [optional] 
**http_proxy** | **str** | Proxy address.  | [optional] 
**no_proxy** | **str** | List of addresses for which the proxy should not be used.  | [optional] 
**password** | **str** | .  | [optional] 
**user** | **str** | Username to authenticate with the proxy.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



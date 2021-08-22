# SharedCodeRepoSpecification

CodeRepoSpecification is a specification for scanning specific repositories

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential_id** | **str** | ID of the credentials in the credentials store to use for authenticating with the code repo service provider.  | [optional] 
**excluded_manifest_paths** | **list[str]** | Paths in the repository the scanner ignores when looking for manifest files to evaluate.  | [optional] 
**explicit_manifest_names** | **list[str]** | Additional manifest files for the scanner to evaluate. Explicitly specify manifest filenames when you use non-standard naming schemes. (e.g., prod-requirements.txt).  | [optional] 
**public_only** | **bool** | Indicates whether this specification is meant for (unauthenticated) public-only scanning (true) or private as well (false).  | [optional] 
**repositories** | **list[str]** | Repository names to scan. The format is &lt;owner&gt;/&lt;repo_name&gt;.  | [optional] 
**target_python_version** | **str** | Python version to consider when resolving Python dependencies. The default value is the latest version.  | [optional] 
**type** | [**SharedCodeRepoProviderType**](SharedCodeRepoProviderType.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



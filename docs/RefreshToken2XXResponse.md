# RefreshToken2XXResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | The new Org Access Token. | [optional] 
**token_type** | **str** | The type of the tokens, which is Bearer. | [optional] 
**scope** | **str** | The scope of the Org Access Token to limit the app&#39;s access to the organization&#39;s resources. **Note**: Currently this property value is empty. The scope of the Org Access Token is based on the permissions granted when the app user installs the app.  | [optional] 
**expires_in** | **int** | The time in seconds in which the new Org Access Token expires. | [optional] 
**refresh_token** | **str** | The Refresh Token, used to obtain another Org Access Token when the new Org Access Token expires. The expiration time for Refresh Tokens is currently set to 30 days and is subject to change. | [optional] 

## Example

```python
from cobo_waas2.models.refresh_token2_xx_response import RefreshToken2XXResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RefreshToken2XXResponse from a JSON string
refresh_token2_xx_response_instance = RefreshToken2XXResponse.from_json(json)
# print the JSON string representation of the object
print(RefreshToken2XXResponse.to_json())

# convert the object into a dict
refresh_token2_xx_response_dict = refresh_token2_xx_response_instance.to_dict()
# create an instance of RefreshToken2XXResponse from a dict
refresh_token2_xx_response_from_dict = RefreshToken2XXResponse.from_dict(refresh_token2_xx_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



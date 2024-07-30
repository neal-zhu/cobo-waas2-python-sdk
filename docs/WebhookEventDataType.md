# WebhookEventDataType

The data type of the event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type** | **str** | The data type of the event. When &#x60;data_type&#x60; is &#x60;Transaction&#x60;, it means the event uses the &#x60;transaction&#x60; schema as its data type. | 

## Example

```python
from cobo_waas2.models.webhook_event_data_type import WebhookEventDataType

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookEventDataType from a JSON string
webhook_event_data_type_instance = WebhookEventDataType.from_json(json)
# print the JSON string representation of the object
print(WebhookEventDataType.to_json())

# convert the object into a dict
webhook_event_data_type_dict = webhook_event_data_type_instance.to_dict()
# create an instance of WebhookEventDataType from a dict
webhook_event_data_type_from_dict = WebhookEventDataType.from_dict(webhook_event_data_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


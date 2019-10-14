# openapi_client.AdminApi

All URIs are relative to *http://localhost:2010/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_action**](AdminApi.md#admin_action) | **GET** /admin/{action} | for admin actions


# **admin_action**
> admin_action(action)

for admin actions

for admin actions

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AdminApi()
action = 'action_example' # str | action to perform

try:
    # for admin actions
    api_instance.admin_action(action)
except ApiException as e:
    print("Exception when calling AdminApi->admin_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | **str**| action to perform | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successfull operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


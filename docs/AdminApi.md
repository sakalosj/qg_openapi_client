# swagger_client.AdminApi

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
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdminApi()
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


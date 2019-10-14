# swagger_client.ScanApi

All URIs are relative to *http://localhost:2010/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_scan**](ScanApi.md#create_scan) | **POST** /scan | Create scan
[**get_scan**](ScanApi.md#get_scan) | **GET** /scan/{scanId} | Get user by id

# **create_scan**
> create_scan(body=body)

Create scan

Create scan

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScanApi()
body = swagger_client.Scan() # Scan | Scan data to be created (optional)

try:
    # Create scan
    api_instance.create_scan(body=body)
except ApiException as e:
    print("Exception when calling ScanApi->create_scan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Scan**](Scan.md)| Scan data to be created | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scan**
> Scan get_scan(scan_id)

Get user by id

Get user by id - description

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScanApi()
scan_id = 789 # int | ID of scan

try:
    # Get user by id
    api_response = api_instance.get_scan(scan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanApi->get_scan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scan_id** | **int**| ID of scan | 

### Return type

[**Scan**](Scan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


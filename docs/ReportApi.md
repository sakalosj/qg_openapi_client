# swagger_client.ReportApi

All URIs are relative to *http://localhost:2010/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_report**](ReportApi.md#create_report) | **POST** /report | Create report
[**get_report**](ReportApi.md#get_report) | **GET** /report/{reportId} | Get report by id

# **create_report**
> create_report(body=body)

Create report

Create Report

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportApi()
body = swagger_client.Report() # Report | Data for report genration (optional)

try:
    # Create report
    api_instance.create_report(body=body)
except ApiException as e:
    print("Exception when calling ReportApi->create_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Report**](Report.md)| Data for report genration | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report**
> Report get_report(report_id)

Get report by id

Get report by id - description

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportApi()
report_id = 789 # int | ID of scan

try:
    # Get report by id
    api_response = api_instance.get_report(report_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportApi->get_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **int**| ID of scan | 

### Return type

[**Report**](Report.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


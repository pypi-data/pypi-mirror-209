
# Getting Started with TesterS

## Introduction

Testing various
api
features

## Install the Package

The package is compatible with Python versions `3 >=3.7, <= 3.11`.
Install the package from PyPi using the following pip command:

```python
pip install tester-stripped-mhr==0.0.1
```

You can also view the package at:
https://pypi.python.org/pypi/tester-stripped-mhr/0.0.1

## Test the SDK

You can test the generated SDK and the server with test cases. `unittest` is used as the testing framework and `pytest` is used as the test runner. You can run the tests as follows:

Navigate to the root directory of the SDK and run the following commands

```
pip install -r test-requirements.txt
pytest
```

## Initialize the API Client

**_Note:_** Documentation for the client can be found [here.](doc/client.md)

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| `port` | `string` | *Default*: `'80'` |
| `suites` | `SuiteCode` | *Default*: `1` |
| `environment` | Environment | The API environment. <br> **Default: `Environment.TESTING`** |
| `http_client_instance` | `HttpClient` | The Http Client passed from the sdk user for making requests |
| `override_http_client_configuration` | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| `http_call_back` | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| `timeout` | `float` | The value to use for connection timeout. <br> **Default: 60** |
| `max_retries` | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| `backoff_factor` | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| `retry_statuses` | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| `retry_methods` | `Array of string` | The http methods on which retry is to be done. <br> **Default: ['GET', 'PUT']** |

The API client can be initialized as follows:

```python
from testers.testers_client import TestersClient
from testers.configuration import Environment

client = TestersClient()
```

## Environments

The SDK can be configured to use a different environment for making API calls. Available environments are:

### Fields

| Name | Description |
|  --- | --- |
| production | - |
| testing | **Default** |

## API Errors

Here is the list of errors that the API might throw.

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | 400 Global | `APIException` |
| 402 | 402 Global | `APIException` |
| 403 | 403 Global | `APIException` |
| 404 | 404 Global | `APIException` |
| 412 | Precondition Failed | [`NestedModelException`](doc/models/nested-model-exception.md) |
| 500 | 500 Global | [`GlobalTestException`](doc/models/global-test-exception.md) |
| Default | Invalid response. | [`GlobalTestException`](doc/models/global-test-exception.md) |

## List of APIs

* [Response Types](doc/controllers/response-types.md)
* [Form Params](doc/controllers/form-params.md)
* [Body Params](doc/controllers/body-params.md)
* [Error Codes](doc/controllers/error-codes.md)
* [Query Param](doc/controllers/query-param.md)
* [Echo](doc/controllers/echo.md)
* [Header](doc/controllers/header.md)
* [Template Params](doc/controllers/template-params.md)

## Classes Documentation

* [Utility Classes](doc/utility-classes.md)
* [HttpResponse](doc/http-response.md)
* [HttpRequest](doc/http-request.md)


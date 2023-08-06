
# Getting Started with JsonValueTester

## Introduction

Testing Special JsonValue feature

## Install the Package

The package is compatible with Python versions `3 >=3.7, <= 3.11`.
Install the package from PyPi using the following pip command:

```python
pip install asad-14-json-generator==0.1.2
```

You can also view the package at:
https://pypi.python.org/pypi/asad-14-json-generator/0.1.2

## Test the SDK

You can test the generated SDK and the server with test cases. `unittest` is used as the testing framework and `pytest` is used as the test runner. You can run the tests as follows:

Navigate to the root directory of the SDK and run the following commands

```
pip install -r test-requirements.txt
pytest
```

## Initialize the API Client

**_Note:_** Documentation for the client can be found [here.](https://www.github.com/asadali-14/python-json-generator/tree/0.1.2/doc/client.md)

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| `environment` | Environment | The API environment. <br> **Default: `Environment.TESTING`** |
| `http_client_instance` | `HttpClient` | The Http Client passed from the sdk user for making requests |
| `override_http_client_configuration` | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| `http_call_back` | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| `timeout` | `float` | The value to use for connection timeout. <br> **Default: 60** |
| `max_retries` | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 3** |
| `backoff_factor` | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| `retry_statuses` | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| `retry_methods` | `Array of string` | The http methods on which retry is to be done. <br> **Default: ['GET', 'PUT']** |

The API client can be initialized as follows:

```python
from jsonvaluetester.jsonvaluetester_client import JsonvaluetesterClient
from jsonvaluetester.configuration import Environment

client = JsonvaluetesterClient()
```

## Environments

The SDK can be configured to use a different environment for making API calls. Available environments are:

### Fields

| Name | Description |
|  --- | --- |
| production | - |
| testing | **Default** |

## List of APIs

* [Json Obj](https://www.github.com/asadali-14/python-json-generator/tree/0.1.2/doc/controllers/json-obj.md)
* [Json Val](https://www.github.com/asadali-14/python-json-generator/tree/0.1.2/doc/controllers/json-val.md)

## Classes Documentation

* [Utility Classes](https://www.github.com/asadali-14/python-json-generator/tree/0.1.2/doc/utility-classes.md)
* [HttpResponse](https://www.github.com/asadali-14/python-json-generator/tree/0.1.2/doc/http-response.md)
* [HttpRequest](https://www.github.com/asadali-14/python-json-generator/tree/0.1.2/doc/http-request.md)


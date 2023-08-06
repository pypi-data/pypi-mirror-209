
# Getting Started with Verizon 5G MEC VNSP API

## Introduction

The API helps manage or use MEC platform hosted services.

## Install the Package

The package is compatible with Python versions `3 >=3.7, <= 3.11`.
Install the package from PyPi using the following pip command:

```python
pip install Apiamtic-python==1.6.9
```

You can also view the package at:
https://pypi.python.org/pypi/Apiamtic-python/1.6.9

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
| `vz_m_2_m_token` | `string` | M2M Session Token |
| `environment` | Environment | The API environment. <br> **Default: `Environment.PRODUCTION`** |
| `http_client_instance` | `HttpClient` | The Http Client passed from the sdk user for making requests |
| `override_http_client_configuration` | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| `http_call_back` | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| `timeout` | `float` | The value to use for connection timeout. <br> **Default: 60** |
| `max_retries` | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| `backoff_factor` | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| `retry_statuses` | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| `retry_methods` | `Array of string` | The http methods on which retry is to be done. <br> **Default: ['GET', 'PUT']** |
| `o_auth_client_id` | `string` | OAuth 2 Client ID |
| `o_auth_client_secret` | `string` | OAuth 2 Client Secret |
| `o_auth_token` | `OAuthToken` | Object for storing information about the OAuth token |
| `o_auth_scopes` | `OAuthScopeEnum` |  |

The API client can be initialized as follows:

```python
from verizon5gmecvnspapi.verizon_5_gmecvnspapi_client import Verizon5gmecvnspapiClient
from verizon5gmecvnspapi.configuration import Environment

client = Verizon5gmecvnspapiClient(
    vz_m_2_m_token='VZ-M2M-Token',
    o_auth_client_id='OAuthClientId',
    o_auth_client_secret='OAuthClientSecret',
    o_auth_scopes=[OAuthScopeEnum.TS_MEC_FULLACCESS]
)
```

## Environments

The SDK can be configured to use a different environment for making API calls. Available environments are:

### Fields

| Name | Description |
|  --- | --- |
| Production | **Default** |
| Staging | - |

## Authorization

This API uses `OAuth 2 Client Credentials Grant`.

## Client Credentials Grant

Your application must obtain user authorization before it can execute an endpoint call in case this SDK chooses to use *OAuth 2.0 Client Credentials Grant*. This authorization includes the following steps

The `fetch_token()` method will exchange the OAuth client credentials for an *access token*. The access token is an object containing information for authorizing client requests and refreshing the token itself.

You must have initialized the client with [scopes]($h//Scopes) for which you need permission to access.

```python
try:
    client.auth_managers['global'].fetch_token()
except OAuthProviderException as ex:
    # handle exception
except APIException as ex:
    # handle exception
```

The client can now make authorized endpoint calls.

### Scopes

Scopes enable your application to only request access to the resources it needs while enabling users to control the amount of access they grant to your application. Available scopes are defined in the `OAuthScopeEnum` enumeration.

| Scope Name | Description |
|  --- | --- |
| `TS_MEC_FULLACCESS` | full access to all VNSP APIs |

### Storing an access token for reuse

It is recommended that you store the access token for reuse.

```python
# store token
save_token_to_database(client.config.o_auth_token)
```

### Creating a client from a stored token

To authorize a client from a stored access token, just set the access token in Configuration along with the other configuration parameters before creating the client:

```python
client = Verizon5gmecvnspapiClient()
client.config.o_auth_token = load_token_from_database()
```

### Complete example

```python
from verizon5gmecvnspapi.verizon_5_gmecvnspapi_client import Verizon5gmecvnspapiClient
from verizon5gmecvnspapi.models.o_auth_scope_enum import OAuthScopeEnum
from verizon5gmecvnspapi.exceptions.o_auth_provider_exception import OAuthProviderException

from verizon5gmecvnspapi.exceptions.api_exception import APIException

# function for storing token to database
def save_token_to_database(o_auth_token):
    # code to save the token to database

# function for loading token from database
def load_token_from_database():
    # load token from database and return it (return None if no token exists)
    pass

from verizon5gmecvnspapi.verizon_5_gmecvnspapi_client import Verizon5gmecvnspapiClient
from verizon5gmecvnspapi.configuration import Environment

client = Verizon5gmecvnspapiClient(
    vz_m_2_m_token='VZ-M2M-Token',
    o_auth_client_id='OAuthClientId',
    o_auth_client_secret='OAuthClientSecret',
    o_auth_scopes=[OAuthScopeEnum.TS_MEC_FULLACCESS]
)
# obtain access token, needed for client to be authorized
previous_token = load_token_from_database()
if previous_token:
    # restore previous access token
    config = client.config.clone_with(o_auth_token=previous_token)
    client = Verizon5gmecvnspapiClient(config)
else:
    # obtain new access token
    try:
        token = client.auth_managers['global'].fetch_token()
        save_token_to_database(token)
        config = client.config.clone_with(o_auth_token=token)
        client = Verizon5gmecvnspapiClient(config)
    except OAuthProviderException as ex:
        # handle exception
    except APIException as ex:
        # handle exception

# the client is now authorized and you can use controllers to make endpoint calls
```

## List of APIs

* [Service Onboarding](doc/controllers/service-onboarding.md)
* [Service Metadata](doc/controllers/service-metadata.md)
* [CSP Profiles](doc/controllers/csp-profiles.md)
* [Service Claims](doc/controllers/service-claims.md)
* [O Auth Authorization](doc/controllers/o-auth-authorization.md)
* [Repositories](doc/controllers/repositories.md)

## Classes Documentation

* [Utility Classes](doc/utility-classes.md)
* [HttpResponse](doc/http-response.md)
* [HttpRequest](doc/http-request.md)


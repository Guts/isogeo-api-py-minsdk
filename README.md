# Isogeo API Python SDK

![PyPI](https://img.shields.io/pypi/v/isogeo-pysdk.svg) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/isogeo-pysdk.svg)

[![Build Status](https://travis-ci.org/isogeo/isogeo-api-py-minsdk.svg?branch=master)](https://travis-ci.org/isogeo/isogeo-api-py-minsdk) [![Build Status](https://dev.azure.com/isogeo/Python%20SDK/_apis/build/status/isogeo.isogeo-api-py-minsdk?branchName=master)](https://dev.azure.com/isogeo/Python%20SDK/_build/latest?definitionId=3&branchName=master) [![codecov](https://codecov.io/gh/isogeo/isogeo-api-py-minsdk/branch/master/graph/badge.svg)](https://codecov.io/gh/isogeo/isogeo-api-py-minsdk)

[![Documentation Status](https://readthedocs.org/projects/isogeo-api-pysdk/badge/?version=latest)](https://isogeo-api-pysdk.readthedocs.io/en/latest/?badge=latest)

A Python package to use Isogeo REST API.

## Requirements

Isogeo API requires oAuth2 authentication. To obtain credentials, send us your request by email [projects+api@isogeo.com](mailto:projects+api@isogeo.com).

Based on the well known [`requests`](https://github.com/requests/requests) package.

## Documentation

- [Package manual and autogenerated modules doc](https://isogeo-api-pysdk.readthedocs.io)
- [Isogeo API](http://help.isogeo.com/api/)
- [Contribution guidelines](/wiki)

## Usage in a nutshell

```python
pip install --user isogeo-pysdk
# using pipenv
pipenv install isogeo-pysdk
```

### Quickstart

```python
from isogeo_pysdk import Isogeo

# authenticate your client application
isogeo = Isogeo(client_id=app_id,
                client_secret=app_secret)

# get the token
token = isogeo.connect()

# search within catalogs shared to the application
search = isogeo.search(token)

# print some statements
print("Search __dict__ keys: ", search.keys())  # search response basic structure
print("Search query parameters: ", search.get('query'))  # search response query passed
print("Total count of metadatas shared: ", search.get("total"))  # total of available resources
print("Count of resources got by request: {}\n".format(len(search.get("results"))))  # total of resources returned by search request
```

Samples are available in `the source repository <https://github.com/isogeo/isogeo-api-py-minsdk/tree/master/isogeo_pysdk/samples>`_.

### Tests

Tests are performed for each published commit:

- by [Travis](https://travis-ci.org/isogeo/isogeo-api-py-minsdk)
- by [Azure Pipelines](https://dev.azure.com/isogeo/Python%20SDK/_build)

```python
pip install --upgrade -r tests/requirements_test.txt
python -m unittest discover
```

Or using the [included Powershell script](https://github.com/isogeo/isogeo-api-py-minsdk/blob/master/tool_test_coverage.ps1):

```powershell
.\tool_test_coverage.ps1
```

#### Coverage

Test coverage is published on [codecov.io](https://codecov.io/gh/isogeo/isogeo-api-py-minsdk).

### Build

To package and upload:

```powershell
.\tool_build_upload.ps1
```

To build docs:

```powershell
.\tool_docs_build.ps1
```
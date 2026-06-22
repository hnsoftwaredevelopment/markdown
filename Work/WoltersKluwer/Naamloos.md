

# Azure Devops

Documentation how to connect from differen environments (Python): [https://docs.microsoft.com/en-us/rest/api/azure/devops/?view=azure-devops-rest-5.1#client-libraries](https://docs.microsoft.com/en-us/rest/api/azure/devops/?view=azure-devops-rest-5.1#client-libraries)

Documentation on Azure Res Api: [https://docs.microsoft.com/en-us/rest/api/azure/devops/?view=azure-devops-rest-5.1](https://docs.microsoft.com/en-us/rest/api/azure/devops/?view=azure-devops-rest-5.1)

## Example files on GitHub
[https://github.com/Microsoft/azure-devops-python-samples](https://github.com/Microsoft/azure-devops-python-samples) 

## Example strings

GET https://dev.azure.com/{organization}/{project}/_apis/build/builds/{buildId}?api-version=5.0

[https://dev.azure.com/WK-NL-TAA-Alure/Alure/_apis/build/latest/Ci-Projections?branchName=master&api-version=5.0-preview.1](https://dev.azure.com/WK-NL-TAA-Alure/Alure/_apis/build/latest/Ci-Projections?branchName=master&api-version=5.0-preview.1)

## PA Token:

aof64no7miwysurzbhmeq324gf4sy3vl736t5yl52ajlaljtequq

# Connect to DevOps with Python

```python  
from azure.devops.connection import Connection  
from msrest.authentication import BasicAuthentication  
import pprint  
  
URL = 'https://dev.azure.com/WK-NL-TAA-Alure/Alure/_apis/build/latest/Ci-Projections?branchName=master&api-version=5.0-preview.1 '  
  
# Fill in with your personal access token and org URL  
personal\_access\_token = 'aof64no7miwysurzbhmeq324gf4sy3vl736t5yl52ajlaljtequq'  
organization_url = 'https://dev.azure.com/WK-NL-TAA-Alure'  
  
# Create a connection to the org  
credentials = BasicAuthentication('', personal\_access\_token)  
connection = Connection(base_url=organization_url, creds=credentials)  
  
# Get a client (the "core" client provides access to projects, teams, etc)  
core_client = connection.clients.get\_core\_client()  
  
# Get the first page of projects  
```python
get\_projects\_response = core_client.get_projects()  
index = 0  
while get\_projects\_response is not None:  
 for project in get\_projects\_response.value:  
  pprint.pprint("\[" \+ str(index) \+ "\] " \+ project.name)  
        index += 1  
  if get\_projects\_response.continuation_token is not None and get\_projects\_response.continuation_token != "":  
  \# Get the next page of projects  
  get\_projects\_response = core_client.get_projects(continuation_token=get\_projects\_response.continuation_token) else:  
  \# All projects have been retrieved  
  get\_projects\_response = None  
```  
  
[!\[Python package\](https://github.com/microsoft/azure-devops-python-api/workflows/Python%20package/badge.svg)\](https://github.com/microsoft/azure-devops-python-api/actions)
\[!\[Build Status\](https://dev.azure.com/mseng/vsts-cli/\_apis/build/status/vsts-python-api?branchName=dev)\](https://dev.azure.com/mseng/vsts-cli/\_build/latest?definitionId=5904&branchName=dev)
\[!\[Python\](https://img.shields.io/pypi/pyversions/azure-devops.svg)\](https://pypi.python.org/pypi/azure-devops)

# Azure DevOps Python API

This repository contains Python APIs for interacting with and managing Azure DevOps. These APIs power the Azure DevOps Extension for Azure CLI. To learn more about the Azure DevOps Extension for Azure CLI, visit the \[Microsoft/azure-devops-cli-extension\](https://github.com/Microsoft/azure-devops-cli-extension) repo.

## Install 

```
pip install azure-devops
```

## Get started


To use the API, establish a connection using a \[personal access token\](https://docs.microsoft.com/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=vsts) and the URL to your Azure DevOps organization. Then get a client from the connection and make API calls.

```python
from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
import pprint

# Fill in with your personal access token and org URL
personal\_access\_token = 'YOURPAT'
organization_url = 'https://dev.azure.com/YOURORG'

# Create a connection to the org
credentials = BasicAuthentication('', personal\_access\_token)
connection = Connection(base\_url=organization\_url, creds=credentials)

# Get a client (the "core" client provides access to projects, teams, etc)
core\_client = connection.clients.get\_core_client()

# Get the first page of projects
get\_projects\_response = core\_client.get\_projects()
index = 0
while get\_projects\_response is not None:
    for project in get\_projects\_response.value:
        pprint.pprint("\[" + str(index) + "\] " + project.name)
        index += 1
    if get\_projects\_response.continuation\_token is not None and get\_projects\_response.continuation\_token != "":
        # Get the next page of projects
        get\_projects\_response = core\_client.get\_projects(continuation\_token=get\_projects\_response.continuation\_token)
    else:
        # All projects have been retrieved
        get\_projects\_response = None
```

## API documentation

This Python library provides a thin wrapper around the Azure DevOps REST APIs. See the \[Azure DevOps REST API reference\](https://docs.microsoft.com/en-us/rest/api/azure/devops/?view=azure-devops-rest-5.1) for details on calling different APIs.

## Samples

Learn how to call different APIs by viewing the samples in the \[Microsoft/azure-devops-python-samples\](https://github.com/Microsoft/azure-devops-python-samples) repo.

## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.microsoft.com.

When you submit a pull request, a CLA-bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., label, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the \[Microsoft Open Source Code of Conduct\](https://opensource.microsoft.com/codeofconduct/).
For more information see the \[Code of Conduct FAQ\](https://opensource.microsoft.com/codeofconduct/faq/) or
contact \[opencode@microsoft.com\](mailto:opencode@microsoft.com) with any additional questions or comments.
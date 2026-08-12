Jira_releases

# Werken met het releaseschema in Jira

```python
from jira import JIRA
import json

jiraURL = 'https://twinfield.atlassian.net'
jiraUserName = 'hnijkamp'
jiraPassword = 'Hn2017!'
jiraProject = 'ALURE'
jiraIssue = 'ALURE-25217'
jiraParentIssue = ''
jiraTaskIssue = ''

options = {'server': jiraURL}
jira = JIRA(options, basic_auth=(jiraUserName, jiraPassword))
#issue = jira.issue(jiraIssue)
projects = jira.project('ALURE')

#print(projects.issuetype)
#print(jira.project_roles('ALURE'))
versions = jira.project_versions('ALURE')
#Store dictionary in list
[v.name for v in reversed(versions)]

for name in reversed(versions):
    if name.archived == True:
        status = 'Archived'
    elif name.released == True:
        status = 'Released'
    else:
        status = 'Unreleased'

    print('Name: ', name, 'Releasedate: ', name.releaseDate, '*** ', status, ' ***')
```


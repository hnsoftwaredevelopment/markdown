How_to_link_a_issues_to_other_issues_(as_blocks)

# How to link a issues to other issues (as blocks)

```Python
from jira import JIRA

options = {
    'server': 'https://jira.atlassian.com'
}
jira = JIRA(options)

issue = jira.issue('JRA-1330')
issue2 = jira2.issue('XX-23')
jira.create_issue_link('Blocks',issue, issue2)
```

## Or use REST API to add issue links in JIRA issues

When **Creating** an issue]
* Make sure Linked Issues is added to the appropriate Create Issue screen
* Run POST /rest/api/2/issue using the following JSON data
```Python
{
   "fields":{
      "project":{
         "key":"TEST"
      },
      "summary":"test bug summary",
      "description":"test bug description",
      "issuetype":{
         "name":"Bug"
      },
      "priority":{
         "name":"Major"
      }
   },
   "update":{
      "issuelinks":[
         {
            "add":{
               "type":{
                  "name":"Blocks",
                  "inward":"is blocked by",
                  "outward":"blocks"
               },
               "outwardIssue":{
                  "key":"TEST-1"
               }
            }
         }
      ]
   }
}
```

## When **Editing** an issue

* Make sure Linked Issues is added to the appropriate Create Issue screen
* Run PUT /rest/api/2/issue/{issueIdOrKey} using the following JSON data

```Python
{
   "update":{
      "issuelinks":[
         {
            "add":{
               "type":{
                  "name":"Blocks",
                  "inward":"is blocked by",
                  "outward":"blocks"
               },
               "outwardIssue":{
                  "key":"TEST-1"
               }
            }
         }
      ]
   }
}
```
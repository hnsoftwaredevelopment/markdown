Create_Subtasks_Jira

# How to create subtasks with jira-python?

How does one create subtasks with the jira-python library ?

 

The trick is that parent id is not the issue id, but the issue key and subtype has to be 'Sub-task'

For example:

```python
rootnn_dict = {
     'project' : { 'key': 'JBIDE' },
     'summary' : 'Test auto created issue',
     'description' : 'Ignore this. will be deleted shortly',
     'issuetype' : { 'name' : 'Task' },
     }

rootnn = jira.create_issue(fields=rootnn_dict)

print("created " + rootnn.key)

rootnn_dict = {
     'project' : { 'key': 'JBIDE' },
     'summary' : 'Test child auto created issue',
     'description' : 'Ignore this child. will be deleted shortly',
     'issuetype' : { 'name' : 'Sub-task' },
     'parent' : { 'id' : rootnn.key},
     }

child = jira.create_issue(fields=rootnn_dict)

print("created child: " + child.key)
```



See [https://answers.atlassian.com/questions/49433/creating-sub-task-of-an-issue-using-rest-api](https://community.atlassian.com/questions/49433/creating-sub-task-of-an-issue-using-rest-api) for the fields to set and then use the regular create_issue() function.

 

I tried this in many various combinations but no luck.

```python
rootnn_dict = {

'project' : { 'key': 'JBIDE' },

'summary' : 'Test chfild auto created issue',

'description' : 'Igfnore this child. will be deleted shortly',

'issuetype' : { 'id' : '5' },

'parent' : { "id" : rootnn.key},

}

child = jira.create_issue(fields=rootnn_dict)
```

where rootnn.key is a valid parent *key*, not just id as stated on your link.

But the last child creation fails.

 

Van <<https://community.atlassian.com/t5/Jira-questions/How-to-create-subtasks-with-jira-python/qaq-p/227017>> 
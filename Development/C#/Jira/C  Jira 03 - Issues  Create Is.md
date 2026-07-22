---
icon: code-2
---
# C  Jira 03 - Issues  Create Issue
C# Jira 03 - Issues: Create Issue

C# Jira - Issues: Create Issue

---

## CURL Command

```
curl -X POST --user jira@example.com:JIRA_API_TOKEN \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/json' \
  --data '
    {
      "fields": {
        "project": {
          "id": "10000"
        },
        "summary": "something is wrong",
        "issuetype": {
          "id": "10000"
        },
        "assignee": {
          "name": "matt"
        },
        "priority": {
          "id": "3"
        },
        "labels": [
          "bugfix",
          "blitz_test"
        ],
        "description": "description",
        "fixVersions": [
          {
            "id": "10001"
          }
        ],
        "customfield_10005": "blah blah"
      }
    }' \
```

## C# Example

```
Chilkat.Rest rest = new Chilkat.Rest();
bool success;

//  URL: https://your-domain.atlassian.net/rest/api/2/issue
bool bTls = true;
int port = 443;
bool bAutoReconnect = true;
success = rest.Connect("your-domain.atlassian.net",port,bTls,bAutoReconnect);
if (success != true) {
    Debug.WriteLine("ConnectFailReason: " + Convert.ToString(rest.ConnectFailReason));
    Debug.WriteLine(rest.LastErrorText);
    return;
}

rest.SetAuthBasic("jira@example.com","JIRA_API_TOKEN");

Chilkat.JsonObject json = new Chilkat.JsonObject();
json.UpdateString("fields.project.id","10000");
json.UpdateString("fields.summary","something is wrong");
json.UpdateString("fields.issuetype.id","10000");
json.UpdateString("fields.assignee.name","matt");
json.UpdateString("fields.priority.id","3");
json.UpdateString("fields.labels[0]","bugfix");
json.UpdateString("fields.labels[1]","blitz_test");
json.UpdateString("fields.description","description");
json.UpdateString("fields.fixVersions[0].id","10001");
json.UpdateString("fields.customfield_10005","blah blah");

rest.AddHeader("Content-Type","application/json");
rest.AddHeader("Accept","application/json");

Chilkat.StringBuilder sbRequestBody = new Chilkat.StringBuilder();
json.EmitSb(sbRequestBody);
Chilkat.StringBuilder sbResponseBody = new Chilkat.StringBuilder();
success = rest.FullRequestSb("POST","/rest/api/2/issue",sbRequestBody,sbResponseBody);
if (success != true) {
    Debug.WriteLine(rest.LastErrorText);
    return;
}

int respStatusCode = rest.ResponseStatusCode;
if (respStatusCode >= 400) {
    Debug.WriteLine("Response Status Code = " + Convert.ToString(respStatusCode));
    Debug.WriteLine("Response Header:");
    Debug.WriteLine(rest.ResponseHeader);
    Debug.WriteLine("Response Body:");
    Debug.WriteLine(sbResponseBody.GetAsString());
    return;
}

Chilkat.JsonObject jsonResponse = new Chilkat.JsonObject();
jsonResponse.LoadSb(sbResponseBody);

string id;
string key;
string self;

id = jsonResponse.StringOf("id");
key = jsonResponse.StringOf("key");
self = jsonResponse.StringOf("self");
```

## Sample JSON Response Body

```
{
  "id": "10023",
  "key": "SCRUM-24",
  "self": "https://chilkat.atlassian.net/rest/api/2/issue/10023"
}
```
---
icon: code-2
---
# C  Jira 07 - Issues  Assign Issue
C# Jira 07 - Issues: Assign Issue

C# Jira - Issues: Assign Issue

---

## CURL Command

```
curl -X PUT --user jira@example.com:JIRA_API_TOKEN \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/json' \
  --data '
    {
      "name": "matt"
    }' \
  --url 'https://your-domain.atlassian.net/rest/api/2/issue/SCRUM-15/assignee'
```

## C# Example

```
Chilkat.Rest rest = new Chilkat.Rest();
bool success;

//  URL: https://your-domain.atlassian.net/rest/api/2/issue/SCRUM-15/assignee
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
json.UpdateString("name","matt");

rest.AddHeader("Content-Type","application/json");
rest.AddHeader("Accept","application/json");

Chilkat.StringBuilder sbRequestBody = new Chilkat.StringBuilder();
json.EmitSb(sbRequestBody);
Chilkat.StringBuilder sbResponseBody = new Chilkat.StringBuilder();
success = rest.FullRequestSb("PUT","/rest/api/2/issue/SCRUM-15/assignee",sbRequestBody,sbResponseBody);
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
```
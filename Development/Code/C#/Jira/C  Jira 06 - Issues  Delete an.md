---
icon: code-2
---
# C  Jira 06 - Issues  Delete an Issue
C# Jira 06 - Issues: Delete an Issue

C# Jira - Issues: Delete an Issue

---

## CURL Command

```
curl -X DELETE --user jira@example.com:JIRA_API_TOKEN \
  --header 'Accept: application/json' \
  --url 'https://your-domain.atlassian.net/rest/api/2/issue/SCRUM-13'
```

## C# Example

```
Chilkat.Rest rest = new Chilkat.Rest();
bool success;

//  URL: https://your-domain.atlassian.net/rest/api/2/issue/SCRUM-13
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

rest.AddHeader("Accept","application/json");

Chilkat.StringBuilder sbResponseBody = new Chilkat.StringBuilder();
success = rest.FullRequestNoBodySb("DELETE","/rest/api/2/issue/SCRUM-13",sbResponseBody);
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

int i;
int count_i;
string strVal;

i = 0;
count_i = jsonResponse.SizeOfArray("errorMessages");
while (i < count_i) {
    jsonResponse.I = i;
    strVal = jsonResponse.StringOf("errorMessages[i]");
    i = i + 1;
}
```

## Sample JSON Body

```
{
  "errorMessages": [
    "You do not have permission to delete issues in this project."
  ],
  "errors": {}
}
```
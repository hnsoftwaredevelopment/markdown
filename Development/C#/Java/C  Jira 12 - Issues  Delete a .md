# C  Jira 12 - Issues  Delete a Comment
C# Jira 12 - Issues: Delete a Comment

C# Jira - Issues: Delete a Comment

---

## CURL Command

```
curl --request DELETE --user jira@example.com:JIRA_API_TOKEN \
  --header 'Accept: application/json' \
  --url 'https://your-domain.atlassian.net/rest/api/2/issue/SCRUM-15/comment/10019'
```

## C# Example

```
Chilkat.Rest rest = new Chilkat.Rest();
bool success;

//  URL: https://your-domain.atlassian.net/rest/api/2/issue/SCRUM-15/comment/10019
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
success = rest.FullRequestNoBodySb("DELETE","/rest/api/2/issue/SCRUM-15/comment/10019",sbResponseBody);
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
C# Jira 05 - Issues: Edit an Issue

C# Jira - Issues: Edit an Issue
***
## CURL Command
```CURL
curl -X PUT --user jira@example.com:JIRA_API_TOKEN \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/json' \
  --data '
    {
      "update": {
        "summary": [
          {
            "set": "Bug in business logic"
          }
        ],
        "labels": [
          {
            "add": "triaged"
          },
          {
            "remove": "blocker"
          }
        ]
      },
      "fields": {
        "customfield_10010": 1
      },
      "historyMetadata": {
        "type": "myplugin:type",
        "description": "text description",
        "descriptionKey": "plugin.changereason.i18.key",
        "activityDescription": "text description",
        "activityDescriptionKey": "plugin.activity.i18.key",
        "actor": {
          "id": "tony",
          "displayName": "Tony",
          "type": "mysystem-user",
          "avatarUrl": "http://mysystem/avatar/tony.jpg",
          "url": "http://mysystem/users/tony"
        },
        "generator": {
          "id": "mysystem-1",
          "type": "mysystem-application"
        },
        "cause": {
          "id": "myevent",
          "type": "mysystem-event"
        },
        "extraData": {
          "keyvalue": "extra data",
          "goes": "here"
        }
      },
      "properties": [
        {
          "key": "key1",
          "value": "can be set at issue create or update time"
        },
        {
          "key": "key2",
          "value": "and there can be multiple properties"
        }
      ]
    }' \
  --url 'https://your-domain.atlassian.net/rest/api/2/issue/SCRUM-15'
```

## C# Example
```C#
Chilkat.Rest rest = new Chilkat.Rest();
bool success;

//  URL: https://your-domain.atlassian.net/rest/api/2/issue/SCRUM-15
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
json.UpdateString("update.summary[0].set","Bug in business logic");
json.UpdateString("update.labels[0].add","triaged");
json.UpdateString("update.labels[1].remove","blocker");
json.UpdateNumber("fields.customfield_10010","1");
json.UpdateString("historyMetadata.type","myplugin:type");
json.UpdateString("historyMetadata.description","text description");
json.UpdateString("historyMetadata.descriptionKey","plugin.changereason.i18.key");
json.UpdateString("historyMetadata.activityDescription","text description");
json.UpdateString("historyMetadata.activityDescriptionKey","plugin.activity.i18.key");
json.UpdateString("historyMetadata.actor.id","tony");
json.UpdateString("historyMetadata.actor.displayName","Tony");
json.UpdateString("historyMetadata.actor.type","mysystem-user");
json.UpdateString("historyMetadata.actor.avatarUrl","http://mysystem/avatar/tony.jpg");
json.UpdateString("historyMetadata.actor.url","http://mysystem/users/tony");
json.UpdateString("historyMetadata.generator.id","mysystem-1");
json.UpdateString("historyMetadata.generator.type","mysystem-application");
json.UpdateString("historyMetadata.cause.id","myevent");
json.UpdateString("historyMetadata.cause.type","mysystem-event");
json.UpdateString("historyMetadata.extraData.keyvalue","extra data");
json.UpdateString("historyMetadata.extraData.goes","here");
json.UpdateString("properties[0].key","key1");
json.UpdateString("properties[0].value","can be set at issue create or update time");
json.UpdateString("properties[1].key","key2");
json.UpdateString("properties[1].value","and there can be multiple properties");

rest.AddHeader("Content-Type","application/json");
rest.AddHeader("Accept","application/json");

Chilkat.StringBuilder sbRequestBody = new Chilkat.StringBuilder();
json.EmitSb(sbRequestBody);
Chilkat.StringBuilder sbResponseBody = new Chilkat.StringBuilder();
success = rest.FullRequestSb("PUT","/rest/api/2/issue/SCRUM-15",sbRequestBody,sbResponseBody);
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


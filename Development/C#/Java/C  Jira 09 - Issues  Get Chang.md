# C  Jira 09 - Issues  Get Change Logs
C# Jira 09 - Issues: Get Change Logs

C# Jira - Issues: Get Change Logs

---

## CURL Command

```
curl --user jira@example.com:JIRA_API_TOKEN \
 --header 'Accept: application/json' \
  --url 'https://your-domain.atlassian.net/rest/api/2/issue/SCRUM-15/changelog'
```

## C# Example

```
Chilkat.Rest rest = new Chilkat.Rest();
bool success;

//  URL: https://your-domain.atlassian.net/rest/api/2/issue/SCRUM-15/changelog
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
success = rest.FullRequestNoBodySb("GET","/rest/api/2/issue/SCRUM-15/changelog",sbResponseBody);
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

string self;
int maxResults;
int startAt;
int total;
bool isLast;
int i;
int count_i;
string id;
string authorSelf;
string authorName;
string authorKey;
string authorAccountId;
string authorEmailAddress;
string authorAvatarUrls48x48;
string authorAvatarUrls24x24;
string authorAvatarUrls16x16;
string authorAvatarUrls32x32;
string authorDisplayName;
bool authorActive;
string authorTimeZone;
string created;
string historyMetadataType;
string historyMetadataDescription;
string historyMetadataDescriptionKey;
string historyMetadataActivityDescription;
string historyMetadataActivityDescriptionKey;
string historyMetadataActorId;
string historyMetadataActorDisplayName;
string historyMetadataActorType;
string historyMetadataActorAvatarUrl;
string historyMetadataActorUrl;
string historyMetadataGeneratorId;
string historyMetadataGeneratorType;
string historyMetadataCauseId;
string historyMetadataCauseType;
string historyMetadataExtraDataKeyvalue;
string historyMetadataExtraDataGoes;
int j;
int count_j;
string field;
string fieldtype;
string from;
string fromString;
string v_to;
string toString;
string fieldId;

self = jsonResponse.StringOf("self");
maxResults = jsonResponse.IntOf("maxResults");
startAt = jsonResponse.IntOf("startAt");
total = jsonResponse.IntOf("total");
isLast = jsonResponse.BoolOf("isLast");
i = 0;
count_i = jsonResponse.SizeOfArray("values");
while (i < count_i) {
    jsonResponse.I = i;
    id = jsonResponse.StringOf("values[i].id");
    authorSelf = jsonResponse.StringOf("values[i].author.self");
    authorName = jsonResponse.StringOf("values[i].author.name");
    authorKey = jsonResponse.StringOf("values[i].author.key");
    authorAccountId = jsonResponse.StringOf("values[i].author.accountId");
    authorEmailAddress = jsonResponse.StringOf("values[i].author.emailAddress");
    authorAvatarUrls48x48 = jsonResponse.StringOf("values[i].author.avatarUrls.48x48");
    authorAvatarUrls24x24 = jsonResponse.StringOf("values[i].author.avatarUrls.24x24");
    authorAvatarUrls16x16 = jsonResponse.StringOf("values[i].author.avatarUrls.16x16");
    authorAvatarUrls32x32 = jsonResponse.StringOf("values[i].author.avatarUrls.32x32");
    authorDisplayName = jsonResponse.StringOf("values[i].author.displayName");
    authorActive = jsonResponse.BoolOf("values[i].author.active");
    authorTimeZone = jsonResponse.StringOf("values[i].author.timeZone");
    created = jsonResponse.StringOf("values[i].created");
    historyMetadataType = jsonResponse.StringOf("values[i].historyMetadata.type");
    historyMetadataDescription = jsonResponse.StringOf("values[i].historyMetadata.description");
    historyMetadataDescriptionKey = jsonResponse.StringOf("values[i].historyMetadata.descriptionKey");
    historyMetadataActivityDescription = jsonResponse.StringOf("values[i].historyMetadata.activityDescription");
    historyMetadataActivityDescriptionKey = jsonResponse.StringOf("values[i].historyMetadata.activityDescriptionKey");
    historyMetadataActorId = jsonResponse.StringOf("values[i].historyMetadata.actor.id");
    historyMetadataActorDisplayName = jsonResponse.StringOf("values[i].historyMetadata.actor.displayName");
    historyMetadataActorType = jsonResponse.StringOf("values[i].historyMetadata.actor.type");
    historyMetadataActorAvatarUrl = jsonResponse.StringOf("values[i].historyMetadata.actor.avatarUrl");
    historyMetadataActorUrl = jsonResponse.StringOf("values[i].historyMetadata.actor.url");
    historyMetadataGeneratorId = jsonResponse.StringOf("values[i].historyMetadata.generator.id");
    historyMetadataGeneratorType = jsonResponse.StringOf("values[i].historyMetadata.generator.type");
    historyMetadataCauseId = jsonResponse.StringOf("values[i].historyMetadata.cause.id");
    historyMetadataCauseType = jsonResponse.StringOf("values[i].historyMetadata.cause.type");
    historyMetadataExtraDataKeyvalue = jsonResponse.StringOf("values[i].historyMetadata.extraData.keyvalue");
    historyMetadataExtraDataGoes = jsonResponse.StringOf("values[i].historyMetadata.extraData.goes");
    j = 0;
    count_j = jsonResponse.SizeOfArray("values[i].items");
    while (j < count_j) {
        jsonResponse.J = j;
        field = jsonResponse.StringOf("values[i].items[j].field");
        fieldtype = jsonResponse.StringOf("values[i].items[j].fieldtype");
        from = jsonResponse.StringOf("values[i].items[j].from");
        fromString = jsonResponse.StringOf("values[i].items[j].fromString");
        v_to = jsonResponse.StringOf("values[i].items[j].to");
        toString = jsonResponse.StringOf("values[i].items[j].toString");
        fieldId = jsonResponse.StringOf("values[i].items[j].fieldId");
        j = j + 1;
    }

    i = i + 1;
}
```

## Sample JSON Body

```
{
  "self": "https://chilkat.atlassian.net/rest/api/2/issue/SCRUM-15/changelog?maxResults=100&startAt=0",
  "maxResults": 100,
  "startAt": 0,
  "total": 7,
  "isLast": true,
  "values": [
    {
      "id": "10009",
      "author": {
        "self": "https://chilkat.atlassian.net/rest/api/2/user?username=admin",
        "name": "admin",
        "key": "admin",
        "accountId": "557058:be8b47b5-3bc0-43f6-b6b2-2cca0de12204",
        "emailAddress": "admin@@chilkatsoft.com",
        "avatarUrls": {
          "48x48": "https://avatar-cdn.atlassian.com/16d54dcc6d4bef86fd7ee62a7cf6334a?s=48&d=https%3A%2F%2Fsecure.gravatar.com%2Favatar%2F16d54dcc6d4bef86fd7ee62a7cf6334a%3Fd%3Dmm%26s%3D48%26noRedirect%3Dtrue",
          "24x24": "https://avatar-cdn.atlassian.com/16d54dcc6d4bef86fd7ee62a7cf6334a?s=24&d=https%3A%2F%2Fsecure.gravatar.com%2Favatar%2F16d54dcc6d4bef86fd7ee62a7cf6334a%3Fd%3Dmm%26s%3D24%26noRedirect%3Dtrue",
          "16x16": "https://avatar-cdn.atlassian.com/16d54dcc6d4bef86fd7ee62a7cf6334a?s=16&d=https%3A%2F%2Fsecure.gravatar.com%2Favatar%2F16d54dcc6d4bef86fd7ee62a7cf6334a%3Fd%3Dmm%26s%3D16%26noRedirect%3Dtrue",
          "32x32": "https://avatar-cdn.atlassian.com/16d54dcc6d4bef86fd7ee62a7cf6334a?s=32&d=https%3A%2F%2Fsecure.gravatar.com%2Favatar%2F16d54dcc6d4bef86fd7ee62a7cf6334a%3Fd%3Dmm%26s%3D32%26noRedirect%3Dtrue"
        },
        "displayName": "Chilkat Admin",
        "active": true,
        "timeZone": "America/Chicago"
      },
      "created": "2018-04-05T14:41:55.852-0500",
      "items": [
        {
          "field": "status",
          "fieldtype": "jira",
          "from": "10000",
          "fromString": "To Do",
          "to": "3",
          "toString": "In Progress"
        }
      ]
    },
    {
      "id": "10010",
      "author": {
        "self": "https://chilkat.atlassian.net/rest/api/2/user?username=admin",
        "name": "admin",
        "key": "admin",
        "accountId": "557058:be8b47b5-3bc0-43f6-b6b2-2cca0de12204",
        "emailAddress": "admin@@chilkatsoft.com",
        "avatarUrls": {
          "48x48": "https://avatar-cdn.atlassian.com/16d54dcc6d4bef86fd7ee62a7cf6334a?s=48&d=https%3A%2F%2Fsecure.gravatar.com%2Favatar%2F16d54dcc6d4bef86fd7ee62a7cf6334a%3Fd%3Dmm%26s%3D48%26noRedirect%3Dtrue",
          "24x24": "https://avatar-cdn.atlassian.com/16d54dcc6d4bef86fd7ee62a7cf6334a?s=24&d=https%3A%2F%2Fsecure.gravatar.com%2Favatar%2F16d54dcc6d4bef86fd7ee62a7cf6334a%3Fd%3Dmm%26s%3D24%26noRedirect%3Dtrue",
          "16x16": "https://avatar-cdn.atlassian.com/16d54dcc6d4bef86fd7ee62a7cf6334a?s=16&d=https%3A%2F%2Fsecure.gravatar.com%2Favatar%2F16d54dcc6d4bef86fd7ee62a7cf6334a%3Fd%3Dmm%26s%3D16%26noRedirect%3Dtrue",
          "32x32": "https://avatar-cdn.atlassian.com/16d54dcc6d4bef86fd7ee62a7cf6334a?s=32&d=https%3A%2F%2Fsecure.gravatar.com%2Favatar%2F16d54dcc6d4bef86fd7ee62a7cf6334a%3Fd%3Dmm%26s%3D32%26noRedirect%3Dtrue"
        },
        "displayName": "Chilkat Admin",
        "active": true,
        "timeZone": "America/Chicago"
      },
      "created": "2018-04-08T00:33:55.852-0500",
      "items": [
        {
          "field": "status",
          "fieldtype": "jira",
          "from": "3",
          "fromString": "In Progress",
          "to": "10001",
          "toString": "Done"
        }
      ]
    },
    {
      "id": "10033",
      "author": {
        "self": "https://chilkat.atlassian.net/rest/api/2/user?username=admin",
        "name": "admin",
        "key": "admin",
        "accountId": "557058:be8b47b5-3bc0-43f6-b6b2-2cca0de12204",
        "emailAddress": "admin@@chilkatsoft.com",
        "avatarUrls": {
          "48x48": "https://avatar-cdn.atlassian.com/16d54dcc6d4bef86fd7ee62a7cf6334a?s=48&d=https%3A%2F%2Fsecure.gravatar.com%2Favatar%2F16d54dcc6d4bef86fd7ee62a7cf6334a%3Fd%3Dmm%26s%3D48%26noRedirect%3Dtrue",
          "24x24": "https://avatar-cdn.atlassian.com/16d54dcc6d4bef86fd7ee62a7cf6334a?s=24&d=https%3A%2F%2Fsecure.gravatar.com%2Favatar%2F16d54dcc6d4bef86fd7ee62a7cf6334a%3Fd%3Dmm%26s%3D24%26noRedirect%3Dtrue",
          "16x16": "https://avatar-cdn.atlassian.com/16d54dcc6d4bef86fd7ee62a7cf6334a?s=16&d=https%3A%2F%2Fsecure.gravatar.com%2Favatar%2F16d54dcc6d4bef86fd7ee62a7cf6334a%3Fd%3Dmm%26s%3D16%26noRedirect%3Dtrue",
          "32x32": "https://avatar-cdn.atlassian.com/16d54dcc6d4bef86fd7ee62a7cf6334a?s=32&d=https%3A%2F%2Fsecure.gravatar.com%2Favatar%2F16d54dcc6d4bef86fd7ee62a7cf6334a%3Fd%3Dmm%26s%3D32%26noRedirect%3Dtrue"
        },
        "displayName": "Chilkat Admin",
        "active": true,
        "timeZone": "America/Chicago"
      },
      "created": "2018-04-12T20:07:08.107-0500",
      "items": [
        {
          "field": "assignee",
          "fieldtype": "jira",
          "fieldId": "assignee",
          "from": null,
          "fromString": null,
          "to": "matt",
          "toString": "Matt of Chilkat"
        }
      ]
    },
    {
      "id": "10035",
      "author": {
        "self": "https://chilkat.atlassian.net/rest/api/2/user?username=admin",
        "name": "admin",
        "key": "admin",
        "accountId": "557058:be8b47b5-3bc0-43f6-b6b2-2cca0de12204",
        "emailAddress": "admin@@chilkatsoft.com",
        "avatarUrls": {
          "48x48": "https://avatar-cdn.atlassian.com/16d54dcc6d4bef86fd7ee62a7cf6334a?s=48&d=https%3A%2F%2Fsecure.gravatar.com%2Favatar%2F16d54dcc6d4bef86fd7ee62a7cf6334a%3Fd%3Dmm%26s%3D48%26noRedirect%3Dtrue",
          "24x24": "https://avatar-cdn.atlassian.com/16d54dcc6d4bef86fd7ee62a7cf6334a?s=24&d=https%3A%2F%2Fsecure.gravatar.com%2Favatar%2F16d54dcc6d4bef86fd7ee62a7cf6334a%3Fd%3Dmm%26s%3D24%26noRedirect%3Dtrue",
          "16x16": "https://avatar-cdn.atlassian.com/16d54dcc6d4bef86fd7ee62a7cf6334a?s=16&d=https%3A%2F%2Fsecure.gravatar.com%2Favatar%2F16d54dcc6d4bef86fd7ee62a7cf6334a%3Fd%3Dmm%26s%3D16%26noRedirect%3Dtrue",
          "32x32": "https://avatar-cdn.atlassian.com/16d54dcc6d4bef86fd7ee62a7cf6334a?s=32&d=https%3A%2F%2Fsecure.gravatar.com%2Favatar%2F16d54dcc6d4bef86fd7ee62a7cf6334a%3Fd%3Dmm%26s%3D32%26noRedirect%3Dtrue"
        },
        "displayName": "Chilkat Admin",
        "active": true,
        "timeZone": "America/Chicago"
      },
      "created": "2018-04-13T08:07:40.815-0500",
      "items": [
        {
          "field": "summary",
          "fieldtype": "jira",
          "fieldId": "summary",
          "from": null,
          "fromString": "As a scrum master, I can see the progress of a sprint via the Burndown Chart >> Click \"Reports\" to view the Burndown Chart",
          "to": null,
          "toString": "Bug in business logic"
        },
        {
          "field": "labels",
          "fieldtype": "jira",
          "fieldId": "labels",
          "from": null,
          "fromString": "",
          "to": null,
          "toString": "triaged"
        }
      ],
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
      }
    },
    {
      "id": "10036",
      "author": {
        "self": "https://chilkat.atlassian.net/rest/api/2/user?username=admin",
        "name": "admin",
        "key": "admin",
        "accountId": "557058:be8b47b5-3bc0-43f6-b6b2-2cca0de12204",
        "emailAddress": "admin@@chilkatsoft.com",
        "avatarUrls": {
          "48x48": "https://avatar-cdn.atlassian.com/16d54dcc6d4bef86fd7ee62a7cf6334a?s=48&d=https%3A%2F%2Fsecure.gravatar.com%2Favatar%2F16d54dcc6d4bef86fd7ee62a7cf6334a%3Fd%3Dmm%26s%3D48%26noRedirect%3Dtrue",
          "24x24": "https://avatar-cdn.atlassian.com/16d54dcc6d4bef86fd7ee62a7cf6334a?s=24&d=https%3A%2F%2Fsecure.gravatar.com%2Favatar%2F16d54dcc6d4bef86fd7ee62a7cf6334a%3Fd%3Dmm%26s%3D24%26noRedirect%3Dtrue",
          "16x16": "https://avatar-cdn.atlassian.com/16d54dcc6d4bef86fd7ee62a7cf6334a?s=16&d=https%3A%2F%2Fsecure.gravatar.com%2Favatar%2F16d54dcc6d4bef86fd7ee62a7cf6334a%3Fd%3Dmm%26s%3D16%26noRedirect%3Dtrue",
          "32x32": "https://avatar-cdn.atlassian.com/16d54dcc6d4bef86fd7ee62a7cf6334a?s=32&d=https%3A%2F%2Fsecure.gravatar.com%2Favatar%2F16d54dcc6d4bef86fd7ee62a7cf6334a%3Fd%3Dmm%26s%3D32%26noRedirect%3Dtrue"
        },
        "displayName": "Chilkat Admin",
        "active": true,
        "timeZone": "America/Chicago"
      },
      "created": "2018-04-13T09:11:35.151-0500",
      "items": [
        {
          "field": "assignee",
          "fieldtype": "jira",
          "fieldId": "assignee",
          "from": "matt",
          "fromString": "Matt of Chilkat",
          "to": "admin",
          "toString": "Chilkat Admin"
        }
      ]
    },
    {
      "id": "10037",
      "author": {
        "self": "https://chilkat.atlassian.net/rest/api/2/user?username=admin",
        "name": "admin",
        "key": "admin",
        "accountId": "557058:be8b47b5-3bc0-43f6-b6b2-2cca0de12204",
        "emailAddress": "admin@@chilkatsoft.com",
        "avatarUrls": {
          "48x48": "https://avatar-cdn.atlassian.com/16d54dcc6d4bef86fd7ee62a7cf6334a?s=48&d=https%3A%2F%2Fsecure.gravatar.com%2Favatar%2F16d54dcc6d4bef86fd7ee62a7cf6334a%3Fd%3Dmm%26s%3D48%26noRedirect%3Dtrue",
          "24x24": "https://avatar-cdn.atlassian.com/16d54dcc6d4bef86fd7ee62a7cf6334a?s=24&d=https%3A%2F%2Fsecure.gravatar.com%2Favatar%2F16d54dcc6d4bef86fd7ee62a7cf6334a%3Fd%3Dmm%26s%3D24%26noRedirect%3Dtrue",
          "16x16": "https://avatar-cdn.atlassian.com/16d54dcc6d4bef86fd7ee62a7cf6334a?s=16&d=https%3A%2F%2Fsecure.gravatar.com%2Favatar%2F16d54dcc6d4bef86fd7ee62a7cf6334a%3Fd%3Dmm%26s%3D16%26noRedirect%3Dtrue",
          "32x32": "https://avatar-cdn.atlassian.com/16d54dcc6d4bef86fd7ee62a7cf6334a?s=32&d=https%3A%2F%2Fsecure.gravatar.com%2Favatar%2F16d54dcc6d4bef86fd7ee62a7cf6334a%3Fd%3Dmm%26s%3D32%26noRedirect%3Dtrue"
        },
        "displayName": "Chilkat Admin",
        "active": true,
        "timeZone": "America/Chicago"
      },
      "created": "2018-04-13T10:04:19.046-0500",
      "items": [
        {
          "field": "Attachment",
          "fieldtype": "jira",
          "fieldId": "attachment",
          "from": null,
          "fromString": null,
          "to": "10000",
          "toString": "starfish.jpg"
        }
      ]
    },
    {
      "id": "10038",
      "author": {
        "self": "https://chilkat.atlassian.net/rest/api/2/user?username=admin",
        "name": "admin",
        "key": "admin",
        "accountId": "557058:be8b47b5-3bc0-43f6-b6b2-2cca0de12204",
        "emailAddress": "admin@@chilkatsoft.com",
        "avatarUrls": {
          "48x48": "https://avatar-cdn.atlassian.com/16d54dcc6d4bef86fd7ee62a7cf6334a?s=48&d=https%3A%2F%2Fsecure.gravatar.com%2Favatar%2F16d54dcc6d4bef86fd7ee62a7cf6334a%3Fd%3Dmm%26s%3D48%26noRedirect%3Dtrue",
          "24x24": "https://avatar-cdn.atlassian.com/16d54dcc6d4bef86fd7ee62a7cf6334a?s=24&d=https%3A%2F%2Fsecure.gravatar.com%2Favatar%2F16d54dcc6d4bef86fd7ee62a7cf6334a%3Fd%3Dmm%26s%3D24%26noRedirect%3Dtrue",
          "16x16": "https://avatar-cdn.atlassian.com/16d54dcc6d4bef86fd7ee62a7cf6334a?s=16&d=https%3A%2F%2Fsecure.gravatar.com%2Favatar%2F16d54dcc6d4bef86fd7ee62a7cf6334a%3Fd%3Dmm%26s%3D16%26noRedirect%3Dtrue",
          "32x32": "https://avatar-cdn.atlassian.com/16d54dcc6d4bef86fd7ee62a7cf6334a?s=32&d=https%3A%2F%2Fsecure.gravatar.com%2Favatar%2F16d54dcc6d4bef86fd7ee62a7cf6334a%3Fd%3Dmm%26s%3D32%26noRedirect%3Dtrue"
        },
        "displayName": "Chilkat Admin",
        "active": true,
        "timeZone": "America/Chicago"
      },
      "created": "2018-04-13T10:04:46.939-0500",
      "items": [
        {
          "field": "Attachment",
          "fieldtype": "jira",
          "fieldId": "attachment",
          "from": null,
          "fromString": null,
          "to": "10001",
          "toString": "starfish.jpg"
        },
        {
          "field": "Attachment",
          "fieldtype": "jira",
          "fieldId": "attachment",
          "from": null,
          "fromString": null,
          "to": "10002",
          "toString": "sample2.docx"
        },
        {
          "field": "Attachment",
          "fieldtype": "jira",
          "fieldId": "attachment",
          "from": null,
          "fromString": null,
          "to": "10003",
          "toString": "sample.pdf"
        }
      ]
    }
  ]
}
```
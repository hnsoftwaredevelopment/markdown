C# Jira 11 - Issues: Update a Comment

C# Jira - Issues: Update a Comment
***
## CURL Command
```CURL
curl --request PUT --user jira@example.com:JIRA_API_TOKEN \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/json' \
  --data '
    {
      "body": "ABC Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque eget venenatis elit. Duis eu justo eget augue iaculis fermentum. Sed semper quam laoreet nisi egestas at posuere augue semper.",
      "visibility": {
        "type": "role",
        "value": "Administrators"
      }
    }' \
  --url 'https://your-domain.atlassian.net/rest/api/2/issue/SCRUM-15/comment/10019'
```

## C# Example
```C#
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

Chilkat.JsonObject json = new Chilkat.JsonObject();
json.UpdateString("body","ABC Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque eget venenatis elit. Duis eu justo eget augue iaculis fermentum. Sed semper quam laoreet nisi egestas at posuere augue semper.");
json.UpdateString("visibility.type","role");
json.UpdateString("visibility.value","Administrators");

rest.AddHeader("Content-Type","application/json");
rest.AddHeader("Accept","application/json");

Chilkat.StringBuilder sbRequestBody = new Chilkat.StringBuilder();
json.EmitSb(sbRequestBody);
Chilkat.StringBuilder sbResponseBody = new Chilkat.StringBuilder();
success = rest.FullRequestSb("PUT","/rest/api/2/issue/SCRUM-15/comment/10019",sbRequestBody,sbResponseBody);
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
string body;
string updateAuthorSelf;
string updateAuthorName;
string updateAuthorKey;
string updateAuthorAccountId;
string updateAuthorEmailAddress;
string updateAuthorAvatarUrls48x48;
string updateAuthorAvatarUrls24x24;
string updateAuthorAvatarUrls16x16;
string updateAuthorAvatarUrls32x32;
string updateAuthorDisplayName;
bool updateAuthorActive;
string updateAuthorTimeZone;
string created;
string updated;
string visibilityType;
string visibilityValue;

self = jsonResponse.StringOf("self");
id = jsonResponse.StringOf("id");
authorSelf = jsonResponse.StringOf("author.self");
authorName = jsonResponse.StringOf("author.name");
authorKey = jsonResponse.StringOf("author.key");
authorAccountId = jsonResponse.StringOf("author.accountId");
authorEmailAddress = jsonResponse.StringOf("author.emailAddress");
authorAvatarUrls48x48 = jsonResponse.StringOf("author.avatarUrls.48x48");
authorAvatarUrls24x24 = jsonResponse.StringOf("author.avatarUrls.24x24");
authorAvatarUrls16x16 = jsonResponse.StringOf("author.avatarUrls.16x16");
authorAvatarUrls32x32 = jsonResponse.StringOf("author.avatarUrls.32x32");
authorDisplayName = jsonResponse.StringOf("author.displayName");
authorActive = jsonResponse.BoolOf("author.active");
authorTimeZone = jsonResponse.StringOf("author.timeZone");
body = jsonResponse.StringOf("body");
updateAuthorSelf = jsonResponse.StringOf("updateAuthor.self");
updateAuthorName = jsonResponse.StringOf("updateAuthor.name");
updateAuthorKey = jsonResponse.StringOf("updateAuthor.key");
updateAuthorAccountId = jsonResponse.StringOf("updateAuthor.accountId");
updateAuthorEmailAddress = jsonResponse.StringOf("updateAuthor.emailAddress");
updateAuthorAvatarUrls48x48 = jsonResponse.StringOf("updateAuthor.avatarUrls.48x48");
updateAuthorAvatarUrls24x24 = jsonResponse.StringOf("updateAuthor.avatarUrls.24x24");
updateAuthorAvatarUrls16x16 = jsonResponse.StringOf("updateAuthor.avatarUrls.16x16");
updateAuthorAvatarUrls32x32 = jsonResponse.StringOf("updateAuthor.avatarUrls.32x32");
updateAuthorDisplayName = jsonResponse.StringOf("updateAuthor.displayName");
updateAuthorActive = jsonResponse.BoolOf("updateAuthor.active");
updateAuthorTimeZone = jsonResponse.StringOf("updateAuthor.timeZone");
created = jsonResponse.StringOf("created");
updated = jsonResponse.StringOf("updated");
visibilityType = jsonResponse.StringOf("visibility.type");
visibilityValue = jsonResponse.StringOf("visibility.value");
```

## Sample JSON Body
```JSON
{
  "self": "https://chilkat.atlassian.net/rest/api/2/issue/10014/comment/10019",
  "id": "10019",
  "author": {
    "self": "https://chilkat.atlassian.net/rest/api/2/user?username=admin",
    "name": "admin",
    "key": "admin",
    "accountId": "557058:be8b47b5-3bc0-43f6-b6b2-2cca0de12204",
    "emailAddress": "admin@chilkatsoft.com",
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
  "body": "ABC Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque eget venenatis elit. Duis eu justo eget augue iaculis fermentum. Sed semper quam laoreet nisi egestas at posuere augue semper.",
  "updateAuthor": {
    "self": "https://chilkat.atlassian.net/rest/api/2/user?username=admin",
    "name": "admin",
    "key": "admin",
    "accountId": "557058:be8b47b5-3bc0-43f6-b6b2-2cca0de12204",
    "emailAddress": "admin@chilkatsoft.com",
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
  "created": "2018-04-14T10:14:41.741-0500",
  "updated": "2018-04-14T10:25:07.558-0500",
  "visibility": {
    "type": "role",
    "value": "Administrators"
  }
}
```

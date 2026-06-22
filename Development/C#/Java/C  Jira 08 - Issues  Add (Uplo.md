# C  Jira 08 - Issues  Add (Upload) Attachments to a
C# Jira 08 - Issues: Add (Upload) Attachments to an Issue

C# Jira - Issues: Add (Upload) Attachments to an Issue

---

## CURL Command

```
curl -X POST --user jira@example.com:JIRA_API_TOKEN \
  --header 'Accept: application/json' \
  --header 'Content-Type: multipart/form-data' \
  --header 'X-Atlassian-Token: no-check' \
  --form 'name=file; file=@starfish.jpg' \
  --form 'name=file; file=@sample2.docx' \
  --form 'name=file; file=@sample.pdf' \
  --url 'https://your-domain.atlassian.net/rest/api/2/issue/SCRUM-15/attachments'
```

## C# Example

```
Chilkat.Rest rest = new Chilkat.Rest();
bool success;

//  URL: https://your-domain.atlassian.net/rest/api/2/issue/SCRUM-15/attachments
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

rest.PartSelector = "1";
Chilkat.Stream fileStream1 = new Chilkat.Stream();
fileStream1.SourceFile = "starfish.jpg";
rest.AddHeader("Content-Disposition","form-data; name=\"file\"; filename=\"starfish.jpg\"");
rest.AddHeader("Content-Type","image/jpeg");
rest.SetMultipartBodyStream(fileStream1);

rest.PartSelector = "2";
Chilkat.Stream fileStream2 = new Chilkat.Stream();
fileStream2.SourceFile = "sample2.docx";
rest.AddHeader("Content-Disposition","form-data; name=\"file\"; filename=\"sample2.docx\"");
rest.AddHeader("Content-Type","application/vnd.openxmlformats-officedocument.wordprocessingml.document");
rest.SetMultipartBodyStream(fileStream2);

rest.PartSelector = "3";
Chilkat.Stream fileStream3 = new Chilkat.Stream();
fileStream3.SourceFile = "sample.pdf";
rest.AddHeader("Content-Disposition","form-data; name=\"file\"; filename=\"sample.pdf\"");
rest.AddHeader("Content-Type","application/pdf");
rest.SetMultipartBodyStream(fileStream3);

rest.PartSelector = "0";

rest.AddHeader("Content-Type","multipart/form-data");
rest.AddHeader("X-Atlassian-Token","no-check");
rest.AddHeader("Accept","application/json");

string strResponseBody = rest.FullRequestMultipart("POST","/rest/api/2/issue/SCRUM-15/attachments");
if (rest.LastMethodSuccess != true) {
    Debug.WriteLine(rest.LastErrorText);
    return;
}

int respStatusCode = rest.ResponseStatusCode;
if (respStatusCode >= 400) {
    Debug.WriteLine("Response Status Code = " + Convert.ToString(respStatusCode));
    Debug.WriteLine("Response Header:");
    Debug.WriteLine(rest.ResponseHeader);
    Debug.WriteLine("Response Body:");
    Debug.WriteLine(strResponseBody);
    return;
}

Chilkat.JsonArray jsonResponse = new Chilkat.JsonArray();
jsonResponse.Load(strResponseBody);

int arrIdx = 0;
int numArrayObjects = jsonResponse.Size;
//  Iterate over the members of the array.
while (arrIdx < numArrayObjects) {
    //  Make sure the array member at this index is a JSON object.
    if (jsonResponse.TypeAt(arrIdx) == 3) {
        Chilkat.JsonObject jObj = jsonResponse.ObjectAt(arrIdx);

        //  ...

    }

    arrIdx = arrIdx + 1;
}
```

## Sample JSON Body

```
[
  {
    "self": "https://chilkat.atlassian.net/rest/api/2/attachment/10001",
    "id": "10001",
    "filename": "starfish.jpg",
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
    "created": "2018-04-13T10:04:44.966-0500",
    "size": 6229,
    "mimeType": "image/jpeg",
    "content": "https://chilkat.atlassian.net/secure/attachment/10001/starfish.jpg",
    "thumbnail": "https://chilkat.atlassian.net/secure/thumbnail/10001/starfish.jpg"
  },
  {
    "self": "https://chilkat.atlassian.net/rest/api/2/attachment/10002",
    "id": "10002",
    "filename": "sample2.docx",
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
    "created": "2018-04-13T10:04:45.706-0500",
    "size": 21082,
    "mimeType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    "content": "https://chilkat.atlassian.net/secure/attachment/10002/sample2.docx"
  },
  {
    "self": "https://chilkat.atlassian.net/rest/api/2/attachment/10003",
    "id": "10003",
    "filename": "sample.pdf",
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
    "created": "2018-04-13T10:04:46.292-0500",
    "size": 178399,
    "mimeType": "application/pdf",
    "content": "https://chilkat.atlassian.net/secure/attachment/10003/sample.pdf"
  }
]
```
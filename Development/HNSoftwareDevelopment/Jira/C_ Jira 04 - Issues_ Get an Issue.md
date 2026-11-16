C# Jira 04 - Issues: Get an Issue

C# Jira - Issues: Get an Issue
***
## CURL Command
```CURL
curl --user jira@example.com:JIRA_API_TOKEN \
  --header 'Accept: application/json' \
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

rest.AddHeader("Accept","application/json");

Chilkat.StringBuilder sbResponseBody = new Chilkat.StringBuilder();
success = rest.FullRequestNoBodySb("GET","/rest/api/2/issue/SCRUM-15",sbResponseBody);
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

string expand;
string id;
string self;
string key;
string fieldsIssuetypeSelf;
string fieldsIssuetypeId;
string fieldsIssuetypeDescription;
string fieldsIssuetypeIconUrl;
string fieldsIssuetypeName;
bool fieldsIssuetypeSubtask;
bool fieldsTimespent;
string fieldsProjectSelf;
string fieldsProjectId;
string fieldsProjectKey;
string fieldsProjectName;
string fieldsProjectProjectTypeKey;
string fieldsProjectAvatarUrls48x48;
string fieldsProjectAvatarUrls24x24;
string fieldsProjectAvatarUrls16x16;
string fieldsProjectAvatarUrls32x32;
string fieldsProjectProjectCategorySelf;
string fieldsProjectProjectCategoryId;
string fieldsProjectProjectCategoryDescription;
string fieldsProjectProjectCategoryName;
bool fieldsAggregatetimespent;
string fieldsResolutionSelf;
string fieldsResolutionId;
string fieldsResolutionDescription;
string fieldsResolutionName;
string fieldsCustomfield_10027;
string fieldsCustomfield_10028;
string fieldsCustomfield_10029;
string fieldsResolutiondate;
int fieldsWorkratio;
string fieldsWatchesSelf;
int fieldsWatchesWatchCount;
bool fieldsWatchesIsWatching;
string fieldsLastViewed;
string fieldsCreated;
bool fieldsCustomfield_10022;
string fieldsCustomfield_10023;
string fieldsPrioritySelf;
string fieldsPriorityIconUrl;
string fieldsPriorityName;
string fieldsPriorityId;
string fieldsCustomfield_10024;
string fieldsCustomfield_10025;
string fieldsCustomfield_10026;
bool fieldsCustomfield_10017;
bool fieldsCustomfield_10018;
int fieldsCustomfield_10019;
bool fieldsAggregatetimeoriginalestimate;
bool fieldsTimeestimate;
string fieldsAssigneeSelf;
string fieldsAssigneeName;
string fieldsAssigneeKey;
string fieldsAssigneeAccountId;
string fieldsAssigneeEmailAddress;
string fieldsAssigneeAvatarUrls48x48;
string fieldsAssigneeAvatarUrls24x24;
string fieldsAssigneeAvatarUrls16x16;
string fieldsAssigneeAvatarUrls32x32;
string fieldsAssigneeDisplayName;
bool fieldsAssigneeActive;
string fieldsAssigneeTimeZone;
string fieldsUpdated;
string fieldsStatusSelf;
string fieldsStatusDescription;
string fieldsStatusIconUrl;
string fieldsStatusName;
string fieldsStatusId;
string fieldsStatusStatusCategorySelf;
int fieldsStatusStatusCategoryId;
string fieldsStatusStatusCategoryKey;
string fieldsStatusStatusCategoryColorName;
string fieldsStatusStatusCategoryName;
bool fieldsTimeoriginalestimate;
bool fieldsDescription;
string fieldsCustomfield_10011;
bool fieldsCustomfield_10012;
string fieldsCustomfield_10013;
bool fieldsCustomfield_10014;
bool fieldsCustomfield_10015;
bool fieldsSecurity;
bool fieldsCustomfield_10008;
bool fieldsAggregatetimeestimate;
bool fieldsCustomfield_10009;
string fieldsSummary;
string fieldsCreatorSelf;
string fieldsCreatorName;
string fieldsCreatorKey;
string fieldsCreatorAccountId;
string fieldsCreatorEmailAddress;
string fieldsCreatorAvatarUrls48x48;
string fieldsCreatorAvatarUrls24x24;
string fieldsCreatorAvatarUrls16x16;
string fieldsCreatorAvatarUrls32x32;
string fieldsCreatorDisplayName;
bool fieldsCreatorActive;
string fieldsCreatorTimeZone;
string fieldsReporterSelf;
string fieldsReporterName;
string fieldsReporterKey;
string fieldsReporterAccountId;
string fieldsReporterEmailAddress;
string fieldsReporterAvatarUrls48x48;
string fieldsReporterAvatarUrls24x24;
string fieldsReporterAvatarUrls16x16;
string fieldsReporterAvatarUrls32x32;
string fieldsReporterDisplayName;
bool fieldsReporterActive;
string fieldsReporterTimeZone;
string fieldsCustomfield_10000;
int fieldsAggregateprogressProgress;
int fieldsAggregateprogressTotal;
bool fieldsCustomfield_10001;
bool fieldsCustomfield_10002;
string fieldsCustomfield_10003;
bool fieldsCustomfield_10004;
bool fieldsEnvironment;
bool fieldsDuedate;
int fieldsProgressProgress;
int fieldsProgressTotal;
string fieldsVotesSelf;
int fieldsVotesVotes;
bool fieldsVotesHasVoted;
int fieldsCommentMaxResults;
int fieldsCommentTotal;
int fieldsCommentStartAt;
int fieldsWorklogStartAt;
int fieldsWorklogMaxResults;
int fieldsWorklogTotal;
int i;
int count_i;
string strVal;
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

expand = jsonResponse.StringOf("expand");
id = jsonResponse.StringOf("id");
self = jsonResponse.StringOf("self");
key = jsonResponse.StringOf("key");
fieldsIssuetypeSelf = jsonResponse.StringOf("fields.issuetype.self");
fieldsIssuetypeId = jsonResponse.StringOf("fields.issuetype.id");
fieldsIssuetypeDescription = jsonResponse.StringOf("fields.issuetype.description");
fieldsIssuetypeIconUrl = jsonResponse.StringOf("fields.issuetype.iconUrl");
fieldsIssuetypeName = jsonResponse.StringOf("fields.issuetype.name");
fieldsIssuetypeSubtask = jsonResponse.BoolOf("fields.issuetype.subtask");
fieldsTimespent = jsonResponse.IsNullOf("fields.timespent");
fieldsProjectSelf = jsonResponse.StringOf("fields.project.self");
fieldsProjectId = jsonResponse.StringOf("fields.project.id");
fieldsProjectKey = jsonResponse.StringOf("fields.project.key");
fieldsProjectName = jsonResponse.StringOf("fields.project.name");
fieldsProjectProjectTypeKey = jsonResponse.StringOf("fields.project.projectTypeKey");
fieldsProjectAvatarUrls48x48 = jsonResponse.StringOf("fields.project.avatarUrls.48x48");
fieldsProjectAvatarUrls24x24 = jsonResponse.StringOf("fields.project.avatarUrls.24x24");
fieldsProjectAvatarUrls16x16 = jsonResponse.StringOf("fields.project.avatarUrls.16x16");
fieldsProjectAvatarUrls32x32 = jsonResponse.StringOf("fields.project.avatarUrls.32x32");
fieldsProjectProjectCategorySelf = jsonResponse.StringOf("fields.project.projectCategory.self");
fieldsProjectProjectCategoryId = jsonResponse.StringOf("fields.project.projectCategory.id");
fieldsProjectProjectCategoryDescription = jsonResponse.StringOf("fields.project.projectCategory.description");
fieldsProjectProjectCategoryName = jsonResponse.StringOf("fields.project.projectCategory.name");
fieldsAggregatetimespent = jsonResponse.IsNullOf("fields.aggregatetimespent");
fieldsResolutionSelf = jsonResponse.StringOf("fields.resolution.self");
fieldsResolutionId = jsonResponse.StringOf("fields.resolution.id");
fieldsResolutionDescription = jsonResponse.StringOf("fields.resolution.description");
fieldsResolutionName = jsonResponse.StringOf("fields.resolution.name");
fieldsCustomfield_10027 = jsonResponse.StringOf("fields.customfield_10027");
fieldsCustomfield_10028 = jsonResponse.StringOf("fields.customfield_10028");
fieldsCustomfield_10029 = jsonResponse.StringOf("fields.customfield_10029");
fieldsResolutiondate = jsonResponse.StringOf("fields.resolutiondate");
fieldsWorkratio = jsonResponse.IntOf("fields.workratio");
fieldsWatchesSelf = jsonResponse.StringOf("fields.watches.self");
fieldsWatchesWatchCount = jsonResponse.IntOf("fields.watches.watchCount");
fieldsWatchesIsWatching = jsonResponse.BoolOf("fields.watches.isWatching");
fieldsLastViewed = jsonResponse.StringOf("fields.lastViewed");
fieldsCreated = jsonResponse.StringOf("fields.created");
fieldsCustomfield_10022 = jsonResponse.IsNullOf("fields.customfield_10022");
fieldsCustomfield_10023 = jsonResponse.StringOf("fields.customfield_10023");
fieldsPrioritySelf = jsonResponse.StringOf("fields.priority.self");
fieldsPriorityIconUrl = jsonResponse.StringOf("fields.priority.iconUrl");
fieldsPriorityName = jsonResponse.StringOf("fields.priority.name");
fieldsPriorityId = jsonResponse.StringOf("fields.priority.id");
fieldsCustomfield_10024 = jsonResponse.StringOf("fields.customfield_10024");
fieldsCustomfield_10025 = jsonResponse.StringOf("fields.customfield_10025");
fieldsCustomfield_10026 = jsonResponse.StringOf("fields.customfield_10026");
fieldsCustomfield_10017 = jsonResponse.IsNullOf("fields.customfield_10017");
fieldsCustomfield_10018 = jsonResponse.IsNullOf("fields.customfield_10018");
fieldsCustomfield_10019 = jsonResponse.IntOf("fields.customfield_10019");
fieldsAggregatetimeoriginalestimate = jsonResponse.IsNullOf("fields.aggregatetimeoriginalestimate");
fieldsTimeestimate = jsonResponse.IsNullOf("fields.timeestimate");
fieldsAssigneeSelf = jsonResponse.StringOf("fields.assignee.self");
fieldsAssigneeName = jsonResponse.StringOf("fields.assignee.name");
fieldsAssigneeKey = jsonResponse.StringOf("fields.assignee.key");
fieldsAssigneeAccountId = jsonResponse.StringOf("fields.assignee.accountId");
fieldsAssigneeEmailAddress = jsonResponse.StringOf("fields.assignee.emailAddress");
fieldsAssigneeAvatarUrls48x48 = jsonResponse.StringOf("fields.assignee.avatarUrls.48x48");
fieldsAssigneeAvatarUrls24x24 = jsonResponse.StringOf("fields.assignee.avatarUrls.24x24");
fieldsAssigneeAvatarUrls16x16 = jsonResponse.StringOf("fields.assignee.avatarUrls.16x16");
fieldsAssigneeAvatarUrls32x32 = jsonResponse.StringOf("fields.assignee.avatarUrls.32x32");
fieldsAssigneeDisplayName = jsonResponse.StringOf("fields.assignee.displayName");
fieldsAssigneeActive = jsonResponse.BoolOf("fields.assignee.active");
fieldsAssigneeTimeZone = jsonResponse.StringOf("fields.assignee.timeZone");
fieldsUpdated = jsonResponse.StringOf("fields.updated");
fieldsStatusSelf = jsonResponse.StringOf("fields.status.self");
fieldsStatusDescription = jsonResponse.StringOf("fields.status.description");
fieldsStatusIconUrl = jsonResponse.StringOf("fields.status.iconUrl");
fieldsStatusName = jsonResponse.StringOf("fields.status.name");
fieldsStatusId = jsonResponse.StringOf("fields.status.id");
fieldsStatusStatusCategorySelf = jsonResponse.StringOf("fields.status.statusCategory.self");
fieldsStatusStatusCategoryId = jsonResponse.IntOf("fields.status.statusCategory.id");
fieldsStatusStatusCategoryKey = jsonResponse.StringOf("fields.status.statusCategory.key");
fieldsStatusStatusCategoryColorName = jsonResponse.StringOf("fields.status.statusCategory.colorName");
fieldsStatusStatusCategoryName = jsonResponse.StringOf("fields.status.statusCategory.name");
fieldsTimeoriginalestimate = jsonResponse.IsNullOf("fields.timeoriginalestimate");
fieldsDescription = jsonResponse.IsNullOf("fields.description");
fieldsCustomfield_10011 = jsonResponse.StringOf("fields.customfield_10011");
fieldsCustomfield_10012 = jsonResponse.IsNullOf("fields.customfield_10012");
fieldsCustomfield_10013 = jsonResponse.StringOf("fields.customfield_10013");
fieldsCustomfield_10014 = jsonResponse.IsNullOf("fields.customfield_10014");
fieldsCustomfield_10015 = jsonResponse.IsNullOf("fields.customfield_10015");
fieldsSecurity = jsonResponse.IsNullOf("fields.security");
fieldsCustomfield_10008 = jsonResponse.IsNullOf("fields.customfield_10008");
fieldsAggregatetimeestimate = jsonResponse.IsNullOf("fields.aggregatetimeestimate");
fieldsCustomfield_10009 = jsonResponse.IsNullOf("fields.customfield_10009");
fieldsSummary = jsonResponse.StringOf("fields.summary");
fieldsCreatorSelf = jsonResponse.StringOf("fields.creator.self");
fieldsCreatorName = jsonResponse.StringOf("fields.creator.name");
fieldsCreatorKey = jsonResponse.StringOf("fields.creator.key");
fieldsCreatorAccountId = jsonResponse.StringOf("fields.creator.accountId");
fieldsCreatorEmailAddress = jsonResponse.StringOf("fields.creator.emailAddress");
fieldsCreatorAvatarUrls48x48 = jsonResponse.StringOf("fields.creator.avatarUrls.48x48");
fieldsCreatorAvatarUrls24x24 = jsonResponse.StringOf("fields.creator.avatarUrls.24x24");
fieldsCreatorAvatarUrls16x16 = jsonResponse.StringOf("fields.creator.avatarUrls.16x16");
fieldsCreatorAvatarUrls32x32 = jsonResponse.StringOf("fields.creator.avatarUrls.32x32");
fieldsCreatorDisplayName = jsonResponse.StringOf("fields.creator.displayName");
fieldsCreatorActive = jsonResponse.BoolOf("fields.creator.active");
fieldsCreatorTimeZone = jsonResponse.StringOf("fields.creator.timeZone");
fieldsReporterSelf = jsonResponse.StringOf("fields.reporter.self");
fieldsReporterName = jsonResponse.StringOf("fields.reporter.name");
fieldsReporterKey = jsonResponse.StringOf("fields.reporter.key");
fieldsReporterAccountId = jsonResponse.StringOf("fields.reporter.accountId");
fieldsReporterEmailAddress = jsonResponse.StringOf("fields.reporter.emailAddress");
fieldsReporterAvatarUrls48x48 = jsonResponse.StringOf("fields.reporter.avatarUrls.48x48");
fieldsReporterAvatarUrls24x24 = jsonResponse.StringOf("fields.reporter.avatarUrls.24x24");
fieldsReporterAvatarUrls16x16 = jsonResponse.StringOf("fields.reporter.avatarUrls.16x16");
fieldsReporterAvatarUrls32x32 = jsonResponse.StringOf("fields.reporter.avatarUrls.32x32");
fieldsReporterDisplayName = jsonResponse.StringOf("fields.reporter.displayName");
fieldsReporterActive = jsonResponse.BoolOf("fields.reporter.active");
fieldsReporterTimeZone = jsonResponse.StringOf("fields.reporter.timeZone");
fieldsCustomfield_10000 = jsonResponse.StringOf("fields.customfield_10000");
fieldsAggregateprogressProgress = jsonResponse.IntOf("fields.aggregateprogress.progress");
fieldsAggregateprogressTotal = jsonResponse.IntOf("fields.aggregateprogress.total");
fieldsCustomfield_10001 = jsonResponse.IsNullOf("fields.customfield_10001");
fieldsCustomfield_10002 = jsonResponse.IsNullOf("fields.customfield_10002");
fieldsCustomfield_10003 = jsonResponse.StringOf("fields.customfield_10003");
fieldsCustomfield_10004 = jsonResponse.IsNullOf("fields.customfield_10004");
fieldsEnvironment = jsonResponse.IsNullOf("fields.environment");
fieldsDuedate = jsonResponse.IsNullOf("fields.duedate");
fieldsProgressProgress = jsonResponse.IntOf("fields.progress.progress");
fieldsProgressTotal = jsonResponse.IntOf("fields.progress.total");
fieldsVotesSelf = jsonResponse.StringOf("fields.votes.self");
fieldsVotesVotes = jsonResponse.IntOf("fields.votes.votes");
fieldsVotesHasVoted = jsonResponse.BoolOf("fields.votes.hasVoted");
fieldsCommentMaxResults = jsonResponse.IntOf("fields.comment.maxResults");
fieldsCommentTotal = jsonResponse.IntOf("fields.comment.total");
fieldsCommentStartAt = jsonResponse.IntOf("fields.comment.startAt");
fieldsWorklogStartAt = jsonResponse.IntOf("fields.worklog.startAt");
fieldsWorklogMaxResults = jsonResponse.IntOf("fields.worklog.maxResults");
fieldsWorklogTotal = jsonResponse.IntOf("fields.worklog.total");
i = 0;
count_i = jsonResponse.SizeOfArray("fields.fixVersions");
while (i < count_i) {
    jsonResponse.I = i;
    i = i + 1;
}

i = 0;
count_i = jsonResponse.SizeOfArray("fields.labels");
while (i < count_i) {
    jsonResponse.I = i;
    i = i + 1;
}

i = 0;
count_i = jsonResponse.SizeOfArray("fields.customfield_10016");
while (i < count_i) {
    jsonResponse.I = i;
    i = i + 1;
}

i = 0;
count_i = jsonResponse.SizeOfArray("fields.versions");
while (i < count_i) {
    jsonResponse.I = i;
    i = i + 1;
}

i = 0;
count_i = jsonResponse.SizeOfArray("fields.issuelinks");
while (i < count_i) {
    jsonResponse.I = i;
    i = i + 1;
}

i = 0;
count_i = jsonResponse.SizeOfArray("fields.components");
while (i < count_i) {
    jsonResponse.I = i;
    i = i + 1;
}

i = 0;
count_i = jsonResponse.SizeOfArray("fields.customfield_10010");
while (i < count_i) {
    jsonResponse.I = i;
    strVal = jsonResponse.StringOf("fields.customfield_10010[i]");
    i = i + 1;
}

i = 0;
count_i = jsonResponse.SizeOfArray("fields.attachment");
while (i < count_i) {
    jsonResponse.I = i;
    i = i + 1;
}

i = 0;
count_i = jsonResponse.SizeOfArray("fields.subtasks");
while (i < count_i) {
    jsonResponse.I = i;
    i = i + 1;
}

i = 0;
count_i = jsonResponse.SizeOfArray("fields.comment.comments");
while (i < count_i) {
    jsonResponse.I = i;
    self = jsonResponse.StringOf("fields.comment.comments[i].self");
    id = jsonResponse.StringOf("fields.comment.comments[i].id");
    authorSelf = jsonResponse.StringOf("fields.comment.comments[i].author.self");
    authorName = jsonResponse.StringOf("fields.comment.comments[i].author.name");
    authorKey = jsonResponse.StringOf("fields.comment.comments[i].author.key");
    authorAccountId = jsonResponse.StringOf("fields.comment.comments[i].author.accountId");
    authorEmailAddress = jsonResponse.StringOf("fields.comment.comments[i].author.emailAddress");
    authorAvatarUrls48x48 = jsonResponse.StringOf("fields.comment.comments[i].author.avatarUrls.48x48");
    authorAvatarUrls24x24 = jsonResponse.StringOf("fields.comment.comments[i].author.avatarUrls.24x24");
    authorAvatarUrls16x16 = jsonResponse.StringOf("fields.comment.comments[i].author.avatarUrls.16x16");
    authorAvatarUrls32x32 = jsonResponse.StringOf("fields.comment.comments[i].author.avatarUrls.32x32");
    authorDisplayName = jsonResponse.StringOf("fields.comment.comments[i].author.displayName");
    authorActive = jsonResponse.BoolOf("fields.comment.comments[i].author.active");
    authorTimeZone = jsonResponse.StringOf("fields.comment.comments[i].author.timeZone");
    body = jsonResponse.StringOf("fields.comment.comments[i].body");
    updateAuthorSelf = jsonResponse.StringOf("fields.comment.comments[i].updateAuthor.self");
    updateAuthorName = jsonResponse.StringOf("fields.comment.comments[i].updateAuthor.name");
    updateAuthorKey = jsonResponse.StringOf("fields.comment.comments[i].updateAuthor.key");
    updateAuthorAccountId = jsonResponse.StringOf("fields.comment.comments[i].updateAuthor.accountId");
    updateAuthorEmailAddress = jsonResponse.StringOf("fields.comment.comments[i].updateAuthor.emailAddress");
    updateAuthorAvatarUrls48x48 = jsonResponse.StringOf("fields.comment.comments[i].updateAuthor.avatarUrls.48x48");
    updateAuthorAvatarUrls24x24 = jsonResponse.StringOf("fields.comment.comments[i].updateAuthor.avatarUrls.24x24");
    updateAuthorAvatarUrls16x16 = jsonResponse.StringOf("fields.comment.comments[i].updateAuthor.avatarUrls.16x16");
    updateAuthorAvatarUrls32x32 = jsonResponse.StringOf("fields.comment.comments[i].updateAuthor.avatarUrls.32x32");
    updateAuthorDisplayName = jsonResponse.StringOf("fields.comment.comments[i].updateAuthor.displayName");
    updateAuthorActive = jsonResponse.BoolOf("fields.comment.comments[i].updateAuthor.active");
    updateAuthorTimeZone = jsonResponse.StringOf("fields.comment.comments[i].updateAuthor.timeZone");
    created = jsonResponse.StringOf("fields.comment.comments[i].created");
    updated = jsonResponse.StringOf("fields.comment.comments[i].updated");
    i = i + 1;
}

i = 0;
count_i = jsonResponse.SizeOfArray("fields.worklog.worklogs");
while (i < count_i) {
    jsonResponse.I = i;
    i = i + 1;
}
```

## Sample JSON Body
```JSON
{
  "expand": "renderedFields,names,schema,operations,editmeta,changelog,versionedRepresentations",
  "id": "10014",
  "self": "https://chilkat.atlassian.net/rest/api/2/issue/10014",
  "key": "SCRUM-15",
  "fields": {
    "issuetype": {
      "self": "https://chilkat.atlassian.net/rest/api/2/issuetype/10001",
      "id": "10001",
      "description": "Stories track functionality or features expressed as user goals.",
      "iconUrl": "https://chilkat.atlassian.net/images/icons/issuetypes/story.svg",
      "name": "Story",
      "subtask": false
    },
    "timespent": null,
    "project": {
      "self": "https://chilkat.atlassian.net/rest/api/2/project/10000",
      "id": "10000",
      "key": "SCRUM",
      "name": "Scrumsoft",
      "projectTypeKey": "software",
      "avatarUrls": {
        "48x48": "https://chilkat.atlassian.net/secure/projectavatar?pid=10000&avatarId=10400",
        "24x24": "https://chilkat.atlassian.net/secure/projectavatar?size=small&pid=10000&avatarId=10400",
        "16x16": "https://chilkat.atlassian.net/secure/projectavatar?size=xsmall&pid=10000&avatarId=10400",
        "32x32": "https://chilkat.atlassian.net/secure/projectavatar?size=medium&pid=10000&avatarId=10400"
      },
      "projectCategory": {
        "self": "https://chilkat.atlassian.net/rest/api/2/projectCategory/10002",
        "id": "10002",
        "description": "Insane Projects",
        "name": "Insane"
      }
    },
    "fixVersions": [
    ],
    "aggregatetimespent": null,
    "resolution": {
      "self": "https://chilkat.atlassian.net/rest/api/2/resolution/10000",
      "id": "10000",
      "description": "Work has been completed on this issue.",
      "name": "Done"
    },
    "customfield_10027": "",
    "customfield_10028": "",
    "customfield_10029": "",
    "resolutiondate": "2018-04-08T00:33:55.852-0500",
    "workratio": -1,
    "watches": {
      "self": "https://chilkat.atlassian.net/rest/api/2/issue/SCRUM-15/watchers",
      "watchCount": 0,
      "isWatching": false
    },
    "lastViewed": "2018-04-12T20:07:08.181-0500",
    "created": "2018-04-03T09:57:55.852-0500",
    "customfield_10022": null,
    "customfield_10023": "",
    "priority": {
      "self": "https://chilkat.atlassian.net/rest/api/2/priority/3",
      "iconUrl": "https://chilkat.atlassian.net/images/icons/priorities/medium.svg",
      "name": "Medium",
      "id": "3"
    },
    "customfield_10024": "",
    "customfield_10025": "",
    "customfield_10026": "",
    "labels": [
    ],
    "customfield_10016": [
    ],
    "customfield_10017": null,
    "customfield_10018": null,
    "customfield_10019": 4.0,
    "aggregatetimeoriginalestimate": null,
    "timeestimate": null,
    "versions": [
    ],
    "issuelinks": [
    ],
    "assignee": {
      "self": "https://chilkat.atlassian.net/rest/api/2/user?username=matt",
      "name": "matt",
      "key": "matt",
      "accountId": "5acf82d7926ac92a7c0d7bd3",
      "emailAddress": "matt@@chilkat.io",
      "avatarUrls": {
        "48x48": "https://avatar-cdn.atlassian.com/ae220e85f283d0ecea372e06ad2261d3?s=48&d=https%3A%2F%2Fsecure.gravatar.com%2Favatar%2Fae220e85f283d0ecea372e06ad2261d3%3Fd%3Dmm%26s%3D48%26noRedirect%3Dtrue",
        "24x24": "https://avatar-cdn.atlassian.com/ae220e85f283d0ecea372e06ad2261d3?s=24&d=https%3A%2F%2Fsecure.gravatar.com%2Favatar%2Fae220e85f283d0ecea372e06ad2261d3%3Fd%3Dmm%26s%3D24%26noRedirect%3Dtrue",
        "16x16": "https://avatar-cdn.atlassian.com/ae220e85f283d0ecea372e06ad2261d3?s=16&d=https%3A%2F%2Fsecure.gravatar.com%2Favatar%2Fae220e85f283d0ecea372e06ad2261d3%3Fd%3Dmm%26s%3D16%26noRedirect%3Dtrue",
        "32x32": "https://avatar-cdn.atlassian.com/ae220e85f283d0ecea372e06ad2261d3?s=32&d=https%3A%2F%2Fsecure.gravatar.com%2Favatar%2Fae220e85f283d0ecea372e06ad2261d3%3Fd%3Dmm%26s%3D32%26noRedirect%3Dtrue"
      },
      "displayName": "Matt of Chilkat",
      "active": true,
      "timeZone": "America/Chicago"
    },
    "updated": "2018-04-12T20:07:08.104-0500",
    "status": {
      "self": "https://chilkat.atlassian.net/rest/api/2/status/10001",
      "description": "",
      "iconUrl": "https://chilkat.atlassian.net/",
      "name": "Done",
      "id": "10001",
      "statusCategory": {
        "self": "https://chilkat.atlassian.net/rest/api/2/statuscategory/3",
        "id": 3,
        "key": "done",
        "colorName": "green",
        "name": "Done"
      }
    },
    "components": [
    ],
    "timeoriginalestimate": null,
    "description": null,
    "customfield_10010": [
      "com.atlassian.greenhopper.service.sprint.Sprint@@3aaca4f7[id=1,rapidViewId=1,state=ACTIVE,name=Sample Sprint 2,goal=<null>,startDate=2018-04-03T14:57:57.335Z,endDate=2018-04-17T15:17:57.335Z,completeDate=<null>,sequence=1]"
    ],
    "customfield_10011": "0|i0000n:",
    "customfield_10012": null,
    "customfield_10013": "3_*:*_1_*:*_208320000_*|*_10000_*:*_1_*:*_189840000_*|*_10001_*:*_1_*:*_0",
    "customfield_10014": null,
    "customfield_10015": null,
    "timetracking": {},
    "security": null,
    "customfield_10008": null,
    "aggregatetimeestimate": null,
    "customfield_10009": null,
    "attachment": [
    ],
    "summary": "As a scrum master, I can see the progress of a sprint via the Burndown Chart >> Click \"Reports\" to view the Burndown Chart",
    "creator": {
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
    "subtasks": [
    ],
    "reporter": {
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
    "customfield_10000": "{}",
    "aggregateprogress": {
      "progress": 0,
      "total": 0
    },
    "customfield_10001": null,
    "customfield_10002": null,
    "customfield_10003": "",
    "customfield_10004": null,
    "environment": null,
    "duedate": null,
    "progress": {
      "progress": 0,
      "total": 0
    },
    "votes": {
      "self": "https://chilkat.atlassian.net/rest/api/2/issue/SCRUM-15/votes",
      "votes": 0,
      "hasVoted": false
    },
    "comment": {
      "comments": [
        {
          "self": "https://chilkat.atlassian.net/rest/api/2/issue/10014/comment/10006",
          "id": "10006",
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
          "body": "Joined Sample Sprint 2 7 days 9 hours 10 minutes ago",
          "updateAuthor": {
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
          "updated": "2018-04-08T00:33:55.852-0500"
        },
        {
          "self": "https://chilkat.atlassian.net/rest/api/2/issue/10014/comment/10007",
          "id": "10007",
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
          "body": "To Do to In Progress 5 days 4 hours 26 minutes ago\r\nIn Progress to Done 2 days 18 hours 34 minutes ago",
          "updateAuthor": {
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
          "updated": "2018-04-08T00:33:55.852-0500"
        }
      ],
      "maxResults": 2,
      "total": 2,
      "startAt": 0
    },
    "worklog": {
      "startAt": 0,
      "maxResults": 20,
      "total": 0,
      "worklogs": [
      ]
    }
  }
}
```

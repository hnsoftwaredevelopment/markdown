C# Jira - Issues: Search for Issues Assigned to a Particular User

---

## CURL Command

```bash
curl -X GET --user jira@example.com:JIRA_API_TOKEN \
   -H "Content-Type: application/json"  \
   https://your-domain.atlassian.net/rest/api/2/search?jql=assignee=matt
```

## C# Example

```csharp
Chilkat.Rest rest = new Chilkat.Rest();
bool success;

//  URL: https://your-domain.atlassian.net/rest/api/2/search?jql=assignee=matt
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

rest.AddHeader("Content-Type","application/json");

Chilkat.StringBuilder sbResponseBody = new Chilkat.StringBuilder();
success = rest.FullRequestNoBodySb("GET","/rest/api/2/search?jql=assignee=matt",sbResponseBody);
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
int startAt;
int maxResults;
int total;
int i;
int count_i;
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
bool fieldsCustomfield_10027;
bool fieldsCustomfield_10028;
bool fieldsCustomfield_10029;
string fieldsResolutiondate;
int fieldsWorkratio;
string fieldsWatchesSelf;
int fieldsWatchesWatchCount;
bool fieldsWatchesIsWatching;
string fieldsLastViewed;
string fieldsCreated;
bool fieldsCustomfield_10022;
string fieldsPrioritySelf;
string fieldsPriorityIconUrl;
string fieldsPriorityName;
string fieldsPriorityId;
bool fieldsCustomfield_10023;
bool fieldsCustomfield_10024;
bool fieldsCustomfield_10025;
bool fieldsCustomfield_10026;
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
int fieldsAggregateprogressProgress;
int fieldsAggregateprogressTotal;
string fieldsCustomfield_10000;
bool fieldsCustomfield_10001;
bool fieldsCustomfield_10002;
bool fieldsCustomfield_10003;
bool fieldsCustomfield_10004;
bool fieldsEnvironment;
bool fieldsDuedate;
int fieldsProgressProgress;
int fieldsProgressTotal;
string fieldsVotesSelf;
int fieldsVotesVotes;
bool fieldsVotesHasVoted;
int fieldsIssuetypeAvatarId;
string fieldsParentId;
string fieldsParentKey;
string fieldsParentSelf;
string fieldsParentFieldsSummary;
string fieldsParentFieldsStatusSelf;
string fieldsParentFieldsStatusDescription;
string fieldsParentFieldsStatusIconUrl;
string fieldsParentFieldsStatusName;
string fieldsParentFieldsStatusId;
string fieldsParentFieldsStatusStatusCategorySelf;
int fieldsParentFieldsStatusStatusCategoryId;
string fieldsParentFieldsStatusStatusCategoryKey;
string fieldsParentFieldsStatusStatusCategoryColorName;
string fieldsParentFieldsStatusStatusCategoryName;
string fieldsParentFieldsPrioritySelf;
string fieldsParentFieldsPriorityIconUrl;
string fieldsParentFieldsPriorityName;
string fieldsParentFieldsPriorityId;
string fieldsParentFieldsIssuetypeSelf;
string fieldsParentFieldsIssuetypeId;
string fieldsParentFieldsIssuetypeDescription;
string fieldsParentFieldsIssuetypeIconUrl;
string fieldsParentFieldsIssuetypeName;
bool fieldsParentFieldsIssuetypeSubtask;
bool fieldsResolution;
int j;
int count_j;
string name;
bool archived;
bool released;
string releaseDate;
string strVal;

expand = jsonResponse.StringOf("expand");
startAt = jsonResponse.IntOf("startAt");
maxResults = jsonResponse.IntOf("maxResults");
total = jsonResponse.IntOf("total");
i = 0;
count_i = jsonResponse.SizeOfArray("issues");
while (i < count_i) {
    jsonResponse.I = i;
    expand = jsonResponse.StringOf("issues[i].expand");
    id = jsonResponse.StringOf("issues[i].id");
    self = jsonResponse.StringOf("issues[i].self");
    key = jsonResponse.StringOf("issues[i].key");
    fieldsIssuetypeSelf = jsonResponse.StringOf("issues[i].fields.issuetype.self");
    fieldsIssuetypeId = jsonResponse.StringOf("issues[i].fields.issuetype.id");
    fieldsIssuetypeDescription = jsonResponse.StringOf("issues[i].fields.issuetype.description");
    fieldsIssuetypeIconUrl = jsonResponse.StringOf("issues[i].fields.issuetype.iconUrl");
    fieldsIssuetypeName = jsonResponse.StringOf("issues[i].fields.issuetype.name");
    fieldsIssuetypeSubtask = jsonResponse.BoolOf("issues[i].fields.issuetype.subtask");
    fieldsTimespent = jsonResponse.IsNullOf("issues[i].fields.timespent");
    fieldsProjectSelf = jsonResponse.StringOf("issues[i].fields.project.self");
    fieldsProjectId = jsonResponse.StringOf("issues[i].fields.project.id");
    fieldsProjectKey = jsonResponse.StringOf("issues[i].fields.project.key");
    fieldsProjectName = jsonResponse.StringOf("issues[i].fields.project.name");
    fieldsProjectProjectTypeKey = jsonResponse.StringOf("issues[i].fields.project.projectTypeKey");
    fieldsProjectAvatarUrls48x48 = jsonResponse.StringOf("issues[i].fields.project.avatarUrls.48x48");
    fieldsProjectAvatarUrls24x24 = jsonResponse.StringOf("issues[i].fields.project.avatarUrls.24x24");
    fieldsProjectAvatarUrls16x16 = jsonResponse.StringOf("issues[i].fields.project.avatarUrls.16x16");
    fieldsProjectAvatarUrls32x32 = jsonResponse.StringOf("issues[i].fields.project.avatarUrls.32x32");
    fieldsProjectProjectCategorySelf = jsonResponse.StringOf("issues[i].fields.project.projectCategory.self");
    fieldsProjectProjectCategoryId = jsonResponse.StringOf("issues[i].fields.project.projectCategory.id");
    fieldsProjectProjectCategoryDescription = jsonResponse.StringOf("issues[i].fields.project.projectCategory.description");
    fieldsProjectProjectCategoryName = jsonResponse.StringOf("issues[i].fields.project.projectCategory.name");
    fieldsAggregatetimespent = jsonResponse.IsNullOf("issues[i].fields.aggregatetimespent");
    fieldsResolutionSelf = jsonResponse.StringOf("issues[i].fields.resolution.self");
    fieldsResolutionId = jsonResponse.StringOf("issues[i].fields.resolution.id");
    fieldsResolutionDescription = jsonResponse.StringOf("issues[i].fields.resolution.description");
    fieldsResolutionName = jsonResponse.StringOf("issues[i].fields.resolution.name");
    fieldsCustomfield_10027 = jsonResponse.IsNullOf("issues[i].fields.customfield_10027");
    fieldsCustomfield_10028 = jsonResponse.IsNullOf("issues[i].fields.customfield_10028");
    fieldsCustomfield_10029 = jsonResponse.IsNullOf("issues[i].fields.customfield_10029");
    fieldsResolutiondate = jsonResponse.StringOf("issues[i].fields.resolutiondate");
    fieldsWorkratio = jsonResponse.IntOf("issues[i].fields.workratio");
    fieldsWatchesSelf = jsonResponse.StringOf("issues[i].fields.watches.self");
    fieldsWatchesWatchCount = jsonResponse.IntOf("issues[i].fields.watches.watchCount");
    fieldsWatchesIsWatching = jsonResponse.BoolOf("issues[i].fields.watches.isWatching");
    fieldsLastViewed = jsonResponse.StringOf("issues[i].fields.lastViewed");
    fieldsCreated = jsonResponse.StringOf("issues[i].fields.created");
    fieldsCustomfield_10022 = jsonResponse.IsNullOf("issues[i].fields.customfield_10022");
    fieldsPrioritySelf = jsonResponse.StringOf("issues[i].fields.priority.self");
    fieldsPriorityIconUrl = jsonResponse.StringOf("issues[i].fields.priority.iconUrl");
    fieldsPriorityName = jsonResponse.StringOf("issues[i].fields.priority.name");
    fieldsPriorityId = jsonResponse.StringOf("issues[i].fields.priority.id");
    fieldsCustomfield_10023 = jsonResponse.IsNullOf("issues[i].fields.customfield_10023");
    fieldsCustomfield_10024 = jsonResponse.IsNullOf("issues[i].fields.customfield_10024");
    fieldsCustomfield_10025 = jsonResponse.IsNullOf("issues[i].fields.customfield_10025");
    fieldsCustomfield_10026 = jsonResponse.IsNullOf("issues[i].fields.customfield_10026");
    fieldsCustomfield_10017 = jsonResponse.IsNullOf("issues[i].fields.customfield_10017");
    fieldsCustomfield_10018 = jsonResponse.IsNullOf("issues[i].fields.customfield_10018");
    fieldsCustomfield_10019 = jsonResponse.IntOf("issues[i].fields.customfield_10019");
    fieldsAggregatetimeoriginalestimate = jsonResponse.IsNullOf("issues[i].fields.aggregatetimeoriginalestimate");
    fieldsTimeestimate = jsonResponse.IsNullOf("issues[i].fields.timeestimate");
    fieldsAssigneeSelf = jsonResponse.StringOf("issues[i].fields.assignee.self");
    fieldsAssigneeName = jsonResponse.StringOf("issues[i].fields.assignee.name");
    fieldsAssigneeKey = jsonResponse.StringOf("issues[i].fields.assignee.key");
    fieldsAssigneeAccountId = jsonResponse.StringOf("issues[i].fields.assignee.accountId");
    fieldsAssigneeEmailAddress = jsonResponse.StringOf("issues[i].fields.assignee.emailAddress");
    fieldsAssigneeAvatarUrls48x48 = jsonResponse.StringOf("issues[i].fields.assignee.avatarUrls.48x48");
    fieldsAssigneeAvatarUrls24x24 = jsonResponse.StringOf("issues[i].fields.assignee.avatarUrls.24x24");
    fieldsAssigneeAvatarUrls16x16 = jsonResponse.StringOf("issues[i].fields.assignee.avatarUrls.16x16");
    fieldsAssigneeAvatarUrls32x32 = jsonResponse.StringOf("issues[i].fields.assignee.avatarUrls.32x32");
    fieldsAssigneeDisplayName = jsonResponse.StringOf("issues[i].fields.assignee.displayName");
    fieldsAssigneeActive = jsonResponse.BoolOf("issues[i].fields.assignee.active");
    fieldsAssigneeTimeZone = jsonResponse.StringOf("issues[i].fields.assignee.timeZone");
    fieldsUpdated = jsonResponse.StringOf("issues[i].fields.updated");
    fieldsStatusSelf = jsonResponse.StringOf("issues[i].fields.status.self");
    fieldsStatusDescription = jsonResponse.StringOf("issues[i].fields.status.description");
    fieldsStatusIconUrl = jsonResponse.StringOf("issues[i].fields.status.iconUrl");
    fieldsStatusName = jsonResponse.StringOf("issues[i].fields.status.name");
    fieldsStatusId = jsonResponse.StringOf("issues[i].fields.status.id");
    fieldsStatusStatusCategorySelf = jsonResponse.StringOf("issues[i].fields.status.statusCategory.self");
    fieldsStatusStatusCategoryId = jsonResponse.IntOf("issues[i].fields.status.statusCategory.id");
    fieldsStatusStatusCategoryKey = jsonResponse.StringOf("issues[i].fields.status.statusCategory.key");
    fieldsStatusStatusCategoryColorName = jsonResponse.StringOf("issues[i].fields.status.statusCategory.colorName");
    fieldsStatusStatusCategoryName = jsonResponse.StringOf("issues[i].fields.status.statusCategory.name");
    fieldsTimeoriginalestimate = jsonResponse.IsNullOf("issues[i].fields.timeoriginalestimate");
    fieldsDescription = jsonResponse.IsNullOf("issues[i].fields.description");
    fieldsCustomfield_10011 = jsonResponse.StringOf("issues[i].fields.customfield_10011");
    fieldsCustomfield_10012 = jsonResponse.IsNullOf("issues[i].fields.customfield_10012");
    fieldsCustomfield_10013 = jsonResponse.StringOf("issues[i].fields.customfield_10013");
    fieldsCustomfield_10014 = jsonResponse.IsNullOf("issues[i].fields.customfield_10014");
    fieldsCustomfield_10015 = jsonResponse.IsNullOf("issues[i].fields.customfield_10015");
    fieldsSecurity = jsonResponse.IsNullOf("issues[i].fields.security");
    fieldsCustomfield_10008 = jsonResponse.IsNullOf("issues[i].fields.customfield_10008");
    fieldsAggregatetimeestimate = jsonResponse.IsNullOf("issues[i].fields.aggregatetimeestimate");
    fieldsCustomfield_10009 = jsonResponse.IsNullOf("issues[i].fields.customfield_10009");
    fieldsSummary = jsonResponse.StringOf("issues[i].fields.summary");
    fieldsCreatorSelf = jsonResponse.StringOf("issues[i].fields.creator.self");
    fieldsCreatorName = jsonResponse.StringOf("issues[i].fields.creator.name");
    fieldsCreatorKey = jsonResponse.StringOf("issues[i].fields.creator.key");
    fieldsCreatorAccountId = jsonResponse.StringOf("issues[i].fields.creator.accountId");
    fieldsCreatorEmailAddress = jsonResponse.StringOf("issues[i].fields.creator.emailAddress");
    fieldsCreatorAvatarUrls48x48 = jsonResponse.StringOf("issues[i].fields.creator.avatarUrls.48x48");
    fieldsCreatorAvatarUrls24x24 = jsonResponse.StringOf("issues[i].fields.creator.avatarUrls.24x24");
    fieldsCreatorAvatarUrls16x16 = jsonResponse.StringOf("issues[i].fields.creator.avatarUrls.16x16");
    fieldsCreatorAvatarUrls32x32 = jsonResponse.StringOf("issues[i].fields.creator.avatarUrls.32x32");
    fieldsCreatorDisplayName = jsonResponse.StringOf("issues[i].fields.creator.displayName");
    fieldsCreatorActive = jsonResponse.BoolOf("issues[i].fields.creator.active");
    fieldsCreatorTimeZone = jsonResponse.StringOf("issues[i].fields.creator.timeZone");
    fieldsReporterSelf = jsonResponse.StringOf("issues[i].fields.reporter.self");
    fieldsReporterName = jsonResponse.StringOf("issues[i].fields.reporter.name");
    fieldsReporterKey = jsonResponse.StringOf("issues[i].fields.reporter.key");
    fieldsReporterAccountId = jsonResponse.StringOf("issues[i].fields.reporter.accountId");
    fieldsReporterEmailAddress = jsonResponse.StringOf("issues[i].fields.reporter.emailAddress");
    fieldsReporterAvatarUrls48x48 = jsonResponse.StringOf("issues[i].fields.reporter.avatarUrls.48x48");
    fieldsReporterAvatarUrls24x24 = jsonResponse.StringOf("issues[i].fields.reporter.avatarUrls.24x24");
    fieldsReporterAvatarUrls16x16 = jsonResponse.StringOf("issues[i].fields.reporter.avatarUrls.16x16");
    fieldsReporterAvatarUrls32x32 = jsonResponse.StringOf("issues[i].fields.reporter.avatarUrls.32x32");
    fieldsReporterDisplayName = jsonResponse.StringOf("issues[i].fields.reporter.displayName");
    fieldsReporterActive = jsonResponse.BoolOf("issues[i].fields.reporter.active");
    fieldsReporterTimeZone = jsonResponse.StringOf("issues[i].fields.reporter.timeZone");
    fieldsAggregateprogressProgress = jsonResponse.IntOf("issues[i].fields.aggregateprogress.progress");
    fieldsAggregateprogressTotal = jsonResponse.IntOf("issues[i].fields.aggregateprogress.total");
    fieldsCustomfield_10000 = jsonResponse.StringOf("issues[i].fields.customfield_10000");
    fieldsCustomfield_10001 = jsonResponse.IsNullOf("issues[i].fields.customfield_10001");
    fieldsCustomfield_10002 = jsonResponse.IsNullOf("issues[i].fields.customfield_10002");
    fieldsCustomfield_10003 = jsonResponse.IsNullOf("issues[i].fields.customfield_10003");
    fieldsCustomfield_10004 = jsonResponse.IsNullOf("issues[i].fields.customfield_10004");
    fieldsEnvironment = jsonResponse.IsNullOf("issues[i].fields.environment");
    fieldsDuedate = jsonResponse.IsNullOf("issues[i].fields.duedate");
    fieldsProgressProgress = jsonResponse.IntOf("issues[i].fields.progress.progress");
    fieldsProgressTotal = jsonResponse.IntOf("issues[i].fields.progress.total");
    fieldsVotesSelf = jsonResponse.StringOf("issues[i].fields.votes.self");
    fieldsVotesVotes = jsonResponse.IntOf("issues[i].fields.votes.votes");
    fieldsVotesHasVoted = jsonResponse.BoolOf("issues[i].fields.votes.hasVoted");
    fieldsIssuetypeAvatarId = jsonResponse.IntOf("issues[i].fields.issuetype.avatarId");
    fieldsParentId = jsonResponse.StringOf("issues[i].fields.parent.id");
    fieldsParentKey = jsonResponse.StringOf("issues[i].fields.parent.key");
    fieldsParentSelf = jsonResponse.StringOf("issues[i].fields.parent.self");
    fieldsParentFieldsSummary = jsonResponse.StringOf("issues[i].fields.parent.fields.summary");
    fieldsParentFieldsStatusSelf = jsonResponse.StringOf("issues[i].fields.parent.fields.status.self");
    fieldsParentFieldsStatusDescription = jsonResponse.StringOf("issues[i].fields.parent.fields.status.description");
    fieldsParentFieldsStatusIconUrl = jsonResponse.StringOf("issues[i].fields.parent.fields.status.iconUrl");
    fieldsParentFieldsStatusName = jsonResponse.StringOf("issues[i].fields.parent.fields.status.name");
    fieldsParentFieldsStatusId = jsonResponse.StringOf("issues[i].fields.parent.fields.status.id");
    fieldsParentFieldsStatusStatusCategorySelf = jsonResponse.StringOf("issues[i].fields.parent.fields.status.statusCategory.self");
    fieldsParentFieldsStatusStatusCategoryId = jsonResponse.IntOf("issues[i].fields.parent.fields.status.statusCategory.id");
    fieldsParentFieldsStatusStatusCategoryKey = jsonResponse.StringOf("issues[i].fields.parent.fields.status.statusCategory.key");
    fieldsParentFieldsStatusStatusCategoryColorName = jsonResponse.StringOf("issues[i].fields.parent.fields.status.statusCategory.colorName");
    fieldsParentFieldsStatusStatusCategoryName = jsonResponse.StringOf("issues[i].fields.parent.fields.status.statusCategory.name");
    fieldsParentFieldsPrioritySelf = jsonResponse.StringOf("issues[i].fields.parent.fields.priority.self");
    fieldsParentFieldsPriorityIconUrl = jsonResponse.StringOf("issues[i].fields.parent.fields.priority.iconUrl");
    fieldsParentFieldsPriorityName = jsonResponse.StringOf("issues[i].fields.parent.fields.priority.name");
    fieldsParentFieldsPriorityId = jsonResponse.StringOf("issues[i].fields.parent.fields.priority.id");
    fieldsParentFieldsIssuetypeSelf = jsonResponse.StringOf("issues[i].fields.parent.fields.issuetype.self");
    fieldsParentFieldsIssuetypeId = jsonResponse.StringOf("issues[i].fields.parent.fields.issuetype.id");
    fieldsParentFieldsIssuetypeDescription = jsonResponse.StringOf("issues[i].fields.parent.fields.issuetype.description");
    fieldsParentFieldsIssuetypeIconUrl = jsonResponse.StringOf("issues[i].fields.parent.fields.issuetype.iconUrl");
    fieldsParentFieldsIssuetypeName = jsonResponse.StringOf("issues[i].fields.parent.fields.issuetype.name");
    fieldsParentFieldsIssuetypeSubtask = jsonResponse.BoolOf("issues[i].fields.parent.fields.issuetype.subtask");
    fieldsResolution = jsonResponse.IsNullOf("issues[i].fields.resolution");
    j = 0;
    count_j = jsonResponse.SizeOfArray("issues[i].fields.fixVersions");
    while (j < count_j) {
        jsonResponse.J = j;
        self = jsonResponse.StringOf("issues[i].fields.fixVersions[j].self");
        id = jsonResponse.StringOf("issues[i].fields.fixVersions[j].id");
        name = jsonResponse.StringOf("issues[i].fields.fixVersions[j].name");
        archived = jsonResponse.BoolOf("issues[i].fields.fixVersions[j].archived");
        released = jsonResponse.BoolOf("issues[i].fields.fixVersions[j].released");
        releaseDate = jsonResponse.StringOf("issues[i].fields.fixVersions[j].releaseDate");
        j = j + 1;
    }

    j = 0;
    count_j = jsonResponse.SizeOfArray("issues[i].fields.labels");
    while (j < count_j) {
        jsonResponse.J = j;
        j = j + 1;
    }

    j = 0;
    count_j = jsonResponse.SizeOfArray("issues[i].fields.customfield_10016");
    while (j < count_j) {
        jsonResponse.J = j;
        j = j + 1;
    }

    j = 0;
    count_j = jsonResponse.SizeOfArray("issues[i].fields.versions");
    while (j < count_j) {
        jsonResponse.J = j;
        j = j + 1;
    }

    j = 0;
    count_j = jsonResponse.SizeOfArray("issues[i].fields.issuelinks");
    while (j < count_j) {
        jsonResponse.J = j;
        j = j + 1;
    }

    j = 0;
    count_j = jsonResponse.SizeOfArray("issues[i].fields.components");
    while (j < count_j) {
        jsonResponse.J = j;
        j = j + 1;
    }

    j = 0;
    count_j = jsonResponse.SizeOfArray("issues[i].fields.customfield_10010");
    while (j < count_j) {
        jsonResponse.J = j;
        strVal = jsonResponse.StringOf("issues[i].fields.customfield_10010[j]");
        j = j + 1;
    }

    j = 0;
    count_j = jsonResponse.SizeOfArray("issues[i].fields.subtasks");
    while (j < count_j) {
        jsonResponse.J = j;
        j = j + 1;
    }

    i = i + 1;
}
```

## Sample JSON Respond body

```json
{
  "expand": "schema,names",
  "startAt": 0,
  "maxResults": 50,
  "total": 4,
  "issues": [
    {
      "expand": "operations,versionedRepresentations,editmeta,changelog,renderedFields",
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
        "customfield_10027": null,
        "customfield_10028": null,
        "customfield_10029": null,
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
        "priority": {
          "self": "https://chilkat.atlassian.net/rest/api/2/priority/3",
          "iconUrl": "https://chilkat.atlassian.net/images/icons/priorities/medium.svg",
          "name": "Medium",
          "id": "3"
        },
        "customfield_10023": null,
        "customfield_10024": null,
        "customfield_10025": null,
        "customfield_10026": null,
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
          "com.atlassian.greenhopper.service.sprint.Sprint@@49e5007b[id=1,rapidViewId=1,state=ACTIVE,name=Sample Sprint 2,goal=<null>,startDate=2018-04-03T14:57:57.335Z,endDate=2018-04-17T15:17:57.335Z,completeDate=<null>,sequence=1]"
        ],
        "customfield_10011": "0|i0000n:",
        "customfield_10012": null,
        "customfield_10013": "3_*:*_1_*:*_208320000_*|*_10000_*:*_1_*:*_189840000_*|*_10001_*:*_1_*:*_0",
        "customfield_10014": null,
        "customfield_10015": null,
        "security": null,
        "customfield_10008": null,
        "aggregatetimeestimate": null,
        "customfield_10009": null,
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
        "aggregateprogress": {
          "progress": 0,
          "total": 0
        },
        "customfield_10000": "{}",
        "customfield_10001": null,
        "customfield_10002": null,
        "customfield_10003": null,
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
        }
      }
    },
    {
      "expand": "operations,versionedRepresentations,editmeta,changelog,renderedFields",
      "id": "10011",
      "self": "https://chilkat.atlassian.net/rest/api/2/issue/10011",
      "key": "SCRUM-12",
      "fields": {
        "issuetype": {
          "self": "https://chilkat.atlassian.net/rest/api/2/issuetype/10003",
          "id": "10003",
          "description": "The sub-task of the issue",
          "iconUrl": "https://chilkat.atlassian.net/secure/viewavatar?size=xsmall&avatarId=10316&avatarType=issuetype",
          "name": "Sub-task",
          "subtask": true,
          "avatarId": 10316
        },
        "parent": {
          "id": "10009",
          "key": "SCRUM-10",
          "self": "https://chilkat.atlassian.net/rest/api/2/issue/10009",
          "fields": {
            "summary": "As a developer, I can update story and task status with drag and drop (click the triangle at far left of this story to show sub-tasks)",
            "status": {
              "self": "https://chilkat.atlassian.net/rest/api/2/status/3",
              "description": "This issue is being actively worked on at the moment by the assignee.",
              "iconUrl": "https://chilkat.atlassian.net/images/icons/statuses/inprogress.png",
              "name": "In Progress",
              "id": "3",
              "statusCategory": {
                "self": "https://chilkat.atlassian.net/rest/api/2/statuscategory/4",
                "id": 4,
                "key": "indeterminate",
                "colorName": "yellow",
                "name": "In Progress"
              }
            },
            "priority": {
              "self": "https://chilkat.atlassian.net/rest/api/2/priority/3",
              "iconUrl": "https://chilkat.atlassian.net/images/icons/priorities/medium.svg",
              "name": "Medium",
              "id": "3"
            },
            "issuetype": {
              "self": "https://chilkat.atlassian.net/rest/api/2/issuetype/10001",
              "id": "10001",
              "description": "Stories track functionality or features expressed as user goals.",
              "iconUrl": "https://chilkat.atlassian.net/images/icons/issuetypes/story.svg",
              "name": "Story",
              "subtask": false
            }
          }
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
          {
            "self": "https://chilkat.atlassian.net/rest/api/2/version/10001",
            "id": "10001",
            "name": "Version 2.0",
            "archived": false,
            "released": false,
            "releaseDate": "2018-04-17"
          }
        ],
        "aggregatetimespent": null,
        "resolution": null,
        "customfield_10027": null,
        "customfield_10028": null,
        "customfield_10029": null,
        "resolutiondate": null,
        "workratio": -1,
        "watches": {
          "self": "https://chilkat.atlassian.net/rest/api/2/issue/SCRUM-12/watchers",
          "watchCount": 0,
          "isWatching": false
        },
        "lastViewed": "2018-04-12T20:06:07.155-0500",
        "created": "2018-04-07T19:24:55.852-0500",
        "customfield_10022": null,
        "priority": {
          "self": "https://chilkat.atlassian.net/rest/api/2/priority/3",
          "iconUrl": "https://chilkat.atlassian.net/images/icons/priorities/medium.svg",
          "name": "Medium",
          "id": "3"
        },
        "customfield_10023": null,
        "customfield_10024": null,
        "customfield_10025": null,
        "customfield_10026": null,
        "labels": [
        ],
        "customfield_10016": [
        ],
        "customfield_10017": null,
        "customfield_10018": null,
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
        "updated": "2018-04-12T20:06:06.924-0500",
        "status": {
          "self": "https://chilkat.atlassian.net/rest/api/2/status/3",
          "description": "This issue is being actively worked on at the moment by the assignee.",
          "iconUrl": "https://chilkat.atlassian.net/images/icons/statuses/inprogress.png",
          "name": "In Progress",
          "id": "3",
          "statusCategory": {
            "self": "https://chilkat.atlassian.net/rest/api/2/statuscategory/4",
            "id": 4,
            "key": "indeterminate",
            "colorName": "yellow",
            "name": "In Progress"
          }
        },
        "components": [
        ],
        "timeoriginalestimate": null,
        "description": null,
        "customfield_10010": [
          "com.atlassian.greenhopper.service.sprint.Sprint@@49e5007b[id=1,rapidViewId=1,state=ACTIVE,name=Sample Sprint 2,goal=<null>,startDate=2018-04-03T14:57:57.335Z,endDate=2018-04-17T15:17:57.335Z,completeDate=<null>,sequence=1]"
        ],
        "customfield_10011": "0|i0000f:",
        "customfield_10012": null,
        "customfield_10013": null,
        "customfield_10014": null,
        "customfield_10015": null,
        "security": null,
        "customfield_10008": null,
        "aggregatetimeestimate": null,
        "customfield_10009": null,
        "summary": "When the last task is done, the story can be automatically closed >> Drag this task to \"Done\" too",
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
        "customfield_10003": null,
        "customfield_10004": null,
        "environment": null,
        "duedate": null,
        "progress": {
          "progress": 0,
          "total": 0
        },
        "votes": {
          "self": "https://chilkat.atlassian.net/rest/api/2/issue/SCRUM-12/votes",
          "votes": 0,
          "hasVoted": false
        }
      }
    },
    {
      "expand": "operations,versionedRepresentations,editmeta,changelog,renderedFields",
      "id": "10007",
      "self": "https://chilkat.atlassian.net/rest/api/2/issue/10007",
      "key": "SCRUM-8",
      "fields": {
        "issuetype": {
          "self": "https://chilkat.atlassian.net/rest/api/2/issuetype/10004",
          "id": "10004",
          "description": "A problem which impairs or prevents the functions of the product.",
          "iconUrl": "https://chilkat.atlassian.net/secure/viewavatar?size=xsmall&avatarId=10303&avatarType=issuetype",
          "name": "Bug",
          "subtask": false,
          "avatarId": 10303
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
          {
            "self": "https://chilkat.atlassian.net/rest/api/2/version/10001",
            "id": "10001",
            "name": "Version 2.0",
            "archived": false,
            "released": false,
            "releaseDate": "2018-04-17"
          }
        ],
        "aggregatetimespent": null,
        "resolution": null,
        "customfield_10027": "",
        "customfield_10028": "",
        "customfield_10029": "",
        "resolutiondate": null,
        "workratio": -1,
        "watches": {
          "self": "https://chilkat.atlassian.net/rest/api/2/issue/SCRUM-8/watchers",
          "watchCount": 0,
          "isWatching": false
        },
        "lastViewed": "2018-04-12T20:06:45.967-0500",
        "created": "2018-04-10T19:07:57.258-0500",
        "customfield_10022": null,
        "priority": {
          "self": "https://chilkat.atlassian.net/rest/api/2/priority/3",
          "iconUrl": "https://chilkat.atlassian.net/images/icons/priorities/medium.svg",
          "name": "Medium",
          "id": "3"
        },
        "customfield_10023": "",
        "customfield_10024": "",
        "customfield_10025": "",
        "labels": [
        ],
        "customfield_10026": "",
        "customfield_10016": [
        ],
        "customfield_10017": null,
        "customfield_10018": null,
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
        "updated": "2018-04-12T20:06:45.784-0500",
        "status": {
          "self": "https://chilkat.atlassian.net/rest/api/2/status/10000",
          "description": "",
          "iconUrl": "https://chilkat.atlassian.net/",
          "name": "To Do",
          "id": "10000",
          "statusCategory": {
            "self": "https://chilkat.atlassian.net/rest/api/2/statuscategory/2",
            "id": 2,
            "key": "new",
            "colorName": "blue-gray",
            "name": "To Do"
          }
        },
        "components": [
        ],
        "timeoriginalestimate": null,
        "description": "*Estimation of Bugs*\n\nScrum teams do not normally apply story point estimates to bugs because bugs are considered to be part of the ongoing work that the team must deal with (i.e the overhead). If you view the story points completed in a sprint as a measure of progress, then bugs also have no value because they do not deliver anything additional to the customer. \n\nHowever, you can apply estimates to bugs if you wish by configuring the \"Story Points\" field to apply to other Issue Types (by default it only applies to Stories and Epics). Some more information on this is in the [documentation|https://confluence.atlassian.com/display/GH/Story+Point].",
        "customfield_10010": [
        ],
        "customfield_10011": "0|hzzzzz:",
        "customfield_10012": null,
        "customfield_10013": null,
        "customfield_10014": null,
        "customfield_10015": null,
        "security": null,
        "customfield_10008": null,
        "customfield_10009": null,
        "aggregatetimeestimate": null,
        "summary": "As a product owner, I'd like to include bugs, tasks and other issue types in my backlog >> Bugs like this one will also appear in your backlog but they are not normally estimated",
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
        "aggregateprogress": {
          "progress": 0,
          "total": 0
        },
        "customfield_10000": "{}",
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
          "self": "https://chilkat.atlassian.net/rest/api/2/issue/SCRUM-8/votes",
          "votes": 0,
          "hasVoted": false
        }
      }
    },
    {
      "expand": "operations,versionedRepresentations,editmeta,changelog,renderedFields",
      "id": "10003",
      "self": "https://chilkat.atlassian.net/rest/api/2/issue/10003",
      "key": "SCRUM-4",
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
          {
            "self": "https://chilkat.atlassian.net/rest/api/2/version/10002",
            "id": "10002",
            "name": "Version 3.0",
            "archived": false,
            "released": false
          }
        ],
        "aggregatetimespent": null,
        "resolution": null,
        "customfield_10027": null,
        "customfield_10028": null,
        "customfield_10029": null,
        "resolutiondate": null,
        "workratio": -1,
        "lastViewed": "2018-04-12T20:06:29.315-0500",
        "watches": {
          "self": "https://chilkat.atlassian.net/rest/api/2/issue/SCRUM-4/watchers",
          "watchCount": 0,
          "isWatching": false
        },
        "created": "2018-04-10T19:07:57.082-0500",
        "customfield_10022": null,
        "priority": {
          "self": "https://chilkat.atlassian.net/rest/api/2/priority/3",
          "iconUrl": "https://chilkat.atlassian.net/images/icons/priorities/medium.svg",
          "name": "Medium",
          "id": "3"
        },
        "customfield_10023": null,
        "customfield_10024": null,
        "customfield_10025": null,
        "customfield_10026": null,
        "labels": [
        ],
        "customfield_10016": [
        ],
        "customfield_10017": null,
        "customfield_10018": null,
        "customfield_10019": 5.0,
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
        "updated": "2018-04-12T20:06:29.215-0500",
        "status": {
          "self": "https://chilkat.atlassian.net/rest/api/2/status/10000",
          "description": "",
          "iconUrl": "https://chilkat.atlassian.net/",
          "name": "To Do",
          "id": "10000",
          "statusCategory": {
            "self": "https://chilkat.atlassian.net/rest/api/2/statuscategory/2",
            "id": 2,
            "key": "new",
            "colorName": "blue-gray",
            "name": "To Do"
          }
        },
        "components": [
        ],
        "timeoriginalestimate": null,
        "description": "This story is estimated at 5 Story Points (as shown in the \"Estimate\" field at the top right of the Detail View). \n\nTry updating the Story Point estimate to 4 by clicking on the \"Estimate\" then typing.\n\n*Estimating using Story Points*\n\nBecause the traditional process of estimating tasks in weeks or days is often wildly inaccurate, many Scrum teams estimate in Story Points instead. Story Points exist merely as a way to estimate a task's difficulty compared to some other task (for example, a 10-point story would probably take double the effort of a 5-point story). As teams mature with Scrum they tend to achieve a consistent number of Story Points from Sprint to Sprint -- this is termed the team's _velocity_. This allows the Product Owner to use the velocity to predict how many Sprints it will take to deliver parts of the backlog. \n\nMany teams use Planning Poker to achieve consensus on Story Point estimates.\n\n*Using Other Estimation Units*\n\nYou can configure JIRA Software to use time-based estimates if you wish. In the configuration for the board, on the \"Estimation\" tab, select \"Original Time Estimate\" as your Estimation Statistic. If you also wish to track the time used during the Sprint, select \"Remaining Estimate and Time Spent\" to enable Time Tracking in JIRA Software.",
        "customfield_10010": [
        ],
        "customfield_10011": "0|i00007:",
        "customfield_10012": null,
        "customfield_10013": null,
        "customfield_10014": null,
        "customfield_10015": null,
        "security": null,
        "customfield_10008": null,
        "aggregatetimeestimate": null,
        "customfield_10009": null,
        "summary": "As a team, I'd like to estimate the effort of a story in Story Points so we can understand the work remaining >> Try setting the Story Points for this story in the \"Estimate\" field",
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
        "customfield_10003": null,
        "customfield_10004": null,
        "environment": null,
        "duedate": null,
        "progress": {
          "progress": 0,
          "total": 0
        },
        "votes": {
          "self": "https://chilkat.atlassian.net/rest/api/2/issue/SCRUM-4/votes",
          "votes": 0,
          "hasVoted": false
        }
      }
    }
  ]
}
```
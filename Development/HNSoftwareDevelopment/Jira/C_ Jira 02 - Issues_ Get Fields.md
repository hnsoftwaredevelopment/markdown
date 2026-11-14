C# Jira 02 - Issues: Get Fields

C# Jira - Issues: Get Fields
***
## CURL Command
```CURL
curl --user jira@example.com:JIRA_API_TOKEN \
  --header 'Accept: application/json' \
  --url 'https://your-domain.atlassian.net/rest/api/2/field'
```

## C# Example
```C#
Chilkat.Rest rest = new Chilkat.Rest();
bool success;

//  URL: https://your-domain.atlassian.net/rest/api/2/field
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
success = rest.FullRequestNoBodySb("GET","/rest/api/2/field",sbResponseBody);
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

Chilkat.JsonArray jsonResponse = new Chilkat.JsonArray();
jsonResponse.LoadSb(sbResponseBody);

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
```JSON

  },
  {
    "id": "fixVersions",
    "key": "fixVersions",
    "name": "Fix Version/s",
    "custom": false,
    "orderable": true,
    "navigable": true,
    "searchable": true,
    "clauseNames": [
      "fixVersion"
    ],
    "schema": {
      "type": "array",
      "items": "version",
      "system": "fixVersions"
    }
  },
  {
    "id": "aggregatetimespent",
    "key": "aggregatetimespent",
    "name": "Σ Time Spent",
    "custom": false,
    "orderable": false,
    "navigable": true,
    "searchable": false,
    "clauseNames": [
    ],
    "schema": {
      "type": "number",
      "system": "aggregatetimespent"
    }
  },
  {
    "id": "resolution",
    "key": "resolution",
    "name": "Resolution",
    "custom": false,
    "orderable": true,
    "navigable": true,
    "searchable": true,
    "clauseNames": [
      "resolution"
    ],
    "schema": {
      "type": "resolution",
      "system": "resolution"
    }
  },
  {
    "id": "customfield_10027",
    "key": "customfield_10027",
    "name": "Capture for JIRA URL",
    "custom": true,
    "orderable": true,
    "navigable": true,
    "searchable": true,
    "clauseNames": [
      "Capture for JIRA URL",
      "cf[10027]"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.bonfire.plugin:bonfire-text",
      "customId": 10027
    }
  },
  {
    "id": "customfield_10028",
    "key": "customfield_10028",
    "name": "Capture for JIRA screen resolution",
    "custom": true,
    "orderable": true,
    "navigable": true,
    "searchable": true,
    "clauseNames": [
      "Capture for JIRA screen resolution",
      "cf[10028]"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.bonfire.plugin:bonfire-text",
      "customId": 10028
    }
  },
  {
    "id": "customfield_10029",
    "key": "customfield_10029",
    "name": "Capture for JIRA jQuery version",
    "custom": true,
    "orderable": true,
    "navigable": true,
    "searchable": true,
    "clauseNames": [
      "Capture for JIRA jQuery version",
      "cf[10029]"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.bonfire.plugin:bonfire-text",
      "customId": 10029
    }
  },
  {
    "id": "resolutiondate",
    "key": "resolutiondate",
    "name": "Resolved",
    "custom": false,
    "orderable": false,
    "navigable": true,
    "searchable": true,
    "clauseNames": [
      "resolutiondate",
      "resolved"
    ],
    "schema": {
      "type": "datetime",
      "system": "resolutiondate"
    }
  },
  {
    "id": "workratio",
    "key": "workratio",
    "name": "Work Ratio",
    "custom": false,
    "orderable": false,
    "navigable": true,
    "searchable": true,
    "clauseNames": [
      "workratio"
    ],
    "schema": {
      "type": "number",
      "system": "workratio"
    }
  },
  {
    "id": "lastViewed",
    "key": "lastViewed",
    "name": "Last Viewed",
    "custom": false,
    "orderable": false,
    "navigable": true,
    "searchable": false,
    "clauseNames": [
      "lastViewed"
    ],
    "schema": {
      "type": "datetime",
      "system": "lastViewed"
    }
  },
  {
    "id": "watches",
    "key": "watches",
    "name": "Watchers",
    "custom": false,
    "orderable": false,
    "navigable": true,
    "searchable": false,
    "clauseNames": [
      "watchers"
    ],
    "schema": {
      "type": "watches",
      "system": "watches"
    }
  },
  {
    "id": "thumbnail",
    "key": "thumbnail",
    "name": "Images",
    "custom": false,
    "orderable": false,
    "navigable": true,
    "searchable": false,
    "clauseNames": [
    ]
  },
  {
    "id": "created",
    "key": "created",
    "name": "Created",
    "custom": false,
    "orderable": false,
    "navigable": true,
    "searchable": true,
    "clauseNames": [
      "created",
      "createdDate"
    ],
    "schema": {
      "type": "datetime",
      "system": "created"
    }
  },
  {
    "id": "customfield_10022",
    "key": "customfield_10022",
    "name": "Flagged",
    "custom": true,
    "orderable": true,
    "navigable": true,
    "searchable": true,
    "clauseNames": [
      "cf[10022]",
      "Flagged"
    ],
    "schema": {
      "type": "array",
      "items": "option",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:multicheckboxes",
      "customId": 10022
    }
  },
  {
    "id": "priority",
    "key": "priority",
    "name": "Priority",
    "custom": false,
    "orderable": true,
    "navigable": true,
    "searchable": true,
    "clauseNames": [
      "priority"
    ],
    "schema": {
      "type": "priority",
      "system": "priority"
    }
  },
  {
    "id": "customfield_10023",
    "key": "customfield_10023",
    "name": "Raised during",
    "custom": true,
    "orderable": true,
    "navigable": true,
    "searchable": true,
    "clauseNames": [
      "cf[10023]",
      "Raised during"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.bonfire.plugin:bonfire-session-cft",
      "customId": 10023
    }
  },
  {
    "id": "customfield_10024",
    "key": "customfield_10024",
    "name": "Capture for JIRA user agent",
    "custom": true,
    "orderable": true,
    "navigable": true,
    "searchable": true,
    "clauseNames": [
      "Capture for JIRA user agent",
      "cf[10024]"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.bonfire.plugin:bonfire-text",
      "customId": 10024
    }
  },
  {
    "id": "customfield_10025",
    "key": "customfield_10025",
    "name": "Capture for JIRA browser",
    "custom": true,
    "orderable": true,
    "navigable": true,
    "searchable": true,
    "clauseNames": [
      "Capture for JIRA browser",
      "cf[10025]"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.bonfire.plugin:bonfire-text",
      "customId": 10025
    }
  },
  {
    "id": "labels",
    "key": "labels",
    "name": "Labels",
    "custom": false,
    "orderable": true,
    "navigable": true,
    "searchable": true,
    "clauseNames": [
      "labels"
    ],
    "schema": {
      "type": "array",
      "items": "string",
      "system": "labels"
    }
  },
  {
    "id": "customfield_10026",
    "key": "customfield_10026",
    "name": "Capture for JIRA operating system",
    "custom": true,
    "orderable": true,
    "navigable": true,
    "searchable": true,
    "clauseNames": [
      "Capture for JIRA operating system",
      "cf[10026]"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.bonfire.plugin:bonfire-text",
      "customId": 10026
    }
  },
  {
    "id": "customfield_10016",
    "key": "customfield_10016",
    "name": "Request participants",
    "custom": true,
    "orderable": true,
    "navigable": true,
    "searchable": true,
    "clauseNames": [
      "cf[10016]",
      "Request participants"
    ],
    "schema": {
      "type": "array",
      "items": "user",
      "custom": "com.atlassian.servicedesk:sd-request-participants",
      "customId": 10016
    }
  },
  {
    "id": "customfield_10017",
    "key": "customfield_10017",
    "name": "Satisfaction",
    "custom": true,
    "orderable": true,
    "navigable": true,
    "searchable": true,
    "clauseNames": [
      "cf[10017]",
      "Satisfaction"
    ],
    "schema": {
      "type": "sd-feedback",
      "custom": "com.atlassian.servicedesk:sd-request-feedback",
      "customId": 10017
    }
  },
  {
    "id": "customfield_10018",
    "key": "customfield_10018",
    "name": "Satisfaction date",
    "custom": true,
    "orderable": true,
    "navigable": true,
    "searchable": true,
    "clauseNames": [
      "cf[10018]",
      "Satisfaction date"
    ],
    "schema": {
      "type": "datetime",
      "custom": "com.atlassian.servicedesk:sd-request-feedback-date",
      "customId": 10018
    }
  },
  {
    "id": "customfield_10019",
    "key": "customfield_10019",
    "name": "Story Points",
    "custom": true,
    "orderable": true,
    "navigable": true,
    "searchable": true,
    "clauseNames": [
      "cf[10019]",
      "Story Points"
    ],
    "schema": {
      "type": "number",
      "custom": "com.atlassian.jira.plugin.system.customfieldtypes:float",
      "customId": 10019
    }
  },
  {
    "id": "timeestimate",
    "key": "timeestimate",
    "name": "Remaining Estimate",
    "custom": false,
    "orderable": false,
    "navigable": true,
    "searchable": false,
    "clauseNames": [
      "remainingEstimate",
      "timeestimate"
    ],
    "schema": {
      "type": "number",
      "system": "timeestimate"
    }
  },
  {
    "id": "aggregatetimeoriginalestimate",
    "key": "aggregatetimeoriginalestimate",
    "name": "Σ Original Estimate",
    "custom": false,
    "orderable": false,
    "navigable": true,
    "searchable": false,
    "clauseNames": [
    ],
    "schema": {
      "type": "number",
      "system": "aggregatetimeoriginalestimate"
    }
  },
  {
    "id": "versions",
    "key": "versions",
    "name": "Affects Version/s",
    "custom": false,
    "orderable": true,
    "navigable": true,
    "searchable": true,
    "clauseNames": [
      "affectedVersion"
    ],
    "schema": {
      "type": "array",
      "items": "version",
      "system": "versions"
    }
  },
  {
    "id": "issuelinks",
    "key": "issuelinks",
    "name": "Linked Issues",
    "custom": false,
    "orderable": true,
    "navigable": true,
    "searchable": true,
    "clauseNames": [
    ],
    "schema": {
      "type": "array",
      "items": "issuelinks",
      "system": "issuelinks"
    }
  },
  {
    "id": "assignee",
    "key": "assignee",
    "name": "Assignee",
    "custom": false,
    "orderable": true,
    "navigable": true,
    "searchable": true,
    "clauseNames": [
      "assignee"
    ],
    "schema": {
      "type": "user",
      "system": "assignee"
    }
  },
  {
    "id": "updated",
    "key": "updated",
    "name": "Updated",
    "custom": false,
    "orderable": false,
    "navigable": true,
    "searchable": true,
    "clauseNames": [
      "updated",
      "updatedDate"
    ],
    "schema": {
      "type": "datetime",
      "system": "updated"
    }
  },
  {
    "id": "status",
    "key": "status",
    "name": "Status",
    "custom": false,
    "orderable": false,
    "navigable": true,
    "searchable": true,
    "clauseNames": [
      "status"
    ],
    "schema": {
      "type": "status",
      "system": "status"
    }
  },
  {
    "id": "components",
    "key": "components",
    "name": "Component/s",
    "custom": false,
    "orderable": true,
    "navigable": true,
    "searchable": true,
    "clauseNames": [
      "component"
    ],
    "schema": {
      "type": "array",
      "items": "component",
      "system": "components"
    }
  },
  {
    "id": "issuekey",
    "key": "issuekey",
    "name": "Key",
    "custom": false,
    "orderable": false,
    "navigable": true,
    "searchable": false,
    "clauseNames": [
      "id",
      "issue",
      "issuekey",
      "key"
    ]
  },
  {
    "id": "timeoriginalestimate",
    "key": "timeoriginalestimate",
    "name": "Original Estimate",
    "custom": false,
    "orderable": false,
    "navigable": true,
    "searchable": false,
    "clauseNames": [
      "originalEstimate",
      "timeoriginalestimate"
    ],
    "schema": {
      "type": "number",
      "system": "timeoriginalestimate"
    }
  },
  {
    "id": "description",
    "key": "description",
    "name": "Description",
    "custom": false,
    "orderable": true,
    "navigable": true,
    "searchable": true,
    "clauseNames": [
      "description"
    ],
    "schema": {
      "type": "string",
      "system": "description"
    }
  },
  {
    "id": "customfield_10010",
    "key": "customfield_10010",
    "name": "Sprint",
    "custom": true,
    "orderable": true,
    "navigable": true,
    "searchable": true,
    "clauseNames": [
      "cf[10010]",
      "Sprint"
    ],
    "schema": {
      "type": "array",
      "items": "string",
      "custom": "com.pyxis.greenhopper.jira:gh-sprint",
      "customId": 10010
    }
  },
  {
    "id": "customfield_10011",
    "key": "customfield_10011",
    "name": "Rank",
    "custom": true,
    "orderable": true,
    "navigable": true,
    "searchable": true,
    "clauseNames": [
      "cf[10011]",
      "Rank"
    ],
    "schema": {
      "type": "any",
      "custom": "com.pyxis.greenhopper.jira:gh-lexo-rank",
      "customId": 10011
    }
  },
  {
    "id": "customfield_10012",
    "key": "customfield_10012",
    "name": "[CHART] Date of First Response",
    "custom": true,
    "orderable": true,
    "navigable": true,
    "searchable": true,
    "clauseNames": [
      "[CHART] Date of First Response",
      "cf[10012]"
    ],
    "schema": {
      "type": "datetime",
      "custom": "com.atlassian.jira.ext.charting:firstresponsedate",
      "customId": 10012
    }
  },
  {
    "id": "customfield_10013",
    "key": "customfield_10013",
    "name": "[CHART] Time in Status",
    "custom": true,
    "orderable": true,
    "navigable": true,
    "searchable": true,
    "clauseNames": [
      "[CHART] Time in Status",
      "cf[10013]"
    ],
    "schema": {
      "type": "any",
      "custom": "com.atlassian.jira.ext.charting:timeinstatus",
      "customId": 10013
    }
  },
  {
    "id": "customfield_10014",
    "key": "customfield_10014",
    "name": "Approvals",
    "custom": true,
    "orderable": true,
    "navigable": true,
    "searchable": true,
    "clauseNames": [
      "Approvals",
      "cf[10014]"
    ],
    "schema": {
      "type": "sd-approvals",
      "custom": "com.atlassian.servicedesk.approvals-plugin:sd-approvals",
      "customId": 10014
    }
  },
  {
    "id": "timetracking",
    "key": "timetracking",
    "name": "Time Tracking",
    "custom": false,
    "orderable": true,
    "navigable": false,
    "searchable": true,
    "clauseNames": [
    ],
    "schema": {
      "type": "timetracking",
      "system": "timetracking"
    }
  },
  {
    "id": "customfield_10015",
    "key": "customfield_10015",
    "name": "Request Type",
    "custom": true,
    "orderable": true,
    "navigable": true,
    "searchable": true,
    "clauseNames": [
      "cf[10015]",
      "Request Type"
    ],
    "schema": {
      "type": "sd-customerrequesttype",
      "custom": "com.atlassian.servicedesk:vp-origin",
      "customId": 10015
    }
  },
  {
    "id": "customfield_10005",
    "key": "customfield_10005",
    "name": "Epic Name",
    "custom": true,
    "orderable": true,
    "navigable": true,
    "searchable": true,
    "clauseNames": [
      "cf[10005]",
      "Epic Name"
    ],
    "schema": {
      "type": "string",
      "custom": "com.pyxis.greenhopper.jira:gh-epic-label",
      "customId": 10005
    }
  },
  {
    "id": "customfield_10006",
    "key": "customfield_10006",
    "name": "Epic Status",
    "custom": true,
    "orderable": true,
    "navigable": true,
    "searchable": true,
    "clauseNames": [
      "cf[10006]",
      "Epic Status"
    ],
    "schema": {
      "type": "option",
      "custom": "com.pyxis.greenhopper.jira:gh-epic-status",
      "customId": 10006
    }
  },
  {
    "id": "security",
    "key": "security",
    "name": "Security Level",
    "custom": false,
    "orderable": true,
    "navigable": true,
    "searchable": true,
    "clauseNames": [
      "level"
    ],
    "schema": {
      "type": "securitylevel",
      "system": "security"
    }
  },
  {
    "id": "customfield_10007",
    "key": "customfield_10007",
    "name": "Epic Colour",
    "custom": true,
    "orderable": true,
    "navigable": true,
    "searchable": true,
    "clauseNames": [
      "cf[10007]",
      "Epic Colour"
    ],
    "schema": {
      "type": "string",
      "custom": "com.pyxis.greenhopper.jira:gh-epic-color",
      "customId": 10007
    }
  },
  {
    "id": "customfield_10008",
    "key": "customfield_10008",
    "name": "Epic Link",
    "custom": true,
    "orderable": true,
    "navigable": true,
    "searchable": true,
    "clauseNames": [
      "cf[10008]",
      "Epic Link"
    ],
    "schema": {
      "type": "any",
      "custom": "com.pyxis.greenhopper.jira:gh-epic-link",
      "customId": 10008
    }
  },
  {
    "id": "attachment",
    "key": "attachment",
    "name": "Attachment",
    "custom": false,
    "orderable": true,
    "navigable": false,
    "searchable": true,
    "clauseNames": [
      "attachments"
    ],
    "schema": {
      "type": "array",
      "items": "attachment",
      "system": "attachment"
    }
  },
  {
    "id": "aggregatetimeestimate",
    "key": "aggregatetimeestimate",
    "name": "Σ Remaining Estimate",
    "custom": false,
    "orderable": false,
    "navigable": true,
    "searchable": false,
    "clauseNames": [
    ],
    "schema": {
      "type": "number",
      "system": "aggregatetimeestimate"
    }
  },
  {
    "id": "customfield_10009",
    "key": "customfield_10009",
    "name": "Parent Link",
    "custom": true,
    "orderable": true,
    "navigable": true,
    "searchable": true,
    "clauseNames": [
      "cf[10009]",
      "Parent Link"
    ],
    "schema": {
      "type": "any",
      "custom": "com.atlassian.jpo:jpo-custom-field-parent",
      "customId": 10009
    }
  },
  {
    "id": "summary",
    "key": "summary",
    "name": "Summary",
    "custom": false,
    "orderable": true,
    "navigable": true,
    "searchable": true,
    "clauseNames": [
      "summary"
    ],
    "schema": {
      "type": "string",
      "system": "summary"
    }
  },
  {
    "id": "creator",
    "key": "creator",
    "name": "Creator",
    "custom": false,
    "orderable": false,
    "navigable": true,
    "searchable": true,
    "clauseNames": [
      "creator"
    ],
    "schema": {
      "type": "user",
      "system": "creator"
    }
  },
  {
    "id": "subtasks",
    "key": "subtasks",
    "name": "Sub-tasks",
    "custom": false,
    "orderable": false,
    "navigable": true,
    "searchable": false,
    "clauseNames": [
      "subtasks"
    ],
    "schema": {
      "type": "array",
      "items": "issuelinks",
      "system": "subtasks"
    }
  },
  {
    "id": "reporter",
    "key": "reporter",
    "name": "Reporter",
    "custom": false,
    "orderable": true,
    "navigable": true,
    "searchable": true,
    "clauseNames": [
      "reporter"
    ],
    "schema": {
      "type": "user",
      "system": "reporter"
    }
  },
  {
    "id": "aggregateprogress",
    "key": "aggregateprogress",
    "name": "Σ Progress",
    "custom": false,
    "orderable": false,
    "navigable": true,
    "searchable": false,
    "clauseNames": [
    ],
    "schema": {
      "type": "progress",
      "system": "aggregateprogress"
    }
  },
  {
    "id": "customfield_10000",
    "key": "customfield_10000",
    "name": "Development",
    "custom": true,
    "orderable": true,
    "navigable": true,
    "searchable": true,
    "clauseNames": [
      "cf[10000]",
      "development"
    ],
    "schema": {
      "type": "any",
      "custom": "com.atlassian.jira.plugins.jira-development-integration-plugin:devsummarycf",
      "customId": 10000
    }
  },
  {
    "id": "customfield_10001",
    "key": "customfield_10001",
    "name": "Team",
    "custom": true,
    "orderable": true,
    "navigable": true,
    "searchable": true,
    "clauseNames": [
      "cf[10001]",
      "Team"
    ],
    "schema": {
      "type": "any",
      "custom": "com.atlassian.teams:rm-teams-custom-field-team",
      "customId": 10001
    }
  },
  {
    "id": "customfield_10002",
    "key": "customfield_10002",
    "name": "Testing status",
    "custom": true,
    "orderable": true,
    "navigable": true,
    "searchable": true,
    "clauseNames": [
      "cf[10002]",
      "Testing status"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.bonfire.plugin:bonfire-testing-status-cft",
      "customId": 10002
    }
  },
  {
    "id": "customfield_10003",
    "key": "customfield_10003",
    "name": "Test sessions",
    "custom": true,
    "orderable": true,
    "navigable": true,
    "searchable": true,
    "clauseNames": [
      "cf[10003]",
      "Test sessions"
    ],
    "schema": {
      "type": "string",
      "custom": "com.atlassian.bonfire.plugin:bonfire-multi-session-cft",
      "customId": 10003
    }
  },
  {
    "id": "customfield_10004",
    "key": "customfield_10004",
    "name": "Organizations",
    "custom": true,
    "orderable": true,
    "navigable": true,
    "searchable": true,
    "clauseNames": [
      "cf[10004]",
      "Organizations"
    ],
    "schema": {
      "type": "array",
      "items": "sd-customerorganization",
      "custom": "com.atlassian.servicedesk:sd-customer-organizations",
      "customId": 10004
    }
  },
  {
    "id": "environment",
    "key": "environment",
    "name": "Environment",
    "custom": false,
    "orderable": true,
    "navigable": true,
    "searchable": true,
    "clauseNames": [
      "environment"
    ],
    "schema": {
      "type": "string",
      "system": "environment"
    }
  },
  {
    "id": "duedate",
    "key": "duedate",
    "name": "Due Date",
    "custom": false,
    "orderable": true,
    "navigable": true,
    "searchable": true,
    "clauseNames": [
      "due",
      "duedate"
    ],
    "schema": {
      "type": "date",
      "system": "duedate"
    }
  },
  {
    "id": "progress",
    "key": "progress",
    "name": "Progress",
    "custom": false,
    "orderable": false,
    "navigable": true,
    "searchable": false,
    "clauseNames": [
      "progress"
    ],
    "schema": {
      "type": "progress",
      "system": "progress"
    }
  },
  {
    "id": "comment",
    "key": "comment",
    "name": "Comment",
    "custom": false,
    "orderable": true,
    "navigable": false,
    "searchable": true,
    "clauseNames": [
      "comment"
    ],
    "schema": {
      "type": "comments-page",
      "system": "comment"
    }
  },
  {
    "id": "votes",
    "key": "votes",
    "name": "Votes",
    "custom": false,
    "orderable": false,
    "navigable": true,
    "searchable": false,
    "clauseNames": [
      "votes"
    ],
    "schema": {
      "type": "votes",
      "system": "votes"
    }
  },
  {
    "id": "worklog",
    "key": "worklog",
    "name": "Log Work",
    "custom": false,
    "orderable": true,
    "navigable": false,
    "searchable": true,
    "clauseNames": [
    ],
    "schema": {
      "type": "array",
      "items": "worklog",
      "system": "worklog"
    }
  }
]
```
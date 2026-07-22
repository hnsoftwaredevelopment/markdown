How_to_get_the_link_to_a_confluence_page

# How to get the link to a confluence page

This only seems to work in the  browser, in the Code I get an error, but this should be the code

```Python
url = jiraURL + '/rest/api/3/issue/' + issue.key + '/remotelink'

#Executing this link in a browser you get response but the code doesn't

headers = {
   "Accept": "application/json",
   "Bearer": "<access_token>"
}

response = requests.request(
   "GET",
   url,
   headers=headers
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
```
> The browser however shows this (for ALURE-27788)
> [{
> "id":32279,
> "self":"https://twinfield.atlassian.net/rest/api/3/issue/ALURE-27788/remotelink/32279",
> "globalId":"appId=f980efca-3786-3977-8bc8-c4537ac97a5a&pageId=905183383",
> "application":{"type":"com.atlassian.confluence",
> ​                     "name":"System Confluence"},
> ​                    "relationship":"Wiki Page",
> ​                    "object":{"url":"https://twinfield.atlassian.net/wiki/pages/viewpage.action?pageId=905183383",
> ​                                 "title":"Wiki Page",
> ​                                 "icon":{},
> ​                                 "status":{"icon":{}}
> ​                    }
> }]


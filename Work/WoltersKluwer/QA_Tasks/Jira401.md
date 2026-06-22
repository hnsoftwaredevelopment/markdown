Jira401

# Jira error: 401 authentication error with correct credentials

If you are using correct credentials to enable your Jira Cloud integration, but still seeing a 401 authentication error, you may need to adjust your integration credentials. 

**Use an API key**

In [April 2019](https://support.aha.io/hc/en-us/articles/360027065111-April-19-2019-Jira-authentication-update), Jira began to move away from password authentication for accessing the Jira Cloud API. You must now authenticate with Jira using an API token.

If you are using a Jira 2.0 integration, follow these instructions to update your authentication method from user/password to API token for each one of your Jira integrations.

1. The first step is to create an API token in Jira. Follow [these instructions from Jira](https://confluence.atlassian.com/cloud/api-tokens-938839638.html) on how to create an API token for your user account.
2. Navigate to **Settings > Product** and select your Jira integration. *Note: If your integration setup uses an integration template, you only need to update the template.* 
3. Navigate to the **Configure Account** integration step.
4. Paste the Jira API token from step 1 into the **Password** field and save. *Important note: For Jira Cloud customers, the Jira user's email address must be used in the Username field.*

If you are using a Jira 1.0 integration, you can update the password in the integration settings.

**Use your Jira email address in the Aha! username field**

The **Username** field requires the email address you use to log in to your Jira account, not a username. Confirm that you have used an email address here, then click **Test connection** to see if you have resolved the issue.

 

If you are still receiving a 401 authentication error even with correct credentials, please reach out to our Customer Success team





# API tokens

#### Related content

- [Deprecation of basic authentication with passwords for Jira and Confluence APIs](https://confluence.atlassian.com/display/Cloud/Deprecation+of+basic+authentication+with+passwords+for+Jira+and+Confluence+APIs)
- [Make changes to a managed user account](https://confluence.atlassian.com/display/Cloud/Make+changes+to+a+managed+user+account)
- [Keep your login details secure](https://confluence.atlassian.com/display/Cloud/Keep+your+login+details+secure)
- [Troubleshoot Atlassian account](https://confluence.atlassian.com/display/Cloud/Troubleshoot+Atlassian+account)
- [Create an admin API key](https://confluence.atlassian.com/display/Cloud/Create+an+admin+API+key)

#### Still need help?

The Atlassian Community is here for you.

[Ask the community](https://community.atlassian.com/t5/custom/page/page-id/create-post-step-1?add-tags=Atlassian+Cloud)

You can use an API token to authenticate a script or other process with an Atlassian Cloud application. You generate the token from your Atlassian account, then copy and paste it to the script.

If you use [two-step verification](https://confluence.atlassian.com/cloud/two-step-verification-913378673.html) to authenticate with your Atlassian Cloud site, then your script will need to use a REST API token to authenticate.



API tokens can be used with the Jira Cloud and Confluence Cloud REST APIs.

If you're using Bitbucket Cloud, see [App passwords](https://confluence.atlassian.com/bitbucket/app-passwords-828781300.html).

## Create an API token

Create an API token from your Atlassian account:

![1563527651220](assets/1563527651220.png)

1. Log in to https://id.atlassian.com/manage/api-tokens.

2. Click **Create API token**.

3. From the dialog that appears, enter a memorable and concise **Label** for your token and click **Create**.

4. Click **Copy to clipboard**, then paste the token to your script, or elsewhere to save:

   ![img](assets/Screen+Shot+2017-09-25+at+5.09.09+pm.png)

Note:

- For security reasons it isn't possible to view the token after closing the creation dialog; if necessary, create a new token.
- You should store the token securely, just as for any password.

## Use an API token

A primary use case for API tokens is to allow scripts to access REST APIs for Atlassian Cloud applications using HTTP basic authentication.

Depending on the details of the HTTP library you use, simply replace your password with the token. For example, when using [curl](https://curl.haxx.se/), you could do something like this:

```none
curl -v https://mysite.atlassian.net --user me@example.com:my-api-token
```

Note that `me@example.com` here is the email address for the Atlassian account you're using to create the token.
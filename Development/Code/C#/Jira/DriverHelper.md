---
icon: code-2
---
# DriverHelper
DriverHelper

DriverHelper

```
namespace PegasusTests.PageHelper.Comm
{
    using System;
    using System.Collections.Generic;
    using System.IO;
    using System.Linq;
    using System.Threading;

    using Atlassian.Jira;

    using LinqToExcel;

    using Microsoft.VisualStudio.TestTools.UnitTesting;

    using OpenQA.Selenium;
    using OpenQA.Selenium.Interactions;
    using OpenQA.Selenium.Support.UI;

    using PegasusTests.PageHelper.Comm;

    public abstract class DriverHelper
    {
        #region Fields

        public static Jira jiraConn;
        public static string[] jiraPassword;
        public static string[] jiraURL;
        public static string[] jiraUsername;

        private readonly IWebDriver _driver;

        private XMLParse _oWaXmlData;

        #endregion Fields

        #region Constructors

        public DriverHelper(IWebDriver idriver)
        {
            _driver = idriver;
        }

        #endregion Constructors

        #region Methods

        public void AcceptAlert()
        {
            WaitForWorkAround(2000);
            GetWebDriver().SwitchTo().Alert().Accept();
        }

        public void AddAttachment(string path, string issueID)
        {
            XMLParse _oWaXmlData = new XMLParse();

            _oWaXmlData.LoadXML("../../Config/ApplicationSettings.xml");
            jiraURL = _oWaXmlData.getData("settings/JiraCredentials", "URL");
            jiraUsername = _oWaXmlData.getData("settings/JiraCredentials", "UserName");
            jiraPassword = _oWaXmlData.getData("settings/JiraCredentials", "Password");
            jiraConn = new Jira(jiraURL[0], jiraUsername[0], jiraPassword[0]);

            string jqlString = "project = PegasusCRM AND issuetype = Bug";
            bool result = false;
            IEnumerable<Atlassian.Jira.Issue> jiraIssues = jiraConn.GetIssuesFromJql(jqlString);
            foreach (var issue in jiraIssues)
            {
                if (issue.Key.Value == issueID)
                {
                    Issue foundissue = jiraConn.GetIssue(issueID);
                    foundissue.AddAttachment(path);
                    Console.WriteLine("Attachment Added Successfully");
                    foundissue.SaveChanges();
                    result = true;
                    break;
                }
            }
            if (!result)
            {
                Console.WriteLine("Failed To Add Attachment");
            }
        }

        public void AddComment(string issueID, string Comment)
        {
            XMLParse _oWaXmlData = new XMLParse();

            _oWaXmlData.LoadXML("../../Config/ApplicationSettings.xml");
            jiraURL = _oWaXmlData.getData("settings/JiraCredentials", "URL");
            jiraUsername = _oWaXmlData.getData("settings/JiraCredentials", "UserName");
            jiraPassword = _oWaXmlData.getData("settings/JiraCredentials", "Password");
            jiraConn = new Jira(jiraURL[0], jiraUsername[0], jiraPassword[0]);

            try
            {
                Issue issue = jiraConn.GetIssue(issueID);
                issue.AddComment(Comment);
                issue.SaveChanges();
                Console.WriteLine("Comment added to Issue - " + issueID + " Successfully");
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
        }

        public void ArrowDown(string locator)
        {
            Assert.IsTrue(IsElementPresent(locator));
            GetWebDriver().FindElement(ByLocator(locator)).SendKeys(Keys.ArrowDown);
        }

        public By ByLocator(string locator)
        {
            By result = null;

            if (locator.StartsWith("//"))
            {
                result = By.XPath(locator);
            }
            else if (locator.StartsWith("xpath="))
            {
                result = By.XPath(locator.Replace("xpath=", ""));
            }
            else if (locator.StartsWith("css="))
            {
                result = By.CssSelector(locator.Replace("css=", ""));
            }
            else if (locator.StartsWith("#"))
            {
                result = By.Name(locator.Replace("#", ""));
            }
            else if (locator.StartsWith("link="))
            {
                result = By.LinkText(locator.Replace("link=", ""));
            }

            else
            {
                result = By.Id(locator);
            }

            return result;
        }

        public int CheckboxCount()
        {
            return _driver.FindElements(By.XPath("//input[@type='checkbox']")).Count();
        }

        public bool CheckExstingIssue(string issueTitle)
        {
            bool result = false;
            bool check = false;
            XMLParse _oWaXmlData = new XMLParse();

            _oWaXmlData.LoadXML("../../Config/ApplicationSettings.xml");
            jiraURL = _oWaXmlData.getData("settings/JiraCredentials", "URL");
            jiraUsername = _oWaXmlData.getData("settings/JiraCredentials", "UserName");
            jiraPassword = _oWaXmlData.getData("settings/JiraCredentials", "Password");
            jiraConn = new Jira(jiraURL[0], jiraUsername[0], jiraPassword[0]);

            try
            {
                string jqlString = "project = PegasusCRM AND issuetype = Bug";
                IEnumerable<Atlassian.Jira.Issue> jiraIssues = jiraConn.GetIssuesFromJql(jqlString);
                foreach (var issue in jiraIssues)
                {
                    if (issue.Summary == issueTitle)
                    {
                        result = true;
                        check = true;
                        break;
                    }
                }
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
            if (!check)
            {
                Console.WriteLine("Issue not found");
            }
            return result;
        }

        // Clear Text box Value.
        public void ClearTextBoxValue(string locator)
        {
            WaitForElementPresent(locator, 20);
            Assert.IsTrue(IsElementPresent(locator));
            var el = GetWebDriver().FindElement(ByLocator(locator));
            el.Clear();
        }

        public void Click(string locator)
        {
            WaitForElementPresent(locator, 20);
            Assert.IsTrue(IsElementPresent(locator));
            _driver.FindElement(ByLocator(locator)).Click();
        }

        // Method to click on button using btn text
        public void ClickButtonText(string btnText)
        {
            var locator = "//span[@class='ui-button-text' and contains(text(), '" + btnText + "')]";
            WaitForElementPresent(locator, 20);
            Click(locator);
        }

        public void ClickViaJavaScript(string locator)
        {
            WaitForElementPresent(locator, 20);
            //Assert.IsTrue(IsElementPresent(locator));
            var el = _driver.FindElement(ByLocator(locator));

            //OpenQA.Selenium.Interactions.Actions actions = new OpenQA.Selenium.Interactions.Actions(driver);
            //actions.MoveToElement(el).ClickAndHold();

            ((IJavaScriptExecutor)_driver).ExecuteScript("arguments[0].click();", el);
        }

        public bool CloseIssue(string issueTitle)
        {
            bool result = false;
            bool check = false;
            XMLParse _oWaXmlData = new XMLParse();

            _oWaXmlData.LoadXML("../../Config/ApplicationSettings.xml");
            jiraURL = _oWaXmlData.getData("settings/JiraCredentials", "URL");
            jiraUsername = _oWaXmlData.getData("settings/JiraCredentials", "UserName");
            jiraPassword = _oWaXmlData.getData("settings/JiraCredentials", "Password");
            jiraConn = new Jira(jiraURL[0], jiraUsername[0], jiraPassword[0]);

            try
            {
                string jqlString = "project = PegasusCRM AND issuetype = Bug";
                IEnumerable<Atlassian.Jira.Issue> jiraIssues = jiraConn.GetIssuesFromJql(jqlString);
                foreach (var issue in jiraIssues)
                {
                    if (issue.Summary == issueTitle)
                    {
                        result = true;
                        check = true;
                        break;
                    }
                }
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
            if (!check)
            {
                Console.WriteLine("Issue not found");
            }
            return result;
        }

        public void CloseSelectedWindow()
        {
            _driver.Close();
        }

        public void CreateIssue(string Summary, string issueType, string Priority, string component, string Assignee, string Descriprion)
        {
            XMLParse _oWaXmlData = new XMLParse();

            _oWaXmlData.LoadXML("../../Config/ApplicationSettings.xml");
            jiraURL = _oWaXmlData.getData("settings/JiraCredentials","URL");
            jiraUsername = _oWaXmlData.getData("settings/JiraCredentials","UserName");
            jiraPassword = _oWaXmlData.getData("settings/JiraCredentials","Password");
            jiraConn = new Jira(jiraURL[0], jiraUsername[0], jiraPassword[0]);

            Issue issue = jiraConn.CreateIssue("PEG");
            try
            {
                issue.Summary = Summary;
                issue.Type = issueType;
                issue.Priority = Priority;
                issue.Assignee = Assignee;
                issue.Description = Descriprion;
                issue.SaveChanges();
                Console.WriteLine("Issue Created Successfully");
                CheckExstingIssue(Summary);
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
        }

        public string CurrentUser()
        {
            string username = System.Security.Principal.WindowsIdentity.GetCurrent().Name;
            string user = username.Substring(username.LastIndexOf('\\') + 1);
            Console.WriteLine(user);
            return user;
        }

        public void DoubleClick(string locator)
        {
            Actions builder = new Actions(GetWebDriver());
            IWebElement el = GetWebDriver().FindElement(ByLocator(locator));
            Assert.IsTrue(IsElementPresent(locator));
            builder.DoubleClick(el).Build().Perform();
        }

        public bool ElementNotAvailable(String locator)
        {
            WaitForWorkAround(2000);
            bool result;
            try
            {
                _driver.FindElement(ByLocator(locator));
                result = false;
            }
            catch (Exception)
            {
                result = true;
            }
            return result;
        }

        public string GetAtrributeByLocator(string locator, string attribute)
        {
            return _driver.FindElement(ByLocator(locator)).GetAttribute(attribute);
        }

        public string GetAtrributeByXpath(string xpath, string attribute)
        {
            return _driver.FindElement(By.XPath(xpath)).GetAttribute(attribute);
        }

        public string GetAttributeValue2(string text)
        {
            return _driver.FindElement(
                    By.XPath("//select[@id='ctl00_ContentPlaceHolderBody_drpClass']/option[contains(text(), '" + text +
                             "')]")).GetAttribute("value");
        }

        public string GetAttributeValuep(string text, string id)
        {
            return _driver.FindElement(By.XPath("//select[@id='" + id + "']/option[contains(text(), '" + text + "')]"))
                    .GetAttribute("value");
        }

        /*    public void drawSign()
             {
                 Actions builder = new Actions(GetWebDriver());
                 Action drawAction = builder.MoveToElement(//*[@id='clicknew']", 50, 100)

                     //signatureWebElement is the element that holds the signature element you have in the DOM
                           .ClickAndHold()
                           .moveByOffset(100, 50)
                           .moveByOffset(6, 7)
                           .release()
                           .build();
                  drawAction.Perform();

             }    */
        public String GetDataFromEXL(string filepath, string Usertype, string Column)
        {
            // var pathToExcelFile = @"D:\pegqa\TestAutomationProject\PegasusTests\Screenshots\EXLFile\AgentImport.xlsx";
            String value = "";
            var excelFile = new ExcelQueryFactory(filepath).Worksheet(0);

            var artistAlbums = from a in excelFile select a;
            int i = 0;
            foreach (var a in artistAlbums)
            {
                if (a["UserType"] == Usertype)
                {
                    value = a[Column];
                }
            }
            Thread.Sleep(1000);
            return value;
        }

        public int GetFullRowFromEXL(string filepath)
        {
            // var pathToExcelFile = @"D:\pegqa\TestAutomationProject\PegasusTests\Screenshots\EXLFile\AgentImport.xlsx";
            var excelFile = new ExcelQueryFactory(filepath).Worksheet(0);

            var artistAlbums = from a in excelFile select a;
            int i = 0;
            foreach (var a in artistAlbums)
            {
                i++;
            }
            Thread.Sleep(1000);
            return i;
        }

        /* dan - Not sure we need this or not
        //Is text Present
        public bool IsTextPresent(string locator, string sTextToFind)
        {
            bool bRetVal = false;
            IWebElement element = GetWebDriver().FindElement(ByLocator(locator));
            if (element.Text == sTextToFind)
            {
                bRetVal = true;
            }

            return bRetVal;
        }
        */
        public string GetIdByAtttribute(string locator)
        {
            var sRetVal = "";

            var we = _driver.FindElement(By.XPath(locator));
            sRetVal = we.GetAttribute("id");

            return sRetVal;
        }

        public string getIssueID(string issueTitle)
        {
            string  result = "";

            XMLParse _oWaXmlData = new XMLParse();

            _oWaXmlData.LoadXML("../../Config/ApplicationSettings.xml");
            jiraURL = _oWaXmlData.getData("settings/JiraCredentials", "URL");
            jiraUsername = _oWaXmlData.getData("settings/JiraCredentials", "UserName");
            jiraPassword = _oWaXmlData.getData("settings/JiraCredentials", "Password");
            jiraConn = new Jira(jiraURL[0], jiraUsername[0], jiraPassword[0]);

            try
            {
                string jqlString = "project = PegasusCRM AND issuetype = Bug";
                IEnumerable<Atlassian.Jira.Issue> jiraIssues = jiraConn.GetIssuesFromJql(jqlString);
                foreach (var issue in jiraIssues)
                {
                    if (issue.Summary == issueTitle)
                    {
                        result = issue.Key.Value;
                        break;
                    }
                }
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
            return result;
        }

        public string GetnewDirectoryName(string directory)
        {
            Thread.Sleep(3000);
            DateTime lastHigh = new DateTime(1900, 1, 1);
            string highDir="";
            foreach (string subdir in Directory.GetDirectories(directory))
            {
                DirectoryInfo fi1 = new DirectoryInfo(subdir);
                DateTime created = fi1.LastWriteTime;
                if (created > lastHigh)
                {
                    highDir = subdir;
                    lastHigh = created;
                }
            }
            return highDir;
        }

        public FileInfo Getnewfilename(DirectoryInfo directory)
        {
            Thread.Sleep(3000);
            return directory.GetFiles().Union(directory.GetDirectories().Select(d => Getnewfilename(d)))
                .OrderByDescending(f => (f == null ? DateTime.MinValue : f.LastWriteTime))
                .FirstOrDefault();
        }

        public int GetRowFromEXL(string filepath, string Usertype)
        {
            //var pathToExcelFile = @"D:\pegqa\TestAutomationProject\PegasusTests\Screenshots\EXLFile\AgentImport.xlsx";
            String value = "";
            var excelFile = new ExcelQueryFactory(filepath).Worksheet(0);

            var artistAlbums = from a in excelFile select a;
            int i = 0;
            foreach (var a in artistAlbums)
            {
                if (a["UserType"] == Usertype)
                {
                    i++;

                }
            }
            Thread.Sleep(1000);
            return i;
        }

        public string GetText(string locator)
        {
            var value = "";
            WaitForElementPresent(locator, 20);
            Assert.IsTrue(IsElementPresent(locator));
            var textval = _driver.FindElement(ByLocator(locator));
            value = textval.Text;
            return value;
        }

        public string GetTextFromNonVisibleElement(string locator)
        {
            var value = "";
            WaitForElementPresent(locator, 20);
            Assert.IsTrue(IsElementPresent(locator));
            var textval = _driver.FindElement(ByLocator(locator));
            value = ((IJavaScriptExecutor)_driver).ExecuteScript("return arguments[0].innerHTML", textval).ToString();
            return value;
        }

        public string GetValue(string locator)
        {
            var value = "";
            WaitForElementPresent(locator, 20);
            Assert.IsTrue(IsElementPresent(locator));
            var textval = _driver.FindElement(ByLocator(locator));
            value = textval.GetAttribute("value");
            return value;
        }

        public IWebDriver GetWebDriver()
        {
            return _driver;
        }

        public bool IsElementPresent(string locator)
        {
            bool result;
            try
            {
                _driver.FindElement(ByLocator(locator));
                result = true;
            }
            catch (Exception)
            {
                result = false;
            }
            return result;
        }

        public bool IsElementVisible(string locator)
        {
            return _driver.FindElement(ByLocator(locator)).Displayed;
        }

        public bool IsFieldDisabled(string locator, string attribute)
        {
            var bRetVal = false;

            try
            {
                bRetVal = Convert.ToBoolean(_driver.FindElement(ByLocator(locator)).GetAttribute(attribute));
            }
            catch (Exception)
            {
                // Ignore exception.
            }

            return bRetVal;
        }

        public void MouseOver(string locator)
        {
            var el = GetWebDriver().FindElement(ByLocator(locator));

            var builder = new Actions(GetWebDriver());
            builder.MoveToElement(el).Build().Perform();
        }

        public void SelectAndClosePopUp(string title)
        {
            foreach (var item in _driver.WindowHandles.Where(item => _driver.SwitchTo().Window(item).Title.Equals(title)))
            {
                _driver.SwitchTo().Window(item);
                _driver.Close();
                break;
            }
        }

        public void SelectDropDown(string locator, string targetValue)
        {
            WaitForElementPresent(locator, 20);
            Assert.IsTrue(IsElementPresent(locator));

            var dropDownListBox = _driver.FindElement(ByLocator(locator));
            var clickThis = new SelectElement(dropDownListBox);
            clickThis.SelectByValue(targetValue);
        }

        public void SelectDropDownByText(string locator, string targetText)
        {
            WaitForElementPresent(locator, 20);
            Assert.IsTrue(IsElementPresent(locator));
            var dropDownListBox = _driver.FindElement(ByLocator(locator));
            var clickThis = new SelectElement(dropDownListBox);

            clickThis.SelectByText(targetText);
        }

        public void SelectWindow(string title)
        {
            foreach (var item in _driver.WindowHandles.Where(item => _driver.SwitchTo().Window(item).Title.Equals(title)))
            {
                _driver.SwitchTo().Window(item);
                break;
            }
        }

        public void SelectWindowWithTitle(string title)
        {
            foreach (var item in _driver.WindowHandles.Where(item => _driver.SwitchTo().Window(item).Title.Contains(title)))
            {
                _driver.SwitchTo().Window(item);
                break;
            }
        }

        public void SendKeys(string locator, string value)
        {
            WaitForElementPresent(locator, 20);
            Assert.IsTrue(IsElementPresent(locator));
            var el = GetWebDriver().FindElement(ByLocator(locator));
            el.Clear();
            el.SendKeys(value);
        }

        public bool SwitchNewWindow(String windowName)
        {
            var currentWindow = GetWebDriver().CurrentWindowHandle;
            var availableWindows = new List<string>(GetWebDriver().WindowHandles);

            foreach (string w in availableWindows)
            {
                if (w != currentWindow)
                {
                    GetWebDriver().SwitchTo().Window(w);
                    if (GetWebDriver().Title == windowName)
                        return true;
                    else
                    {
                        GetWebDriver().SwitchTo().Window(currentWindow);
                    }
                }
            }

            return false;
        }

        public void SwitchWindowWithSimilerTitle(string title, string Id)
        {
            foreach (var item in _driver.WindowHandles.Where(item => _driver.SwitchTo().Window(item).Title.Equals(title) && item != Id))
            {
                _driver.SwitchTo().Window(item);
                break;
            }
        }

        //Upload File
        public void UploadFile(string locator, string value)
        {
            WaitForElementPresent(locator, 20);
            Assert.IsTrue(IsElementPresent(locator));
            var el = GetWebDriver().FindElement(ByLocator(locator));
            el.SendKeys(value);
        }

        public void VerifyAlertText(String text)
        {
            WaitForWorkAround(2000);
            String AlertText=GetWebDriver().SwitchTo().Alert().Text;
            Console.WriteLine("Alert Text  = " + AlertText);
            Assert.IsTrue(AlertText.Contains(text));
        }

        // Method to verify text in page source
        public void VerifyPageText(string text)
        {
            var result = GetWebDriver().PageSource.Contains(text);
            Assert.IsTrue(result, "Text String: " + text + "Not Found.");
        }

        public void VerifyTextNotPresent(string text)
        {
            var result = GetWebDriver().PageSource.Contains(text);
            Assert.IsFalse(result, "Text String: " + text + "Found.");
        }

        public void WaitForElementEnabled(string locator, int timeout)
        {
            for (var i = 0; i < timeout * 10; ++i)
            {
                if (IsElementPresent(locator) && _driver.FindElement(ByLocator(locator)).Enabled)
                {
                    break;
                }

                try
                {
                    Thread.Sleep(100);
                }
                catch (Exception)
                {
                    // Ignore exception.
                }
            }
        }

        public void WaitForElementNotEnabled(string locator, int timeout)
        {
            for (var i = 0; i < timeout * 10; ++i)
            {
                if (IsElementPresent(locator) && !_driver.FindElement(ByLocator(locator)).Enabled)
                {
                    break;
                }

                try
                {
                    Thread.Sleep(100);
                }
                catch (Exception)
                {
                    // Ignore exception.
                }
            }
        }

        public void WaitForElementNotVisible(string locator, int timeout)
        {
            for (var i = 0; i < timeout * 10; ++i)
            {
                if (IsElementPresent(locator) && !_driver.FindElement(ByLocator(locator)).Displayed)
                {
                    break;
                }

                try
                {
                    Thread.Sleep(100);
                }
                catch (Exception)
                {
                    // Ignore exception.
                }
            }
        }

        public void WaitForElementPresent(string locator, int timeout)
        {
            for (var i = 0; i < timeout * 10; ++i)
            {
                if (IsElementPresent(locator))
                {
                    break;
                }

                try
                {
                    Thread.Sleep(100);
                }
                catch (Exception)
                {
                    //e.printStackTrace();
                }
            }
        }

        public void WaitForElementVisible(string locator, int timeout)
        {
            for (var i = 0; i < timeout * 10; ++i)
            {
                if (IsElementPresent(locator) && _driver.FindElement(ByLocator(locator)).Displayed)
                {
                    break;
                }

                try
                {
                    Thread.Sleep(100);
                }
                catch (Exception)
                {
                    // Ignore exception.
                }
            }
        }

        public void WaitForText(string text, int timeout)
        {
            for (var i = 0; i < timeout; ++i)
            {
                if (GetWebDriver().PageSource.Contains(text))
                {
                    break;
                }
                else
                {
                    Thread.Sleep(1000);
                }
            }
        }

        public void WaitForTextHide(String text, int timeout)
        {
            for (var i = 0; i < timeout; ++i)
            {
                if (GetWebDriver().PageSource.Contains(text))
                {
                    Thread.Sleep(1000);
                }
                else
                {
                    break;
                }
            }
        }

        // Wait
        public void WaitForWorkAround(int number)
        {
            Thread.Sleep(number);
        }

        // Count number Of Rows.
        public int XpathCount(string xPath)
        {
            var count = _driver.FindElements(By.XPath(xPath)).Count;
            return count;
        }

        #endregion Methods
    }
}
```
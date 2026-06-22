Open Excel from C#

# Open Excel from C#
Add a reference of the type COM using the solution Explorer, right click on References an select "Add reference"

Then select the Microsoft Excel Object Library
![750f9f85db1bc74ab5cc7986c036e266.png](attachments/7e5c5e2803474f3e8dd2db7a16cae502.png)

In the project create a new class named Excel.cs
```C# 
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Microsoft.Office.Interop.Excel;
using _Excel = Microsoft.Office.Interop.Excel;

namespace genertatefactsheets
{
    class Excel
    {
        string pathToExcelFile = "";
        string workSheetName = "";
        _Application excel = new _Excel.Application();
        Workbook excelWorkbook;
        Worksheet excelWorksheet;

        public Excel(string pathToExcelFile, string workSheetName)
        {
            this.pathToExcelFile = pathToExcelFile;
            this.workSheetName = workSheetName;
            excelWorkbook = excel.Workbooks.Open(pathToExcelFile);
            excelWorksheet = excelWorkbook.Worksheets[workSheetName];
        }

        public string ReadCell(int excelCellRow, int excelCellColumn)
        {
            if (excelWorksheet.Cells[excelCellRow, excelCellColumn].Value2 != null)
            {
                string excelValue = excelWorksheet.Cells[excelCellRow, excelCellColumn].Value2;
                excel.Workbooks.Close();

                return excelValue;
            }
            else
                return "";
        }
    }
}
```

From the main application you can use the Excel Class as shown in this example

```C#
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace genertatefactsheets
{
    public partial class GenerateFactsheets : Form
    {
        public GenerateFactsheets()
        {
            InitializeComponent();
        }

        private void showApplicationScreen(object sender, EventArgs e)
        {
            string pathToExcelFile = @"c:\Data\OneDrive - Wolters Kluwer\Factsheets\Factsheet checklist.xlsx";
            string pathToDocuments = @"c:\Data\OneDrive - Wolters Kluwer\Factsheets";
            string excelWorksheetReleases = "Releases";
            string excelWorksheetFactsheets = "Factsheets";

            int excelCellRowCurrentRelease  = 2, excelCellColumnCurrentRelease  = 11;
            int excelCellRowPreviousRelease = 2, excelCellColumnPreviousRelease = 18;
            int excelCellRowCurrentBuild    = 2, excelCellColumnCurrentBuild    = 14;
            int excelCellRowPreviousBuild   = 2, excelCellColumnPreviousBuild   = 21;

            int excelCellRowNumberOfFactsheets = 1, excelCellColumnNumberOfFactsheets = 4;

            lblExcelFileValue.Text = pathToExcelFile;
            lblOutputFolderValue.Text = pathToDocuments;

            string excelCellValueCurrentRelease     = getExcelValue(pathToExcelFile, excelWorksheetReleases, excelCellRowCurrentRelease , excelCellColumnCurrentRelease);
            string excelCellValuePreviousRelease    = getExcelValue(pathToExcelFile, excelWorksheetReleases, excelCellRowPreviousRelease, excelCellColumnPreviousRelease);
            string excelCellValueCurrentBuild       = getExcelValue(pathToExcelFile, excelWorksheetReleases, excelCellRowCurrentBuild   , excelCellColumnCurrentBuild);
            string excelCellValuePreviousBuild      = getExcelValue(pathToExcelFile, excelWorksheetReleases, excelCellRowPreviousBuild  , excelCellColumnPreviousBuild);

            lblPreviousReleaseVersionValue.Text = excelCellValuePreviousRelease;
            lblPreviousReleaseBuildValue.Text = excelCellValuePreviousBuild;
            lblCurrentReleaseVersionValue.Text = excelCellValueCurrentRelease;
            lblCurrentReleaseBuildValue.Text = excelCellValueCurrentBuild;

            // Get all documents from Excel file
            Excel excel = new Excel(@pathToExcelFile, excelWorksheetFactsheets);
            string ReadValue = excel.ReadCell(excelCellRowNumberOfFactsheets, excelCellColumnNumberOfFactsheets);
            int numberOfFactsheets = int.Parse(ReadValue);
            MessageBox.Show(ReadValue);
        }

        public string getExcelValue(string pathToExcelFile, string excelWorksheet, int excelRowIndex, int excelColumnIndex)
        {
            Excel excel = new Excel(@pathToExcelFile, excelWorksheet);
            string readValue = excel.ReadCell(excelRowIndex, excelColumnIndex);
            return readValue;
        }
    }
}
```
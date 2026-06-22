Factsheets_with_TKInter

```python
__author__ = "Hebert Nijkamp"
__license__ = "Wolters Kluwer - Alure"
__version__ = 1.3

import tkinter as tk

import comtypes.client
from docx import Document
from openpyxl import load_workbook

# -----------------------------------------------------
# | Factsheet creator                                 |
# | Creates factsheets from the factsheet excel sheet |
# -----------------------------------------------------

wdFormatPDF = 17
path = 'c:\\Data\\Cloud\\OneDrive - Wolters Kluwer\\Data\\Factsheets\\'

workbook = load_workbook(path+'Factsheet checklist.xlsx', data_only=True)
worksheet = workbook['Releases']

curVersion = worksheet['K2'].value
curBuild = worksheet['N2'].value
preVersion = worksheet['R2'].value
preBuild = worksheet['U2'].value

curTxt = 'behoort bij versie ' + preVersion + ' build ' + preBuild
newTxt = 'behoort bij versie ' + curVersion + ' build ' + curBuild

worksheet = workbook['Factsheets']
numFactsheets = worksheet['D1'].value

FSList = []

for makeFSList in range(2, numFactsheets + 2):
    print(makeFSList - 2, worksheet['B' + str(makeFSList)].value)
    FSList.append(worksheet['B' + str(makeFSList)].value)

print(numFactsheets, FSList)

# Define window
window = tk.Tk()
window.title('Factsheets generator (' + curVersion + '.' + curBuild + ')')
window.geometry('640x480')

# SCREENTITLE
title = tk.Label(text='Create Factsheets for release ' + curVersion + '.' + curBuild)
title.grid(column=0, row=0, orientation='w')

emptyLine = tk.Label()
emptyLine.grid(column=0, row=1)

# LABELS
row = 2
chkBox = []
for count in range(1, numFactsheets):
    chkBox[count]


for readLine in range(2, numFactsheets + 2):
    preFileName = path + worksheet['D' + str(readLine)].value
    newFileName = path + worksheet['C' + str(readLine)].value
    pdfFileName = newFileName.replace('.docx', '.pdf')
    print('☑', pdfFileName.replace('.pdf', ''))

    document = Document(preFileName)
    document.core_properties.content_status = newTxt

    for paragraph in document.paragraphs:
        if curTxt in paragraph.text:
            print(paragraph.text)
            paragraph.text = newTxt
            print(paragraph.text)

    document.save(newFileName)

    word = comtypes.client.CreateObject('Word.Application')
    doc = word.Documents.Open(newFileName)
    doc.SaveAs(pdfFileName, FileFormat=wdFormatPDF)
    doc.Close()
    word.Quit()
```
add_calendar_events

Releasedata toevoegen aan de outlook agenda, hiervoor worden de releasedata uit de Excel sheet C:\data\python\Alure\releases.xlsx gehaald

Alleen de zichtbare regels worden uitgelezen, hiervoor wordt in de Excelsheet een functie gebruikt in de cellen N1 en O1. Belangrijk is dat de formule in deze cellen bevestigd worden met CTRL_+SHIFT+ENTER anders geven ze niet de alleen zichtbare regels weer.

Er is geen validatie of de gemaakte afspraak al bestaat in de agenda

Bij de datum/tijd uit Excel wordt 1 uur opgeteld om de tijd in de juiste tijdzone te zetten.

```python
import win32com.client
from openpyxl import load_workbook
import datetime

path = 'c://data/python/alure/'

workbook = load_workbook(path+'releases.xlsx', data_only=True)
worksheet = workbook['Release']

fstRow = worksheet['N1'].value
lstRow = worksheet['O1'].value

outlook = win32com.client.Dispatch("Outlook.Application")
namespace = outlook.GetNamespace("MAPI")

recipient = namespace.createRecipient("herbert.nijkamp@wolterskluwer.com")
resolved = recipient.Resolve()
calendar = namespace.GetDefaultFolder

for counter in range(fstRow, lstRow + 1):
    relNmbr = worksheet["A" + str(counter)].value
    relRegS = worksheet["B" + str(counter)].value + datetime.timedelta(hours=1)
    relAccT = worksheet["C" + str(counter)].value + datetime.timedelta(hours=1)
    relRelD = worksheet["D" + str(counter)].value + datetime.timedelta(hours=1)
    relRelM = worksheet["E" + str(counter)].value + datetime.timedelta(hours=1)
    relName = worksheet["L" + str(counter)].value

    appointment = outlook.CreateItem(1) # 1=outlook appointment item
    appointment.Subject = "Regression test: " + relNmbr + " - (" + relName[:len(relName) - 5] + ")"
    appointment.Start = relRegS
    appointment.Duration = 4320
    appointment.Save()

    appointment = outlook.CreateItem(1) # 1=outlook appointment item
    appointment.Subject = "Acceptance test: "  + relNmbr + " - (" + relName[:len(relName) - 5] + ")"
    appointment.Start = relAccT
    appointment.Duration = 1440
    appointment.Save()

    appointment = outlook.CreateItem(1) # 1=outlook appointment item
    appointment.Subject = "Release: "  + relNmbr + " - (" + relName[:len(relName) - 5] + ")"
    appointment.Start = relRelD
    appointment.Duration = 1440
    appointment.Save()

    appointment = outlook.CreateItem(1) # 1=outlook appointment item
    appointment.Subject = "Releasenews: "  + relNmbr + " - (" + relName[:len(relName) - 5] + ")"
    appointment.Start = relRelM
    appointment.Duration = 1440
    appointment.Save()
```
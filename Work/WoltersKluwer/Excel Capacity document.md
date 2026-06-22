Excel Capacity document

# Excel Capacity document

This document counts many sheets, for every sprint there is an additional sheet.

When additions or changes has to be made throug all the sheets this is a huge job.

Better to use a Maco to itterate through all sheets and do the change.

Best is to record the change once and place a for next loop arround this to do the change in all, sprint related, sheets.

Important to turn off automatic recalculation when the script starts and switch it on again when it is finished.

Example VBA macro

```VBA
   Application.Calculation = xlManual
    For Count = 101 To 200
        Sheet = "Sprint " & Count
        Sheets(Sheet).Select
        Rows("20:20").Select
        Selection.Insert Shift:=xlDown, CopyOrigin:=xlFormatFromLeftOrAbove
        Range("A20").Select
        ActiveCell.FormulaR1C1 = "Dragged into Sprint"
        Range("B20").Select
        ActiveCell.FormulaR1C1 = "=INDIRECT(""'Sprint ""&R2C2&""'!""&""C20"")"
        Range("C20").Select
        Application.CutCopyMode = False
        ActiveCell.FormulaR1C1 = "=SUM(R[-3]C:R[-1]C)-R[-4]C"
        Range("C22").Select
    Next
    Application.Calculation = xlAutomatic
```

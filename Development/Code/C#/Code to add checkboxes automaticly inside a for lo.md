Code to add checkboxes automaticly inside a for loop

Code to add checkboxes automaticly inside a for loop
(for loop itself is missing)

```c#
System.Windows.Forms.CheckBox checkbox = new System.Windows.Forms.CheckBox
{
	Tag = "chk" + (readRow - excelStartRow + 1).ToString(),
	Name = "chk" + (readRow - excelStartRow + 1).ToString(),
	Text = readRowValueFactsheetname,
	AutoSize = true
};

if (readRowValueActive == "TRUE")
{
	checkbox.Enabled = true;
}
else
{
	checkbox.Enabled = false;
}

checkbox.Location = new System.Drawing.Point(checkboxPosX, checkboxPosY * 20);

this.Controls.Add(checkbox);

if (checkboxPosY - checkboxStartPosY == 11)
{
	checkboxPosY = checkboxStartPosY;
	checkboxPosX += 300;
}
else
{
	checkboxPosY += 1;
}
```
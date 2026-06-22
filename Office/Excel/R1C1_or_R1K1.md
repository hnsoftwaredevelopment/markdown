R1C1_or_R1K1

Using the R1C1 notation in indirect formulas works perfect, only the problem is when you open the spreadsheet on a machine where Office is set to another location then R1C1 can become R1K1, L1K1, L1C1 or whatever.

How can we determine what characters are used to identify the Rows and Columns.

Use =ADDRESS(1, 1, 1, 0) in a cell to do that it returns the R1C1 as a result.
Now with the LEFT and MID formulas you can extract the letters used for Row and Column

First character is the letter used to address the row, use LEFT to get this character

> LEFT(ADDRESS(1;1;1;0);1) (Will give “R” as a result)

The third character is used to identify the column, use the MID formula to get this character

> MID(ADDRESS(1;1;1;0);3;1) (will give “C” as a result)



Normally you would use the next formula to create a cell reference:

> CONCAT(“R”;ROW();“C”;COLUMN())



Use the next notation to make it language independent

> CONCAT(LEFT(ADDRESS(1;1;1;0);1);ROW();MID(ADDRESS(1;1;1;0);3;1);COLUMN())




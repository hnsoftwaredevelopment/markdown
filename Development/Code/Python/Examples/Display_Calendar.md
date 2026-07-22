Display_Calendar

# Python Program to Display Calendar
*Python has a built-in function, calendar to work with date related tasks. You will learn to display the calendar of a given date in this example.*

------

In the program below, we import the calendar module. The built-in function month() inside the module takes in the year and the month and displays the calendar for that month of the year.

```python
# Python program to display calendar of given month of the year

# import module
import calendar

yy = 2014
mm = 11

# To ask month and year from the user
# yy = int(input("Enter year: "))
# mm = int(input("Enter month: "))

# display the calendar
print(calendar.month(yy, mm))
```

```asciiarmor
>>>   November 2014
>>> Mo Tu We Th Fr Sa Su
>>>                1  2
>>> 3  4  5  6  7  8  9
>>> 10 11 12 13 14 15 16
>>> 17 18 19 20 21 22 23
>>> 24 25 26 27 28 29 30
```
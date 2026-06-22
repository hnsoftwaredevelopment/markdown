ics

calender event file using ics



```python
from ics import Calendar, Event

c = Calendar()
e = Event()

e.name = "Test event"
e.begin = '2019-01-14T11:00:00+01:00'
e.end = '2019-01-14T11:15:00+01:00'
c.events.add(e)
print(c.events)
with open('mijnafspraak.ics', 'w') as f:
    f.writelines(c)
```
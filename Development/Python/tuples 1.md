tuples 1

Tuples

A Tuple is in fact a unchangeable list.

Where the content of a list can change in Python, the content of a tuple is carved in stone. So it cannot be changed.

But tuples are fast and do not consume as much memory as lists ad therefore they are useful.

You can identify a tuple because its surrounded by brackets (), a list is surrounded by square brackets []

Example of working with Tuples

```python
# (age, country, knows_python)
# add values to the first tuple
survey1 = (27, "vietnam", True)

# split up the tuple in individual variables
age= survey[0]
country= survey[1]
knows_python= survey[2]

# print the individual variables to check the content of the first tuple
print("Age =", age)
print("Country =", country)
print("Knows Python?", knows_python)
>>> Age = 27
>>> Country = Vietnam
>>> Knows Python? True

# fill a second tuple with the same content-structure
surevey2 = (21, "Switzerland", False)

# now fill the individual variables using the definitiopn of the first tuple
age, country, knows_python = survey2

# print the individual variables to check the content of the second tuple
print("Age =", age)
print("Country =", country)
print("Knows Python?", knows_python)
>>> Age = 21
>>> Country = Switzerland
>>> Knows Python? False


```


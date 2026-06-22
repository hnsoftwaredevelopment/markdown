Tips

# Various small tips for Python

[TOC]

# If, elif, then, else

## Different ways to test multiple

```python
# Different ways to test multiple
# flags at once in Python
x, y, z = 0, 1, 0

if x == 1 or y == 1 or z == 1:
    print('passed')

if 1 in (x, y, z):
    print('passed')

# These only test for truthiness:
if x or y or z:
    print('passed')

if any((x, y, z)):
    print('passed')
```



# Lists, Tuples, Dictionaries

## Some need actions with lists

```python
# Python's list slice syntax can be used without indices
# for a few fun and useful things:

# You can clear all elements from a list:
>>> lst = [1, 2, 3, 4, 5]
>>> del lst[:]
>>> lst
[]

# You can replace all elements of a list
# without creating a new list object:
>>> a = lst
>>> lst[:] = [7, 8, 9]
>>> lst
[7, 8, 9]
>>> a
[7, 8, 9]
>>> a is lst
True

# You can also create a (shallow) copy of a list:
>>> b = lst[:]
>>> b
[7, 8, 9]
>>> b is lst
False
```



## Usage of Itertools

```python
# itertools.permutations() generates permutations 
# for an iterable. Time to brute-force those passwords ;-)

>>> import itertools
>>> for p in itertools.permutations('ABCD'):
...     print(p)

('A', 'B', 'C', 'D')
('A', 'B', 'D', 'C')
('A', 'C', 'B', 'D')
('A', 'C', 'D', 'B')
('A', 'D', 'B', 'C')
('A', 'D', 'C', 'B')
('B', 'A', 'C', 'D')
('B', 'A', 'D', 'C')
('B', 'C', 'A', 'D')
('B', 'C', 'D', 'A')
('B', 'D', 'A', 'C')
('B', 'D', 'C', 'A')
('C', 'A', 'B', 'D')
('C', 'A', 'D', 'B')
('C', 'B', 'A', 'D')
('C', 'B', 'D', 'A')
('C', 'D', 'A', 'B')
('C', 'D', 'B', 'A')
('D', 'A', 'B', 'C')
('D', 'A', 'C', 'B')
('D', 'B', 'A', 'C')
('D', 'B', 'C', 'A')
('D', 'C', 'A', 'B')
('D', 'C', 'B', 'A')
```



## Python's list comprehensions are awesome

```python
# Python's list comprehensions are awesome.

vals = [expression 
        for value in collection 
        if condition]

# This is equivalent to:

vals = []
for value in collection:
    if condition:
        vals.append(expression)

# Example:

>>> even_squares = [x * x for x in range(10) if not x % 2]
>>> even_squares
[0, 4, 16, 36, 64]
```



## Dictionaries

### Dicts can be used to emulate switch/case statements

```python
# Because Python has first-class functions they can
# be used to emulate switch/case statements

def dispatch_if(operator, x, y):
    if operator == 'add':
        return x + y
    elif operator == 'sub':
        return x - y
    elif operator == 'mul':
        return x * y
    elif operator == 'div':
        return x / y
    else:
        return None


def dispatch_dict(operator, x, y):
    return {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y,
    }.get(operator, lambda: None)()


>>> dispatch_if('mul', 2, 8)
16

>>> dispatch_dict('mul', 2, 8)
16

>>> dispatch_if('unknown', 2, 8)
None

>>> dispatch_dict('unknown', 2, 8)
None
```



### Get on dicts

```python
# The get() method on dicts
# and its "default" argument

name_for_userid = {
    382: "Alice",
    590: "Bob",
    951: "Dilbert",
}

def greeting(userid):
    return "Hi %s!" % name_for_userid.get(userid, "there")

>>> greeting(382)
"Hi Alice!"

>>> greeting(333333)
"Hi there!"
```



### How to sort a Python dict by value

```python
# How to sort a Python dict by value
# (== get a representation sorted by value)

>>> xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}

>>> sorted(xs.items(), key=lambda x: x[1])
[('d', 1), ('c', 2), ('b', 3), ('a', 4)]

# Or:

>>> import operator
>>> sorted(xs.items(), key=operator.itemgetter(1))
[('d', 1), ('c', 2), ('b', 3), ('a', 4)]
```



### Merge two dictionaries

```python
# How to merge two dictionaries
# in Python 3.5+

>>> x = {'a': 1, 'b': 2}
>>> y = {'b': 3, 'c': 4}

>>> z = {**x, **y}

>>> z
{'c': 4, 'a': 1, 'b': 3}

# In Python 2.x you could
# use this:
>>> z = dict(x, **y)
>>> z
{'a': 1, 'c': 4, 'b': 3}

# In these examples, Python merges dictionary keys
# in the order listed in the expression, overwriting 
# duplicates from left to right.
#
# See: https://www.youtube.com/watch?v=Duexw08KaC8
```





# Date & Time

## Timeit function

```python
# The "timeit" module lets you measure the execution
# time of small bits of Python code

>>> import timeit
>>> timeit.timeit('"-".join(str(n) for n in range(100))',
                  number=10000)

0.3412662749997253

>>> timeit.timeit('"-".join([str(n) for n in range(100)])',
                  number=10000)

0.2996307989997149

>>> timeit.timeit('"-".join(map(str, range(100)))',
                  number=10000)

0.24581470699922647
```



## When To `__repr__` vs `__str__`?

```python
# When To Use __repr__ vs __str__?
# Emulate what the std lib does:
>>> import datetime
>>> today = datetime.date.today()

# Result of __str__ should be readable:
>>> str(today)
'2017-02-02'

# Result of __repr__ should be unambiguous:
>>> repr(today)
'datetime.date(2017, 2, 2)'

# Python interpreter sessions use 
# __repr__ to inspect objects:
>>> today
datetime.date(2017, 2, 2)
```



# Strings

## Count Collections

```python
# collections.Counter lets you find the most common
# elements in an iterable:

>>> import collections
>>> c = collections.Counter('helloworld')

>>> c
Counter({'l': 3, 'o': 2, 'e': 1, 'd': 1, 'h': 1, 'r': 1, 'w': 1})

>>> c.most_common(3)
[('l', 3), ('o', 2), ('e', 1)]
```





# Numbers

## Fill up integers with leading zero’s

```python
n = '4'
n.zfill(3)
>>> '004'
```



# Debugging & deep Dive info

## Use build in function to disassemble functions

```python
# You can use Python's built-in "dis"
# module to disassemble functions and
# inspect their CPython VM bytecode:

>>> def greet(name):
...     return 'Hello, ' + name + '!'

>>> greet('Dan')
'Hello, Dan!'

>>> import dis
>>> dis.dis(greet)
2   0 LOAD_CONST     1 ('Hello, ')
    2 LOAD_FAST      0 (name)
    4 BINARY_ADD
    6 LOAD_CONST     2 ('!')
    8 BINARY_ADD
   10 RETURN_VALUE
```



# Classes & Functions

## @classmethod vs @staticmethod vs "plain" methods

```python
# @classmethod vs @staticmethod vs "plain" methods
# What's the difference?

class MyClass:
    def method(self):
        """
        Instance methods need a class instance and
        can access the instance through `self`.
        """
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        """
        Class methods don't need a class instance.
        They can't access the instance (self) but
        they have access to the class itself via `cls`.
        """
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        """
        Static methods don't have access to `cls` or `self`.
        They work like regular functions but belong to
        the class's namespace.
        """
        return 'static method called'

# All methods types can be
# called on a class instance:
>>> obj = MyClass()
>>> obj.method()
('instance method called', <MyClass instance at 0x1019381b8>)
>>> obj.classmethod()
('class method called', <class MyClass at 0x101a2f4c8>)
>>> obj.staticmethod()
'static method called'

# Calling instance methods fails
# if we only have the class object:
>>> MyClass.classmethod()
('class method called', <class MyClass at 0x101a2f4c8>)
>>> MyClass.staticmethod()
'static method called'
>>> MyClass.method()
TypeError: 
    "unbound method method() must be called with MyClass "
    "instance as first argument (got nothing instead)"
```



# Web services

## Build in HTTP server

```python
# Python has a HTTP server built into the
# standard library. This is super handy for
# previewing websites.

# Python 3.x
$ python3 -m http.server

# Python 2.x
$ python -m SimpleHTTPServer 8000

# (This will serve the current directory at
#  http://localhost:8000)
```


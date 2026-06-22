Merge_dicts

# How to merge two dicts

```python
# How to merge two dicts

x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}
 
z = {**x, **y}
 
print(z)

>>> {'c': 4, 'a': 1, 'b': 3}

# In Python 2.x you could use this:
z = dict(x, **y)
print z
>>> {'a': 1, 'c': 4, 'b': 3}
```


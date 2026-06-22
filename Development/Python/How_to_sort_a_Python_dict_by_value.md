How_to_sort_a_Python_dict_by_value

# How to sort a Python dict by value
## Get a representation sorted by value

```python
xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}
sorted(xs.items(), key=lambda x: x[1])
```

## Or:

```python
import operator
sorted(xs.items(), key=operator.itemgetter(1))
```


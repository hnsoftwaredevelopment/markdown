Check_variables_better

```python
# Different ways to test multiple
# flags at once in Python
x, y, z = 0, 1, 0

# Classic
if x == 1 or y == 1 or z == 1:
    print('passed')

# Alternative
if 1 in (x, y, z):
    print('passed')

# These only test for truthiness:
# Classic
if x or y or z:
    print('passed')

# Alternative
if any((x, y, z)):
    print('passed')
```


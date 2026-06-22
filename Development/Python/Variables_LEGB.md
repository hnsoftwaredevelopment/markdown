Variables_LEGB

follow a route to determine what value a variable should have. This route is called LEGD that stands for:

Local, Enclosing, Global, Built-in

```python
import builtins

x = 'global x'


def test(z):
    # it is possible to use the global variable her with next commented out line
    # global x
    # but this is not prefered, just be aware that it is possible to overwrite a
    # global variable inside a function

    x = 'local x'
    print(x)
    print(z)


def outer():
    x = 'outer x'
    y = 'enclosng y'

    def inner():
        # it is possible to use the enclosing variable her with next commented out line
        # nonlocal x

        x = 'inner x'
        print(x)
        print(y)   # variable y is not found in the local part, 
                   # but in the enclosing part one level higher
    
    inner()
    print(x)


outer()
test('local z')
print(x)

print('Built in variables: ', dir(builtins))
```

```
>>> inner x
>>> enclosng y
>>> outer x
>>> local x
>>> local z
>>> global x
>>> Built in variables:  ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']

Process finished with exit code 0
```

See that in the code the variable x is used on different  location, but in the result you see all those different x’s back. Never the variable from another level in the code is replaced





[Look at this video for more info](https://www.youtube.com/watch?v=QVdf0LgmICw)
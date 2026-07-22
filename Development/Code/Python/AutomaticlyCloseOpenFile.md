AutomaticlyCloseOpenFile

Opening files inside the ‘with’ function makes the file to automaticly close when done.

For example

```python
f = open(‘hello.txt’, ‘w’)
	f.write(‘Hello, world’)
	f.close()
```

Of course the above piece of program does that trick also, but….

If an exception occurs after the f.write statement the file is not closed and will remain open

So you have to catch the exceptions, to always close the file



```python
f = open(‘hello.txt’, ‘w’)
try:
	f.write(‘Hello, world’)
Finaly:
    f.close()
```



Now the file is always closed. Nice piece of code for writing one single line in the text file

It is easier to use the with function



```python
With open(‘hello.txt’, ‘w’) as f:
	f.write(‘Hello, world’)
```

This does the same trick, always closes the file even if an exception occurs.




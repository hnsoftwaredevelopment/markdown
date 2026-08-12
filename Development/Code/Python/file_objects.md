file_objects

## Open for reading

f = open('test.txt', 'r')



## Open for writing

f = open('test.txt', 'w')



## Open for appending

f = open('test.txt', 'a')



## Open for reading and writing

f = open('test.txt', 'r+')



Print: Filename: print(f.name)

Print mode: print(f.mode)



Closing a file

It is important to close a file after usage. so use f.close() at the end of the program to close previously opened file.



It is also possible to close the file automatically, when using a while loop. This is called a context_manager.

the code looks like this

```python
while open('test.txt', 'r') as file:
	print(file.name)
    print(file.mode)
    print(file.read())

#When while loop ends the file is closed
```


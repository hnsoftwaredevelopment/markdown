Format Strings

# Escape caracters to use in Strings

|Esc|Description|
|---|---|
|\n|Newline|
|\t|Tab|
|\a|ASCII Bell|
|\ooo|Character with octal value "ooo"|
|\xhh|Character with hex value "hh"|
|\\|Backslash|
|\"|Double quote|
|\'|Single quote|
|\b|Backspace|
|\r|Carriage return|

\r means go back to the start of the line and type the rest of the text

So `print("Hello Nice world\rGoodbye")`
Will endup as
'Goodbyece World'

You can also make use of raw strings, this means you don't need to use the Escape character for backslah,but symply use it als a backslas

Example
With Escape
`Print("C:\\Windows\\System32\\Drivers")`

as raw string (add an 'r' in before the string)
`print(r"c:\windows\System32\Drivers")`

This can make strings more readable

# Repeat string
You can simply repeate strings
Example
`print(10*'=')`

> ==========

# format strings
Use variables in strings
1. 'Hello %s' %name  # C-Style
2. 'My name is {1}, {0}  {1}'.format('James', 'Bond')
3. f'I am {age} years old'
 
Example 1.1
```python
first = 'James'
last = 'Bond'
age = 90

print('No, Mr. $s, I expect you to die'%last)
```
> 'No, Mr. Bond I expect you to die'

Example 1.2
```python
first = 'James'
last = 'Bond'
age = 90

print('The name is %s, %s %s'%(last, first, last)
```
> 'The name is Bond, James Bond'

Example 1.3
```python
first = 'James'
last = 'Bond'
age = 90
# where %s means insert a string %d means insert an integer
print('Sean Connery is now %d years old'%age
```
> 'Sean Connery is now 90 years old'

Example 1.4
```python
# %f means insert a float
print('pi: %f \nshort pi %0.2f'%(math.pi, math.pi)
```
> 'pi: 3.141593'
> 'short pi: 3.14'

Example 3.1
```python
first = 'James'
last = 'Bond'
age = 90

print(f'No, Mr. {last}, I expect you to die'%last)
```
> 'No, Mr. Bond I expect you to die'

Example 3.2
```python
first = 'James'
last = 'Bond'
age = 90

print('The name is {last}, {firs} {last'%(last, first, last)
```
> 'The name is Bond, James Bond'

Example 3.3
```python
print(f'3 x pi: {3*math.pi} \nshort 3 x pi: {3*math.pi:.2f})'
```
> '3 x pi: 9.42477796076938'
> 'short 3 x pi: 9.42'

## Make use of a different seperator
When you use different arguments in the print command the arguments are seperated with a space bij default

`print("hello", "world")`
> Hello World

You can change the seperator using the sep argument
`print("Hello", "world", sep="-")`
> Hello-World

Or you can remove the seperator using the sep argument
`print("Hello", "world", sep="")`
> HelloWorld

You can even use escape characters
`print("Hello", "world", sep="\n")`
> Hello
> World

## Prevent print() to go to the next line at the end
Bij default every print statement ends with a '\n' so the cursor moves to the next line.

This is maybe not what you want, it can be that you want to stay on the same line to add more info from another print() statement to the same line.

Then you can use the argument `end=''`

But most of the time this is not enough, because now youre programm will buffer the output until it recieves a '\n' and the print everything at once to the screen.

to avoid this, in addition to `end=''` you will need tho enable flush `flush = true` 

Example:
```Python
import time

def count_items(items):
    print('Counting ', end='', flush=True)
    num = 0
    for item in items:
        num += 1
        time.sleep(1)
        print('.', end='', flush=True)

    print(f'\nThere were {num} items')
```

Run 1:
> .

Run 2:
> ..

Run 3:
> ...

> There where 3 items


Python_first_steps

# First Steps With Python

by [Derrick Kearney](https://realpython.com/python-first-steps/#author) [15 Comments](https://realpython.com/python-first-steps/#reader-comments)  [basics](https://realpython.com/tutorials/basics/) [python](https://realpython.com/tutorials/python/)

Table of Contents

- (1) What Is Python?
  - [Python Properties](https://realpython.com/python-first-steps/#python-properties)
- (2) Getting Python – A Prelim
  - [Choosing a Python Version](https://realpython.com/python-first-steps/#choosing-a-python-version)
- [(3) How Do I Get Python?](https://realpython.com/python-first-steps/#3-how-do-i-get-python)
- (4) Confirming the Python Install
  - [Python Shell](https://realpython.com/python-first-steps/#python-shell)
- (5) Language Primitives
  - [Variables](https://realpython.com/python-first-steps/#variables)
  - [Built-in Data Types](https://realpython.com/python-first-steps/#built-in-data-types)
  - [Comments](https://realpython.com/python-first-steps/#comments)
  - [Need Help?](https://realpython.com/python-first-steps/#need-help)
- (6) Coding in Python
  - [The Shell (redux)](https://realpython.com/python-first-steps/#the-shell-redux)
  - [IDLE](https://realpython.com/python-first-steps/#idle)
  - [Code Editor](https://realpython.com/python-first-steps/#code-editor)
- (7) Picking a Coding Editor
  - [What should you look for in a code editor?](https://realpython.com/python-first-steps/#what-should-you-look-for-in-a-code-editor)
  - [Which editor should I use?](https://realpython.com/python-first-steps/#which-editor-should-i-use)
- [(8) Python Idioms = Happy Coding](https://realpython.com/python-first-steps/#8-python-idioms-happy-coding)
- (9) Counting to 10
  - [Let’s Make a Plan (pseudocode!)](https://realpython.com/python-first-steps/#lets-make-a-plan-pseudocode)
- (10) Errors and Exceptions
  - [Syntax Errors](https://realpython.com/python-first-steps/#syntax-errors)
  - [Exceptions](https://realpython.com/python-first-steps/#exceptions)
  - [Semantic Errors](https://realpython.com/python-first-steps/#semantic-errors)
- (11) Python’s Power - Packages/Modules
  - [Pip](https://realpython.com/python-first-steps/#pip)
- [(12) Next Steps](https://realpython.com/python-first-steps/#12-next-steps)
- [(13) Riding a Bike](https://realpython.com/python-first-steps/#13-riding-a-bike)
- [(14) Simple Advice for New Python Coders](https://realpython.com/python-first-steps/#14-simple-advice-for-new-python-coders)
- [(15) Test Your Knowledge](https://realpython.com/python-first-steps/#15-test-your-knowledge)

Welcome! **This tutorial details how to get started with Python**. It’s written, edited, and updated by Derrick Kearney (Canadian, Python master, foodie) and Michael Herman (from the Real Python team, of course).

I (Derrick) help administer several Python groups where I field countless questions each day. In this post I’ll answer the question I hear the most, **“How do I get started with Python?”**



![Python Cheat Sheet](assets/python-logo.8eb72ea6927b.png)



## (1) What Is Python?

Python, named after the British comedy group Monty Python, is an interpreted, interactive, object-oriented programming language. Its flexibility allows it to do many things, both big and small. Python can be used to write simple programs, but it also possesses the full power required to create complex, large-scale enterprise solutions. Some of the ways in which Python is used includes:

- Desktop graphical application development, including games;
- Mathematical and scientific analysis of data; and,
- Web and internet development.

Python’s presence in the world of computer programming can be found everywhere. For example, Python is used in some of the largest internet sites on earth - like [Reddit, Dropbox, and Youtube](https://realpython.com/world-class-companies-using-python/), to name a few. The popular Python web framework Django powers both Instagram and Pinterest. LucasFilms’s award winning visual effects company, Industrial Light & Magic, uses Python to make help make their magic come to life.

*It’s easy to forget just how powerful Python is because it’s so easy to learn.*

### Python Properties

Python is…

1. *Strongly* typed. It enforces data types so you can’t concatenate a string and a integer, for example.
2. *Dynamically*, *implicitly* typed. So, you don’t have to explicitly declare variable data types. Data types are enforced at runtime.
3. *Case sensitive*. For example, `token` and `TOKEN` are two different variables.
4. *Object-oriented*. [Everything is an object](https://realpython.com/python3-object-oriented-programming/).

## (2) Getting Python – A Prelim

Python is free, [open-source](https://docs.python.org/2/license.html) software that works on Linux, Mac, Windows, and various other platforms (21 in total). It comes preinstalled on Mac and most distributions of Linux; however, you may need to download the latest version ([see below](https://realpython.com/learn/python-first-steps/#3-how-do-i-get-python)).

To check your version, open the terminal and run the following command:

 ```python
python -V
```

### Choosing a Python Version

It can be confusing for both new and seasoned programmers on deciding between Python 2 or 3. Fortunately, there are few syntactical differences between the two and you can run both version on your computer.

Currently, there are two main versions of Python - 2.x and 3.x.

> Only version 3.5.x is in active development, in terms of gaining new features and functionality, while Python 2.7.x as well as 3.2.x to 3.4.x are actively maintained.

**Which version is right for you?** Well, that’s up to you. Honestly, there are few differences between the two that will affect you at this early stage, so either choice will suffice. Plus, once you’ve learned one, it’s not too difficult to learn the other.

In general, if you’re just starting to learn Python, go with 3.4.x, since it’s a better version as there are added features along with plenty of bug fixes and refinements. However, 2.7x has much more support from third-party libraries. If you know you’ll need to use a library that has not been ported to version 3.4.x, then it may be best to start with 2.7x.

The examples in this series will be shown in version [3.4.2](https://www.python.org/download/releases/3.4.2/), which is the current version as of writing. That said, most of the examples will work fine with either version since many of the features and updates added to 3.4.x were also added to 2.7.x. We’ll discuss any differences that you should be aware of as they arise.

## (3) How Do I Get Python?

Regardless of your operating system, you can download Python from the [Python Software Foundation](https://www.python.org/) (PSF). Grab the version specific to your OS and processor (32 or 64-bit).

**OS-specific instructions**:

- *Mac*: I strongly recommend using [Homebrew](http://brew.sh/) to install and manage different version of Python. Check out the directions [here](https://gist.github.com/mjhea0/3c7d97e1d20ab86eb41e). You can also download Python from the [PSF](https://www.python.org/).
- *Linux*: Again, Python is included on various flavors of Linux. Be sure to upgrade to the latest version using the package manager, if necessary.
- *Windows*: Download Python direct from the [PSF](https://www.python.org/).

> Windows users: Make sure you select the option to add Python to your system path during the installation process:
>
> [![Adding python.exe to the system path](assets/msi_install_path.4208ac34dc20.png)](https://files.realpython.com/media/msi_install_path.4208ac34dc20.png)
>
> (From the drop-down select the option, “Will be installed on local hard drive”.)

## (4) Confirming the Python Install

Let’s do a quick sanity check to ensure Python installed correctly.

### Python Shell

Open the Python Interactive Shell:

- *Mac*: Open your terminal and run: `python` or `python3`, depending upon your installation.
- *Linux*: Open your terminal and run: `python`
- *Windows*: If you have only one version of Python installed simply run `python`. If you have both Python 2.7 and Python 3 installed, run `python` for Python 2.7 and/or `py -3` for Python 3.

> Windows users: Ensure that your account has administrative privileges: Run the command prompt at an elevated level by right-clicking the command prompt icon, and then selecting ‘Run as Administrator’.

The interactive Python Shell should open, and your command prompt or terminal window should look similar to this:

\>>>

 ```python
Python 3.4.1 (v3.4.1:c0e311e010fc, May 18 2014, 00:54:21)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

While you’re here, you might as well run your first line of code…

*Python 2*:

\>>>

 ```python
>>> print "Python is fun!"
```

*Python 3*:

\>>>

 ```python
>>> print("Python is fun!")
```

> If you’re running Python 2.x, the `print` command is a statement rather than a function in Python 3.x.

You should see:

\>>>

 ```python
Python is fun!
```

And that’s it: You’ve just written your first Python program! Each time you entered a line, Python immediately executed the statement, displaying the value between the quotes.

Once done, you can use `exit()` to leave the Python Shell. Or:

- *Mac and Linux users*: Ctrl+D and then press Enter
- *Windows users*: Ctrl+D and then press Enter

Keep your terminal or command prompt open. We still have more to do! Let’s continue using the Shell as we run through the Python primitives.

## (5) Language Primitives

In this section we’ll look at the Python coding primitives - variables, built-in data types, comments, syntax, and semantics.

### Variables

[Variables are containers](https://realpython.com/python-variables/) for data. The syntax to declare them is: `variable_name = variable_value`. While you can name variables anything you’d like (except for a few [reserved keywords](https://docs.python.org/2/reference/lexical_analysis.html#keywords)), you *should* use a naming scheme that makes intuitive sense. The variable name *should* provide some indication as to what the values assigned to it are.

For example, many new programers, use simple variable names like `x` and `y`. Do (err, try) not to do this. Instead, if you have two numbers - say `1` and `52` - use the variable names `num1` and `num2` instead of `x` and `y`. That way when others read your program, they can make an educated guess that `num1` and `num2` are probably numbers of some sort. Think of others when writing your programs, as well as your future self. Your future self will thank you.

### Built-in Data Types

Python has [a number of built-in data types](https://realpython.com/python-data-types/) such as numbers (integers, floats, complex numbers), strings, lists, tuples, and dictionaries.

Each of these can be manipulated using:

1. Operators
2. Functions
3. Data-type methods

> Be sure to type each example out along with me.

**Numbers**

Numbers can be integers, floating points, Booleans, or complex numbers. The former three are the most important:

- Integers are whole numbers - `1`, `2`, `22`, `476`, `-99999`
- Floats have decimal points - `1.0`, `2.22`, `22.098`, `476.1`, `-99999.9`
- Booleans represent either `True` or `False` (or `1` or `0`). They represent data that can only be one thing or another.

**Manipulating numbers**

*Operators*

You’ve seen operators before. They’re things like addition (or concatenation) and subtraction, just like you learned in Elementary school.

\>>>

 ```python
>>> 2 + 3   # Addition
5
>>> num1 = 10
>>> num2 = 9.99
>>> num3 = num1 + num2
>>> num3
19.990000000000002
>>> 8 - 5   # Subtraction
3
>>> 2 * 6   # Multiplication
12
>>> 12 / 3  # Division
4.0
>>> 7 % 3   # Modulus (returns the remainder from division)
1
>>> 3 ** 2  # Raise to the power
9
```

Putting your pre-algebra skills to the test, let’s look at comparisons, which evaluate to boolean values - e.g., either `True` or `False` (or `1` or `0`).

\>>>

 ```python
>>> 2 < 5
True
>>> 4 > 10
False
>>> 3 >= 3
True
>>>
>>> 5 == 6
False
>>> 6 != 9
True
```

*Functions*

Python provides you with a number of built-in [functions](https://docs.python.org/3/library/functions.html#built-in-functions) for manipulating integers. These are *always* available to you. Please note: These functions can be used on *any* data type. There are a number of modules available in the Python Standard Library as well, such as `math`. To use the functions associated with these modules, you’ll first have to import the module. More on this later. For now, let’s look at a few examples of built-in functions.

`float()` - given an integer, this function returns a float.

\>>>

 ```python
>>> float(9)
9.0
>>> float(-99999)
-99999.0
```

`int()` - given a float, this function returns and integer. This function does NOT round the input up (ceiling) to the nearest integer – it simply throws out anything after the decimal point (flooring) and returns the number. So the input of 10.6 returns 10, NOT 11. Similarly, 3.25 returns 3.

\>>>

 ```python
>>> int(10.6)
10
>>> int(3.25)
3
```

*Data-type methods*

Besides functions, there a number of [data-type methods](https://docs.python.org/3.4/library/stdtypes.html) associated with each type of number.

`float.is_integer()` - tests if a float is finite.

\>>>

 ```python
>>> (10.0).is_integer()
True
>>> (10.1).is_integer()
False
```

**Strings**

Strings are lines of text that are declared with single or double quotes:

\>>>

 ```python
>>> simple_string = "hey!"
>>> simple_string
'hey!'
>>> "hello world!"
'hello world!'
>>> escaped = 'can\'t'
>>> escaped
"can't"
>>> not_escaped = "can't"
>>> not_escaped
"can't"
```

**Manipulating strings**

*Operators*

Like numbers, you can [concatenate strings](https://realpython.com/python-strings/) (string concatenation):

\>>>

 ```python
>>> "happy" + " " + "birthday"
'happy birthday'
>>> "my name is " + "john"
'my name is john'
```

*Functions*

Let’s look at just a few [functions](https://docs.python.org/3/library/functions.html#built-in-functions) that are good to use for string manipulation:

`len()` - given a string, this function returns the length of it.

\>>>

 ```python
>>> len(name_string)
15
```

`slice()` - given a start and stop value, you can access a set of, or single, character(s).

\>>>

 ```python
>>> print("Hello"[2])
l
>>> print("Hello"[3])
l
>>> print("Hello"[0])
H
>>> print("Hello"[0:2])
He
```

*Data-type methods*

While we’ll only touch on a few data-type methods, be sure to check out the full Python [documentation](https://docs.python.org/3/library/stdtypes.html#string-methods) as there are a number of important functions that you should be aware of.

`string.capitalize()` - returns the string with the first letter capitalized.

\>>>

 ```python
>>> lower_case_string = "michael"
>>> lower_case_string.capitalize()
'Michael'
>>> ("empire").capitalize()
'Empire'
```

`string.format()` - you can easily format values into strings.

\>>>

 ```python
>>> name = "John Doe"
>>> greeting = "My name is {}".format(name)
>>> greeting
'My name is John Doe'
>>>
```

`string.strip()` - returns the string with the leading and trailing whitespace removed.

\>>>

 ```python
>>> are_you_happy = "     Yes      "
>>> are_you_happy.strip()
'Yes'
```

**Lists**

Lists, which are called Arrays in nearly every other programming language, group various types of data together.

1. `create_a_list = []`
2. `numbers_list = [1, 2, 3]`
3. `strings_list = ["spam", "eggs", "cheese"]`
4. `mixed_list = ["Hello", [1, 2, 3], False]`

As you can see above, lists may contain any data type (you can mix and match, too), including other lists or nothing at all. You can access parts of lists just like strings with indexes. The syntax is the same:

\>>>

 ```python
>>> create_a_list = []
>>> create_a_list
[]
>>> numbers_list = [1, 2, 3, 200]
>>> numbers_list
[1, 2, 3, 200]
>>> strings_list = ["batman", "superman", "iron man"]
>>> strings_list
['batman', 'superman', 'iron man']
>>> mixed_list = ["Hello World", [4, 5, 6], False]
>>> mixed_list
['Hello World', [4, 5, 6], False]
```

You can access elements from the list from either the beginning or end of the list:

\>>>

 ```python
>>> numbers_list[0]
1
>>> numbers_list[0:1]
[1]
>>> numbers_list[0:2]
[1, 2]
```

Watch how you can create a new list just by accessing the elements:

\>>>

 ```python
>>> numbers_list = [1, 2, 3, 200]
>>> new_list = numbers_list[0:3]
>>> new_list
[1, 2, 3]
```

Negative indexes count from the last item backwards:

\>>>

 ```python
>>> strings_list = ["batman", "superman", "iron man"]
>>> strings_list[-1]
'iron man'
```

If you nest a list within another list, you can access the inner list using multiple indexes:

\>>>

 ```python
>>> mixed_list = ["Hello World", [4, 5, 6], False]
>>> mixed_list[1][2]
6
```

**Manipulating lists**

*Operators*

Lists can be concatenated:

\>>>

 ```python
>>> fruits = ["apples", "grapes", "oranges"]
>>> veggies = ["corn", "kale", "mushrooms"]
>>> grocery_list = fruits + veggies
>>> grocery_list
['apples', 'grapes', 'oranges', 'corn', 'kale', 'mushrooms']
```

*Functions*

In general, you can think of lists as strings - only each piece of data is an element. What does that mean in practical terms? Well, the same functions you use on strings can be used for lists.

`len()` - given a list, this function returns the length of it.

\>>>

 ```python
>>> numbers_list = [1, 2, 3, 200]
>>> len(numbers_list)
4
```

`slice()` - given a start and stop value, you can access a set of elements.

\>>>

 ```python
>>> hello = ["H", "e", "l", "l", "o"]
>>> hello[2]
'l'
>>> hello[3]
'l'
>>> hello[0]
'H'
>>> hello[0:2]
['H', 'e']
```

*Data-type methods*

Again, check out the Python [documentation](https://docs.python.org/3.4/tutorial/datastructures.html#more-on-lists) to see all available list methods.

`list.append()` - used to add an item to the end of a list

\>>>

 ```python
>>> fruits = ["apples", "grapes", "oranges"]
>>> fruits.append("blueberries")
>>> fruits
['apples', 'grapes', 'oranges', 'blueberries']
```

`list.sort()` - sort this list

\>>>

 ```python
>>> fruits.sort()
>>> fruits
['apples', 'blueberries', 'grapes', 'oranges']
```

`list.pop()` - given an index value, remove an element from the list

\>>>

 ```python
>>> numbers_list = [1, 2, 3, 200]
>>> numbers_list.pop(2)
3
>>> numbers_list
[1, 2, 200]
```

**Tuples**

Tuples are similar to lists, but they are immutable - which means they cannot be changed after creation.

\>>>

 ```python
my_tuple = ("Michael", "Herman", 31, "Software Developer")
```

Just like a list, you can also use indexes to access different elements:

\>>>

 ```python
>>> my_tuple = ("Michael", "Herman", 31, "Software Developer")
>>> my_tuple[1]
'Herman'
```

> Often tuples are used for dictionary keys since they should (err, must) be immutable.

**Manipulating tuples**

*Operators*

Yes, you can add two tuples:

\>>>

 ```python
>>> first_tuple = (1, 2)
>>> second_tuple = (3, 4)
>>> third_tuple = first_tuple + second_tuple
>>> third_tuple
(1, 2, 3, 4)
```

*Functions*

`list()` - used to convert a tuple to a list

\>>>

 ```python
>>> first_tuple = (1, 2)
>>> list(first_tuple)
[1, 2]
```

> What about converting a list to a tuple? Is there a function for that? Where would you go to find out?

*Data-type methods*

Because tuples are immutable, many of the [list methods](https://docs.python.org/3.4/library/stdtypes.html) don’t work on tuples.

\>>>

 ```python
>>> first_tuple = (1, 2)
>>> first_tuple.append(3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'append'
>>> first_tuple.pop(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'pop'
>>> first_tuple.sort()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'sort'
>>> first_tuple.reverse()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'reverse'
```

**Dictionaries**

Dictionaries are a type of associative array (an object) implemented using hash tables containing key/value pairs. They are unordered.

 ```python
my_dict = {"Key 1": "Value 1", "name": "michael herman", "pi": 3.14}
```

You can return a key’s value using the following syntax:

\>>>

 ```python
>>> my_dict = {"Key 1": "Value 1", "name": "michael herman", "pi": 3.14}
>>> my_dict["name"]
'michael herman'
>>> my_dict["Key 1"]
'Value 1'
```

**Manipulating dictionaries**

Research this on your own, using the Python [documentation](https://docs.python.org/3.4/library/). Need help? Comment below.

Speaking of comments…

### Comments

Comments are used to describe your code so other developers can quickly understand what’s happening (as well as your future self).

 ```python
# This a comment on it's own line
# You create them with the hash symbol
var = "Hello"  # They can also be on the same line as code
```

### Need Help?

Like a good friend, Python is always available if you get stuck. Perhaps you want to know how a specific object works, simply open the Python shell and then call `help()` to get help or `dir()` to see which methods are available for that particular object.

## (6) Coding in Python

There are three basic approaches to coding in Python. We already used one of them - the interactive Python Shell.

### The Shell (redux)

This is the least powerful of the three. Although you can create functions in the Shell, typically it is reserved for simple, one-line statements to get quick feedback on your code.

For example, let’s look at a simple expression. Open the Shell and run:

\>>>

 ```python
>>> 24 + 10
34
```

The Python Shell simply evaluated `24 + 10`, adding the two numbers, and outputted the sum, `34`.

Try one more:

\>>>

 ```python
>>> import this
```

Take a minute to read the output. These are some *important* concepts in Python, which will help you write [idiomatic](http://mrjoelkemp.com/2013/05/what-is-idiomatic-programming/) Python code.

Close the Python interactive Shell. Once closed, our code is gone. In other words, the code typed into the Python Shell is not persistent - and cannot be reused. As coders, we want code that we can reuse to save precious keystrokes. Unfortunately, the Python Shell fails in this regard.

### IDLE

Python comes with a program named IDLE (named after Monty Python’s Eric Idle). IDLE is interactive and can be used exactly like the Python Shell. It can also be used for code reuse since we can create *and save* Python code. That said, IDLE still is not as powerful as the last method, so we will skip it for now.

> If you are interested in using IDLE check out the excellent guide [One Day of IDLE Toying](https://hkn.eecs.berkeley.edu/~dyoo/python/idle_intro/index.html).

### Code Editor

The best approach is to use an actual coding editor. Some people prefer an [Integrated Development Environment](https://wiki.python.org/moin/IntegratedDevelopmentEnvironments) (IDE), but a far simpler code editor is much better for learning purposes.

> Why? When you are learning something new you want to peel off as many layers of complexity as possible. Simplify things. By adding a complex IDE into the mix, which you will have to learn how to operate, you are just adding more and more layers, making the task - learning Python - even more difficult.

## (7) Picking a Coding Editor

A Python program, in its basic form, is simply lines of text (code) saved in a file with a *.py* file extension. Python code can be written in something as basic as Notepad - but there’s no reason to put yourself through such an ordeal since there are much better options available. At it’s core, a code editor should provide a number of features that help a programmer create programs (Python scripts and modules, in our case). In most cases, code editors allow the user to customize the program itself, to suit your needs and style.

### What should you look for in a code editor?

- Ease of use
- Syntax highlighting
- Auto-indentation
- Tabbed views
- Line numbering
- Ability to customize the look and feel of the editor
- Availability of add-ons

Take a look at the following example:

[![The Good Bad and Ugly](assets/good_and_ugly.3081ad7216b2.png)](https://files.realpython.com/media/good_and_ugly.3081ad7216b2.png)

So, not only is the code easier to read in the editor ([Sublime Text](http://www.sublimetext.com/)) on the top (due to the syntax highlighting and line numbering), but it’s also identifying three simple errors, one of which is a show-stopper. (Can you figure out which one?) Meanwhile, the editor (Notepad) at the bottom does not display the errors and is hard on the eyes since it’s black and while.

### Which editor should I use?

One of the most popular code editors is [Sublime Text 3](http://www.sublimetext.com/) (shown above). It is powerful, cross-platform, and free to try out.

> Be sure to support the project by purchasing a license if you continue to use it.

If you want something simpler, check out [gedit](https://wiki.gnome.org/Apps/Gedit), which is also cross-platform. [Notepad++](http://notepad-plus-plus.org/) is also a great editor, but it’s for Windows only. Both of these editors are free and although neither possesses the power of Sublime Text, they are still useful.

A third option is [Vim](http://www.vim.org/), which is free and available for Mac, Linux, and Windows. Vim has a steep learning curve but it has a loyal user base. Steve Francia’s [Vim Distribution](https://github.com/spf13/spf13-vim) is the best programming setup for Vim that I have ever seen.

I personally prefer [Sublime Text 3](http://www.sublimetext.com/). Check out the blog post [Setting Up Sublime Text 3 for Full Stack Python Development](https://realpython.com/setting-up-sublime-text-3-for-full-stack-python-development/) to see how to customize it specifically for writing Python code.

*Remember: There are many different options when it comes to code editors, both free and commercial. Do your research, and don’t be afraid to experiment! Just remember: an editor should help you adhere to Python coding standards, practices, and idioms…*

## (8) Python Idioms = Happy Coding

[PEP 8 – Style Guide for Python Code](http://legacy.python.org/dev/peps/pep-0008/) is the style guide for programming Python code. Study this.

One idiom that trips up many new Python developers is indentation. Python uses indentation (4 spaces) to logically organize code into sections called [code blocks](http://en.wikipedia.org/wiki/Block_(programming). A code block starts with an indent and ends with a dedent (un-indent?). Incorrect indentation will generate an error in Python preventing your code from executing. And this is exactly where having a properly setup code editor pays off, since it will catch indentation errors and highlight them for you. You should also use spaces instead of tabs when indenting. Most editors will allow you to convert tabs to spaces, so that when you tab it is actually applying 4 spaces.

Let’s revisit the errors from the above image…

1. Line 2 - No space around the `<` operator. As explained in [PEP8](http://legacy.python.org/dev/peps/pep-0008/#other-recommendations), Python expects spaces around operators. This is not a critical error but problematic as your code should be clean and readable.
2. Line 4 - There are two errors here, including the show stopper. As stated above, Python uses indention to define code blocks. `count = count + 1`, is part of a block of code that starts on line 2, so that it must be indented 4 spaces in order for Python to include it in the code block.

## (9) Counting to 10

Ready to dive into a basic example?!

If you are brand new to programming you may not *fully* understand the code but it’s the concepts that are important. Python is designed to read very easily and this example demonstrates that principle. We are going to fix the broken code above, and add one more code block to emphasize the concepts of code blocks and indentation.

Many programmers get overwhelmed when they initially approach a problem. An effective approach to help solve the problem, regardless of size, is to logically divide the problem into parts.

For example, let’s code a basic program that counts from 1 to 10. Each time the count increments we want to display a new number, and to help with the concept of code blocks we are going to show what happens after we reach 10. One approach to help in development of a workflow, is to use pseudocode.

### Let’s Make a Plan (pseudocode!)

[![Let's make a plan](assets/pseudo.c74774d5fe1e.jpg)](https://files.realpython.com/media/pseudo.c74774d5fe1e.jpg)

I like to keep things organized on my computer, so first create a folder, put it in your “documents” folder or someplace similar. I created a folder called, `python_code`. Learning to code is hands on, so open up your code editor, and enter the following code. *Do not copy and paste no matter how tempting it is. Doing so will hinder learning.*

**Python 2.7**:

 ```python
# Python 2.7

count = 1
# Code block 1
while count < 11:
    print count
    count = count + 1
# Code block 2
if count == 11:
    print 'Counting complete.'
```

**Python 3**:

 ```python
# Python 3

count = 1
# Code block 1
while count < 11:
    print(count)
    count = count + 1
# Code block 2
if count == 11:
    print('Counting complete.')
```

Note that the first line of each example has a `#` (hash character), followed by a space and then an explanation. This is an inline comment. Such comments have a number of purposes, but for the most part they are used to either explain code or summarize a specific approach a developer took. Do the comments in the above examples make sense to you? If not, change them.

Finally, as you will soon come to find out, comments are ignored by Python when the code is executed.

Did you notice that the examples use both single `=`, and double `==`? This can be confusing.

1. n the expression `count = 1`, the `=` assigns the value of 1 to the variable named `count`.
2. In the conditional `if count == 11:`, the `==` compares the value of `count` with `11`, returning a boolean `True` or `False`. Can you tell what the statement evaluates to in the above example after each iteration?

------

Save the file as *count_to_ten.py* in the folder you created then exit the editor. Open a terminal or command prompt and navigate to the folder you created.

Now run the code: `python count_ten.py`

> You may need to replace `python` with `python3` or `py -3`, depending on your setup. See [Step 4](https://realpython.com/learn/python-first-steps/#4-confirming-the-python-install) for more info.

And the output should look something like this:

[![Count to ten](assets/count_ten.3317a3c183ee.png)](https://files.realpython.com/media/count_ten.3317a3c183ee.png)

Congrats! You just wrote your first program.

## (10) Errors and Exceptions

Errors are something that irritate and frustrate programmers at every level of experience.

In Python, there are two types of code-based errors, [syntax errors and exceptions](https://realpython.com/python-exceptions/).

### Syntax Errors

We have already seen this error already - incorrect indentation. Syntax errors will prevent execution of the program. In this example, the `if` statement is missing a colon to end the statement. As you can see Python is very helpful to point out the error:

\>>>

 ```python
>>> if x < 9
   File "<stdin>", line 1
     if x < 9
             ^
SyntaxError: invalid syntax
```

### Exceptions

Exception errors occur during program execution. Python has a number of built-in [exceptions](https://docs.python.org/2/library/exceptions.html#bltin-exceptions). For example:

\>>>

 ```python
>>> 12/0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: integer division or modulo by zero
```

### Semantic Errors

Semantic errors are errors that happen as a result of one or more problems in logic.

These errors can be more complex, because no error is generated. The code runs but generates unexpected and/or incorrect output, or no output. A classic example of this, would be an infinite loop that most new programmers experience at least once.

## (11) Python’s Power - Packages/Modules

One of the great things about Python is the plethora of available modules, both built into the Python core and [third party packages/libraries](https://wiki.python.org/moin/UsefulModules) - used to extend the language. These modules can be very helpful. Some of the more utilized built-in Python modules include:

- [math](https://docs.python.org/2/library/math.html): mathematical functions from the standard library of the C (you’ve seen this one already)
- [random](https://docs.python.org/2/library/random.html): a pseudo-random number generator
- [datetime](https://docs.python.org/2/library/datetime.html): used for manipulating dates and times
- [re](https://docs.python.org/2/library/re.html): for working with regular expressions

For example, here we `import math` to use `pi`, `sqrt` (square root) and `pow` (raising to the power):

[![Pi, Square Root and Raising to the Power](assets/math_module.bea93eef6dbf.png)](https://files.realpython.com/media/math_module.bea93eef6dbf.png)

> **Warning**: Do not name your Python files the same as a module - like *math.py* or *random.py*. This will cause conflicts, resulting in unexpected behavior in your code. So if you are using the math module, do not name your file *math.py*. Make sense?

### Pip

The best way to manage Python’s third party packages/modules is with [pip](https://pip.pypa.io/en/latest/). New coders frequently hit a wall when they are following some example code and they see the following error when they try to run the code: `ImportError: No module named MODULE_XXXX`.

These modules need to be manually installed using Pip. In Python 3, pip, called *pip3*, is included. If you used Homebrew to install Python, pip is included as well. Starting with Python 2.7.9, pip is also included. If you are using a Python version prior to 2.7.9, follow these instructions to install pip:

1. Download [get-pip.py](https://bootstrap.pypa.io/get-pip.py), confirm that the file was saved with a *.py* extension.
2. Navigate to the location of the downloaded file in the Terminal or Command Prompt.
3. Run: `python get-pip.py`
4. Read the [official pip documentation](https://pip.readthedocs.org/) for more information.

## (12) Next Steps

There are plenty of online tutorials, books, and videos freely available.

My first stop was one of the most popular free choices, [Learn Python the Hard Way](http://learnpythonthehardway.org/book/). Zed Shaw’s tutorial is laid out in a progressive and logical exercise format. I found it very useful for learning the syntax, but I needed more.

One of the best ways of learning how to code is by building - the project driven learning approach. That’s how I came across Real Python. There are three [Real Python](https://realpython.com/courses/) that cost a modest fee, which are frequently updated (usually bi-monthly) to keep up with changes (free of charge).

Another place that truly helped me was MIT’s course, *Introduction to Computer Science and Programming*, which covers various computer science concepts along with Python. The course can be found in two locations.

1. The Harvard and MIT non-profit online initiative ([Edx.org](https://www.edx.org/)) offers the course in two parts. They are challenging and provide an excellent approach to problem solving. Both parts are graded.
2. The other route is from the MIT open courseware, [Introduction to Computer Science and Programming MIT 6.00x](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/). The course is not graded, but it has a very active online community that is quite helpful.

There are other online courses of course. Again, this is personal choice, so do your own research.

Another source of free learning materials comes from the PSF:

- [Python 2.7](https://docs.python.org/2.7/tutorial/index.html)
- [Python 3.4](https://docs.python.org/3.4/tutorial/index.html)

Above all, it is important that you do not fall into finding the “best” book or video search and get lost. Do some research. Ask around. But pick something and *stick with it*! Open your code editor and start coding! Make a commitment to yourself to complete it.

**Free PDF Download:** [Python 3 Cheat Sheet](https://realpython.com/optins/view/python-cheat-sheet-short/)

## (13) Riding a Bike

Coding is like riding a bike: You can watch people to see how it is done, and sometimes you can get a push, but in the end it is a solo event. When I get stuck, or need to brush up on a new concept, the first place I go is Google. If I get an error message, typing in the exact error message, into Google, will often bring up a result in the first page that solves my problem.

Check out these resources as well:

1. The official Python Docs - [Python 2.7](https://docs.python.org/2.7/) or [Python 3](https://docs.python.org/3/)
2. [Tutorials Point](http://www.tutorialspoint.com/python/index.htm) has some very simple and easy to follow examples when I need a quick refresh.
3. [Jeff Knupp’s](http://www.jeffknupp.com/) website (the author of the Idiomatic Python series of tutorials and books)
4. The [Real Python Tutorials section](https://realpython.com/) has more specific topics and advanced subjects like Python’s Web Frameworks, Django and Flask.
5. Bernd Klein’s [Python Course](http://www.python-course.eu/index.php) contains excellent coverage of Python; his discussion of advanced topics is really helpful.
6. [Stack Overflow](http://stackoverflow.com/), the Q&A for coding, has some great explanations of Python topics. How [Python can slice a string](http://stackoverflow.com/questions/509211/explain-pythons-slice-notation?rq=1), is one truly excellent example.

If you get stuck on a problem, try these simple suggestions:

1. Stop coding!
2. Get out a piece of paper and map out how to solve the problem using plain words (pseudocode); use a flow chart if necessary. Refer to the [example above](https://realpython.com/learn/python-first-steps/#9-counting-to-10).
3. At some point you will be introduced to Python’s [exception handling](https://docs.python.org/2/tutorial/errors.html) - the `try/except`block. Do not use use a `try` until your code is working. The `try` can suppress valuable error messages that help identify problems in code.
4. If you are not getting expected output - i.e., perhaps Python is displaying a word instead of a number (incorrect data type) - add a print statement right after the variable assignment and then right before the expected output. This is an effective, quick and dirty problem solver.
5. If you are still stumped, a great tool is the [Python Visualizer](http://www.pythontutor.com/visualize.html#mode=edit). This tool allows you to ‘step through’ your code as it executes. The Python Visualizer has examples to help you if needed.
6. One final note - and this is very important - is that a frustrated brain is not going to help. When you start to get annoyed because something is not working, take a break, clear your brain. Go for a run. Do something else. You will be amazed just how effective this can be. Often, you’ll come back with clear eyes and see a simple typo, a misspelled keyword, etc.

## (14) Simple Advice for New Python Coders

I say this in the nicest kind of way - *no one is going to spoon feed you*. Coders expect other coders - yes, even beginners - to try and resolve the issue themselves. At some point we all need guidance, though.

Once you have tried and truly have hit the wall ask for help, before you smash your keyboard or other inanimate object(s). There are a number of places to get help - [code forums](http://pythonistacafe.com/), Facebook Groups, the [IRC channel #python](https://www.python.org/community/irc/), to name a few. Take a minute to read any rules or guidelines for any of the groups that you use. Make it easy for others to help you by explaining the problem and what you have tried. If there is an error, include that information as well.

Have fun coding!

## (15) Test Your Knowledge

1. What does it mean that Python is a strong, dynamically typed language?
2. How do you access the Python Shell?
3. How do you declare a variable?
4. What’s the difference between a variable name and a variable value?
5. What are Python’s built-in data types?
6. What’s the difference between an integer and a floating point number?
7. What are boolean values?
8. What does the `%` operator do?
9. What’s the difference between a list and a tuple?
10. What’s a dictionary?
11. Why should you use comments in your code?
12. Test out the `help()` function. What did you learn?
13. Pass in `float` to the `dir()` function. What did you learn?
14. One primitive that we didn’t go over is `None`. What does it represent?
15. You can check the data type of a variable or a value by using the `type()` function. Test this out using various data types and variables. What did you learn?

Open your text editor and create a new file called *exercise.py*. Copy and paste the following code into the file:

 ```python
##########################################################################
## Modify the variables so that all of the statements evaluate to True. ##
##########################################################################

var1 =
var6 =
var2 =
var3 =
var4 =
var5 =

############################################
## Don't edit anything below this comment ##
############################################

# integers
print(type(var1) is int)
print(type(var6) is float)
print(var1 < 35)
print(var1 <= var6)

# strings
print(type(var2) is str)
print(var2[5] == 'n' and var2[0] == "p")

# lists
print(type(var3) is list)
print(len(var3) == 5)

# tuples
print(type(var4) is tuple)
print(var4[2] == "Hello, Python!")

# dictionaries
print(type(var5) is dict)
print("happy" in var5)
print(7 in var5.values())
print(var5.get("egg") == "salad")
print(len(var5) == 3)
var5["tuna"] = "fish"
print(len(var5) == 3)
```

Following the instructions, update the code. When done, run the code from your terminal to test using the `python exercise.py` command. Good luck!
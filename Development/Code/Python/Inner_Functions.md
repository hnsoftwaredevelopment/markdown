Inner_Functions

# Python Inner Functions—What Are They Good For?

by [Real Python](https://realpython.com/inner-functions-what-are-they-good-for/#team) [16 Comments](https://realpython.com/inner-functions-what-are-they-good-for/#reader-comments)  [intermediate](https://realpython.com/tutorials/intermediate/) [python](https://realpython.com/tutorials/python/)

Table of Contents

- [Encapsulation](https://realpython.com/inner-functions-what-are-they-good-for/#encapsulation)
- [Keepin’ it DRY](https://realpython.com/inner-functions-what-are-they-good-for/#keepin-it-dry)
- Closures and Factory Functions
  - [What’s a Closure?](https://realpython.com/inner-functions-what-are-they-good-for/#whats-a-closure)
  - [An Example](https://realpython.com/inner-functions-what-are-they-good-for/#an-example)
  - [What’s Happening in the Example](https://realpython.com/inner-functions-what-are-they-good-for/#whats-happening-in-the-example)
  - [A Real World Example](https://realpython.com/inner-functions-what-are-they-good-for/#a-real-world-example)
- [Conclusion](https://realpython.com/inner-functions-what-are-they-good-for/#conclusion)

Let’s look at three common reasons for writing inner functions.

**Note:** In Python, functions are [“first-class citizens.”](https://realpython.com/primer-on-python-decorators/#first-things-first) This means that they are on par with any other object (integers, strings, lists, modules, and so on). You can dynamically create or destroy them, pass them to other functions, return them as values, and so forth.

This tutorial uses Python version 3.4.1.

## Encapsulation

You use inner functions to [protect](http://en.wikipedia.org/wiki/Information_hiding) them from everything happening outside of the function, meaning that they are hidden from the global scope.

Here’s a simple example that highlights that concept:

 ```python
def outer(num1):
    def inner_increment(num1):  # Hidden from outer code
        return num1 + 1
    num2 = inner_increment(num1)
    print(num1, num2)

inner_increment(10)
# outer(10)
```

Try calling `inner_increment()`:

 ```python
Traceback (most recent call last):
  File "inner.py", line 7, in <module>
    inner_increment()
NameError: name 'inner_increment' is not defined
```

Now comment out the `inner_increment()` call and uncomment the outer function call, `outer(10)`, passing in `10` as the argument:

 ```python
10 11
```

**Note:** Keep in mind that this is just an example. Although this code does achieve the desired result, it’s probably better to make `inner_increment()` a top-level “private” function using a leading underscore: `_inner_increment()`.

The following recursive example is a slightly better use case for a nested function:

 ```python
def factorial(number):

    # Error handling
    if not isinstance(number, int):
        raise TypeError("Sorry. 'number' must be an integer.")
    if not number >= 0:
        raise ValueError("Sorry. 'number' must be zero or positive.")

    def inner_factorial(number):
        if number <= 1:
            return 1
        return number*inner_factorial(number-1)
    return inner_factorial(number)

# Call the outer function.
print(factorial(4))
```

Test this out as well. One main advantage of using this design pattern is that by performing all argument checking in the outer function, you can safely skip error checking altogether in the inner function.

**Note:** For a more detailed discussion of recursion, see [Thinking Recursively in Python](https://realpython.com/python-thinking-recursively/).

## Keepin’ it [DRY](http://en.wikipedia.org/wiki/Don't_repeat_yourself)

Perhaps you have a giant function that performs the same chunk of code in numerous places. For example, you might write a function that processes a file, and you want to accept either an open file object or a file name:

 ```python
def process(file_name):
    def do_stuff(file_process):
        for line in file_process:
            print(line)
    if isinstance(file_name, str):
        with open(file_name, 'r') as f:
            do_stuff(f)
    else:
        do_stuff(file_name)
```

**Note:** Again, it is common to just make `do_stuff()` a private top-level function, but if you want to hide it away as an internal function, you can.

How about a practical example?

Let’s say you want to know the number of WiFi hotspots in New York City. Yes, the city has the [raw data](https://data.cityofnewyork.us/City-Government/NYC-Wi-Fi-Hotspot-Locations/yjub-udmw) to tell us. Visit the site and download the CSV:

 ```python
def process(file_name):

    def do_stuff(file_process):
        wifi_locations = {}

        for line in file_process:
            values = line.split(',')
            # Build the dict and increment values.
            wifi_locations[values[1]] = wifi_locations.get(values[1], 0) + 1

        max_key = 0
        for name, key in wifi_locations.items():
            all_locations = sum(wifi_locations.values())
            if key > max_key:
                max_key = key
                business = name

        print(f'There are {all_locations} WiFi hotspots in NYC, '
              f'and {business} has the most with {max_key}.')

    if isinstance(file_name, str):
        with open(file_name, 'r') as f:
            do_stuff(f)
    else:
        do_stuff(file_name)
```

Run the function:

\>>>

 ```python
>>> process('NAME_OF_THE.csv')
There are 1251 WiFi hotspots in NYC, and Starbucks has the most with 212.
```

## Closures and Factory Functions

Now we come to the most important reason to use inner functions. All of the inner function examples we’ve seen so far have been ordinary functions that merely happened to be nested inside another function. In other words, we could have defined these functions in another way (as discussed). There is no specific reason for why they need to be nested.

But when it comes to closures, that is not the case: you must use nested functions.

### What’s a Closure?

A closure simply causes the inner function to remember the state of its environment when called. Beginners often think that a closure is the inner function, but it’s really caused by the inner function. The closure “closes” the local variable on the stack, and this stays around after the stack creation has finished executing.

### An Example

Here’s an example:

 ```python
def generate_power(number):
    """
    Examples of use:

    >>> raise_two = generate_power(2)
    >>> raise_three = generate_power(3)
    >>> print(raise_two(7))
    128
    >>> print(raise_three(5))
    243
    """

    # Define the inner function ...
    def nth_power(power):
        return number ** power
    # ... that is returned by the factory function.

    return nth_power
```

### What’s Happening in the Example

Let’s take a look at what is going on in that example:

1. `generate_power()` is a factory function, which simply means that it creates a new function each time it is called and then returns the newly created function. Thus, `raise_two()` and `raise_three()` are the newly created functions.

2. What does this new, inner function do? It takes a single argument, `power`, and returns `number**power`.

3. Where does the inner function get the value of `number` from? This is where the closure comes into play: `nth_power()` gets the value of `power` from the outer function, the factory function. Let’s step through this process:

   - Call the outer function: `generate_power(2)`.
   - Build `nth_power()`, which takes a single argument `power`.
   - Take a snapshot of the state of `nth_power()`, which includes `power=2`.
   - Pass that snapshot into `generate_power()`.
   - Return `nth_power()`.

   To put it another way, the closure “initializes” the number bar in `nth_power()` and then returns it. Now, whenever you call that newly returned function, it will always see its own private snapshot that includes `power=2`.

### A Real World Example

Now let’s consider a real world example:

 ```python
def has_permission(page):
    def inner(username):
        if username == 'Admin':
            return "'{0}' does have access to {1}.".format(username, page)
        else:
            return "'{0}' does NOT have access to {1}.".format(username, page)
    return inner


current_user = has_permission('Admin Area')
print(current_user('Admin'))

random_user = has_permission('Admin Area')
print(random_user('Not Admin'))
```

This is a simplified function to check if a certain user has the correct permissions to access a certain page. You could easily modify this to grab the user in session to check if they have the correct credentials to access a certain route. Instead of checking if the user is just equal to `'Admin'`, you could query the database to check the permission and then return the correct view depending on whether the credentials are correct or not.

## Conclusion

The use of closures and factory functions is the most common and powerful use for inner functions. In most cases, when you see a decorated function, the decorator is a factory function that takes a function as argument and returns a new function that includes the old function inside the closure. Stop. Take a deep breath. Grab a coffee. Read that again.

To put it another way, a decorator is just syntactic sugar for implementing the process outlined in the `generate_power()` example.

I’ll leave you with a final example:

 ```python
def generate_power(exponent):
    def decorator(f):
        def inner(*args):
            result = f(*args)
            return exponent**result
        return inner
    return decorator


@generate_power(2)
def raise_two(n):
    return n

print(raise_two(7))


@generate_power(3)
def raise_three(n):
    return n

print(raise_two(5))
```

If your code editor allows it, view `generate_power(exponent)` and `generate_power(number)`side-by-side to illustrate the concepts discussed. (Sublime Text has Column View, for example.)

If you have not coded the two functions, open the code editor and start coding. For new programmers, coding is a hands-on activity: like riding a bike, you just have to do it and do it solo. So back to the task at hand!

After you have typed the code, you can now clearly see that it is similar in that it produces the same results, but there are differences. For those who have never used decorators, noting these differences will be the first step in understanding them if you venture down that path.
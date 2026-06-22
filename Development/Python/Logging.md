Logging

Logging is a build in module for Python and can be simply imported using:

```python
import logging
```

There are 5 levels of logging

- DEBUG: Detailed information, typically of interest only when diagnosing problems.
- INFO: Confirmation that things are working as expected.
- WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
- ERROR: Due to a more serious problem, the software has not been able to perform some function.
- CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

[Useful YouTube tutorial on Logging](https://www.youtube.com/watch?v=g8nQ90Hk328)

```python

# Logging.py
import logging

"""
DEBUG   : Detailed information, typically of interest only when diagnosing problems.
		  logging.basicConfig(level=logging.DEBUG)
		  
INFO    : Confirmation that things are working as expected.
		  logging.basicConfig(level=logging.INFO)
		  
WARNING : An indication that something unexpected happened, or indicative of some problem
          in the near future (e.g. ‘disk space low’). 
          The software is still working as expected.
		  logging.basicConfig(level=logging.WARNING)  # This is the default setting
          
ERROR   : Due to a more serious problem, the software has not been able to 
          perform some function.
		  logging.basicConfig(level=logging.ERROR)

CRITICAL: A serious error, indicating that the program itself may be unable 
          to continue running.
   		  logging.basicConfig(level=logging.CRITICAL)

"""

logging.basicConfig(filename='test.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# When you just want to show the log in the console use
# logging.basicConfig(level=logging.DEBUG)


def add(x,y):
	"""Add Function"""
	return x + y
	

def subtract(x,y):
	"""Subtract Function"""
	return x - y
	
	
def multiply(x,y):
	"""Multiply Function"""
	return x * y
	
	
def divide(x,y):
	"""Divide Function"""
	return x / y
	

num_1 = 10
num_2 = 5

add_result = add(num_1, num_2)
# Default type of logging, just print the result to check
# print('Add: {} + {} = {}'.format(num_1, num_2, add_result))

# Actual logging
logging.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
# Default type of logging, just print the result to check
# print('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

# Actual logging
logging.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
# Default type of logging, just print the result to check
# print('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

# Actual logging
logging.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
# Default type of logging, just print the result to check
# print('Div: {} / {} = {}'.format(num_1, num_2, div_result))

# Actual logging
logging.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result))


```



Another example

```python
# employee.py
import logging

logging.basicConfig(filename='employee.log', level=logging.INFO,
                    format='%(levelname)s:%(message)s')


class Employee:
    """A sample Employee class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last

        logging.info('Created Employee: {} - {}'.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('John', 'Smith')
emp_2 = Employee('Corey', 'Schafer')
emp_3 = Employee('Jane', 'Doe')
```

[More info on Logging](https://docs.python.org/3/library/logging.html)

[LogAttributes to config the logfile](https://docs.python.org/3/library/logging.html#logrecord-attributes)

If you use Employee from inside Logging, then the format of the logging is set in the employee.py to INFO

The setting in logging.py where it is set to DEBUG is ingnored.
To solve this make use of a logger. 

First we change employee.py

```python
# employee.py
logger = logging.getLogger(__name__)    # set the logger and use the name of the module
logger.setLevel(logging.INFO)           # Set the loglevel

# define the format of the logging here, instead of in the baseConfig
formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

# make shure the logging will end up in its own logfile
file_handler = logging.FileHandler('employee.log')
file_handler.setFormatter(formatter)     # Set the format of the logging here
logger.addHandler(file_handler)

# Since al logging configuration is done above, this line is no longer necesary 
# logging.basicConfig(filename='employee.log', level=logging.INFO, format='%(levelname)s:%(message)s')


class Employee:
    """A sample Employee class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last
		
        # Change logging.info to o use the logger
        logger.info('Created Employee: {} - {}'.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('John', 'Smith')
emp_2 = Employee('Corey', 'Schafer')
emp_3 = Employee('Jane', 'Doe')
```



In the logging.py we added two kinds of logging

Logging to a file (file_handler)
Logging to the console (stream_handler)

Also there is a difference, the default level of logging is set to DEBUG, so all info will be logged, but, only errors are written to the log file

```python
import logging
import employee

"""
DEBUG   : Detailed information, typically of interest only when diagnosing problems.
          logging.basicConfig(level=logging.DEBUG)

INFO    : Confirmation that things are working as expected.
          logging.basicConfig(level=logging.INFO)

WARNING : An indication that something unexpected happened, or indicative of some problem
          in the near future (e.g. ‘disk space low’). 
          The software is still working as expected.
          logging.basicConfig(level=logging.WARNING)  # This is the default setting

ERROR   : Due to a more serious problem, the software has not been able to 
          perform some function.
          logging.basicConfig(level=logging.ERROR)

CRITICAL: A serious error, indicating that the program itself may be unable 
          to continue running.
          logging.basicConfig(level=logging.CRITICAL)
"""

logger = logging.getLogger(__name__)    # set the logger and use the name of the module
logger.setLevel(logging.DEBUG)           # Set the loglevel

# define the format of the logging here, instead of in the baseConfig
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')

# make shure the logging will end up in its own logfile
file_handler = logging.FileHandler('test.log')
file_handler.setLevel(logging.ERROR)          # set the logging to errors only
file_handler.setFormatter(formatter)          # Set the format of the logging here

# The above code logs to the specified file, but it is also usefull to log to the console
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)         # Set the format of the logging here

logger.addHandler(file_handler)       # set the filehandler to write log to a logfile
logger.addHandler(stream_handler)     # set the streamhandler to write log to the console


# When you just want to show the log in the console use
# logging.basicConfig(level=logging.DEBUG)


def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    try:
        result = x / y
    except ZeroDivisionError:
        logger.exception('Tried to divide by zero')
    else:
        return result


num_1 = 10
num_2 = 0

add_result = add(num_1, num_2)
# Default type of logging, just print the result to check
# print('Add: {} + {} = {}'.format(num_1, num_2, add_result))

# Actual logging
logger.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
# Default type of logging, just print the result to check
# print('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

# Actual logging
logger.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
# Default type of logging, just print the result to check
# print('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

# Actual logging
logger.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
# Default type of logging, just print the result to check
# print('Div: {} / {} = {}'.format(num_1, num_2, div_result))

# Actual logging
logger.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result))

```


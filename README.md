# Object orientated programming (OOP) in Python
## Four Pillars of OOP
## Functions and good practice of functions
**DRY** - Don't Repeat Yourself

Let's create a function
- Syntax -> `def` is used to declare followed by name of the `function():`

#### First iteration
```python
def function():
    print("This is a function")
```
- `pass` is the keyword that allows the interpreter to skip this without any errors

- To call the function `function()`

- If the function is not called the code would execute with no errors but no output
- DRY - Don't Repeat Yourself by declaring functions and re-using code

#### Second iteration using return statement
```py
def function():
    print("This is the print function")
    return "This is from the return statement"

print(function())
```

#### Third iteration with the user's name as a string as an argument/args

```python
def greeting(name):
    return "Hello " + name + "!"

print(greeting("Greg"))
```

#### Creating a function to prompt user to enter their name and display the name back to user with greeting message
```python
Name = input("What is your name?    ")
def greeting(name):
    return "Hello " + name.capitalize() + "!"

print(greeting(Name))
```
#### Creating a function with multiple arguments as an int
```python
def add(num1, num2):
    return num1 + num2

print(add(9, 3))

def multiply(num1, num2):
    return num1 * num2
    print(" This is the required outcome of 2 numbers: ")  # This line of code will not execute as the return
                                                           # statement is the last line of code that the function executes
print(multiply(4, 6))
```

## Python Modules and Packages
### Modules
- Python's extensive documentation on python.org
- We have used functions that we created as well as built-in

- `import` is the keyword that is used to import any module available in python.org

To import specifically from a file
```py
from random import random
```

#### `math` Module
- `math` module is used to calculate values
```py
import math

num1 = 23.425  # float

# In a real life scenario, the value needs to be rounded depending on the value
# If the value is less than .5, round it down, if the decimal value is more than or equal to .5, round it up

print(math.ceil(num1))  # Round up
print(math.floor(num1))  # Round down
print(math.pi)  # Prints the value of pi
```

#### `random` Module
- `random` module is used for random value generation

```py
import random  # 

print(random.random())  # A random float between 0.0 and 0.99 is generated every time the program is executed
```

#### Interacting with the machine using python
#####`os` Module
```python
import os  # used to get information about the operating system of the machine
```
We use this module to facilitate the code for different users on different operating systems
```py
import math, datetime, sys  # sys is used to get system specific information

work_dir = os.getcwd()  # `getcwd` provides the current location/path
print(work_dir)
```
For Linux/MacOS
```py
print(os.getuid())  # `getuid` provides the current user id
print(os.cpu_count())  # `cpu.count()` provides the total core and thread count of the machine's cpu - works on Windows too
print(os.uname())  # `uname()` gives system-dependent version information
```
#### Other examples of modules
```py
print(datetime.date.today())  # Shows today's date
print(sys.path)  # Shows the absolute path
```
### Packages
`pip` is a package manager in python to install any packages
#### `requests` package
`requests` is a package to interact with a live API

For the `requests` package, `pip` was used to install the package

This package makes an API call to any web address using requests packages
```python
import requests

requests_api = requests.get("https://www.bbc.co.uk")
```

```py
print(requests_api.status_code)  # Status Codes are type: int - 200 for success, 404 and above for failure
```
Using the status code, the website can be tested to see if it is running normally
```py
if requests_api.status_code == 200:
    print("The website is running normally")
```
Other uses for requests package
```python
print(requests_api.headers)  # Shows the headers of the url as type: dict
print(requests_api.content)  # Shows the content of the url as type: bytes
```

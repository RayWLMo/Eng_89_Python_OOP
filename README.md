# Object orientated programming (OOP) in Python
## Four Pillars of OOP
### Abstraction
Remove unnecessary information that doesn't need to be seen by the user
### Inheritance

### Encapsulation
Only authorised users can see restricted data
### Polymorphism
### Demonstrating the 4 Pillars of OOP
#### Step 1 - Creating an Animal class
- Step one: create an animal.py file to create a parent class
```python
class Animal:  # follow the correct naming convention (capitalized for classes)
```

Declaring attributes in the init method
- Initialise with built-in method called __init__(self)
- `self` refers to current class
```py
    def __init__(self):  # Declaring attributes in the init method
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True
```
Declaring methods/behaviours
```py
    def breathe(self):
        return "Keep breathing to stay alive"

    def eat(self):
        return "Keep eating to stay alive"

    def move(self):
        return "Move around to stay aware"
```
We need to create an object of this class in order to use any methods
```py
cat = Animal()  # Creating an object of Animal class
```
For `cat` as a user, the functionality inside Animal class and the method breathe is abstracted
```py
print(cat.eat())
print(cat.breath())  
```
#### Step 2 - Create a reptile class to inherit Animal class
- Step two: Create a file called reptile.py to abstract data and inherit from animal.py

if not in the same directory, the class needs to be imported with an absolute path

 - Because they are in the directory, it can be imported as so.
```py
from animal import Animal
```
Declaring Attributes
```py
class Reptile(Animal):  # Inheriting from Animal class

    def __init__(self):
        super().__init__()  # super() is used to inherit everything from the parent class
        self.cold_blooded = True
        self.heart_chambers = [3, 4]
```
Declaring Methods/behaviours
```py
    def seek_heat(self):
        return "Must sit in the sun for some heat"

    def hunt(self):
        return "Must hunt for food to survive"

    def use_venom(self):
        return "Uses venom on prey and potential threats"
```
Creating an object of the Reptile class
```py
smart_reptile = Reptile()
print(smart_reptile.breathe())  # breathe() method is inherited from Animal class
print(smart_reptile.hunt())  # hunt() is available in Reptile class
```
#### Step 3 - Creating a Snake class
- step three: create a file called snake.py
Importing the class from last step
```py
from reptile import Reptile
```
Declaring Attributes
```py
class Snake(Reptile):

    def __init__(self):
        super().__init__()
        self.forked_tongue = True
        self.tetrapods = False
```
Adding specific methods/behaviours
```py
    def use_tongue_to_smell(self):
        return "Uses tongue to seek out prey by smelling"

    def slithers_to_move(self):
        return "Slides side to side in a slither motion to move"

```
Creating an object of Snake class
```py
smart_snake = Snake()
print(smart_snake.move())  # move() is inherited from Animal class
print(smart_snake.hunt())  # hunt() is inherited from Reptile class
print(smart_snake.use_tongue_to_smell())  # use_tongue_to_smell() is available from Snake class
```
#### Step 4 - Creating a Python class
- step four: create a file called python.py and this point we should be able to utilise inheritance from multiple classes - everything available
Importing from last step
```py
from snake import Snake
```
Declaring Attributes
```py
class Python(Snake):
    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True
```
Declaring Methods/behaviours
```py
    def digest_large_prey(self):
        return "Digests large animals so has a wider selection of prey"

    def climb(self):
        return "Able to climb up trees and other various vertical surfaces"

    def constricts_prey(self):
        return "Able to constrict prey to kill them effectively"
```
Creating an object of Python class
```py
fast_python = Python()
print(fast_python.move())  # move() is inherited from Animal class
print(fast_python.hunt())  # hunt() inherited from Reptile class
print(fast_python.use_tongue_to_smell())  # use_tongue_to_smell() is inherited from Snake class
print(fast_python.constricts_prey())  # constricts_prey() is available from Python class
```

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
from file_name import Class_Name
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
##### `os` Module
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
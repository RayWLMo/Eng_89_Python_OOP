# Object orientated programming (OOP) in Python
## Four Pillars of OOP
### Functions and good practice of functions
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
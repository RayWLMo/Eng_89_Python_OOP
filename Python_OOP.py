# # Let's create a function
# # Syntax -> def is used to declare followed by name of the function():
#
# # First iteration
#
# def function():
#     print("This is a function")
#
#
# # pass  # pass is the keyword that allows the interpreter to skip this without any errors
#
# function()  # To call the function
#
# # If the function is not called the code would execute with no errors but no output
# # DRY - Don't Repeat Yourself by declaring functions and re-using code
#
# # Second iteration using return statement
#
# def function():
#     print("This is the print function")
#     return "This is from the return statement"
#
#
# print(function())
#
# # Third iteration with with username as a string as an argument/args
#
# def greeting(name):
#     return "Hello " + name + "!"
#
#
# print(greeting("Greg"))
#
# # Create a function to prompt user to enter their name and display the name back to user with greeting message
#
# Name = input("What is your name?    ")
# def greeting(name):
#     return "Hello " + name.capitalize() + "!"
#
# print(greeting(Name))
#
# # Lets create a function with multiple arguments as an int
#
# def add(num1, num2):
#     return num1 + num2
#
# print(add(9, 3))
#
# def multiply(num1, num2):
#     return num1 * num2
#     print(" This is the required outcome of 2 numbers: ")  # This line of code will not execute as the return
#                                                            # statement is the last line of code that the function executes
# print(multiply(4, 6))



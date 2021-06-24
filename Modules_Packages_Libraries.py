# # Python's extensive documentation on python.org
# # We have used functions that we created as well as built-in
#
# # `import` is the keyword that is used to import any module available in python.org
#
# # Can import from a file
#
# from random import random
#
# # `math` Module
#
# import math  # To calculate values
#
# num1 = 23.425  # float
#
# # In a real life scenario, the value needs to be rounded depending on the value
# # If the value is less than .5, round it down, if the decimal value is more than or equal to .5, round it up
#
# print(math.ceil(num1))  # Round up
# print(math.floor(num1))  # Round down
# print(math.pi)  # Prints the value of pi
#
# # `Random` Module
#
# import random  # To generate random values
#
# print(random.random())  # A random float between 0.0 and 0.99 is generated every time the program is executed
#
# # Interacting with the machine using python
# import os  # used to get information about the operating system of the machine
#
# # We use this module to facilitate the code for different users on different operating systems
#
# import math, datetime, sys  # sys is used to get system specific information
#
# work_dir = os.getcwd()  # `getcwd` provides the current location/path
# print(work_dir)
#
# #  For Linux/MacOS
# print(os.getuid())  # `getuid` provides the current user id
# print(os.cpu_count())  # `cpu.count()` provides the total core and thread count of the machine,s cpu - works on Windows too
# print(os.uname())  # `uname()` gives system-dependent version information
#
# print(datetime.date.today())  # Shows today's date
# print(sys.path)  # Shows the absolute path
#
# # `requests` is a package to interact with a live API
# # this package makes an API call to any web address using requests packages
# # `pip` is a package manager in python to install any packages
# # For the `requests` package, `pip` was used to install the package
# In the terminal -> pip install requests

import requests

requests_api = requests.get("https://www.bbc.co.uk")

print(requests_api.status_code)  # Status Codes are type: int - 200 for success, 404 and above for failure
# Using this, the website can be tested to see if it running normally
if requests_api.status_code == 200:
    print("The website is running normally")
print(requests_api.headers)  # Shows the headers of the url as type: dict
print(requests_api.content)  # Shows the content of the url as type: bytes


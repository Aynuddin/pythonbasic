# Step 9: Modules, Packages & the Python Standard Library
# In Java, code is structured into packages (e.g. package com.company.app;) and imported with 'import java.util.*'.
# In Python, EVERY file ending with .py is automatically a MODULE! No setup needed.
#
# Key Java vs Python comparisons:
# - Java 'import java.util.Random;'      --> Python 'import random' or 'from random import randint'
# - Java 'public static void main'       --> Python 'if __name__ == "__main__":'
# - Java package folders                 --> Python package folders (folders containing an __init__.py)
# - Java JAR files / Maven dependencies  --> Python 'pip' and PyPI packages (e.g., pip install requests)

print("--- 1. IMPORTING BUILT-IN MODULES (Standard Library) ---")
# Python comes with "batteries included" — hundreds of built-in modules ready to use!

# Style A: Import the whole module
import math
print("math.sqrt(49):", math.sqrt(49))      # 7.0
print("math.ceil(4.2):", math.ceil(4.2))    # 5 (rounds up)
print("math.pi:", round(math.pi, 4))        # 3.1416

# Style B: Import specific functions/constants directly (saves typing 'math.')
from math import pow, floor
print("pow(2, 5):", pow(2, 5))              # 32.0
print("floor(4.9):", floor(4.9))            # 4 (rounds down)

# Style C: Import with an alias (nickname) using 'as' (very common in data science, e.g. import numpy as np)
import math as m
print("Using alias m.factorial(5):", m.factorial(5)) # 120


print("\n--- 2. ESSENTIAL BUILT-IN MODULES: RANDOM & DATETIME ---")
import random
from datetime import datetime, date

# Generating random numbers and picking random items:
lucky_number = random.randint(1, 100) # Random integer between 1 and 100 (inclusive)
print("Random number (1-100):", lucky_number)

fruits = ["Apple", "Banana", "Cherry", "Mango", "Orange"]
picked_fruit = random.choice(fruits)  # Picks one random element from a list
print("Random fruit chosen:", picked_fruit)

cards = [1, 2, 3, 4, 5]
random.shuffle(cards)                 # Shuffles list in-place
print("Shuffled cards:", cards)

# Working with dates and times:
now = datetime.now()
print("Current Date & Time:", now)
# Formatting dates nicely using strftime:
# %Y = 4-digit year, %m = 2-digit month, %d = day, %H = hour, %M = minute, %S = second
formatted_time = now.strftime("%d-%b-%Y %H:%M:%S")
print("Formatted Date & Time:", formatted_time)


print("\n--- 3. OPERATING SYSTEM & SYSTEM MODULES (os & sys) ---")
import os
import sys

# os module lets you interact with folders, files, and operating system paths
current_dir = os.getcwd() # Get Current Working Directory
print("Current Directory:", current_dir)
print("Does 'sample.txt' exist?", os.path.exists("sample.txt"))

# sys module gives info about Python runtime itself
print("Python Version:", sys.version.split()[0])
print("Operating System Platform:", sys.platform)


print("\n--- 4. IMPORTING YOUR OWN CUSTOM MODULE ---")
# You can import ANY .py file located in the same directory!
# We created 'helper_utils.py' in this folder. Let's import and use its functions:
import helper_utils
from helper_utils import greet_user, is_palindrome

# Calling functions defined inside helper_utils.py:
greeting = greet_user("Ayn")
print("Greeting from custom module:", greeting)

discount_result = helper_utils.calculate_discount(500, 20)
print("Discount calculation (500 with 20% off):", discount_result)

print("Is 'racecar' a palindrome?", is_palindrome("racecar"))
print("Is 'python' a palindrome?", is_palindrome("python"))

# LOOK CAREFULLY:
# Notice how the test code inside 'helper_utils.py' (under if __name__ == "__main__":)
# did NOT print here! That is because when helper_utils is imported, its __name__ is
# "helper_utils", NOT "__main__".


print("\n--- 5. WHAT IS A PACKAGE? ---")
# A MODULE = A single .py file.
# A PACKAGE = A folder that contains multiple modules, usually with an __init__.py file.
#
# Example folder structure:
#   my_project/
#   │
#   ├── main.py
#   └── my_package/
#       ├── __init__.py      (Marks this folder as a Python package)
#       ├── database.py      (Module: e.g., connect_db())
#       └── payment.py       (Module: e.g., process_card())
#
# In main.py, you would import like this:
#   from my_package.payment import process_card
#   from my_package.database import connect_db


# -------------------------------------------------------------
# 6. THE 'if __name__ == "__main__":' IDIOM (Python's main method)
# -------------------------------------------------------------
# In Java, execution starts at:
#   public static void main(String[] args) { ... }
#
# In Python, execution starts at line 1 of the file you run.
# To ensure code only runs when this file is executed directly (not when imported):
if __name__ == "__main__":
    print("\n--- [modules.py] EXECUTION ENTRY POINT ---")
    print(f"This file is being run directly! __name__ is: {__name__}")
    print("All top-level statements above have run successfully.")


# -------------------------------------------------------------
# PRACTICE SECTION FOR YOU:
# Try these tasks to practice working with modules!
#
# Task 1: Generate an Order ID
#         - Use 'datetime.now()' and 'random.randint(100, 999)'
#         - Create an order ID string in the format: "ORD-YYYYMMDD-<random_number>"
#           (e.g., "ORD-20260904-742")
#         - Print the generated Order ID.
#
# Task 2: Add a new function to 'helper_utils.py' and import it here
#         - Open 'helper_utils.py' and add:
#             def celsius_to_fahrenheit(celsius):
#                 return (celsius * 9/5) + 32
#         - Import 'celsius_to_fahrenheit' in this file and convert 25°C to Fahrenheit.
#
# Task 3: Use the 'os' module to inspect a file
#         - Use 'os.path.exists("products.json")' to check if 'products.json' is present.
#         - If it exists, print its full absolute path using 'os.path.abspath("products.json")'.
# -------------------------------------------------------------

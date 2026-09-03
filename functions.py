# Step 4: Functions in Python
# A function is a reusable block of code that performs a specific task.
# Instead of rewriting the same code again and again, you write it once inside a function and call it whenever needed!

print("--- 1. DEFINING AND CALLING A FUNCTION ---")
# Use the 'def' keyword to define a function, followed by its name and parentheses ()
def say_hello():
    print("Hello! Welcome to Python Functions.")

# Defining a function doesn't run it. You must "call" it:
say_hello()
say_hello()  # You can reuse it as many times as you want!


print("\n--- 2. FUNCTIONS WITH PARAMETERS (INPUTS) ---")
# Parameters are variables inside the parentheses that receive information when the function is called.
def greet_person(name):
    print("Hello,", name, "! Hope you are having a great day.")

greet_person("Ayn")
greet_person("John")


print("\n--- 3. FUNCTIONS WITH MULTIPLE PARAMETERS ---")
def describe_person(name, role, city):
    print(name, "is a", role, "based in", city)

describe_person("Ayn", "Developer", "Bangalore")


print("\n--- 4. RETURN VALUES (OUTPUTS) ---")
# 'return' sends a result back to the place where the function was called.
# Difference between print() and return:
# - print() just displays text on the screen.
# - return gives back a value that you can store in a variable or use in calculations.

def add_numbers(a, b):
    result = a + b
    return result

sum_total = add_numbers(10, 25)
print("The sum is:", sum_total)


print("\n--- 5. DEFAULT PARAMETER VALUES ---")
# You can provide a default value if the caller doesn't pass one.
def greet_with_role(name, role="Learner"):
    print("Welcome", name, "- Role:", role)

greet_with_role("Ayn")                     # Uses default role "Learner"
greet_with_role("Ayn", "Python Developer") # Overrides default with "Python Developer"


print("\n--- 6. COMBINING FUNCTIONS WITH IF/ELSE (From Step 3!) ---")
# You can use if/else conditions inside functions!
def check_voting_eligibility(age):
    if age >= 18:
        return "Eligible for voting"
    else:
        return "Not eligible for voting"

print("Age 20 check:", check_voting_eligibility(20))
print("Age 15 check:", check_voting_eligibility(15))


# -------------------------------------------------------------
# PRACTICE SECTION FOR YOU:
# Try writing your own functions below!
#
# Task 1: Create a function called 'multiply(x, y)' that returns x * y.
# Task 2: Create a function called 'is_even(number)' that returns True if the number is even, and False if it is odd. (Hint: use number % 2 == 0)
# Task 3: Call your functions and print the results!
# -------------------------------------------------------------
#Task 1
def multiply(x,y):
    return x*y

total_mul=multiply(10,5)
print(total_mul)

#Task 2
def is_even(num):
    if(num % 2==0):
        return True
    else:
        return False

print(is_even(5))    

#Task 3



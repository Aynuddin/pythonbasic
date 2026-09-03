# Step 7: Error & Exception Handling in Python
# In Java, you use: try { ... } catch (Exception e) { ... } finally { ... }
# In Python, you use: try: ... except Exception as e: ... finally: ...
#
# Key comparisons:
# - Java 'try'                 --> Python 'try'
# - Java 'catch'               --> Python 'except'
# - Java 'finally'             --> Python 'finally'
# - Java 'throw'               --> Python 'raise'
# - Python Bonus: 'else' block --> Runs ONLY if NO error happened in try!

print("--- 1. BASIC TRY...EXCEPT ---")
# Without try/except, division by zero crashes the entire program!
try:
    result = 10 / 0 # 0 is requied
except ZeroDivisionError as e:
    print("Caught an error:", e)
    print("Program continues running safely without crashing!")


print("\n--- 2. CATCHING MULTIPLE SPECIFIC EXCEPTIONS ---")
# Best practice: catch specific errors instead of a generic catch-all.
def convert_and_divide(number_str):
    try:
        val = int(number_str)       # May raise ValueError if not a number
        result = 100 / val           # May raise ZeroDivisionError
        return result
    except ValueError:
        print(f"Error: '{number_str}' is not a valid integer!")
    except ZeroDivisionError:
        print("Error: Cannot divide 100 by zero!")
    except Exception as e:
        # Generic fallback for any unexpected error (Java's catch (Exception e))
        print("Unexpected error occurred:", e)

convert_and_divide("20")  # Valid: returns 5.0
convert_and_divide("abc") # Triggers ValueError
convert_and_divide("0")   # Triggers ZeroDivisionError


print("\n--- 3. THE 'ELSE' AND 'FINALLY' BLOCKS ---")
# - 'else': runs ONLY if the try block succeeded without any errors.
# - 'finally': runs ALWAYS, whether there was an error or not (like cleanup).
def check_server_status(port):
    try:
        print(f"Attempting connection on port {port}...")
        if port == 80:
            print("Connected successfully!")
        else:
            raise ConnectionError("Port refused connection!")
    except ConnectionError as err:
        print("Exception caught:", err)
    else:
        print("Else block: Connection was smooth with zero errors.")
    finally:
        print("Finally block: Closing connection / releasing resources (Always runs).")

check_server_status(80)
print("-" * 30)
check_server_status(8080)


print("\n--- 4. RAISING EXCEPTIONS (Java's 'throw') ---")
# Use 'raise' when you want to enforce a rule and stop bad input.
def set_user_age(age):
    if age < 0:
        raise ValueError("Age cannot be a negative number!")
    if age > 150:
        raise ValueError("Age is unrealistically high!")
    print(f"Age set successfully to: {age}")

try:
    set_user_age(25)
    set_user_age(-5)  # Throws ValueError!
except ValueError as err:
    print("Validation Error:", err)


print("\n--- 5. CUSTOM EXCEPTIONS ---")
# Just like in Java (class MyException extends Exception):
# In Python, create a class that inherits from 'Exception'!
class InsufficientFundsException(Exception):
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsException(f"Cannot withdraw ${amount}. Current balance: ${self.balance}")
        self.balance -= amount
        print(f"Withdrew ${amount}. Remaining balance: ${self.balance}")

account = BankAccount(500)
try:
    account.withdraw(200)
    account.withdraw(600)  # Will raise our custom exception!
except InsufficientFundsException as err:
    print("Custom Exception Caught:", err)


# -------------------------------------------------------------
# PRACTICE SECTION FOR YOU:
#
# Task 1: Safe Division
# Write a function 'safe_divide(a, b)' that:
# - Uses try/except to divide a / b.
# - Catches ZeroDivisionError and returns "Cannot divide by zero".
# - Catches TypeError (in case someone passes text instead of numbers) and returns "Both inputs must be numbers".
# - Test it with (10, 2), (10, 0), and (10, "hello").
#
# Task 2: Safe Dictionary Key Lookup
# Given user = {"name": "Ayn", "role": "Developer"}
# Write a function 'get_profile_field(user_dict, key_name)' that:
# - Tries to return user_dict[key_name]
# - Catches KeyError and returns f"Field '{key_name}' does not exist!"
# - Test it with "role" and "salary".
#
# Task 3: Raise Validation Error
# Write a function 'validate_password(password)' that:
# - If len(password) < 8, raises a ValueError("Password must be at least 8 characters long!")
# - Otherwise returns "Password is valid!"
# - Call it inside a try/except block to test both a short and a valid password.
# -------------------------------------------------------------

# Task 1
def safe_divide(a,b):
    try:
       result = a/b
       return result
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Both inputs must be numbers"

print("Both inputs are numbers:" , safe_divide(10,2))
print("One number other number zero" , safe_divide(10,0))
print("One number other string : ", safe_divide(10,"hello"))

#Task 2

def get_profile_field(user_dict,key_name):
    try:
        return user_dict[key_name]
    except KeyError:
        return f"Field {key_name} doest not exist!"


# user dict
user = {
    "name":"Ayn",
    "role":"Developer"
}

print("Get the field value by giving proper field name :",get_profile_field(user,"name"))
print("Get the field value by giving proper field name :",get_profile_field(user,"salary"))

#Task 3

def validate_password(password):

    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long!")
    else:
        return "Password is valid!"

# Test Cas1
try:
    print("Test 1:", validate_password("ayn@1234"))
except ValueError as err:
    print(err)

#Test Case 2

try:
    print("Test 2:", validate_password("ayn"))
except ValueError as err:
    print(err)





       
       
   



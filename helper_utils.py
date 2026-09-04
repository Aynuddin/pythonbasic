# Helper module to demonstrate custom imports in Python
# A module is simply a Python file (.py) containing functions, classes, or variables that you want to reuse!

def greet_user(name):
    """Returns a greeting message."""
    return f"Hello, {name}! Welcome to Python Modules."

def calculate_discount(price, discount_percent):
    """Calculates discounted price."""
    return price - (price * discount_percent / 100)

def is_palindrome(word):
    """Checks if a string reads the same forwards and backwards."""
    clean_word = str(word).lower().replace(" ", "")
    return clean_word == clean_word[::-1]


# -------------------------------------------------------------
# THE FAMOUS: if __name__ == "__main__":
# -------------------------------------------------------------
# Every Python file has a built-in variable called __name__.
# - If you run THIS file directly (python helper_utils.py), __name__ is "__main__".
# - If another file IMPORTS this file, __name__ becomes "helper_utils" (the filename).
#
# This 'if' check acts like Java's 'public static void main(String[] args)':
# Code inside this block ONLY runs when you execute this file directly,
# but it is completely IGNORED when someone imports this module!
# -------------------------------------------------------------
if __name__ == "__main__":
    print("--- [helper_utils.py] RUNNING DIRECTLY (Test Mode) ---")
    print("Current __name__ is:", __name__)
    print("Testing greet_user:", greet_user("Ayn"))
    print("Testing calculate_discount:", calculate_discount(1000, 10))
    print("Testing is_palindrome ('radar'):", is_palindrome("radar"))
    print("------------------------------------------------------\n")

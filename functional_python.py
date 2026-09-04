# Step 10: Functional Python — Comprehensions, Lambda, Map & Filter
# In Java, you use Java Streams to process collections:
#   list.stream().filter(x -> x > 10).map(x -> x * 2).collect(Collectors.toList());
#
# In Python, we have:
# 1. Comprehensions (concise, expressive, and the most "Pythonic" way to work with collections)
# 2. Lambda functions (quick, one-line anonymous functions)
# 3. Built-in map() and filter() functions

print("--- 1. LIST COMPREHENSIONS ---")
# Syntax: [ expression for item in iterable if condition ]
# Instead of writing 4-5 lines of for-loop + append, you write it in ONE clean line!

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Traditional way (verbose):
squared_traditional = []
for n in numbers:
    squared_traditional.append(n ** 2)
print("Traditional squared:", squared_traditional)

# Pythonic List Comprehension way:
squared_comp = [n ** 2 for n in numbers]
print("Comprehension squared:", squared_comp)

# Filtering with 'if':
even_numbers = [n for n in numbers if n % 2 == 0]
print("Even numbers only:", even_numbers)

# If-Else inside List Comprehension:
# Syntax: [ value_if_true if condition else value_if_false for item in iterable ]
labels = ["Even" if n % 2 == 0 else "Odd" for n in numbers]
print("Labels:", labels)


print("\n--- 2. DICTIONARY & SET COMPREHENSIONS ---")
# Dict Comprehension: { key_expr: value_expr for item in iterable }
words = ["python", "developer", "backend", "code"]
word_lengths = {word: len(word) for word in words}
print("Word lengths dictionary:", word_lengths)

# Swapping keys and values in a dictionary:
original_dict = {"a": 1, "b": 2, "c": 3}
inverted_dict = {v: k for k, v in original_dict.items()}
print("Inverted dictionary:", inverted_dict)

# Set Comprehension: creates a unique set automatically
num_list = [1, 2, 2, 3, 4, 4, 5, 5]
unique_squares = {x ** 2 for x in num_list}
print("Unique squares set:", unique_squares)


print("\n--- 3. LAMBDA FUNCTIONS (Anonymous Functions) ---")
# In Java:   (a, b) -> a + b
# In Python: lambda a, b: a + b
#
# A lambda can take any number of arguments, but can only have ONE expression (which is returned).
# Useful when you need a throwaway function for a few seconds.

# Simple lambda:
add = lambda a, b: a + b
print("Lambda add(10, 20):", add(10, 20))

# The real power of lambda: Custom Sorting with sorted(..., key=lambda)
users = [
    {"name": "Ayn", "age": 25, "role": "Developer"},
    {"name": "Sara", "age": 22, "role": "Designer"},
    {"name": "John", "age": 30, "role": "Manager"}
]

# Sort users by age (ascending):
by_age = sorted(users, key=lambda u: u["age"])
print("Users sorted by age:")
for u in by_age:
    print(" ", u["name"], "->", u["age"])

# Sort users by name alphabetically:
by_name = sorted(users, key=lambda u: u["name"])
print("Users sorted by name:", [u["name"] for u in by_name])


print("\n--- 4. FILTER() AND MAP() ---")
# filter(function, iterable) -> keeps items where function returns True (like Java stream.filter)
# map(function, iterable)    -> transforms every item (like Java stream.map)
# Note: Both return an iterator, so wrap them in list() to see results!

raw_scores = [35, 78, 92, 49, 88, 62, 20]

# Keep only passing scores (>= 50):
passing_scores = list(filter(lambda s: s >= 50, raw_scores))
print("Passing scores (>= 50):", passing_scores)

# Add a 5-mark bonus to all scores:
bonus_scores = list(map(lambda s: s + 5, raw_scores))
print("Scores with +5 bonus:", bonus_scores)

# Combining map + filter:
# Get bonus scores ONLY for passing students:
passing_bonus = list(map(lambda s: s + 5, filter(lambda s: s >= 50, raw_scores)))
print("Passing scores with bonus:", passing_bonus)


# -------------------------------------------------------------
# PRACTICE SECTION FOR YOU:
#
# Task 1 (List Comprehension):
# Given this list of prices in USD:
#   prices = [20, 150, 45, 300, 80, 500]
# Use a list comprehension to calculate prices with 10% tax added (price * 1.10),
# but ONLY for items that cost more than $50.
#
# Task 2 (Dictionary Comprehension):
# Given this list of city names:
#   cities = ["new york", "london", "tokyo", "paris", "delhi"]
# Use a dictionary comprehension to create a dict where:
#   key   = Capitalized city name (use city.title())
#   value = length of the city name
#
# Task 3 (Lambda & Sorting):
# Given this list of products:
#   products = [
#       {"name": "Laptop", "price": 1200},
#       {"name": "Mouse", "price": 25},
#       {"name": "Monitor", "price": 300},
#       {"name": "Keyboard", "price": 75}
#   ]
# Sort this list of products by 'price' in DESCENDING order (highest first)
# using sorted(products, key=lambda ..., reverse=True).
#
# Task 4 (filter + lambda):
# From the 'products' list above, use filter() and lambda to get all
# products that cost less than $100. Convert to a list and print their names.
# -------------------------------------------------------------

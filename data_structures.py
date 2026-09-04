# Step 5: Data Structures in Python (Lists & Dictionaries)
# So far, your variables only stored one value at a time (e.g., name = "Ayn", age = 25).
# Data structures allow you to store multiple items in a single variable!

print("--- 1. LISTS (ORDERED & CHANGEABLE) ---")
# A list is written with square brackets [].
fruits = ["apple", "banana", "mango", "orange"]
print("Full list:", fruits)

# In Python, indexing starts at 0:
print("First fruit (index 0):", fruits[0])
print("Second fruit (index 1):", fruits[1])
print("Last fruit (negative index -1):", fruits[-1])

# Slicing: get a portion of the list [start:stop] (stops before index 3)
print("First 3 fruits:", fruits[0:3])


print("\n--- 2. LIST METHODS (MODIFYING LISTS) ---")
# Add a new item to the end with .append()
fruits.append("grapes")
print("After append:", fruits)

# Remove an item with .remove()
fruits.remove("banana")
print("After removing banana:", fruits)

# Count how many items are in the list with len()
print("Number of fruits:", len(fruits))


print("\n--- 3. LOOPING THROUGH A LIST ---")
# Instead of using range(), you can loop directly through items in a list:
numbers = [10, 25, 40, 55, 70]
print("Printing each number:")
for num in numbers:
    print("Item:", num)


print("\n--- 4. DICTIONARIES (KEY-VALUE PAIRS) ---")
# Dictionaries store data in "key": "value" pairs, wrapped in curly braces {}.
# Think of it like a real dictionary: look up a word (key) to find its definition (value).
student = {
    "name": "Ayn",
    "age": 25,
    "course": "Python",
    "is_passed": True
}

print("Student dict:", student)
# Accessing values using their key:
print("Student Name:", student["name"])
print("Course:", student["course"])

# Adding or updating a key-value pair:
student["grade"] = "A"
student["age"] = 26  # Updates existing age
print("Updated student:", student)


print("\n--- 5. LOOPING THROUGH A DICTIONARY ---")
# Loop through keys and values:
for key, value in student.items():
    print(key, "-->", value)


print("\n--- 6. COMBINING FUNCTIONS + DATA STRUCTURES ---")
# Functions can take a list as an input and process it!
def find_highest_number(num_list):
    highest = num_list[0]
    for n in num_list:
        if n > highest:
            highest = n
    return highest

scores = [45, 88, 92, 67, 99, 74]
print("Scores:", scores)
print("Highest Score:", find_highest_number(scores))


# -------------------------------------------------------------
# PRACTICE SECTION FOR YOU:
#
# Task 1: Create a list of 4 of your favorite movies or hobbies.
#         - Print the first and last item.
#         - Add a 5th item using .append().
#
# Task 2: Create a dictionary called 'car' with keys: "brand", "model", "year".
#         - Print the brand of the car.
#         - Update the "year" to the current year.
#
# Task 3: Write a function called 'count_even_numbers(numbers_list)'
#         that loops through a list and returns how many even numbers are in it.
#         (Hint: reuse your is_even logic from Step 4!)
# -------------------------------------------------------------

#Task 1
hobbies = ["Swimming","Reading","Coding","Gaming"]

print(hobbies[0])
print(hobbies[-1]) #last item always found in index -1
hobbies.append("Batting")
print("After Updating 5th item : ",hobbies)

#Task 2
car = {
    "brand":"BMW",
    "model":"BMW-01",
    "year":2023
}
car_brand = car["brand"]
print("Brand of car :",car_brand)

car["year"] = 2026
print("After updating car model : ",car)

#Task 3

def count_even_number(nums):
    count_even=0
    for num in nums:
        if(num % 2 == 0):
            count_even+=1
    return count_even

numbers = [1,2,3,4,5,6,7,8,9,10]
print("Even numbers count in list",count_even_number(numbers))


# -------------------------------------------------------------
# LEVEL-UP PRACTICE CHALLENGES:
# 
# Challenge 1: Find the Average of a List
# Write a function 'calculate_average(num_list)' that:
# - Adds all numbers together in a loop
# - Divides the total by len(num_list)
# - Returns the average
# Test list: [10, 20, 30, 40, 50] (Expected result: 30.0)
#
# Challenge 2: Phonebook Lookup (Checking if key exists)
# Given this dictionary:
# phonebook = {"Ayn": "9876543210", "John": "9123456780", "Alice": "9988776655"}
# Write a function 'find_number(phonebook, name)' that:
# - Uses 'if name in phonebook:' to check if the person exists.
# - If found, return their number.
# - If not found, return "Contact not found".
#
# Challenge 3: Real-World Filter (List of Dictionaries)
# Given this list of employees:
# employees = [
#     {"name": "Ayn", "department": "IT"},
#     {"name": "Sara", "department": "HR"},
#     {"name": "Rahul", "department": "IT"},
#     {"name": "Emily", "department": "Marketing"}
# ]
# Write a function 'get_it_team(emp_list)' that:
# - Loops through the list
# - Collects names of employees where emp["department"] == "IT" into a new list
# - Returns that list of names
# (Expected result: ['Ayn', 'Rahul'])
# -------------------------------------------------------------

#Challenge 1
def calculate_average(num_List):
    sum=0
    for i in num_List:
        sum+=i
    avg = sum/len(num_List)
    return avg

numbers=[10,20,30,40,50]
print("Average of the numbers from list : ", calculate_average(numbers))

#Challenge 2

def find_number(phonebook,name):
    if(name in phonebook):
        return phonebook.get(name)  # phonebook[name]   
    else:
        return "Contact Not Found"
phonebook={
    "Ayn":"9876543210",
    "John":"9123456780",
    "Alice":"9988776655"
}
print("Find the phone number : ", find_number(phonebook,"John"))

#Challenge 3
def get_it_team(empList):
    names=[]
    for emp in empList:
        if(emp["department"] == "IT"):
            names.append(emp["name"])
    return names

empList =[{
    "name":"Ayn",
    "department":"Developer",
},{
    "name":"John",
    "department":"IT",
},{
    "name":"Rahul",
    "department":"Developer",
},{
    "name":"Aysha",
    "department":"IT",
}]

print("IT employees names are : ", get_it_team(empList))


print("\n--- 7. SETS (JAVA'S HASHSET: UNIQUE & UNORDERED) ---")
# Sets are written with curly braces {} (like dicts, but without colons/keys).
# Key properties:
# 1. No duplicate values allowed (duplicates are discarded automatically).
# 2. Unordered (no indexing like set[0]).
# 3. Super fast O(1) membership check using 'in'.

# Example A: Automatic duplicate removal
skills = {"Python", "Java", "Python", "SQL", "Java"}
print("Skills (duplicates removed):", skills)

# Example B: Adding and removing items
skills.add("Docker")
skills.remove("SQL")
print("After add/remove:", skills)

# Example C: Set operations (Intersection & Union)
team_a = {"Python", "Java", "C++"}
team_b = {"Java", "Python", "Go"}

# Common skills (Intersection - like SQL INNER JOIN)
common_skills = team_a & team_b
print("Common skills (team_a & team_b):", common_skills)

# All skills combined (Union - like SQL FULL JOIN)
all_skills = team_a | team_b
print("All combined skills (team_a | team_b):", all_skills)

# Note: To create an empty set, use set() because {} creates an empty dictionary!
empty_set = set()


print("\n--- 8. TUPLES (READ-ONLY / IMMUTABLE LISTS) ---")
# Tuples are written with parentheses ().
# Key properties:
# 1. Ordered (has index 0, 1, 2...).
# 2. IMMUTABLE: Once created, you CANNOT change, add, or remove items.
# 3. Faster and safer than lists when data should never be modified.

# Example A: Creating a tuple
screen_resolution = (1920, 1080)
print("Screen resolution:", screen_resolution)
print("Width (index 0):", screen_resolution[0])

# Trying to change will cause an error:
# screen_resolution[0] = 2560  # <-- TypeError: 'tuple' object does not support item assignment!

# Example B: Tuple Unpacking (very common in Python!)
# Extract values into separate variables in one line:
width, height = screen_resolution
print("Unpacked -> Width:", width, "Height:", height)

# Example C: Functions returning multiple values (secretly returns a tuple!)
def get_user_location():
    latitude = 12.9716
    longitude = 77.5946
    return latitude, longitude  # Returns a tuple (12.9716, 77.5946)

lat, lon = get_user_location()
print("Location:", lat, lon)


# -------------------------------------------------------------
# PRACTICE SECTION FOR SETS & TUPLES:
#
# Task 4: Remove Duplicates from a List using a Set
# Given this list of order IDs with duplicates:
# order_ids = [101, 102, 105, 101, 108, 102, 105, 109]
# Convert this list to a set to remove duplicates, 
# then convert it back to a list and print it.
#
# Task 5: Common Items between two Sets
# friend1_hobbies = {"Gaming", "Football", "Reading", "Music"}
# friend2_hobbies = {"Cooking", "Gaming", "Music", "Traveling"}
# Find and print the hobbies both friends have in common using '&' (intersection).
#
# Task 6: Tuple Unpacking with a Function
# Write a function called 'get_stats(numbers_list)' that:
# - Finds the smallest number (use min(numbers_list))
# - Finds the largest number (use max(numbers_list))
# - Returns both as a tuple: min_val, max_val
# Call the function with [45, 12, 89, 5, 67] and unpack the result into:
# lowest, highest = get_stats(...)
# Print lowest and highest.
# -------------------------------------------------------------

#Task
order_ids = [101, 102, 105, 101, 108, 102, 105, 109]
# i convert list into set
unique_ids = set(order_ids)
print("After removing duplicate : ",unique_ids)

#convert unquie _ids set into list
unique_ids_list = list(unique_ids)
print("after converting unique ids into list : ",unique_ids_list)

#Task 5
# for find the common element from two sets
friend1_hobbies = {"Gaming", "Football", "Reading", "Music"}
friend2_hobbies = {"Cooking", "Gaming", "Music", "Traveling"}
common_hoobies= friend1_hobbies & friend2_hobbies
print("Coomon hobbies of both friend are :", common_hoobies)

#Task 6
def min_max_num(numbers_list):
    min_num = min(numbers_list)
    max_num = max(numbers_list)
    return min_num, max_num

numbers_list = [45, 12, 89, 5, 67]
min,max = min_max_num(numbers_list)
print("Min number : ",min)
print("Max number : ",max)


# Creating a Dictionary with None (Null) values
user = {

    "id":101,
    "name":"John",
    "email":None,
    "is_active":True
}

print("User : ",user)
print("Email :" , user["email"])

# Using the built-in dict() function
# Instead of curly braces {}, you can use the dict() constructor:

person = dict(id=101,name="Sham", email = "sham@gmail.com")
print("Person :",person)

# print all fileds
print("id : ",person["id"])
print("name : ",person["name"])
print("email : ",person["email"])

# Adding a new key-value pair (after creation)
# user["phone"] = "9988776655"
# user["is_active"] = False

# print("\n--- 4. UPDATING VALUES ---")
# user["name"] = "John Doe"
# print("Updated User:", user)

# Creating a Dict from Two Lists (using zip())

key=["id","name","email","is_active"]
value=[101,"John","sham",True]

usr = dict(zip(key,value))
print(usr)

# Creating a Dict from a List of Tuples

pairs = [("brand", "BMW"), ("year", 2026), ("owner", None)]

card = dict(pairs)
print("Convert tuple into dict :",card)




    









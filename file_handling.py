# Step 8: File Handling & Context Managers in Python
# In Java, reading/writing files requires BufferedReader, FileReader, and verbose try-with-resources.
# In Python, the 'with' keyword manages files cleanly and closes them automatically!
#
# Key Modes:
# - 'w' : Write mode (creates a new file or OVERWRITES existing content)
# - 'r' : Read mode (reads existing file; throws FileNotFoundError if missing)
# - 'a' : Append mode (adds new content to the END without deleting existing data)

print("--- 1. WRITING TO A FILE ('w') ---")
# 'with open(...)' is a Context Manager (like Java's try-with-resources).
# It guarantees the file will be CLOSED automatically, even if an error occurs!
with open("sample.txt", "w") as file:
    file.write("Hello from Python File Handling!\n")
    file.write("Line 2: Learning Python is awesome.\n")

print("File 'sample.txt' written successfully.")


print("\n--- 2. READING FROM A FILE ('r') ---")
# Method A: Read the entire file at once with .read()
with open("sample.txt", "r") as file:
    content = file.read()
    print("Full Content:\n", content)

# Method B: Read line by line using a for loop (memory efficient for large files!)
print("Reading line by line:")
with open("sample.txt", "r") as file:
    for line in file:
        print("->", line.strip())  # .strip() removes the trailing newline '\n'


print("\n--- 3. APPENDING TO A FILE ('a') ---")
# 'a' mode adds new lines without erasing what's already there:
with open("sample.txt", "a") as file:
    file.write("Line 3: This line was appended later!\n")

with open("sample.txt", "r") as file:
    print("Updated Content after append:\n", file.read())


print("\n--- 4. HANDLING FILE ERRORS (From Step 7!) ---")
# If a file doesn't exist, Python raises FileNotFoundError.
# We can catch it cleanly using try/except:
try:
    with open("non_existent_file.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Caught Error: The requested file does not exist on disk!")


print("\n--- 5. WORKING WITH JSON FILES ---")
# Earlier in OOP, you learned json.dumps() and json.loads() for strings.
# For direct file read/write, Python provides:
# - json.dump(data, file) -> writes data directly to a JSON file!
# - json.load(file)       -> reads data directly from a JSON file into a Python dict/list!

import json

user_data = {
    "name": "Ayn",
    "role": "Developer",
    "skills": ["Python", "Java", "SQL"],
    "is_active": True
}

# Saving a dictionary to 'user.json':
with open("user.json", "w") as json_file:
    json.dump(user_data, json_file, indent=4)  # indent=4 makes it pretty and readable

print("Saved data to 'user.json'!")

# Reading the JSON file back into a Python dictionary:
with open("user.json", "r") as json_file:
    loaded_user = json.load(json_file)
    print("Loaded from JSON file:", loaded_user)
    print("User Name:", loaded_user["name"])
    print("Skills:", loaded_user["skills"])


# -------------------------------------------------------------
# PRACTICE SECTION FOR YOU:
#
# Task 1: Write a list of 3 goals to a text file
# Create a list: my_goals = ["Learn Core Python", "Build a Project", "Master APIs"]
# Use 'with open("my_goals.txt", "w") as f:' and write each goal on a new line.
# (Hint: use f.write(goal + "\n"))
#
# Task 2: Read and print each goal with a line number
# Open "my_goals.txt" in read mode ('r').
# Loop through the file and print:
# "Goal 1: Learn Core Python", "Goal 2: Build a Project", etc.
#
# Task 3: Save and read a list of products in JSON
# Create a list of dictionaries:
# products = [
#     {"id": 1, "name": "Laptop", "price": 1200},
#     {"id": 2, "name": "Mouse", "price": 25}
# ]
# 1. Save it to 'products.json' using json.dump(products, f, indent=4).
# 2. Read it back using json.load(f) and print each product name and price!
# -------------------------------------------------------------

#Task 1
goals = ["Learn Core Python", "Build a Project", "Master APIs"]

with open("goals.txt" ,"w") as f:
     for goal in goals:
        f.write(goal + "\n")
print("File Writing completed!")

#Task 2

with open("goals.txt", "r") as f:
    count=0
    for line in f:
        count+=1
        print(f"Goal {count}: {line}")

print("File Reading finished !!")

#Task 3

products = [
    {"id": 1, "name": "Laptop", "price": 1200},
    {"id": 2, "name": "Mouse", "price": 25}
]

# TestCase 1 : to write the products in json file
with open("products.json","w") as file:

    json.dump(products,file,indent=4)

print("Products saved to products.json")

# TestCase 2 : To read json file from products.json file

with open("products.json","r") as file:
    read_json = json.load(file)
    print("Read Json from products.json file",read_json)

print("First product name : ", read_json[0]["name"])


# To Read and Write file using specific folder then

#with open("folder_name/my_file.txt", "w")  # Write inside folder
#with open("folder_name/my_file.txt", "r")  # Read from folder






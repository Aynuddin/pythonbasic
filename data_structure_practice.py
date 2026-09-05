# To declare a empty list in python as arr = []
# now add the value and print

print("------------------List-----------------------")
# Declare an empty list using square bracket []
l1 =[]
# add single element in list used append()
l1.append(1)
l1.append(2)
print(l1)

# add mutiple elements in list used l1.extend([e1,e2,...])

l1.extend([3,4])
print(l1)

# Add at specific index ex: l1.insert(index,element)

l1.insert(2,8)
print(l1)

# Remove specific value  l1.remove(element)

l1.remove(3)
print(l1)

# clear() : remove every thing
# pop() : remove from last/index

l1.pop(1)
print(l1)

# Find index of value from list using index(value)

ind=l1.index(4)
print(ind)

# Count Occurence list.count(element) : it will give the count of the element
l1.append(4)
count=l1.count(4)
print(count)

# sort list using sort method sort()
list=[1,2,4,3,5,7,6]
list.sort()
print(list)

# Reverse of list using reverse()
list.reverse()
print(list)

# Copy list : list.copy()

l2=list.copy()
print(l2)

# extra methods of list
length = len(list)

print("Length :",length)
print("Maxmium elem :",max(list))
print("Minimum Element : ",min(list))
print("Sum of list : ",sum(list))
print("to make list sorted : ",sorted(list)) # by default ascending

print("------------------Dictionaris-----------------------")

# Declare a dictionaries or map 
# Both are valid declare for dict
kv1 = dict()
kv= {}

kv["id"] =1
kv["name"] = "Ayn"
kv["age"] = 25

print(kv)

# get(key) : Get value for a key
#nm = kv.get("name")
nm = kv["name"]
print(nm)

# keys() : Get all keys
keys = kv.keys()
for k in keys:
    print("Get all keys : ",k)

# items() : Get key-value pairs
items = kv.items()
for key,value in items:
    print(key,value)

# values() : Get all values
values = kv.values()
for val in values:
    print(val)

# update({key:value}) :  here you can update the particular key value

kv.update({"name":"Ayn Uddin"})
print("After update : ",kv)

# pop(key) : Remove a particular key:
kv.pop("age")
print("After Renove using pop : ",kv)

# popitem() : Removes the last inserted key-value pair:

# clear() : this will clear dict (kv)

# fromkeys() : Create dictionary from keys
keys = [1,2,3,4,2,3,2]
kvs = dict.fromkeys(keys,0)
print(kvs)

# find the frequency of each element
freq = {}
for key in keys:
    if(key in freq):
        freq[key] = freq.get(key) +1
    else:
        freq[key] = 1
print("Frequency of element : ",freq)

# remove duplicate from keys
remove_duplicate = freq.keys()
print("Remove duplicate : ",remove_duplicate)

# another way to collect
unique_list = []
for k,v in freq.items():
    unique_list.append(k)
print("Remove duplicate : ",unique_list)

find_Dup = []
for k,v in freq.items():
    if(v > 1):
        find_Dup.append(k)
print("Find Duplicate : ",find_Dup)

# find the majority of element of an array
maxCount = 0
for k,v in freq.items():
    if(v > maxCount):
        maxCount=v
        majority=k
print(f"Majority of element: {majority} & Maxium Count of element: {maxCount}")


print("\n------------------Strings-----------------------")
# 1. Indexing: Access individual characters by position
# Positive indexing starts at 0 from the left; negative indexing starts at -1 from the right.
text = "Python Programming"
print("Original string:", text)
print("First character (index 0):", text[0])
print("Character at index 7:", text[7])
print("Last character (index -1):", text[-1])
print("Second to last character (index -2):", text[-2])

# 2. Slicing: [start : stop : step] (stop index is exclusive)
print("Slice [0:6] (first 6 chars):", text[0:6])         # "Python"
print("Slice [:6] (from start to index 6):", text[:6])   # "Python"
print("Slice [7:] (from index 7 to end):", text[7:])     # "Programming"
print("Slice [-11:] (last 11 chars):", text[-11:])       # "Programming"
print("Slice with step 2 [0:6:2]:", text[0:6:2])         # "Pto"
print("Reverse a string with [::-1]:", text[::-1])       # "gnimmargorP nohtyP"

# 3. Common String Methods
msg = "  Hello, Python World!  "
print("Original msg:", repr(msg))
print("upper():", msg.upper())                          # convert to UPPERCASE
print("lower():", msg.lower())                          # convert to lowercase
print("strip():", repr(msg.strip()))                    # removes spaces from both sides
print("lstrip():", repr(msg.lstrip()))                  # removes spaces from left side
print("rstrip():", repr(msg.rstrip()))                  # removes spaces from right side
print("replace('World', 'Universe'):", msg.replace("World", "Universe"))
print("count('o'):", msg.count("o"))                    # count occurrences of character/word
print("find('Python'):", msg.find("Python"))            # returns starting index (or -1 if not found)
print("startswith('  Hello'):", msg.startswith("  Hello")) # True or False
print("endswith('World!  '):", msg.endswith("World!  "))   # True or False
print("title():", "python data science".title())        # Capitalizes Every Word

# 4. String Manipulation: split() and join()
# split(delimiter) splits a string into a list of strings
csv_data = "apple,banana,cherry,dates"
fruits_list = csv_data.split(",")
print("split(',') ->", fruits_list)

# join(iterable) joins a list of strings into one string using the given separator
joined_text = " - ".join(fruits_list)
print("' - '.join(...) ->", joined_text)

# 5. String Manipulation Exercises:
# Palindrome Check:
word = "radar"
is_palindrome = (word == word[::-1])
print(f"Is '{word}' a palindrome?:", is_palindrome)

# Counting Vowels in a string:
sample = "Python Programming"
vowels = "aeiou"
vowel_count = sum(1 for ch in sample.lower() if ch in vowels)
print(f"Number of vowels in '{sample}':", vowel_count)


print("\n------------------Sets-----------------------")
# Sets are UNORDERED collections of UNIQUE elements (no duplicates allowed).
# Note: {} creates an empty dictionary. To create an empty set, use set().
s1 = {1, 2, 3, 4, 5}
empty_s = set()
print("Set s1:", s1)
print("Type of set():", type(empty_s))

# Automatic duplicate removal from list:
numbers_with_dups = [1, 2, 2, 3, 4, 4, 4, 5]
unique_set = set(numbers_with_dups)
print("Duplicates removed using set():", unique_set)

# 1. add() - adds a single element to the set
s1.add(10)
s1.add(3)  # Already present, set will ignore it
print("After s1.add(10):", s1)

# 2. remove() vs discard()
# remove(x) removes x, but raises KeyError if x is NOT in the set!
s1.remove(10)
print("After s1.remove(10):", s1)
# s1.remove(99)  # <-- Would crash with KeyError: 99

# discard(x) removes x safely; if x is NOT found, it does NOTHING (no error!)
s1.discard(99)  # Safe, no error raised!
print("After s1.discard(99) (safe removal):", s1)

# 3. Set Operations: union, intersection, difference
set_A = {1, 2, 3, 4, 5}
set_B = {4, 5, 6, 7, 8}
print("Set A:", set_A)
print("Set B:", set_B)

# union() or | operator : combines all unique elements from both sets
union_res = set_A.union(set_B)          # or: set_A | set_B
print("Union (A | B):", union_res)

# intersection() or & operator : common elements present in BOTH sets
intersection_res = set_A.intersection(set_B)  # or: set_A & set_B
print("Intersection (A & B):", intersection_res)

# difference() or - operator : elements in A that are NOT in B
diff_A_B = set_A.difference(set_B)      # or: set_A - set_B
print("Difference (A - B):", diff_A_B)
diff_B_A = set_B.difference(set_A)      # or: set_B - set_A
print("Difference (B - A):", diff_B_A)

# symmetric_difference() or ^ operator : elements in either A or B, but NOT both
sym_diff = set_A.symmetric_difference(set_B)  # or: set_A ^ set_B
print("Symmetric Difference (A ^ B):", sym_diff)


print("\n------------------Lambda Functions-----------------------")
# Lambda is an anonymous (unnamed), one-line function.
# Syntax: lambda arguments : single_expression

# 1. Basic lambdas:
square = lambda x: x ** 2
print("Lambda square(6):", square(6))

add_two = lambda a, b: a + b
print("Lambda add_two(15, 25):", add_two(15, 25))

is_even = lambda n: n % 2 == 0
print("Lambda is_even(10):", is_even(10))
print("Lambda is_even(7):", is_even(7))

# 2. Key practical use-case: Custom sorting with sorted(..., key=lambda)
students = [
    {"name": "Ayn", "score": 88},
    {"name": "Zack", "score": 95},
    {"name": "Sara", "score": 76},
    {"name": "Rahul", "score": 91}
]

# Sort by score ascending:
sorted_by_score = sorted(students, key=lambda s: s["score"])
print("Sorted by score (ascending):", sorted_by_score)

# Sort by score descending (highest first):
sorted_by_score_desc = sorted(students, key=lambda s: s["score"], reverse=True)
print("Sorted by score (descending):", sorted_by_score_desc)

# Sort by student name alphabetically:
sorted_by_name = sorted(students, key=lambda s: s["name"])
print("Sorted by name alphabetically:", sorted_by_name)


print("\n------------------map()-----------------------")
# map(function, iterable)
# Transforms/modifies every item in an iterable using the provided function.
# Returns an iterator, so wrap it in list() to see results.

numbers = [1, 2, 3, 4, 5]

# 1. Transform numbers: square each item
squared_list = list(map(lambda x: x ** 2, numbers))
print("Original numbers:", numbers)
print("Squared using map():", squared_list)

# 2. Convert types: list of numeric strings to integers
str_nums = ["10", "20", "30", "40", "50"]
int_nums = list(map(int, str_nums))
print("Converted strings to ints using map():", int_nums)

# 3. Clean up strings: trim and title-case names
raw_names = ["  ayn uddin ", " JOHN doe", "sara connor  "]
cleaned_names = list(map(lambda name: name.strip().title(), raw_names))
print("Cleaned names using map():", cleaned_names)


print("\n------------------filter()-----------------------")
# filter(function, iterable)
# Keeps only items where the function evaluates to True.
# Returns an iterator, so wrap it in list() to see results.

raw_values = [12, -7, 5, 0, -3, 18, 25, -1, 30]

# 1. Filter only positive numbers (> 0)
positive_nums = list(filter(lambda x: x > 0, raw_values))
print("Original values:", raw_values)
print("Positive numbers using filter():", positive_nums)

# 2. Filter even numbers
all_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_nums = list(filter(lambda x: x % 2 == 0, all_nums))
print("Even numbers using filter():", even_nums)

# 3. Filter words by length
words = ["python", "ai", "developer", "go", "code", "backend"]
long_words = list(filter(lambda w: len(w) > 3, words))
print("Words with length > 3 using filter():", long_words)

# 4. Combining filter() and map() together!
# Task: Take only even numbers from 1 to 10, then double them
evens_doubled = list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, all_nums)))
print("Filtered evens and mapped (doubled):", evens_doubled)

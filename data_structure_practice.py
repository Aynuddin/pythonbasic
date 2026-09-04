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






# Comprehensions: It is a concise way to create a new collection by iterating an existing collection
# for minimal code. It is expression loop and optional condition

# [expression for variable in iterable if condition] -- list
# {expression for variable in iterable if condition} -- set
# {key:expression for variable in iterable if condition} -- dictionary
# () -- tuple

# List comprehension
numbers = [1,2,3,4,5,6,7,8,9,10]

# extract only even
even_num = [x for x in numbers if x % 2==0]
print("Even number :",even_num)

users = [
    {"id": 101, "name": "John", "active": True},
    {"id": 102, "name": "Ayn", "active": False},
    {"id": 103, "name": "Mike", "active": True},
    {"id": 104, "name": "David", "active": True},
    {"id": 105, "name": "John", "active": False},
    {"id": 106, "name": "Mike", "active": False},
    {"id": 107, "name": "David", "active": True}
]

# print user name
usrs_name = [user["name"] for user in users]
print("Users name lsit : ",usrs_name)

# print id whose active is true
ids_active = [user["id"] for user in users if user["active"] == True]
print("Users ID : ",ids_active)

# print id and name whose users active is false
user_inactive = [[user.get("id") , user.get("name")] for user in users if user.get("active") == False]
create_dict = dict(user_inactive)
print("Dict obj :",create_dict)
for user in user_inactive:
    print("Inactive users : ",user)

# Dictionary comprehension

user_ids_map = {user["id"] : user["name"] for user in users}

print("User ids map : ",user_ids_map)

# Set comprehension
user_name_set = {user["name"] for user in users}
print("User unqiue name in list : ",user_name_set)

# create a dictionaris for id with active
id_with_active_map = {user["id"] : user.get("active") for user in users}
print("User ID with active : ",id_with_active_map)

# from keys only dict

numbers = [1,2,3,2,3,4]
sk={}   
for i in numbers:
    if i in sk:
        sk[i]+=1
    else:
        sk[i]=1
print("Dict using for loop : ",sk)


# ------ lambda function--------
# Lambda is an anynomous function
# expression : lambda arguments : one-line expression

sum = lambda x,y : x+y
print("Sum of two numbers : ", sum(10,20))

mul = lambda x,y : x*y
print("Multiplication of two numbers :", mul(10,20))

emp1 = {
    "id":101,
    "name":"Ayn",
    "salary":65000
}

emp2 = {
    "id":102,
    "name":"John",
    "salary":60000
}

emp3 = {
    "id":103,
    "name":"Mukesh",
    "salary":70000
}

emp_list = []
emp_list.append(emp1)
emp_list.append(emp2)
emp_list.append(emp3)
print("List of emp : ", emp_list)

# using lambda expression sort the employee by using salary
# natural sorting ascending order of salary
sort_emp = sorted(emp_list, key = lambda emp : emp.get("salary"))
print("After sorting emp according to salary (ascending) : ",sort_emp)

# reverse sorting descending order of salary
sort_emp = sorted(emp_list, key = lambda emp : emp.get("salary"),reverse=True)
print("After sorting emp according to salary (descending) : ",sort_emp)

# only print name from list
# map syntax : map(lambda arguments : expression ,obj)
# obj ex: list,tuple,set
# here emp_list is obj & lambda is function

emp_name = map(lambda emp : emp.get("name"),emp_list)
print("List of names from emp : ",list(emp_name))

# filter 
# syntax = filter(lambda arguments : expression , obj)
# obj ex: list,tuple,set

filter_name = filter(lambda emp : emp.get("name").startswith("A"), emp_list)
em = list(filter_name)
for e in em:
    print(e.get("name"))
print("After filtering the list : ", em)

# lambda with if-else expression
# syntax : lambda argument : expression1 if condition else expression2
# <value_if_true> if <condition> else <value_if_false>
# ex : 20,30 , 20 if a > b else b
large = lambda a,b : a if a>b else b
print("Large of two number : ", large(20,30))




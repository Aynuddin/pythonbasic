# Step 6: Object-Oriented Programming (OOP) in Python
# Since you have a Java background, this will feel very natural!
# 
# Key Java vs Python OOP concepts:
# - Java 'class'                   --> Python 'class'
# - Java Constructor 'Car()'       --> Python '__init__(self, ...)'
# - Java 'this' keyword            --> Python 'self'
# - Java 'toString()'              --> Python '__str__(self)'
# - Java 'extends' (Inheritance)   --> Python 'class ElectricCar(Car):'

print("--- 1. BASIC CLASS & OBJECT ---")
# In Python, we define a class using 'class ClassName:'
class Person:
    # The __init__ method is the CONSTRUCTOR (runs automatically when object is created)
    # 'self' is like Java's 'this' - it refers to the current instance!
    def __init__(self, name, role):
        self.name = name      # Instance variable
        self.role = role

    # An instance method (must always take 'self' as the first parameter)
    def introduce(self):
        print(f"Hi, I am {self.name} and I work as a {self.role}.")

# Creating objects (No 'new' keyword needed in Python!)
person1 = Person("Ayn", "Developer")
person2 = Person("John", "QA Engineer")

person1.introduce()
person2.introduce()


print("\n--- 2. CONSTRUCTOR WITH DEFAULT VALUES ---")
class BankAccount:
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New Balance: {self.balance}")
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. Remaining Balance: {self.balance}")
        else:
            print("Insufficient funds!")

# Testing the BankAccount class
my_account = BankAccount("Ayn", 1000)
my_account.deposit(500)
my_account.withdraw(300)
my_account.withdraw(2000)  # Should trigger insufficient funds


print("\n--- 3. THE __str__ METHOD (Java's toString) ---")
# By default, printing an object prints something like <__main__.Car object at 0x...>.
# Defining __str__ gives a readable string when print(object) is called!
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.year} {self.brand} {self.model}"

car1 = Car("BMW", "M3", 2024)
print("Car object printed:", car1)  # Automatically calls car1.__str__()!


print("\n--- 4. INHERITANCE (Java's 'extends') ---")
# In Python, pass the parent class inside parentheses: class Child(Parent):
class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_capacity):
        # super().__init__() calls the parent class constructor (like super() in Java)
        super().__init__(brand, model, year)
        self.battery_capacity = battery_capacity

    def charge(self):
        print(f"{self.brand} {self.model} is charging with a {self.battery_capacity} kWh battery.")

ev = ElectricCar("Tesla", "Model 3", 2025, 75)
print(ev)       # Inherited __str__ from Car!
ev.charge()     # Child-specific method


# -------------------------------------------------------------
# PRACTICE SECTION FOR YOU:
#
# Task 1: Create a class called 'Book' with:
#         - Attributes in __init__: title, author, price
#         - A method 'apply_discount(percent)' that reduces the price by that percent
#         - A '__str__' method that returns: "<title> by <author> - $<price>"
#         - Create a book object, print it, apply a 10% discount, and print again.
#
# Task 2: Create a class 'Student' with:
#         - Attributes: name, marks (which should be a list of numbers, e.g. [80, 90, 85])
#         - A method 'calculate_average()' that returns the average mark of the student.
#         - Create a student object and print their average!
# -------------------------------------------------------------

#Task 1

class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price

    def apply_discount(self,percent):
        discounted_price = self.price - (self.price*percent/100)
        return discounted_price

    def __str__(self):
        #return f"{self.title} by {self.author} - ${self.price}"
        return f"""
            Title: {self.title}
            Author: {self.author}
            Price: ${self.price}
        """

book1 = Book("Python", "John", 1000)
print("Book :",book1)
print("Discounted Price :",book1.apply_discount(10))

#Task 2

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def calculate_average(self):
        total_marks=0
        for num in self.marks:
            total_marks+=num
            avg=total_marks / len(self.marks)
        return avg

student1 = Student("ayn",[1,2,3,4,5])
print("Student average marks :", student1.calculate_average())

# I will try to convert python object to json object

# for that i will import first json and use two methods
# 1) dumps() -> it will convert python obj to json obj
# 2) loads() -> it will convert json obj to python obj
# Note -> it will convert only those objects whose data types are acceptable in json
# exmaple like, __dict__ or list,dictionaries,string,int,float,bool

import json

# here book object convert to json object inside dumps() method pass any dict type
book2 = Book("Java","Ayn",20)
book_json = json.dumps(book2.__dict__)
print("Book Json obj :",book_json)

# Agin convert json object to python object using loads method
book_dict = json.loads(book_json)
print("Book dict :",book_dict)
    

    

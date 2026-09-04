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


print("\n--- 5. ENCAPSULATION (Private Attributes & Getters/Setters) ---")
# In Java:
#   private double balance;
#   public double getBalance() { return balance; }
#   public void setBalance(double b) { this.balance = b; }
#
# In Python:
# - Default: self.name            --> PUBLIC (accessible anywhere)
# - Single underscore: self._age   --> PROTECTED (convention: internal use only)
# - Double underscore: self.__pin  --> PRIVATE (name mangling: cannot be accessed directly outside class!)
#
# Pythonic Getters & Setters: We use the '@property' decorator!
# This lets callers use standard dot syntax (account.balance = 500) while running validation under the hood!

class SecureBankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute (note double underscore '__')

    # GETTER using @property
    # Now you can call: print(account.balance) WITHOUT parentheses!
    @property
    def balance(self):
        return self.__balance

    # SETTER using @<attribute>.setter
    # Runs when you do: account.balance = 1000
    @balance.setter
    def balance(self, new_balance):
        if new_balance >= 0:
            self.__balance = new_balance
            print(f"Balance successfully updated to: ${self.__balance}")
        else:
            print("Error: Balance cannot be negative!")

secure_acc = SecureBankAccount("Ayn", 1000)
print("Accessing balance via getter:", secure_acc.balance)

# Updating via setter:
secure_acc.balance = 1500  # Calls @balance.setter
secure_acc.balance = -200  # Triggers error message

# Trying to access the private attribute directly will FAIL:
try:
    print(secure_acc.__balance)
except AttributeError as e:
    print("Direct private access blocked:", e)


print("\n--- 6. POLYMORPHISM (Many Forms / Method Overriding) ---")
# In Java: Subclasses override parent methods and can be stored in Parent reference types.
# In Python: Different classes can implement methods with the same name.
# Python also uses "Duck Typing": 'If it walks like a duck and quacks like a duck, it's a duck!'

class Dog:
    def speak(self):
        return "Woof! Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Cow:
    def speak(self):
        return "Moo!"

# A single function that works polymorphically with ANY object that has a .speak() method:
def animal_sound(animal):
    print(f"Animal says: {animal.speak()}")

animals = [Dog(), Cat(), Cow()]
for a in animals:
    animal_sound(a)


print("\n--- 7. ABSTRACTION (Abstract Base Classes & Interfaces) ---")
# In Java:
#   abstract class PaymentGateway { abstract void pay(double amount); }
#   interface PaymentGateway { void pay(double amount); }
#
# In Python:
#   We import 'ABC' (Abstract Base Class) and '@abstractmethod' from the standard 'abc' module!
#   Any child class MUST implement all @abstractmethod methods, otherwise Python will throw an error!

from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount):
        """Every payment method must implement this!"""
        pass

    @abstractmethod
    def refund(self, amount):
        """Every payment method must implement this!"""
        pass

class CreditCardPayment(PaymentGateway):
    def process_payment(self, amount):
        print(f"Paid ${amount} using Credit Card.")

    def refund(self, amount):
        print(f"Refunded ${amount} back to Credit Card.")

class UpiPayment(PaymentGateway):
    def process_payment(self, amount):
        print(f"Paid ${amount} instantly using UPI.")

    def refund(self, amount):
        print(f"Refunded ${amount} instantly to UPI ID.")

# Testing Abstraction & Polymorphism together:
payments = [CreditCardPayment(), UpiPayment()]
for p in payments:
    p.process_payment(250)
    p.refund(50)


# -------------------------------------------------------------
# PRACTICE SECTION: ENCAPSULATION & POLYMORPHISM / ABSTRACTION
#
# Task 3 (Encapsulation):
# Create a class 'Employee' with:
# - An attribute 'name' (public)
# - A private attribute '__salary' (initialized in __init__)
# - A getter '@property def salary(self)' that returns __salary
# - A setter '@salary.setter def salary(self, value)':
#     - If value > 0, update __salary
#     - Else print "Salary must be positive!"
# - Test creating an employee, accessing salary, updating with a positive value,
#   and trying to update with a negative value.
#
# Task 4 (Abstraction & Polymorphism):
# - Create an abstract class 'Shape(ABC)' with an '@abstractmethod def area(self)'
# - Create a subclass 'Circle(Shape)' with attribute 'radius'
#   (Area formula: 3.14159 * radius * radius)
# - Create a subclass 'Rectangle(Shape)' with attributes 'width' and 'height'
#   (Area formula: width * height)
# - Put both in a list and loop through them to print their areas!
# -------------------------------------------------------------

#Task 3

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.__salary=salary

    #Getter
    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, new_sal):
        try:
            if new_sal < 0:
                raise ValueError("Salary must be positive")

            self.__salary = new_sal
            print(f"Salary successfully updated to: ${self.__salary}")
        except ValueError as e:
            print("Error:", e)


emp = Employee("Ayn",2000)
# Getting the salary
print("Accessing Salary of employee via getter is : ", emp.salary)

# updating positive (+) salary 
emp.salary=25000
#emp.salary=-200
try:
   print("Salary after increasing : ",emp.salary) 
except AttributeError as e:
    print(e)


# Task 4

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius

class Reactangle(Shape):
    def __init__(self,height,width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

shapes = [Circle(5),Reactangle(5,10)]

for shape in shapes:
    print(f"Area : ", shape.area())

        




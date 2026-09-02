# Control Flow: Making Decisions and Repeating Actions

print("--- 1. IF, ELIF, and ELSE ---")
# 'if' statements let the computer make decisions based on conditions.
age = 20

# Python uses "Indentation" (spaces at the start of the line) to know what code belongs inside the 'if' block!
# This is very important in Python!
if age >= 18:
    print("You are an adult!")
elif age >= 13: # elif stands for "else if"
    print("You are a teenager.")
else:
    print("You are a child.")


print("\n--- 2. FOR LOOPS ---")
# 'for' loops are used to repeat an action a specific number of times.
# range(5) gives us numbers from 0 to 4 (it stops before 5).
for i in range(5):
    print("Counting in a for loop:", i)


print("\n--- 3. WHILE LOOPS ---")
# 'while' loops repeat an action AS LONG AS a condition remains True.
countdown = 3
while countdown > 0:
    print("Liftoff in...", countdown)
    countdown = countdown - 1  # We must decrease it, or the loop will run forever!

print("Blastoff!")

# if,elif and else i wrote

age=15

if age>=18:
    print("you are eligible for voting!")
elif age <= 18 and age >= 13:
    print("you are teenager!")
else:
    print("you are child!")

# example of for loop in numbers 10
for i in range(10):
    print(i)
     
# while loop example 
count=10
while(count > 1):
    print(count)
    count=count-1

print("Practice all the three loops")
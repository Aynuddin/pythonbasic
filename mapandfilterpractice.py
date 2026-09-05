numbers = [1,2,3,4,5,6]

# use map and lamda function to add 2 times of each el

result = map(lambda x: x*2,numbers)
print("Result of 2 times element map : ",list(result))

# only even number
result1 = filter(lambda x : x % 2 == 0 , numbers)
print("Result of even number filter : ",list(result1))
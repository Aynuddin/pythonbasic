text = "python programming"

# see the length of the string
#print("Length of the string : ", len(text))

# find the substring or extract string
#print("Starting index at 0 t0 3", text[0:3])
# starting from index 3
#print("Starting from index 3 :" , text[3:])
# ending with index 5
#print("Ending with index 5 :" , text[:5])
# last 4 character
#print("Last 4 character of a string : ", text[-4:])
# second last character
#print("Second to last character (index -2):", text[-2])

# last character
#print("Last character : ", text[-1])

# Concate two string
text1 ="python"
text2 = " programming"
#print("Concate two string : ", text1 + text2)

# Common String methods
msg = "  Hello, Python world!  "
msg1="python data science"
#print("Original msg:", repr(msg))

# upper case
#print("Convert uppercase : ", msg.upper())

# lower case
#print("Convert lowercase : ", msg.lower())

# strip() : remove spaces from both sides
#print("Remove spaces from both sides : ", msg.strip())

# lstrip() : removes spaces from left side
#print("Remove spaces from left side : ", msg.lstrip())

# rstrip() : removes spaces from right side
#print("Remove spaces from right side : ", msg.rstrip())

# replace() : replaces a substring with another substring
#print("Replace 'World' with 'Universe' : ", msg.replace("world", "Universe"))

# count() : counts the number of occurrences of a substring
#print("Count 'o' : ", msg.count("o"))

# find() : finds the index of a substring
#print("Find 'data' : ", msg1.find("data"))

# startswith() : checks if a string starts with a substring
#print("Starts with '  Hello' : ", msg.startswith("  Hello"))

# endswith() : checks if a string ends with a substring
#print("Ends with 'World!  ' : ", msg.endswith("World!  "))

# title() : converts the first character of each word to uppercase
#print("Convert to title case : ", msg.title())

# syntax :: means starting point : ending point : step 

#print("move forward with one step : ", text[::2]) # pto rgamn

#print("move backward with one step : ", text[::-1]) # gnimmargorp nohtyp

# String split() and join() method

data="Python Java Javascript Typescript"
rev_text=[]
data_split = data.split(" ")
print("After splitting string : ",data_split)
# here reverse the word character by character without changing position
for d1 in data_split:
    for d2 in range(len(d1) - 1,-1,-1):
        rev_text.append(d1[d2])
    rev_text.append(" ")
print("After reversing the string : ", "".join(rev_text).strip()) # nohtyP avaJ tpircsavaJ tpircsepyT

# reverse of word of a string 
data_split = data.split(" ")
rev_text1=[]
for d in range(len(data_split) -1, -1,-1):
    rev_text1.append(data_split[d])
    rev_text1.append(" ")
print("After reversing the word of a string : ", "".join(rev_text1).strip()) # Typescript Javascript Java Python

# reverse of word and also reverse the character of each word
data_split = data.split(" ")
rev_text1=[]
for d in range(len(data_split) -1, -1,-1):
    rev_text1.append(data_split[d][::-1])
    rev_text1.append(" ")
print("After reversing the word and also reverse the character of each word : ", "".join(rev_text1).strip()) # tpircsepyT tpircsavaJ avaJ nohtyP

str="pythonprogramming"
# frequency of character
freq={}
for ch in str:
    if ch in freq:
        freq[ch]=freq[ch]+1
    else:
        freq[ch] =1
print("Frequency of character : ",freq)
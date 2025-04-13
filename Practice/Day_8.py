"""  Find all occurrences of a substring in a given string by ignoring the case
Write a program to find all occurrences of “USA” in a given string ignoring the case.

Given:
 
str1 = "Welcome to USA. usa awesome, isn't it?"
Expected Outcome: The USA count is: 2

solution 1-

str = "Welcome to USA. usa awesome, isn't usa USA UsA it?"
w="USA"
c=0

#for x in range(len(str)):
    if w==str[x:x+3].upper():
        c+=1

solution 2-

new_str=str.upper()
c=new_str.count(w)

print(c)

"""
""" Calculate the sum and average of the digits present in a string
Given a string s1, write a program to return the sum and average of the digits that appear in the string, ignoring all other characters.

Given:str1 = "PYnative29@#8496"

Expected Outcome:
Sum is: 38 Average is  6.333333333333333

solution 1-

str1 = "PYnative29@#8496"
c=0
sum=0
for x in range(len(str1)):
    if str1[x].isdigit():
        c+=1
        sum=sum+int(str1[x])
print("Sum : ",sum," Avg : ",sum/c)


solution 2-

input_str = "PYnative29@#8496"
total = 0
cnt = 0
for char in input_str:
    if char.isdigit():
        total += int(char)
        cnt += 1

# average = sum / count of digits
avg = total / cnt
print("Sum is:", total, "Average is ", avg)


solution 3-

import re

input_str = "PYnative29@#8496"
digit_list = [int(num) for num in re.findall(r'\d', input_str)]
print('Digits:', digit_list)

# use the built-in function sum
total = sum(digit_list)

# average = sum / count of digits
avg = total / len(digit_list)
print("Sum is:", total, "Average is ", avg)


"""


""" Write a program to count occurrences of all characters within a string
Given:

str1 = "Apple"
Expected Outcome:

{'A': 1, 'p': 2, 'l': 1, 'e': 1}

str1 = "Apple"

char_dict=dict()
for x in str1:
    c=str1.count(x)
    char_dict[x]=c

print(char_dict)

"""

""" Reverse a given string

str1 = "PYnative"
print(str1[::-1])
"""

""" Find the last position of a given substring
Write a program to find the last position of a substring “Emma” in a given string.

Given:

str1 = "Emma is a data scientist who knows Python. Emma works at google."
Expected Output:

Last occurrence of Emma starts at index 43

import re
str = "Emma is a data scientist who knows Python. Emma works at google."
print(str.rfind("Emma"))

str1 = "Emma is a data scientist who knows Python. Emma works at google."
print("Original String is:", str1)

index = str1.rfind("Emma")
print("Last occurrence of Emma starts at index:", index)
"""

 


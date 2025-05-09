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

"""******************
 Find the last position of a given substring
Write a program to find the last position of a substring “Emma” in a given string.

Given:

str1 = "Emma is a data scientist who knows Python. Emma works at google."
Expected Output:

Last occurrence of Emma starts at index 43


"""

""" Split a string on hyphens
Write a program to split a given string on hyphens and display each substring.

Given:

str1 = Emma-is-a-data-scientist
Expected Output:

Displaying each substring:

Emma
is
a
data
scientist

str ="Emma-is-a-data-scientist"
ns=str.split("-")
#print(ns)
print("\n".join(ns))

 """

"""
Remove empty strings from a list of strings
Given:

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
Expected Output:

Original list of sting
['Emma', 'Jon', '', 'Kelly', None, 'Eric', '']

After removing empty strings
['Emma', 'Jon', 'Kelly', 'Eric']

Show Hint :
Use the built-in function filter() to remove empty strings from a list
Or use the for loop and if condition to remove the empty strings from a list


Solution 1: Using the loop and if condition

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
res_list = []
for s in str_list:
    # check for non empty string
    if s:
        res_list.append(s)
print(res_list)
 
Solution 2: Using the built-in function filter()

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

# use built-in function filter to filter empty value
new_str_list = list(filter(None, str_list))

print("After removing empty strings")
print(new_str_list)
"""

import re
str = "/*Jon is @developer & musician"
ns=re.findall('[^/*@& ]+',str)
print(' '.join(ns))

import re

str1 = "/*Jon is @developer & musician"
print("Original string is : ", str1)

# replace special symbols with ''
res = re.sub(r'[^\w\s]', '', str1)
print("New string is : ", res)

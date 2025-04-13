""" Count all letters, digits, and special symbols from a given string
Given:

str1 = "P@#yn26at^&i5ve"
Expected Outcome:

Total counts of chars, digits, and symbols 

Chars = 8 
Digits = 3 
Symbol = 4


str1 = "P@#yn26at^&i5ve"
c=0
d=0
s=0
for x in range(len(str1)):
    if str1[x].isalpha():
        c+=1
    elif str1[x].isdigit():
        d+=1
    else:
        s+=1

print(str1,"\nChars = ",c,"\nDigits = ",d,"\nSymbol = ",s)

"""

"""
Create a mixed String using the following rules
Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result.

Given:

s1 = "Abc"
s2 = "Xyz"
Expected Output: AzbycX


s1 = "Abc"
s2 = "Xyz"

# get string length
s1_length = len(s1)
s2_length = len(s2)

# get length of a bigger string
length = s1_length if s1_length > s2_length else s2_length
result = ""

# reverse s2
s2 = s2[::-1]

# iterate string 
# s1 ascending and s2 descending
for i in range(length):
    if i < s1_length:
        result = result + s1[i]
    if i < s2_length:
        result = result + s2[i]

print(result)

"""

"""
String characters balance Test
Write a program to check if two strings are balanced. For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2. The character’s position doesn’t matter.

Given:

Case 1:
s1 = "Yn"
s2 = "PYnative"
Expected Output:True


Case 2:
s1 = "Ynf"
s2 = "PYnative"
Expected Output: False


s1 = "Ynf"
s2 = "PYnative"
f=''
for x in range(len(s1)):
    f='False'
    for y in range(len(s2)):
        if s1[x]==s2[y]:
            f='True'


if f=='True':
    print("True")
else:
    print("False")

"""    


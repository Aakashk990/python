"""Create a string made of the first, middle and last character
Write a program to create a new string made of an input string’s first, middle, and last character.

Given:
str1 = "James"

Expected Output: Jms
"""

str = "James"
print(str[0]+str[int(len(str)/2)]+str[-1])


""" Create a new string made of the first, middle, and last characters of each input string
Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last characters.

Given:
s1 = "America"
s2 = "Japan"

Expected Output: AJrpan
"""

s1 = "America"
s2 = "Japan"
m1=int(len(s1)/2)
m2=int(len(s2)/2)
print(s1[0]+s2[0]+s1[m1]+s2[m2]+s1[-1]+s2[-1])



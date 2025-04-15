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
"""

str ="Emma-is-a-data-scientist"
ns=str.split("-")
#print(ns)
print("\n".join(ns))

 
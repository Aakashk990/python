""" Print the following pattern
Write a program to print the following start pattern using the for loop

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*

n=10
for x in range(n):
    for y in range(n):
        if x>=y:
            print("*",end=" ")
    print("\t\t")
for x in range(n-1):
    for y in range(n-1): 
        if x<=y:
            print("*",end=" ")
    print("\t\t")

"""

""" Print following pattern
              * 
            * * 
          * * * 
        * * * * 
      * * * * * 
    * * * * * * 
  * * * * * * * 
* * * * * * * * 
  * * * * * * * 
    * * * * * * 
      * * * * * 
        * * * * 
          * * * 
            * * 
              * 

n=8
for x in range(1,n+1):
    print('  '*(n-x)+'* '*x)
for x in range(1,n):
    print('  '*x+'* '*(n-x))

"""


""" Print following pattern

    * 
   * * 
  * * * 
 * * * * 
* * * * * 
 * * * * 
  * * * 
   * * 
    * 

n=5
for x in range(1,n+1):
    print(' '*(n-x)+'* '*x)
for x in range(1,n):
    print(' '*x+'* '*(n-x))

"""


"""Create a string made of the first, middle and last character
Write a program to create a new string made of an input string’s first, middle, and last character.

Given:
str1 = "James"

Expected Output: Jms

str = "James"
print(str[0]+str[int(len(str)/2)]+str[-1])

"""

""" Create a string made of the middle three characters
Write a program to create a new string made of the middle three characters of an input string.

Given:
str1 = "JhonDipPeta"

Output :Dip


str1 = "JhonDipPeta"
str2 = "JaSonAy"
print(str1[int(len(str1)/2)-1]+str1[int(len(str1)/2)]+str1[int(len(str1)/2)+1])

"""


""" Append new string in the middle of a given string
Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.

Given:
s1 = "Ault"
s2 = "Kelly"

Expected Output: AuKellylt

s1 = "Ault"
s2 = "Kelly"
s3a=s1[:int(len(s1)/2)]+s2
s3=s3a+s1[int(len(s1)/2):]
print(s3)

"""

""" Create a new string made of the first, middle, and last characters of each input string
Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last characters.

Given:
s1 = "America"
s2 = "Japan"

Expected Output: AJrpan

s1 = "America"
s2 = "Japan"
m1=int(len(s1)/2)
m2=int(len(s2)/2)
print(s1[0]+s2[0]+s1[m1]+s2[m2]+s1[-1]+s2[-1])

"""

""" Arrange string characters such that lowercase letters should come first
Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.

Given:
str1 = PyNaTive

Expected Output: yaivePNT

str1 = "PYnAtivE"
print('Original String:', str1)
lower = []
upper = []
for char in str1:
    if char.islower():
        # add lowercase characters to lower list
        lower.append(char)
    else:
        # add uppercase characters to lower list
        upper.append(char)

# Join both list
sorted_str = ''.join(lower + upper)
print('Result:', sorted_str)

"""
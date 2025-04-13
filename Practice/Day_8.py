"""  Find all occurrences of a substring in a given string by ignoring the case
Write a program to find all occurrences of “USA” in a given string ignoring the case.

Given:

str1 = "Welcome to USA. usa awesome, isn't it?"
Expected Outcome:

The USA count is: 2

str = "Welcome to USA. usa awesome, isn't usa USA UsA it?"
w="USA"
c=0

#for x in range(len(str)):
    #print(str[x:x+3])
   # if w==str[x:x+3].upper():
   #     c+=1

new_str=str.upper()
c=new_str.count(w)

print(c)

"""

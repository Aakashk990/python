""" Calculate the sum and average of the digits present in a string
Given a string s1, write a program to return the sum and average of the digits that appear in the string, ignoring all other characters.

Given:str1 = "PYnative29@#8496"

Expected Outcome:
Sum is: 38 Average is  6.333333333333333
"""

#solution 1-

str1 = "PYnative29@#8496"
c=0
sum=0
for x in range(len(str1)):
    if str1[x].isdigit():
        c+=1
        sum=sum+int(str1[x])
print("Sum : ",sum," Avg : ",sum/c)


#solution 2-

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


#solution 3-

import re

input_str = "PYnative29@#8496"
digit_list = [int(num) for num in re.findall(r'\d', input_str)]
print('Digits:', digit_list)

# use the built-in function sum
total = sum(digit_list)

# average = sum / count of digits
avg = total / len(digit_list)
print("Sum is:", total, "Average is ", avg)



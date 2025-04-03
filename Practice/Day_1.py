""" Print the Sum of a Current Number and a Previous number
sum=0
pre=0
for x in range(1,11):
    sum=x+(x-1)
    print(f'curr no. {x} prev no. {pre} Sum : {sum}')
    pre+=1

"""

""" Print characters present at an even index number
string=input('Enter string : ')
#print(len(string))
for x in range(len(string)):
    if x%2==0:
        print('Printing string :',string[x])
        #print('x : ',x)

"""

""" Remove first n characters from a string
s,n=input('Enter string & n : ').split()
n=int(n)
print(s[n:])
"""

""" Check if the first and last numbers of a list are the same

num_x=[10,20,30,40,10]
num_b=[20,60,40,50,40]
print("True" if num_x[0]==num_x[-1] else "False")

def first_last_same(numberList):
    print("Given list:", numberList)
    
    first_num = numberList[0]
    last_num = numberList[-1]
    
    if first_num == last_num:
        return True
    else:
        return False

numbers_x = [10, 20, 30, 40, 10]
print("result is", first_last_same(numbers_x))

numbers_y = [75, 65, 35, 75, 30]
print("result is", first_last_same(numbers_y))

"""


""" Find the number of occurrences of a substring in a string

import re
text = "Emma is good developer. Emma is a writer"
#print(count(re.findall('Emma',text)))
print(text.count("Emma",0,len(text)))

"""

""" Print the following pattern
     1
     22
     333
     4444
     55555

n=5
for x in range(1,n):
    #print(x)
    for y in range(x):
        print(x,end=" ")
    print('\n')


"""

""" Check Palindrome Number

#print(54545//10)
num=54545454545454545454545
s_num=list(str(num))
i_num=list(map(int,s_num))
r_num=list(reversed(i_num))
print(s_num)
print(i_num)
print(r_num)
if i_num==r_num:
    print('Yes. given number is palindrome number')


""" 
******* need to create logical solution for above question (9)
""" Find the factorial of a given number

num=int(input("Enter a no. : "))
fact=1
for i in range(1,num+1):
    fact*=i
print(fact)

"""

""" Reverse a integer number

solution 1-

#num=int(input("Enter a no. : "))
num=76542
a=0
new_num=0
while num!=0:
    a=num//10
    #b=num%10
    new_num=new_num*10+(num%10)
    num=a
    #print("a : ",a)
    #print("new_num : ",new_num)

print("Reversed no. : ",new_num)


solution 2-
num = 76542
reverse_number = 0
print("Given Number ", num)
while num > 0:
    reminder = num % 10
    reverse_number = (reverse_number * 10) + reminder
    num = num // 10
print("Revere Number ", reverse_number)

"""

""" Print elements from a given list present at odd index positions

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(my_list[1::2])
"""

""" Calculate the cube of all numbers from 1 to a given number

num=10
input_number = 6
for i in range(1, input_number + 1):
    print("Current Number is :", i, " and the cube is", (i * i * i))

"""


""" Find the sum of the series up to n terms
Write a program to calculate the sum of series up to n terms. 
For example, if n = 5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690

num=5
sum=0
i=2
for x in range(1,num+1):
     sum=sum+i
     i=(i*10)+2
     #print("sum : ",sum)
     #print("i : ",i)
print("Sum : ",sum)

"""




""" Display Fibonacci series up to 10 terms
Have you ever wondered about the Fibonacci Sequence? Its a series of numbers in which the next number is found by adding up the two numbers before it. The first two numbers are 0 and 1.
The first 10 terms of the Fibonacci sequence, starting with 0 and 1, are: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series is 13 + 21 = 34.
--------------------------
--------------------------
"""

num=int(input("Enter a number : "))
sum=0
a=0
b=1
print("Fibonacci series : ",a,b,end=" ")
for x in range(num-2):
    sum=a+b
    a=b
    b=sum
    print(sum,end=" ")
    
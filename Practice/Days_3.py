""" Print the following pattern
Write a Python code to print the following number pattern using a loop.

1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5


num=10
for x in range(1,num):
    for y in range(1,num):
        if x>=y:
            print(y,end=" ")
    print("\t\t")
    """

""" Calculate sum of all numbers from 1 to a given number
 if the user entered 10, the output should be 55 (1+2+3+4+5+6+7+8+9+10)

Expected Output:

Enter number 10
Sum is:  55

n=20
sum=0
for x in range(1,n+1):
    sum=sum+x
print(sum)

"""


"""  Display numbers from a list using a loop
Write a Python program to display only those numbers from a list that satisfy the following conditions

The number must be divisible by five
If the number is greater than 150, then skip it and move to the following number
If the number is greater than 500, then stop the loop
Given:

numbers = [12, 75, 150, 180, 145, 525, 50]
Expected output:

75
150
145

n = [12, 75, 150, 180, 145, 525, 50]
for x in n:
    if x%5==0:
        if x>500:
            break
        elif x>150:
            continue
        else:
            print(x)

"""

""" Count the total number of digits in a number

n=1234567890
b=0
while n!=0:
    n=n//10
    b=b+1
print(b)

"""

""" Print the following pattern
Write a Python program to print the reverse number pattern using a for loop.

5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1


n=5
for x in range(n,0,-1):
    for y in range(n,0,-1):
        if x>=y:
            print(y,end=" ")
    print("\t\t")

"""
"""Print all prime numbers within a range
Note: A Prime Number is a number that cannot be made by multiplying other whole numbers. A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers.

Examples:

6 is not a prime number because it can be made by 2×3 = 6
37 is a prime number because no other whole numbers multiply to make it.
Given:

# range
start = 25
end = 50

-----------------------------
-----------------------------

start = 25
end = 50
print("Prime numbers between", start, "and", end, "are:")

for num in range(start, end + 1):
    # all prime numbers are greater than 1
    # if number is less than or equal to 1, it is not prime
    if num > 1:
        for i in range(2, num):
            # check for factors
            if (num % i) == 0:
                # not a prime number so break inner loop and
                # look for next number
                break
        else:
            print(num)
            """

""" prime number

num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")
"""

""" Display Fibonacci series up to 10 terms
Have you ever wondered about the Fibonacci Sequence? Its a series of numbers in which the next number is found by adding up the two numbers before it. The first two numbers are 0 and 1.
The first 10 terms of the Fibonacci sequence, starting with 0 and 1, are: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series is 13 + 21 = 34.
--------------------------
--------------------------

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
    """


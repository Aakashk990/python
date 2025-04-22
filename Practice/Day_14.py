""" Find the highest worked emp

work_hr=[('A',100),('B',4000),('C',800),('D',8000)]

def check(work_hr):
    n=0
    m=''
    for x,y in work_hr:
        if y>n:
            n=y
            m=x
    
    return(m,n)
    
r=check(work_hr)
print(r)

"""

""" Create an inner function to calculate the addition in the following way
Create an outer function that will accept two parameters, a and b
Create an inner function inside an outer function that will calculate the addition of a and b
At last, an outer function will add 5 into addition and return it

def outer(a,b):

    def inner(a,b):
        return a+b
    
    return(inner(a,b)+5)

print(outer(2,3))

"""

""" Create a recursive function
Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.

A recursive function is a function that calls itself again and again.

Expected Output:
55

def s(n):
    if n:
        return(n+s(n-1))
    else:
        return 0

print(s(10))

"""















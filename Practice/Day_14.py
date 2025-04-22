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

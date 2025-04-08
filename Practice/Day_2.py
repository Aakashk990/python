""" Get each digit from a number in the reverse order.
num=7536
while num>0:
    a=num%10
    num=num//10
    print(a,end=" ")
    """


""" Print multiplication table from 1 to 10
for x in range(1,11):
    for y in range(1,11):
        print(x*y,end=" ")
    print("\t\t")
    
    """

""" Print a downward half-pyramid pattern of stars

n=10
for i in range(n):
    for j in range(n):
        if i<=j:
            print('*',end=" ") 
    print(" ")
    """

""" Get an int value of base raises to the power of exponent
Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.

Note here exp is a non-negative integer, and the base is an integer.

Expected output :
base = 2
exponent = 5

2 raises to the power of 5: 32 i.e. (2 *2 * 2 *2 *2 = 32)

 
base=10
expo=5
num=1
for x in range(expo):
    num=num*base
print(num)

"""

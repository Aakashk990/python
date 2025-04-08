""" Get an int value of base raises to the power of exponent
Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.

Note here exp is a non-negative integer, and the base is an integer.

Expected output :
base = 2
exponent = 5

2 raises to the power of 5: 32 i.e. (2 *2 * 2 *2 *2 = 32)

"""

base=10
expo=5
num=1
for x in range(expo):
    num=num*base
print(num)


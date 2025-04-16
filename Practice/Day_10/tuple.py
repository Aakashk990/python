#################### TUPLES  ###################



""" Reverse the tuple

tuple1 = (10, 20, 30, 40, 50)
print(tuple1[::-1])

"""

""" Access value 20 from the tuple
The given tuple is a nested tuple. write a Python program to print the value 20.

Given:
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))

Expected output:
20

tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
print(tuple1[1][1])
"""


""" Unpack the tuple into 4 variables
Write a program to unpack the following tuple into four variables and display each variable.

Given:

tuple1 = (10, 20, 30, 40)
Expected output:

tuple1 = (10, 20, 30, 40)
# Your code
print(a) # should print 10
print(b) # should print 20
print(c) # should print 30
print(d) # should print 40


tuple1 = (10, 20, 30, 40)

# unpack tuple into 4 variables
a, b, c, d = tuple1
print(a)
print(b)
print(c)
print(d)

"""

""" Swap two tuples in Python
Given:

tuple1 = (11, 22)
tuple2 = (99, 88)
Expected output:

tuple1: (99, 88)
tuple2: (11, 22)

solution 1 - (made by me)

tuple1 = (11, 22)
tuple2 = (99, 88)

t=tuple1
tuple1=tuple2
tuple2=t
print("Tuple1 :",tuple1,"\n","Tuple2 :",tuple2)


solution 2- 

tuple1 = (11, 22)
tuple2 = (99, 88)
tuple1, tuple2 = tuple2, tuple1
print(tuple2)
print(tuple1)
"""

"""  Copy specific elements from one tuple to a new tuple
Write a program to copy elements 44 and 55 from the following tuple into a new tuple.

Given:
tuple1 = (11, 22, 33, 44, 55, 66)

Expected output:
tuple2: (44, 55)


tuple1 = (11, 22, 33, 44, 55, 66)
tuple2=tuple1[3:5]
print(tuple2)

"""

""" Sort a tuple of tuples by 2nd item

Given:
tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))

Expected output:
(('c', 11), ('a', 23), ('d', 29), ('b', 37))

solution 1 - using lambda

tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
tuple1 = tuple(sorted(list(tuple1), key=lambda x: x[1]))
print(tuple1)

solution 2- without using lambda

from operator import itemgetter

tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))

# Use itemgetter to sort by the second item (index 1)
sorted_tuple = tuple(sorted(tuple1, key=itemgetter(1)))

print(sorted_tuple)
"""

""" Check if all items in the tuple are the same

tuple1 = (45, 45, 45, 45)

Expected output:
True

tuple1 = (45, 45, 45, 45)
print(all(x==tuple1[0] for x in tuple1))
"""














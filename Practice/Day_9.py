""" Reverse a list in Python

list1 = [100, 200, 300, 400, 500]
print(list1[::-1])
"""

""" Concatenate two lists index-wise
Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.

Given:

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

Expected output: ['My', 'name', 'is', 'Kelly']


list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
print([x + y for x,y in zip(list1,list2)])

"""


"""  Turn every item of a list into its square
Given a list of numbers. write a program to turn every item of a list into its square.

Given:

numbers = [1, 2, 3, 4, 5, 6, 7]
Expected output:

[1, 4, 9, 16, 25, 36, 49]

numbers = [1, 2, 3, 4, 5, 6, 7]
l=[x**2 for x in numbers]
print(l)

"""

""" Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
Expected output:

['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']


list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

print([x+y for x in list1 for y in list2])

"""

""" Iterate both lists simultaneously
Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order.

Given

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

Expected output:

10 400
20 300
30 200
40 100

solution 1- (made by me)

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

list2.reverse()
l3=list(zip(list1,list2))
#print(l3)
for x,y in l3:
    print(x,y)

    
solution 2- 

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for x, y in zip(list1, list2[::-1]):
    print(x, y)


    """
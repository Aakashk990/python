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


"""Remove empty strings from the list of strings
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
Expected output:

["Mike", "Emma", "Kelly", "Brad"]


list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

# remove None from list1 and convert result into list
res = list(filter(None, list1))
print(res)

"""

""" Add new item to list after a specified item
Write a program to add item 7000 after 6000 in the following Python List

Given:

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
Expected output:

[10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]


list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)

"""

"""   Extend nested list by adding the sublist
You have given a nested list. Write a program to extend it by adding the sublist ["h", "i", "j"] in such a way that it will look like the following list.

Given List:

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

# sub list to add
sub_list = ["h", "i", "j"]

Expected Output:
['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']



list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# sub list to add
sub_list = ["h", "i", "j"]

list1[2][1][2].extend(sub_list)
print(list1)

"""

""" Replace list’s item with new value if found
You have given a Python list. Write a program to find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of an item.

Given:
list1 = [5, 10, 15, 20, 25, 50, 20]

Expected output:
[5, 10, 15, 200, 25, 50, 20]

list1 = [5, 10, 15, 20, 25, 50, 20]
n=list1.index(20)
list1[n]=200
print(list1)

"""

"""Remove all occurrences of a specific item from a list.
Given a Python list, write a program to remove all occurrences of item 20.

Given:
list1 = [5, 20, 15, 20, 25, 50, 20]
Expected output:
[5, 15, 25, 50]

solution 1-
list1 = [5, 20, 15, 20, 25, 50, 20]
print([x for x in list1 if x!=20])

solution 2- 

list1 = [5, 20, 15, 20, 25, 50, 20]

while 20 in list1:
    list1.remove(20)
print(list1)

"""
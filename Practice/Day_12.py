""" Create a Python set such that it shows the element from both lists in a pair

Given:
first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]

Expected Output:
Result is  {(6, 36), (8, 64), (4, 16), (5, 25), (3, 9), (7, 49), (2, 4)}


first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]

t1=set(zip(first_list,second_list))
print(t1)

"""

""" Find the intersection (common) of two sets and remove those elements from the first set

Given:
first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

Expected Output:
Intersection is  {57, 83, 29}
First Set after removing common element  {65, 42, 78, 23}

first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

#t={first_set.remove(a) for a in first_set for b in second_set if a==b}
c=first_set.intersection(second_set)
print(c)

for i in c:
    first_set.remove(i)

print(first_set)

"""
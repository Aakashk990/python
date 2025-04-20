""" Create a list by picking an odd-index items from the first list and even index items from the second
Given two lists, l1 and l2, write a program to create a third list l3 by picking an odd-index element from the list l1 and even index elements from the list l2.

Given:

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
Expected Output:

Element at odd-index positions from list one
[6, 12, 18]
Element at even-index positions from list two
[4, 12, 20, 28]

Printing Final third list
[6, 12, 18, 4, 12, 20, 28]



l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

#l1_odd=[l1[1::2] for x in l1]
l1_odd=l1[1::2]
l2_even=l2[0::2]
l3=l1_odd+l2_even
print(l3)

"""


""" Remove and add item in a list
Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list.

Given:

list1 = [54, 44, 27, 79, 91, 41]
Expected Output:

List After removing element at index 4  [34, 54, 67, 89, 43, 94]
List after Adding element at index 2  [34, 54, 11, 67, 89, 43, 94]
List after Adding element at last  [34, 54, 11, 67, 89, 43, 94, 11]


l1=[34, 54, 67, 11, 89, 43, 94]
item=l1.pop(3)
print(l1)
l1.insert(2,item)
l1.append(item)
print(l1)

"""

""" Slice list into 3 equal chunks and reverse each chunk

Given:
sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

Expected Outcome:
Chunk  1 [11, 45, 8]
After reversing it  [8, 45, 11]
Chunk  2 [23, 14, 12]
After reversing it  [12, 14, 23]
Chunk  3 [78, 45, 89]
After reversing it  [89, 45, 78]


Solution 1- 

sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89,90]
size=int(len(sample_list)/3)
print(size)
chuck1=slice(0,size)
print(list(reversed(sample_list[chuck1])))
chuck2=slice(size,size*2)
print(list(reversed(sample_list[chuck2])))
chuck3=slice(size*2,size*3)
print(list(reversed(sample_list[chuck3])))


solution 2- 

sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89,90]
size=int(len(sample_list)/3)
i=0
j=size
for x in range(size):
    chuck4=slice(i,j)
    print("After chunk ",j," : ")
    print(list(reversed(sample_list[chuck4])))
    i=j
    j=i+j

"""

""" Count the occurrence of each element from a list
Write a program to iterate a given list and count the occurrence of each element and create a dictionary to show the count of each element.

Given:
sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

Expected Output:
Printing count of each item   {11: 2, 45: 3, 8: 1, 23: 2, 89: 1}

sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
new_set=set(sample_list)
new_dict={x:sample_list.count(x) for x in new_set }
print("Printing count of each item : ",new_dict)

"""



first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]

t1=set(zip(first_list,second_list))
print(t1)












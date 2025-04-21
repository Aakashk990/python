""" Checks if one set is a subset or superset of another set. If found, delete all elements from that set

Given:
first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}

Expected Output:
First set is subset of second set - True
Second set is subset of First set -  False

First set is Super set of second set -  False
Second set is Super set of First set -  True

First Set  set()
Second Set  {67, 73, 43, 48, 83, 57, 29}



first_set = {57, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

print("First Set ", first_set)
print("Second Set ", second_set)

print("First set is subset of second set -", first_set.issubset(second_set))
print("Second set is subset of First set - ", second_set.issubset(first_set))

print("First set is Super set of second set - ", first_set.issuperset(second_set))
print("Second set is Super set of First set - ", second_set.issuperset(first_set))

if first_set.issubset(second_set):
    first_set.clear()

if second_set.issubset(first_set):
    second_set.clear()

print("First Set ", first_set)
print("Second Set ", second_set)

"""

""" Iterate a given list and check if a given element exists as a key’s value in a dictionary. If not, delete it from the list

Given:
roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}

Expected Outcome:
After removing unwanted elements from list [47, 69, 76, 97]

roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
print(sample_dict.values())
new_l=[]
for x in roll_number:
    if x in sample_dict.values():
        new_l.append(x)

roll_number[:]=[ x for x in roll_number if x in sample_dict.values() ]
print(new_l)
print(roll_number)
"""



""" Get all values from the dictionary and add them to a list but don’t add duplicates

Given:
speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}

Expected Outcome:
[47, 52, 44, 53, 54]

speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
l=[]
l[:]=speed.values()
new_l=list(set(l))
print(new_l)


speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53,
         'july': 54, 'Aug': 44, 'Sept': 54}

print("Dictionary's values - ", speed.values())

speed_list = list()

# iterate dict values
for val in speed.values():
    # check if value not present in a list
    if val not in speed_list:
        speed_list.append(val)
print("unique list", speed_list)
"""


""" Remove duplicates from a list and create a tuple and find the minimum and maximum number

Given:
sample_list = [87, 45, 41, 65, 94, 41, 99, 94]

Expected Outcome:
unique items [87, 45, 41, 65, 99]
tuple (87, 45, 41, 65, 99)
min: 41
max: 99


sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
t=list(set(sample_list))
print(t)
print(tuple(t))
print(max(t))
print(min(t))
"""


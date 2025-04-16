""" Convert two lists into a dictionary
given:
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
Expected output:

{'Ten': 10, 'Twenty': 20, 'Thirty': 30}



keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
l1=dict(zip(keys,values))
print(l1)
"""


""" Merge two Python dictionaries into one

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

Expected output:
{'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

solution 1 -(Python 3.5+)
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict3={**dict1,**dict2}
print(dict3)

solution 2- 
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict3 = dict1.copy()
dict3.update(dict2)
print(dict3)

"""


""" Print the value of key ‘history’ from the below dict
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
Expected output:

80


sampleDict = {"class": {"student": {"name": "Mike","marks": {"physics": 70,"history": 80}}}}
print(sampleDict['class']['student']['marks']['history'])


"""

"""Initialize dictionary with default values
In Python, we can initialize the keys with the same values.

Given:

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
Expected output:

{'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}



employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

res = dict.fromkeys(employees, defaults)
print(res)

# Individual data
print(res["Kelly"])
"""

""" Create a dictionary by extracting the keys from a given dictionary
Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.

Given dictionary:

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

Expected output:
{'name': 'Kelly', 'salary': 8000}


solution 1-

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

new_dict=dict()
for x in keys:
    new_dict.update({x:sample_dict[x]})


print(new_dict)

solution 2 - Dictionary Comprehension

sampleDict = { 
  "name": "Kelly",
  "age":25, 
  "salary": 8000, 
  "city": "New york" }

keys = ["name", "salary"]

newDict = {k: sampleDict[k] for k in keys}
print(newDict)

"""


""" Delete a list of keys from a dictionary
Given:

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]

Expected output:
{'city': 'New york', 'age': 25}


solution 1- 

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]

for x in keys:
    sample_dict.pop(x)

print(sample_dict)


Solution 2: Dictionary Comprehension

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
# Keys to remove
keys = ["name", "salary"]

sample_dict = {k: sample_dict[k] for k in sample_dict.keys() - keys}
print(sample_dict)

"""

""" Check if a value exists in a dictionary
We know how to check if the key exists in a dictionary. Sometimes it is required to check if the given value is present.

Write a Python program to check if value 200 exists in the following dictionary.

Given:

sample_dict = {'a': 100, 'b': 200, 'c': 300}
Expected output:

200 present in a dict


sample_dict = {'a': 100, 'b': 200, 'c': 300}
for x in sample_dict.values():
    if x==200:
        print('present')

"""

""" Rename key of a dictionary
Write a program to rename a key city to a location in the following dictionary.

Given:

sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
Expected output:

{'name': 'Kelly', 'age': 25, 'salary': 8000, 'location': 'New york'}


sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

sample_dict['location'] = sample_dict.pop('city')
print(sample_dict)

"""


"""  Get the key of a min & max value from the following dictionary
sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}


sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
print(max(sample_dict))
print(min(sample_dict))

"""

""" Change value of a key in a nested dictionary
Write a Python program to change Brad’s salary to 8500 in the following dictionary.

Given:
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}

Expected output:
{
   'emp1': {'name': 'Jhon', 'salary': 7500},
   'emp2': {'name': 'Emma', 'salary': 8000},
   'emp3': {'name': 'Brad', 'salary': 8500}
}


sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}

sample_dict['emp3']['salary']=8500
print(sample_dict['emp3']['salary'])


"""



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















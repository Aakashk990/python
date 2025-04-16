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
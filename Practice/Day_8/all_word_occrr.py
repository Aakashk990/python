""" Write a program to count occurrences of all characters within a string
Given:

str1 = "Apple"
Expected Outcome:

{'A': 1, 'p': 2, 'l': 1, 'e': 1}
"""

str1 = "Apple"

char_dict=dict()
for x in str1:
    c=str1.count(x)
    char_dict[x]=c

print(char_dict)


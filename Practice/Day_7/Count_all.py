""" Count all letters, digits, and special symbols from a given string
Given:

str1 = "P@#yn26at^&i5ve"
Expected Outcome:

Total counts of chars, digits, and symbols 

Chars = 8 
Digits = 3 
Symbol = 4
"""

str1 = "P@#yn26at^&i5ve"
c=0
d=0
s=0
for x in range(len(str1)):
    if str1[x].isalpha():
        c+=1
    elif str1[x].isdigit():
        d+=1
    else:
        s+=1

print(str1,"\nChars = ",c,"\nDigits = ",d,"\nSymbol = ",s)


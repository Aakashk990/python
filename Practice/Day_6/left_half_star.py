""" Print the following pattern
Write a program to print the following start pattern using the for loop

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
"""

n=10
for x in range(n):
    for y in range(n):
        if x>=y:
            print("*",end=" ")
    print("\t\t")
for x in range(n-1):
    for y in range(n-1): 
        if x<=y:
            print("*",end=" ")
    print("\t\t")


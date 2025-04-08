""" Print the following pattern half pyramid
Write a Python code to print the following number pattern using a loop.

1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
"""

num=10
for x in range(1,num):
    for y in range(1,num):
        if x>=y:
            print(y,end=" ")
    print("\t\t")
    
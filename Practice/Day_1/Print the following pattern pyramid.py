""" Print the following pattern pyramid
     1
     22
     333
     4444
     55555
"""
n=5
for x in range(1,n):
    #print(x)
    for y in range(x):
        print(x,end=" ")
    print('\n')



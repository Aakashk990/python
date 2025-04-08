""" Calculate sum of all numbers from 1 to a given number
 if the user entered 10, the output should be 55 (1+2+3+4+5+6+7+8+9+10)

Expected Output:

Enter number 10
Sum is:  55

"""

n=20
sum=0
for x in range(1,n+1):
    sum=sum+x
print(sum)


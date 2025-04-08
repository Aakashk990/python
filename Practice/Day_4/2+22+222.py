"""Find the sum of the series up to n terms
Write a program to calculate the sum of series up to n terms. 
For example, if n = 5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690
"""


num=5
sum=0
i=2
for x in range(1,num+1):
     sum=sum+i
     i=(i*10)+2
     #print("sum : ",sum)
     #print("i : ",i)
print("Sum : ",sum)
#Find the factorial of a given number

num=int(input("Enter a no. : "))
fact=1
for i in range(1,num+1):
    fact*=i
print(fact)


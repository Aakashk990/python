
#solution 1-

#num=int(input("Enter a no. : "))
num=76542
a=0
new_num=0
while num!=0:
    a=num//10
    #b=num%10
    new_num=new_num*10+(num%10)
    num=a
    #print("a : ",a)
    #print("new_num : ",new_num)

print("Reversed no. : ",new_num)


#solution 2-
num = 76542
reverse_number = 0
print("Given Number ", num)
while num > 0:
    reminder = num % 10
    reverse_number = (reverse_number * 10) + reminder
    num = num // 10
print("Revere Number ", reverse_number)

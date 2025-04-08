sum=0
pre=0
for x in range(1,11):
    sum=x+(x-1)
    print(f'curr no. {x} prev no. {pre} Sum : {sum}')
    pre+=1
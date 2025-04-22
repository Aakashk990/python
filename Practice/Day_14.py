""" Find the highest worked emp

work_hr=[('A',100),('B',4000),('C',800),('D',8000)]

def check(work_hr):
    n=0
    m=''
    for x,y in work_hr:
        if y>n:
            n=y
            m=x
    
    return(m,n)
    
r=check(work_hr)
print(r)

"""
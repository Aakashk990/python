string=input('Enter string : ')
#print(len(string))
for x in range(len(string)):
    if x%2==0:
        print('Printing string :',string[x])
        #print('x : ',x)
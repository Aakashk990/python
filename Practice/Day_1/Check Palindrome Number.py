#print(54545//10)
num=54545454545454545454545
s_num=list(str(num))
i_num=list(map(int,s_num))
r_num=list(reversed(i_num))
print(s_num)
print(i_num)
print(r_num)
if i_num==r_num:
    print('Yes. given number is palindrome number')
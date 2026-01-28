n = int(input())

#n-1번째까지
for i in range(1,n):
    if(i==1):
        print(' '*(n-i)+'*')
    else:
        print(' '*(n-i)+'*'+' '*(2*i-3)+'*')

#n번째줄
print('*'*(2*n-1))
n = int(input())
j=0
for i in range(1,2*n):
    if(i<=n):
        print('*'*i + ' '*2*(n-i)+'*'*i)
    else:
        j+=1
        print('*'*(i-2*j) + ' '*2*(i-n)+'*'*(i-2*j))
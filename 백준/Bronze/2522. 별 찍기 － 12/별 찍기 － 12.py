n = int(input())
for i in range(1,n+1):
    print(' '*(n-i)+'*'*i)
for i in range(n+1,2*n):
    print(' '*(i-n)+'*'*(2*n-i))
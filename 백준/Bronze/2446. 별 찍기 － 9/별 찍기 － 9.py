n = int(input())
for i in range(1,n+1):
    print(' '*(i-1)+'*'*(2*n-(2*i-1)))
for i in range(n+1,2*n):
    print(' '*(2*n-1-i)+'*'*(2*i-(2*n-1)))
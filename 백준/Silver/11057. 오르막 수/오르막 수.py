#문제 잘못 읽음(0으로 시작할 수 있음)
import sys
n = int(sys.stdin.readline())

d = [[0]*10 for _ in range(n+1)]

for i in range(10):
    d[1][i] = 1

for x in range(2,n+1):
    d[x][0] = 1
    for i in range(1,10):
        d[x][i] = d[x][i-1]+d[x-1][i]
        
print(sum(d[n])%10007)
import sys

n, k = map(int, sys.stdin.readline().split())
#dp[i][j] : i를 j개의 수(0~i)로 만드는 경우의 수

dp = [ [0]*(k+1) for _ in range(n+1)] 

for j in range(1,k+1): #0을 만드는 경우의 수: 1
    dp[0][j] = 1

for i in range(1, n+1): #1개로 만드는 경우의 수 = 자기 자신 =- 1
    dp[i][1] = 1
    
for i in range(1,n+1):
    for j in range(2,k+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j]

print(dp[n][k]%1000000000)
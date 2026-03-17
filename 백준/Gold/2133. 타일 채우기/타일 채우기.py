import sys

n  = int(sys.stdin.readline()) 
#dp[i]: 3*i 크기 벽을 주어진 타일로 채우는 경우의 수

dp = [0 for _ in range(31)]

dp[2] = 3
    
for i in range(4,n+1,2):
    dp[i] = dp[i-2]*3 + sum(dp[:i-2])*2 + 2
        
print(dp[n])
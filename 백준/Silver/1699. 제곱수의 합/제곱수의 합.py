import sys

n  = int(sys.stdin.readline()) #자연수
#n을 제곱수의 합으로 표현할 때, 최소 항의 개수
#dp[i]: i를 제곱수 합으로 표현할 때, 최소 항의 개수

dp = [0]*(n+1)

for i in range(n+1):
    dp[i] = i #최악의 경우: 1을 i번 쓰는 경우
    j=1
    while j*j <= i:
        dp[i] = min(dp[i-j*j] + 1, dp[i])
        j+=1
        
print(dp[n])
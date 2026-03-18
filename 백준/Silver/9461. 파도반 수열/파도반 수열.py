import sys

t  = int(sys.stdin.readline())
cases = []
for _ in range(t):
    cases.append(int(sys.stdin.readline()))

dp = [0]*101
#dp[i]: i번째에서 시도에서, 가장 긴 변의 길이
dp[1],dp[2],dp[3] = 1,1,1

for n in cases:
    for i in range(4,n+1):
        dp[i] = max(dp[i-3]+dp[i-2], dp[i-1])
    print(dp[n])
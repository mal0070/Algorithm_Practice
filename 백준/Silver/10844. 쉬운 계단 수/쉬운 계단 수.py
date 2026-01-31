import sys
n = int(sys.stdin.readline())
#계단수의 개수 -> 계단수 길이(n), 마지막 자리의 값(i)에 따라 달라짐
dp = [[0]*10 for _ in range(n+1)]
#1의 자리수 초기화: 각 마지막자리당 개수-1개
for i in range(1,10):
    dp[1][i] = 1

for x in range(2,n+1):
    for i in range(10):
        if i == 0:
            dp[x][i] = dp[x-1][1]
        elif i == 9:
            dp[x][i] = dp[x-1][8]
        else:
            dp[x][i] = dp[x-1][i-1] + dp[x-1][i+1]

print(sum(dp[n])% 1000000000)
import sys
n  = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

dp = [1]*n #초기화
    
for i in range(1,len(arr)):
    for j in range(i):
        if (arr[j] < arr[i]):
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
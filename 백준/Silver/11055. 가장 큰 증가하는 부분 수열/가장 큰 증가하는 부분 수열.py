import sys
n  = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

#dp에 저장할 것: 합
dp = arr[:]
for i in range(1, len(arr)):
    for j in range(i):
        if(arr[i]>arr[j]):
            dp[i] = max(dp[i],dp[j]+arr[i])

print(max(dp))
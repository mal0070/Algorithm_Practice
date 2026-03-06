import sys
n  = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

dp = arr[:]

#조건:연속 -> 바로 뒤 인덱스여아만함
for i in range(1,n):
   dp[i] = max(dp[i],dp[i-1]+arr[i])

print(max(dp))
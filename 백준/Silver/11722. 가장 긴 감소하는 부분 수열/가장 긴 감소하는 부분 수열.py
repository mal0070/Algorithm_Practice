import sys
n  = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

#dp[i]: i번째 숫자로 끝나는 수열의 길이
dp = [1]*n
for i in range(1,n):
    for j in range(i):
        #감소하는 부분수열
        if(arr[i]<arr[j]):
            dp[i] = max(dp[i],dp[j]+1)
            
print(max(dp))
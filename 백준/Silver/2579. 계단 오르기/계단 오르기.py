import sys

n  = int(sys.stdin.readline()) #자연수
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

#dp: i번째 계단 밟았을 때, 최대 점수 
dp = [0]*n
dp[0] = arr[0] #n=1
if n>1:
    dp[1] = arr[0]+arr[1]
if n>2:
    dp[2] = max(arr[0]+arr[2],arr[1]+arr[2])

for i in range(3,n):
    dp[i] = max(dp[i-2] + arr[i], dp[i-3]+arr[i-1]+arr[i])
    
print(dp[n-1])

n = int(input())
#구하는 것: 2*n 크기의 직사각형을 채우는 방법 수
if n == 1: 
    print(1)
elif n == 2:
    print(2)
else:
    dp = [0]*(n+1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3,n+1):
        dp[i] = dp[i-1]+dp[i-2]

    print(dp[n]%10007)
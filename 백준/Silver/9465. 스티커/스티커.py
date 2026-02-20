import sys
T = int(sys.stdin.readline())

#기본적인 규칙잡고, 예외처리 -> 지그재그로 가다가, 더 큰 값이 나오면 건너뜀
#최대값을 누적해가며 어떤 스티커를 뗄지 선택
#dp 테이블: 스티커에 적힌 점수값들로 초기화
#for문을 통해 dp 계속 갱신:합으로

for _ in range(T):
    n = int(input())
    dp = [list(map(int,input().split())) for _ in range(2)]
    
    if n > 1:
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]
    
    for i in range(2,n):
        dp[0][i] += max(dp[1][i-1],dp[1][i-2])
        dp[1][i] += max(dp[0][i-1],dp[0][i-2])
    
    print(max(dp[0][n-1],dp[1][n-1])) #2가지 경로 중 max 선택
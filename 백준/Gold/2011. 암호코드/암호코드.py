import sys

code = sys.stdin.readline().replace(" ","")
n = len(code)
#dp[i] : 앞에서부터 1개 사용했을 때, 해석할 수 있는 경우의 수
dp = [0]*(n+1) #_25114 -> n-2계산위해 인덱스하나늘림
dp[0] = 1 #아무것도 안하는 방법 = 1
dp[1] = 1

if code[0] == '0':
    print(0)
    exit()

for i in range(2,n+1):
    #한 자리
    if code[i-1] != '0':
        dp[i] += dp[i-1]
    
    #두 자리
    num = int(code[i-2:i])
    if(10<= num <= 26):
        dp[i] += dp[i-2]
    
    dp[i]%=1000000

print(dp[n])
import sys
n  = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

#문제 분해 => 2개의 dp 문제로 쪼깸
#dp 기준: 변경되는 지점 
#dp: i번째 숫자가 끝인 증가 수열의 길이 + i번째 숫자가 시작인 감소 수열의 길이 - 1(i번째수가 겹침)

dp_asc = [1]*n
dp_dsc = [1]*n

#증가수열(0~i)
for i in range(1,n):
    for j in range(i):
        if arr[j]<arr[i]:
            dp_asc[i] = max(dp_asc[i], dp_asc[j]+1)
 #감소수열 (i~n-1)           
for i in range(n-1,-1,-1):
    for j in range(n-1,i,-1):
        if arr[j]<arr[i]:
            dp_dsc[i] = max(dp_dsc[i], dp_dsc[j]+1)

#바이토닉: 같은 인덱스를 꼭대기로 해야함
result = 0
for i in range(n):
    result = max(result, dp_asc[i]+dp_dsc[i]-1)


print(result)        
            
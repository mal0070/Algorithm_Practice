import sys
T = int(sys.stdin.readline())
testcase = []
for _ in range(T):
    testcase.append(int(sys.stdin.readline()))
    
for n in testcase: 
    #기본 배열 -> 최소 4의 길이로(d[1],d[2],d[3] 값 넣기 위해)
    d = [0]*max(4,(n+1)) #배열을 처음부터 넉넉하게 만들기(index에러 방지. 처음에 n=1이여서 배열길이가 2일때도 d[3]만들게 했음)
    d[1], d[2], d[3] = 1,2,4
    
    for i in range(4,n+1):
        d[i] = d[i-1]+d[i-2]+d[i-3]
            
    print(d[n])
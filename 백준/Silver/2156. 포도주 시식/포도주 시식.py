import sys
n = int(sys.stdin.readline())
#가장 많은 양, 3연속 안됨 - 누적합(dp)
#마지막 상황을 기준으로 생각, 생각단위:3
wine = []
for _ in range(n):
    wine.append(int(sys.stdin.readline()))

d = [0]*n
#초기화
d[0] = wine[0]
if n > 1:
   d[1] = d[0] + wine[1]

if n > 2:
    d[2] = max(d[1], wine[0]+wine[2], wine[1]+wine[2])

#dp갱신
for i in range(3,n):
    d[i] = max(d[i-3]+wine[i-1]+wine[i], d[i-2]+wine[i], d[i-1])

print(d[n-1])
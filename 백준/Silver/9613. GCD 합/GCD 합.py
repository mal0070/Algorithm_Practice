import sys

def gcd(a,b):
    while b:
        a, b = b, a%b
    return a


t = int(sys.stdin.readline())
for _ in range(t):
    total = 0
    nums = list(map(int, sys.stdin.readline().split()))
    for i in range(1,len(nums)): #n을 신뢰하지 않기(사용자 입력이기 때문에) -> 실제 리스트 길이 기반 접근으로 방어적 코딩
        for j in range(i+1,len(nums)):
            total+=gcd(nums[i], nums[j])
    print(total)
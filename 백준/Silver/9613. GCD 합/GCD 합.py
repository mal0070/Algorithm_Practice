import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

t = int(sys.stdin.readline())

for _ in range(t):
    total = 0
    
    # 🔥 빈 줄 방지
    while True:
        line = sys.stdin.readline().strip()
        if line:
            nums = list(map(int, line.split()))
            break

    n = nums[0]

    for i in range(1, n):
        for j in range(i+1, n+1):
            total += gcd(nums[i], nums[j])

    print(total)
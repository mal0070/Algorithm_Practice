import sys

t = int(sys.stdin.readline())

def gcd(a,b):
    while b:
        a,b = b, a%b
    return a

def lcm(a,b):
    return a*b // gcd(a,b)

for _ in range(t):
   a,b = map(int,sys.stdin.readline().split())
   print(lcm(a,b))
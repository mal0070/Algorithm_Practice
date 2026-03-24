import sys

a,b = map(int,sys.stdin.readline().split())

def gcd(a,b):
    while b:
        a,b = b, a%b
    return a

st = str(gcd(a,b))

if st == ('1' * len(st)):
    print(st)
else:
    print('1'*gcd(a,b))
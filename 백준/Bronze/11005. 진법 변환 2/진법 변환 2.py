import sys

n, b = map(int, sys.stdin.readline().split())

answer = ''
digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while n:
    n, mod = divmod(n,b)
    answer+=digits[mod]

print(answer[::-1])

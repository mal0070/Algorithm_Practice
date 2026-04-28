import math

def solution(a, b): #유한소수(기약분수일때,2와 5만 존재)이면 1, 아니면 2
    div = math.gcd(a,b)
    num = b // div

    while num>1 and (num%2 ==0 or num%5==0):
        if num % 2 == 0:
            num //=2
        elif num%5 ==0:
            num //=5
    
    if num == 1:
        return 1
    else:
        return 2
   

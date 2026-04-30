import math

def solution(numer1, denom1, numer2, denom2):
    answer = []
    
    a = math.gcd(denom1,denom2) #최대공약수
    b = denom1 // a * denom2 #최소공배수
    
    new_numer = numer1* (b//denom1) + numer2* (b//denom2)
    
    c = math.gcd(new_numer,b)
    
    return [new_numer//c, b//c] #분자, 분모 (기약분수)
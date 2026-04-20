def solution(n): #n이하의 최대 팩토리얼
    x = 1
    fact = 1
    while fact <= n:
        x +=1
        fact *= x
    return x - 1
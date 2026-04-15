def solution(n):
    #n의 소인수를 오름차순으로
    answer = []
    
    for i in range(2, n+1):
        while n % i == 0:
            if i not in answer:
                answer.append(i)
            n = n // i
    
    return answer
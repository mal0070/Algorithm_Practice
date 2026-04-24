def solution(sides):
    answer = 0
    #1. 답이 가장 긴 변일 경우
    tri = sides[0] + sides[1]
    for i in range(max(sides), tri):
        answer +=1
    #2. 둘 중 가장 큰 변이 긴 변일 경우
    for i in range(max(sides)):
        if min(sides)+i > max(sides):
            answer +=1
    return answer
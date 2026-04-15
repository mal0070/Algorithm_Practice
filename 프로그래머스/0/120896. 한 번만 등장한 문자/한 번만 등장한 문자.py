def solution(s):
    #한 번만 등장하는 문자 -> 사전순으로 정렬
    answer = []
    for i in s:
        if s.count(i) == 1:
            answer.append(i)
    
    answer.sort()
    
    return ''.join(answer)
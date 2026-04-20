def solution(my_string): #자연수들의합
    answer = 0
    
    #알파벳 제거
    for s in my_string:
        if s.isalpha():
            my_string = my_string.replace(s,",") #알파벳 제거, 구분자 삽입
    
    #숫자 합 계산
    a = my_string.split(',')
    for x in a:
        if x.isdigit():
            answer += int(x)
    
    return answer
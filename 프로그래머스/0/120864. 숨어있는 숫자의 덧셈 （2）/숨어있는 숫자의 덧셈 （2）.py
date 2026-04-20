def solution(my_string): #자연수들의합
    #알파벳 제거
    for s in my_string:
        if s.isalpha():
            my_string = my_string.replace(s," ") #알파벳 제거, 공백 삽입
    
    #숫자 합 계산
    a = my_string.split() #공백 기준으로 나눔 -> 깔끔하게 나눠짐
    return sum(list(map(int, a)))
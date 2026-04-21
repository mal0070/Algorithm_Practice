def solution(my_string):
    my_string = my_string.split()
    
    #홀수인덱스는 연산자
    answer = int(my_string[0])
    for i in range(1,len(my_string)-1):
        if i%2 !=0:
            if my_string[i] == '+':
                answer += int(my_string[i+1])
            else:
                answer -= int(my_string[i+1])
    
    return answer
def solution(my_str, n):
    return [my_str[i:i+n] for i in range(0, len(my_str), n)] #슬라이싱은 인덱스 초과해도 에러 안남
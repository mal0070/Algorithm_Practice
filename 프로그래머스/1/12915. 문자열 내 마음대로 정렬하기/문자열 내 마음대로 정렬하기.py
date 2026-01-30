def solution(strings, n):#각 문자열의 n번째 인덱스글자를 기준으로 / 오름차순 정렬
    #먼저 오름차순 정렬하고 시작!!
    strings.sort()
    strings.sort(key=lambda str: str[n])
    
    return strings
   
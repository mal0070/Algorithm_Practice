def solution(s):
    answer = 0 #Z를 만나면 그 앞 숫자를 뺌
    s = s.split() #["1", "2", "Z", 3"]
    for i in range(len(s)):
        if s[i] == "Z":
            answer -= int(s[i-1])
        else:
            answer+=int(s[i])
        
    return answer
def solution(before, after):
    #만들 수 있다: 문자열 모두 포함, 개수 동일

    if set(before) == set(after): #문자열 모두 포함하면
        for x in set(before): #alpe
            if before.count(x) != after.count(x): #아닌 경우 검사로 모든 경우 검사, 개수가 동일하지 않으면
                return 0
        return 1
        
    return 0 #포함X
    
    
    
def solution(spell, dic):
    count = 0
    
    for word in dic: #dzx
        for s in spell:#z
            if word.count(s) == 1:
                count+=1
        if count == len(spell):
            return 1
        count = 0 #초기화
    
    return 2
def solution(dots):
    #한 번에 두 개를 선택하고, 두 선분의 기울기 비교해서 같으면 return 1
    #아니면 return 0
    
    def is_parallel(a,b,c,d):
        [x1,y1] = dots[a]
        [x2,y2] = dots[b]
        [x3,y3] = dots[c]
        [x4,y4] = dots[d]
        
        m1 = (y1-y2) / (x1-x2)
        m2 = (y3-y4) / (x3-x4)
        
        return m1 == m2 #True, False
    
    cases = [
        (0,1, 2,3),
        (0,2, 1,3),
        (0,3, 1,2),
    ]
    
    for (a,b,c,d) in cases:
        if is_parallel(a,b,c,d):
            return 1
        
    return 0
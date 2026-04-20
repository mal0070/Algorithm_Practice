def solution(emergency):
    result = []
    a = sorted(emergency, reverse=True) #큰 순서대로
    
    for pa in emergency:
        result.append(a.index(pa)+1)
    return result
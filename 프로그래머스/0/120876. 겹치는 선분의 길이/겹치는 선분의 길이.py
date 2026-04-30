def solution(lines):
    sets = []
    answer = 0
    for [start,end] in lines:
        sets.append({i for i in range(start,end)})
    
    
    return len((sets[0] & sets[1])| (sets[0] & sets[2]) | (sets[1] & sets[2]))
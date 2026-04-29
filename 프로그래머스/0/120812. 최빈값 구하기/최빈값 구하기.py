def solution(array):
    set_array = list(set(array))
    counts = [array.count(n) for n in set_array] 
    value = []
    
    for x in counts:
        if max(counts) == x:
            value.append(x)
        
    if len(value) > 1:
        return -1
    
    return set_array[counts.index(max(counts))]
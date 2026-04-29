def solution(array):
    set_array = list(set(array))
    counts = [array.count(n) for n in set_array] #[1,1,3,3,3,1]
    value = []
    answer = []
    
    for x in counts:
        if max(counts) == x:
            value.append(x)
        
    if len(value) > 1:
        return -1
    
    return set_array[counts.index(max(counts))]
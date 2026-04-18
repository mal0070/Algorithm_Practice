def solution(array, n):
    differ = []
    array.sort()
    for i in array:
        differ.append(abs(i-n))
    
    answer = [array[differ.index(min(differ))]]
    
    return min(answer)
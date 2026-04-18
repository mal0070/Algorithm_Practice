def solution(array, n):
    #리스트를 만들지않고 해결
    answer = array[0]
    min_diff = abs(n-answer)
    for x in array[1:]:
        diff = abs(n-x)
        if diff < min_diff or (diff == min_diff and answer > x):
            min_diff = diff
            answer = x
    
    return answer
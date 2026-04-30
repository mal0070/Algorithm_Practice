def solution(num, total):
    answer = []
    
    mid = total // num
    answer.append(mid)
    
    if total % num !=0:
        answer.append(mid+1)
        
    while len(answer) != num:
        answer.append(min(answer)-1)
        answer.append(max(answer)+1)
    
    answer.sort()
    return answer
                
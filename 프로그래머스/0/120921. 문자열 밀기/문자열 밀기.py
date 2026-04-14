def solution(A, B):
    answer = 0
    while A != B: #hello ==> ohell
        last = A[len(A)-1] #o
        A = last + A[:len(A)-1] #ohell
        answer+=1
        
        if answer > len(A)+1:
            return -1
        
    return answer
    
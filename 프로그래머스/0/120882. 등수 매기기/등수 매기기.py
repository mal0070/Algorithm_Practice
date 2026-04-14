def solution(score):
    arr = []
    answer = []
    
    
    for i in score:
        aver = sum(i) /2
        arr.append(aver)
        
    sorted_arr = sorted(arr,  reverse=True) #등수
    for i in range(len(arr)):#arr
        ranking = sorted_arr.index(arr[i]) + 1
        answer.append(ranking)
    
    return answer
'''
입력값 〉 [[1, 3], [3, 1], [2, 3], [3, 2], [1, 2], [1, 1]]
기댓값 〉 [3, 3, 1, 1, 5, 6]
2 2 2
'''
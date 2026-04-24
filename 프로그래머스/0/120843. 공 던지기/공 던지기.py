def solution(numbers, k):
    count = 1
    i = 0
    
    while count < k: #count == k 이면 빠져나옴
        i+=2 #공던짐
        if i > len(numbers)-1: #last index 넘어가면
            i = i - len(numbers)
        count +=1
    return numbers[i]


def solution(common):
    num = 0
    #common의 길이: 최소 3
    if (common[1] - common[0]) == (common[2] - common[1]):
        num = common[1] - common[0]
        return common[len(common)-1] + num
    else:
        num = common[1] // common[0]
        return common[len(common)-1] * num
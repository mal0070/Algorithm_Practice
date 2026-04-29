def solution(numlist, n):
    #n과 가까운 수 정렬, 같다면 더 큰 수가 앞
    return  sorted(numlist, key=lambda x:(abs(x-n),-x))
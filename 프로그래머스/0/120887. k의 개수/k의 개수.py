def solution(i, j, k):
    arr = [str(x) for x in range(i,j+1)]
    a = "".join(arr)
    return a.count(str(k))
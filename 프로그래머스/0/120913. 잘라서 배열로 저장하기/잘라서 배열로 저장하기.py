def solution(my_str, n):
    answer = []
    n_str = ''
    for i in my_str:
        n_str = n_str + i
        if len(n_str) == n:
            answer.append(n_str)
            n_str = ''
    
    div, mod = divmod(len(my_str), n)
    
    if mod > 0:
        answer.append(my_str[n*div:])
            
    return answer
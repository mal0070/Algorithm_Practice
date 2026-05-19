def solution(babbling): 
    answer = 0
    words = ['aya', 'ye', 'woo', 'ma']
    
    for b in babbling:
        for i in range(4):
            b = b.replace(words[i]," ")
        if b.isspace():
            answer += 1
    return answer
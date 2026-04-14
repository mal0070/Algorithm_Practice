def solution(chicken):
    answer = 0
    coupon = 0
    
    while chicken >= 10:
        chicken, re = divmod(chicken,10) #몫, 나머지
        answer+= chicken #108+10+1
        chicken+=re #1 + 8 + 0 + 1
        
    return answer #최대 공짜치킨 수


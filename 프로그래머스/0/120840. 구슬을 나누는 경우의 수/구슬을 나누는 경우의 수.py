def solution(balls, share):
    numer = 1
    deno = 1
    
    a = balls-share
    
    while balls > a:
        numer *= balls 
        balls -= 1
        
    while share > 1:
        deno *= share
        share -= 1
        
    return numer // deno
    
   

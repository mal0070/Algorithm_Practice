def solution(balls, share):
    numer = 1
    deno = 1
    
    for i in range(1, share+1):
        numer *= balls 
        balls -= 1
        
        deno *= i
        
    return numer // deno
    
   

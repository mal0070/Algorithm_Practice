function solution(sides) { //가장 긴 변의 길이 < a+b
    let answer = 0;
    
    sides.sort((a,b)=>a-b);
    console.log(sides);
    let sum = sides[0]+sides[1];
        
    //가장 긴 변이 sides[1]
    //sides[1] - sides[0] +1 부터 sides[1] 까지
    answer = (sides[1] - (sides[1]-sides[0]))+(sum-1 - sides[1]);
    
    
    
    return answer;
}
function solution(new_id) {
    let answer = new_id.toLowerCase() // 1단계
    .replace(/[^\w\-\.]/g, '') //2단계
    .replace(/\.{2,}/g,'.'); // 3단계
    
    //4단계
    if(answer[0] === '.')  answer = answer.slice(1);
    if(answer[answer.length-1] === '.') answer = answer.slice(0,-1);
    
    //5단계
    if(answer.length === 0) answer ='a';
    
    
    //6단계 
    if(answer.length >= 16){
        answer = answer.slice(0,15); 
    if(answer[answer.length-1] === '.') answer = answer.slice(0,-1);
    }

    //7단계
    if(answer.length <=2){
        answer = answer.padEnd(3,answer[answer.length-1]);
    }
    return answer;
    
}



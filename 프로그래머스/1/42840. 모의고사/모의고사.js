function solution(answers) { //정답 12345
    let result = [];
    
    const len = answers.length;
    
    let one = [1,2,3,4,5];
    let two = [2,1,2,3,2,4,2,5];
    let three = [3,3,1,1,2,2,4,4,5,5];
    
    
    let score1 = answers.filter((answer,i)=> answer === one[i%one.length]).length;
    let score2 = answers.filter((answer,i)=> answer === two[i%two.length]).length;
    let score3 = answers.filter((answer,i)=> answer === three[i%three.length]).length;
    
    const max = Math.max(score1,score2,score3);
    if(max === score1) result.push(1);
    if(max === score2) result.push(2);
    if(max === score3) result.push(3);
    
    return result
    
    
    
}

function solution(s) {
    //문자열을 배열처럼 쓸 수 있다..
    if(s[0] === ")") return false;
    
    let num = 0;
    for (let e of s){
        (e === "(") ? num+=1 : num-=1;
        if(num<0) return false;
    }
    if(num === 0) return true; 
    else return false;
}                 
                     
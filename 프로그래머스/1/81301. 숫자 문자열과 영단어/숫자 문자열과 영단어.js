function solution(s) {
    const numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'];
    
    numbers.forEach((number,index)=> {
       while(s.includes(number)){
           s = s.replace(number, index);
       }
    });
    return Number(s);
}
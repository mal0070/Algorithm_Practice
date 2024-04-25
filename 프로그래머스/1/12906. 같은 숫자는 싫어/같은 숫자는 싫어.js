function solution(arr) //0~9 연속제거
{
    let ans = [];
    
    for(let i=0;i<arr.length;i++){
        if (arr[i] !== arr[i+1]){
           ans.push(arr[i]);
        } 
    }
  
    return ans;
}
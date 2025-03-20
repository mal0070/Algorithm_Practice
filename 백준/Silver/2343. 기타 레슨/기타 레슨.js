const fs = require('fs');
const input = fs.readFileSync('/dev/stdin', 'utf8').trim().split('\n'); // 백준 경로:'/dev/stdin'

const [N, M] = input[0].split(' ').map(Number); //강의 수: N개  블루레이 개수: M개
const lessons = input[1].split(' ').map(Number);

let start = Math.max(...lessons);
let end = lessons.reduce((prev,cur)=> prev+cur, 0);

//이진탐색을 끝까지 진행하여 최솟값을 찾아야함
while(start <= end){
  let mid = Math.floor((start + end)/2);
  let sum = 0;
  let bluerayCount = 1; //최소 블루레이 개수는 1개부터 시작
 
  for(let i=0;i<N;i++){
    sum += lessons[i];
    if(sum >  mid){
      sum = lessons[i]; //다음 블루레이에 현재 강의 저장
      bluerayCount++;
    }
  }

  if(bluerayCount <= M){
    end = mid - 1;
  } else {
    start = mid + 1;
  }
}

console.log(start);
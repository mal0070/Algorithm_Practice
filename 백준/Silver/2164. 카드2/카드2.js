const fs = require('node:fs');
const n = Number.parseInt(fs.readFileSync('/dev/stdin','utf8')); // 백준 경로:'/dev/stdin'

const deque = []
for(let i=1; i<=n; i++) deque.push(i);

let front = 0; //첫번째 원소를 가리키는 포인터

while(deque.length - front > 1){
    front++; //첫번째 카드 버리기
    deque.push(deque[front]); //두번째 카드를 맨 뒤로 이동
    front++; //세번째 카드가 맨 위에 있음
}

console.log(deque[front]);

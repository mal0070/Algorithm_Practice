const fs = require('node:fs');
const input = fs.readFileSync('/dev/stdin','utf8').split(' '); // 백준 경로:'/dev/stdin'

const [n, k] = input.map(Number);
const circle = [];
const result = [];

for(let i=1;i<=n;i++) circle.push(i); //[1,2,3,4,5,6,7]

//k번째 사람을 제거한다.
//제거하고, 그 시점부터 다시 k번째

let remove = 0;
while(circle.length>0){
    remove = (remove + k-1) % circle.length;
    result.push(circle.splice(remove,1)[0]);
}

console.log(`<${result.join(', ')}>`);
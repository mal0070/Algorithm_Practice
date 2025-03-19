const fs = require('fs');
const input = fs.readFileSync('/dev/stdin', 'utf8').trim().split('\n'); // 백준 경로:'/dev/stdin'

const N = parseInt(input[0]);
const arrayA = input[1]
  .split(' ')
  .map(Number)
  .sort((a, b) => a - b);
const M = parseInt(input[2]);
const arrayB = input[3].split(' ').map(Number);

const result = [];

//B의 수가 A에 존재하면 1, 아니면 0

//binary search

for (const target of arrayB) {
  let start = 0;
  let end = N - 1;
  let found = false;

  while (start <= end) {
    //루프 종료 조건 : 시작인덱스>종료인덱스
    let mid = Math.floor((start + end) / 2);
    let midValue = arrayA[mid];

    if (midValue > target) {
      end = mid - 1;
    } else if (midValue < target) {
      start = mid + 1;
    } else {
      //midValue === target
      result.push(1);
      found = true;
      break;
    }
  }
  if (!found) {
    result.push(0);
  }
}

console.log(result.join('\n'));
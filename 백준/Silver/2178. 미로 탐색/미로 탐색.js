const fs = require('fs');
const input = fs.readFileSync('/dev/stdin', 'utf8').trim().split('\n'); // 백준 경로:'/dev/stdin'

const [N, M] = input[0].split(' ').map(Number);
const grid = input.slice(1).map((line) => line.split('').map(Number));

const directions = [
  [-1, 0],
  [1, 0],
  [0, -1],
  [0, 1],
]; //상,하,좌,우

const bfs = () => {
  const queue = [[0,0,1]]; //시작노드 좌표 x,y,현재깊이 저장
  grid[0][0] = 0; //재방문 방지

  while (queue.length) {
    const [x,y,depth] = queue.shift();

    if (x === N - 1 && y === M - 1) {
      return depth;
    }

    for (const [dx, dy] of directions) { //상하좌우 탐색
      const nx = x + dx;
      const ny = y + dy;
      if (nx >= 0 && ny >= 0 && nx < N && ny < M && grid[nx][ny] === 1) {//좌표 유효성 검사 & 이동가능
          queue.push([nx,ny,depth+1]);
          grid[nx][ny] = 0;
      }
    }
  }
  return depth;
};

console.log(bfs());

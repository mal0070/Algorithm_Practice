const fs = require('fs');
const input = fs.readFileSync('/dev/stdin', 'utf8').trim().split('\n'); // 백준 경로:'/dev/stdin'

const V = Number(input[0]); //정점 개수
const edges = input.slice(1).map((line) => line.split(' ').map(Number)); //간선 정보

//2차원 배열 인접리스트 만들기
const adjList = Array.from({ length: V + 1 }, () => []);

for (const edge of edges) {
  for (let i = 1; i < edge.length-1; i += 2) { //-1을 만날 때 까지
      adjList[edge[0]].push([edge[i], edge[i + 1]]); //[연결노드, 가중치] 형태로 각 인덱스(노드)에 저장
  }
}


//거리 저장 배열 => 특정 노드에서 연결된 노드의 끝까지 가중치 저장
let distance = Array(V + 1).fill(0);

//bfs -> 모든 정점까지의 거리를 최단거리로 탐색함
//탐색하면서 할 일: 방문배열 추가, 거리 업데이트
const bfs = (start) => {
  const queue = [start]; //큐에 시작 노드 삽입
  let visited = new Set(); //방문 기록 초기화
  visited.add(start);

  while (queue.length) {
    const node = queue.shift();
    for (const [neighbor, dist] of adjList[node]) {
      if (!visited.has(neighbor)) {
        queue.push(neighbor);
        visited.add(neighbor);
        distance[neighbor] = distance[node]+dist;
      }
    }
  }
};

bfs(1); //첫번째 bfs에서 가장 가중치가 크고, 끝에 있는 점 찾음
let farthestNode = distance.indexOf(Math.max(...distance));

//이 점에서 다시 bfs를 하여 가장 끝점 찾음 => 지름 구함
distance.fill(0); //distance 배열 초기화
bfs(farthestNode);

console.log(Math.max(...distance));//distance 중 가장 큰 값 출력
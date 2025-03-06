const fs = require('fs');
const input = fs.readFileSync('/dev/stdin', 'utf8').trim().split('\n');

const [N, M] = input[0].split(' ').map(Number); //정점, 엣지
const edges = input.slice(1).map(line => line.split(' ').map(Number));

//정점 개수 만큼 빈 배열 넣기. 인덱스를 키로 사용
const adjList = Array.from({length: N+1},()=>[]);

//연결 정보 추가
for(const [u,v] of edges){
    adjList[u].push(v);
    adjList[v].push(u);
}

const visited = Array(N+1).fill(0); //방문X: 0으로
let components = 0;

const dfs = (node) => {
    if(visited[node]===1) return; //이미 방문한 경우 종료
    visited[node] = 1; //방문처리

    //현재 노드에서 연결된 모든 노드 탐색
    for(const neighbor of adjList[node]){
        if(!visited[neighbor]) dfs(neighbor);
    }
    
};

for(let i=1;i<N+1;i++){
    if(visited[i]===0){
        components++;
        dfs(i);
    }
}

console.log(components);




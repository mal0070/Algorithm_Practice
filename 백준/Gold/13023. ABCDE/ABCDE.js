const fs = require('fs');
const input = fs.readFileSync('/dev/stdin', 'utf8').trim().split('\n'); // 백준 경로:'/dev/stdin'

const [N, M] = input[0].split(' ').map(Number); //사람 수, 친구 관계 수
const friends = input.slice(1).map(line => line.split(' ').map(Number));


//인접 리스트 만들기
const adjList = Array.from({length: N},()=>[]); //인덱스를 키로 사용
for (const [u,v] of friends){
    adjList[u].push(v);
    adjList[v].push(u);
}

//방문 배열 0으로 초기화
const visited = Array(N).fill(0);

let depth = 0;
let arrive = false;

const dfs = (node, depth) => {
    //종료조건
    if(depth === 5){
        arrive = true;
        return;
    }

    visited[node] = 1;
    for(const neighbor of adjList[node]){
        if(!visited[neighbor]){
            dfs(neighbor, depth+1);
            if (arrive) return;
        }
    }
    
    visited[node] = false; //백트래킹으로 상태를 되돌려 다른 경로도 탐색
};

for(let i=0;i<N;i++){
    dfs(i,1);//depth 1로 시작
    if(arrive) break;
}

console.log(arrive ? 1 : 0);
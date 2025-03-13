const fs = require('fs');
const input = fs.readFileSync('/dev/stdin', 'utf8').trim().split('\n'); // 백준 경로:'/dev/stdin'

const [N, M, V] = input[0].split(' ').map(Number);
const edges = input.slice(1).map(line => line.split(' ').map(Number));

// 인접 리스트 만들기
const adjList = Array.from({ length: N + 1 }, () => []);
for (const [u, v] of edges) {
    adjList[u].push(v);
    adjList[v].push(u);
}

// 각 노드의 인접 리스트를 오름차순으로 정렬
for (const nodes of adjList) {
    nodes.sort((a, b) => a - b);
}

const dfsResult = [];
const bfsResult = [];

const dfs = (node, visited) => {
    visited.add(node);
    dfsResult.push(node);

    for (const neighbor of adjList[node]) {
        if (!visited.has(neighbor)) {
            dfs(neighbor, visited);
        }
    }
};

const bfs = (start, visited) => {
    const queue = [start];
    visited.add(start);

    while (queue.length) {
        const node = queue.shift();
        bfsResult.push(node);

        for (const neighbor of adjList[node]) {
            if (!visited.has(neighbor)) {
                visited.add(neighbor);
                queue.push(neighbor);
            }
        }
    }
};

// DFS
let visited = new Set();
dfs(V, visited);

// BFS
visited = new Set();
bfs(V, visited);

console.log(dfsResult.join(' '));
console.log(bfsResult.join(' '));

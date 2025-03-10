#백준 1260

from collections import deque


n, m, v = map(int, input().split())
#graph = dict() #노드(키)의 값이 중복되지 않게 하기 위해
graph = {i: [] for i in range(1, n+1)} #입력 노드 번호 제한

#그래프 만드는 부분을 틀림
for _ in range(m): #간선이 연결하는 두 정점의 번호 입력받음
    key, child = map(int, input().split())
    if key not in graph:
        graph[key] = [] #노드가 됨
    if child not in graph:
        graph[child] = []
    graph[key].append(child)
    graph[child].append(key) #양방향이니까

'''
def dfs(graph, start, visited=[]):
    visited.append(start) #시작노드 -> 방문
    for node in graph[start]: #연결 노드들 
        if node not in visited: #방문해야하면
            dfs(graph, node, visited) #재귀함수 돌려서 추가시키기
    return visited
'''
def dfs(graph, start): #재귀돌리면 안됨 간선중복 때문이듯
    visited = []
    need_visited = deque()
    need_visited.append(start)
    while need_visited:
        node = need_visited.pop() #가장 마지막 요소 뽑기
        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])
    return visited


#정렬 필요: dfs에서는 노드들을 내림차순으로 정리해야 제대로 출력된다. (간선 중복때문인가)
for key in graph:
    graph[key].sort(reverse=True)
dfs_result = dfs(graph, v)
print(*dfs_result, sep=' ')



def bfs(graph, start):
    need_visited = deque()
    need_visited.append(start)
    visited = []
   
    while need_visited:
        node = need_visited.popleft()
        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])  
    return visited

for key in graph:
    graph[key].sort() #BFS는 오름차순으로 정렬
bfs_result = bfs(graph, v)
print(*bfs_result, sep= ' ')


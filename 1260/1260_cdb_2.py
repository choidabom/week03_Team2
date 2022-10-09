# 1260: DFS와 BFS
# deque 활용 & defaultdict 활용

import sys
from collections import defaultdict, deque
sys.stdin = open("1260/input.txt","r")
input = sys.stdin.readline

def dfs(start):
    visited[start] = True
    print(start, end=" ")
    for node in graph[start]:
        if not visited[node]:
            dfs(node)

def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for node in graph[v]:
            if not visited[node]:
                visited[node] = True
                queue.append(node)

# N: 정점 개수, M: 간선 개수, V: 탐색 시작 번호
N, M, V = map(int, input().split())
graph = defaultdict(list)
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    graph[i].sort()

# visited를 하나만 선언해주면 안 된다. 
visited = [False] * (N+1)
dfs(V)
print()
visited = [False] * (N+1)
bfs(V)
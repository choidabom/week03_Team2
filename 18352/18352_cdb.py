<<<<<<< HEAD
# 18352: 특정 거리의 도시 찾기

=======
>>>>>>> jaemin
import sys
sys.stdin = open("18352/input.txt","r")
from collections import deque, defaultdict
input = sys.stdin.readline

def bfs(graph, start, costs, visited):
    queue = deque([start])
    costs[start] = 0
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                costs[i] = costs[v] + 1
                visited[i] = True
                queue.append(i)

    flag = False
    for idx, cost in enumerate(costs):
        if cost == K:
            print(idx)
            flag = True
    if flag == False:
        print(-1)

N, M, K, X = map(int, input().split())
graph = defaultdict(list)
costs = [-1] * (N+1)
visited = [False] * (N+1)

for _ in range(M):
    A, B = map(int, input().split())
    # A번 도시에서 B번 도시로 이동하는 단방향 도로가 존재함.
    graph[A].append(B)

<<<<<<< HEAD
bfs(graph, X, costs, visited)
=======
bfs(graph, X, costs, visited)

>>>>>>> jaemin

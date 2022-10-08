import sys
sys.stdin = open("input.txt","r")
sys.setrecursionlimit(10**8)

N, M = map(int, sys.stdin.readline().split())
graph = [[] for i in range(N+1)]
visited = [False] * (N+1)
# print(N, M)
# print(graph)
# print(visited)

for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(start):
    visited[start] = True
    for i in graph[start]:
        if visited[i] == False:
            visited[i] == True
            dfs(i)

count = 0
for i in range(1, N+1):
    if visited[i] == False:
        count += 1
        dfs(i)

print(count)
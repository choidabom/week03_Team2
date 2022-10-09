# 11274: 연결 요소의 개수 
import sys
sys.setrecursionlimit(10**8)

N, M = map(int, sys.stdin.readline().split())
graph = [[] for i in range(N+1)]
visited = [False] * (N+1)

for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(start):
    visited[start] = True
    for i in graph[start]:
        if visited[i] == False:
            # 재귀를 돌면 True가 되기 때문에 중복
            # visited[i] == True
            # 빼고 돌렸을 경우 정답은 맞지만 시간이 조금 더 걸림
            dfs(i)

count = 0
for i in range(1, N+1):
    if visited[i] == False:
        count += 1
        dfs(i)
print(count)
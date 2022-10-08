import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline

N = int(input()) # 컴퓨터의 수
M = int(input()) # 네트워크 상에 직접 연결 컴퓨터 쌍의 수
graph = [[] for i in range(N+1)]
visited = [False] * (N+1)

for i in range(M):
    x, y = map(int, input().split())
    graph[y].append(x)
    graph[x].append(y)

print(graph)
print(visited)

def dfs(start):
    visited[start] = True
    for i in graph[start]:
        if visited[i] == False:
            visited[i] = True
            dfs(i)
    return visited

print(dfs(1))
cnt = 0
for i in range(1, N+1):
    if visited[i] == True:
        cnt += 1
print(cnt-1)
import sys
sys.stdin = open("2606/input.txt","r")
input = sys.stdin.readline

def dfs(start):
    visited[start] = True
    for i in graph[start]:
        if visited[i] == False:
            dfs(i)

N = int(input()) 
M = int(input()) 
graph = [[] for i in range(N+1)]
visited = [False] * (N+1)

for i in range(M):
    x, y = map(int, input().split())
    graph[y].append(x)
    graph[x].append(y)

dfs(1)
cnt = 0
for i in range(1, N+1):
    if visited[i] == True:
        cnt += 1
print(cnt-1)
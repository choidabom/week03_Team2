import sys
sys.stdin = open("5_input.txt","r")

sys.setrecursionlimit(5000)

def dfs(n) :            
    visited[n] = True
    
    for i in graph[n] :
        if not visited[i] :
            dfs(i)



n, m = map(int, sys.stdin.readline().rstrip().split())
# print(n, m)

graph = [[] for _ in range(n+1)]
for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)

# print(graph)

visited = [False] * (n+1)
cnt = 0

# 1~n번 노드를 각각 돌면서 확인

for i in range(1, n+1) :    
    if not visited[i] :     # 방문 안 했으면,
        if not graph[i] :   # 방문도 안 했는데 이 지점에 연결된 그래프가 없다면
            cnt += 1
            visited[i] = True
        else :      # 연결된 점이 있다면 dfs(i)
            dfs(i)
            cnt += 1

print(cnt)
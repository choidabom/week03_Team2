import sys
sys.stdin = open("6_input.txt","r")

cnt = 0
def dfs(n) :
    global cnt
    visited[n] = True
    cnt += 1
    for i in graph[n] :
        if visited[i] == False :
            dfs(i)
    

n = int(input())
m = int(input())
visited = [False] * (n+1)
graph = [[] * n for _ in range(n+1)]
for _ in range(m) :
    start, end = map(int, sys.stdin.readline().rstrip().split())
    graph[start].append(end)
    graph[end].append(start)

# print(graph)


dfs(1)
print(cnt-1)




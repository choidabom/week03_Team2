import sys
sys.stdin = open("7_input.txt","r")
sys.setrecursionlimit(5000)

n = int(input())
# print(n)

graph = [[] for _ in range(n+1)]
for _ in range(n-1) :
    start, end = map(int, sys.stdin.readline().strip().split())
    graph[start].append(end)
    graph[end].append(start)

# print(graph)

visited = [False] * (n+1)
# print(visited)

parent_list = [0] * (n+1)

def dfs(x) :
    visited[x] = True
    for i in graph[x] :
        if not visited[i] :
            parent_list[i] = x
            dfs(i)
    # print(parent_list)
dfs(1)
for i in parent_list[2:] :
    print(i)
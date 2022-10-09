import sys
sys.stdin = open("2606/input.txt","r")
from collections import deque, defaultdict
input = sys.stdin.readline

def bfs(v, visited, graph):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
    print(visited.count(True)-1)

def init():
    N = int(input())
    M = int(input())
    graph = defaultdict(list)
    visited = [False] * (N+1)
    for i in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    bfs(1, visited, graph)

init()

# 1260: DFS와 BFS
# dfs, bfs => 재귀 활용, 입력값 dict 활용

import sys
sys.stdin = open('1260/input.txt', 'r')

# 특징적인 것은 visited 자료형을 기본 함수 인자로 포함시키고,
# 방문한 리스트들을 재귀함수를 통해 visited에 담는 방식

def dfs(graph, start): # dfs: 깊이 우선 탐색
    visited.append(start)
    for node in graph[start]:
        if node not in visited:
            dfs(graph, node)
    return visited

def bfs(graph, start): # bfs: 
    need_visited, visited = [], []
    need_visited.append(start)

    while need_visited:
        node = need_visited[0]
        del need_visited[0]
        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])
    return visited

if __name__ == "__main__":
    # N: 정점 개수, M: 간선 개수, V: 탐색 시작 번호
    N, M, V = map(int, sys.stdin.readline().split())
    graph = {i: [] for i in range(1, N+1)}
    print(graph)
    visited = []

    for i in range(M):
        k, v = map(int, sys.stdin.readline().split())
        if v not in graph[k]:
            graph[k].append(v)
            graph[v].append(k)

    for k in graph:
        graph[k].sort()
    
    for i in dfs(graph, V):
        print(i, end=" ")
    print()
    for i in bfs(graph, V):
        print(i, end=" ")


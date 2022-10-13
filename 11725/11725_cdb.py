# 11725: 트리의 부모 찾기

import sys
sys.stdin = open("11725/input.txt","r")
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)


N = int(input())
nodes = [[] for _ in range(N+1)]
visited  = [False for _ in range(N+1)]
result = [0 for _ in range(N+1)] # 각 인덱스들의 부모를 넣어둘 리스트

for _ in range(N-1):   # N-1개의 줄에 트리 상에 연결되 두 정점
    k, v = map(int, input().split(' '))
    nodes[k].append(v)
    nodes[v].append(k)

def dfs(parent):                          
    visited[parent] = True
    for child in nodes[parent]:
        if visited[child] != True: # parent의 인접 노드인 child를 방문하지 않았다면 
            result[child] = parent
            dfs(child)

dfs(1)
print(*result[2:], sep="\n")
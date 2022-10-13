
from collections import defaultdict
import sys

sys.setrecursionlimit(1000000)

input = sys.stdin.readline

K = int(input())

def dfs(start, color):
  global res
  if visited[start] ==0:
    visited[start] = color
    for next in graph[start]:
      if visited[next] != 0:
        if visited[next] == visited[start]:
          res = 0
          return #False
      else:
        dfs(next, color*-1)


for _ in range(K):
    V, E = map(int, input().split()) #V는 정점의 개수, E는 간선의 개수

    graph = defaultdict(list) 

    
    visited = {i: 0 for i in range(1,V+1)}  # 방문한 정점 체크

    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    res =1

    for i in range(1, V+1):
      dfs(i, 1)


    if res == 0:
      print("NO")
    else:
      print("YES")
import sys
sys.setrecursionlimit(1000000)
sys.stdin= open("input.txt")
input = sys.stdin.readline

K = int(input())

def dfs(itr):
  for r in graph[itr]: 
    if visited[itr] == False:
      if visited[r] == 1: 
        visited[itr] = 2
      elif visited[r] ==2: 
        visited[itr] = 1
      dfs(r)
    elif (visited[itr] == visited[r]):
      return False 
  return True 

for _ in range(K):
    V, E = map(int, input().split()) 
    graph = [[] for _ in range(V + 1)]  
    visited = [False] * (V + 1)

    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, V+1):
      if visited[i]==False:
          visited[i] = 1
          for itr in graph[i]: 
            result = dfs(itr) 
            if not result:
                break

    if result == False:
      print("NO")
    else:
      print("YES")
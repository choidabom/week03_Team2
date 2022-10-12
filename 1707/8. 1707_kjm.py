# https://www.acmicpc.net/problem/1707
# https://blog.naver.com/ej_0109/222670620333
import sys

sys.setrecursionlimit(1000000)
sys.stdin= open("input.txt")
input = sys.stdin.readline

K = int(input())

def dfs(itr):
  for r in graph[itr]: # r은 3과 인접한 놈들임 itr은 3이고
    if visited[itr] == False:
      if visited[r] == 'red':
        visited[itr] = 'blue'
      else:
        visited[itr] = 'red'
      dfs(r)
    else: 


  # if visited[itr] == False:
  #   if visited[itr] =='red':
  #     visited[itr]='blue'
  #   else:
  #     visited[itr]='red'
  #   for i in graph[itr]:
  #     dfs(i)
  # else:
  #   for i in graph[itr]:
  #     if visited[itr] == visited[i]:
  #       return False
  # return True    

for _ in range(K):
    V, E = map(int, input().split()) #V는 정점의 개수, E는 간선의 개수
    graph = [[] for _ in range(V + 1)]  # 빈 그래프 생성
    visited = [False] * (V + 1)  # 방문한 정점 체크
    # 관계정리 했고
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    # 방명록에 흔적을 남길거임.
    for i in range(1, V+1):
      if visited[i]==False:
          visited[i] = 'red'
          for itr in graph[i]:
            result=dfs(itr) #return값 true/false
            print(result)
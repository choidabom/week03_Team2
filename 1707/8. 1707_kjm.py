# https://www.acmicpc.net/problem/1707
# https://blog.naver.com/ej_0109/222670620333
# 배열로 쓰면 메모리 초과 뜨네?dict로 해야하는 듯?

from collections import defaultdict
import sys

sys.setrecursionlimit(1000000)
sys.stdin= open("input.txt")
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

  # for r in graph[node]: # r은 3과 인접한 1,2 임/ node은 3이고
  #   if visited[node] == False:
  #     # 3이 색이 없으니 칠해야하는데 인접한 곳의 색을 피해서 칠해야해
  #     if visited[r] == 'red': #1 인경우. (이미 빨간색임)
  #       visited[node] = 'blue'
  #     elif visited[r] =='blue': #인접한 곳의 색이 없거나 아님 파란색일수도 있음
  #       visited[node] = 'red'
  #     # elif visited[r]==False:
  #     #   visited[node] ='red' # 인접한 곳에 색이 없으면 걍 red칠해 
  #     dfs(r)
  #   elif (visited[node] == visited[r]): #3이 이미 색이 칠해져있을 수도? 그럼 그 색과 다른 색이 다른지만 비교.
  #     return 1 #잘못 됐으면 1을 반환
  # return 0 #이상 없이 for가 끝났으면 0을 반환


  # for i in graph[node]:
  #     for i in graph[node]:
  #       if visited[i] == 0:  # 색을 안칠했으면 색을 챌해준다.
  #           if visited[node] == 'red':  # 인접 노드의 색을 다르게 칠해준다.
  #               visited[i] = 'blue'
  #           elif visited[node] == 'blue':
  #               visited[i] = 'red'
  #           check = dfs(i)  # i의 인접노드도 확인한다.
  #           if not check:  # i의 인접노드도 확인했는데 색깔이 똑같다면 False를 return
  #               return False
  #       elif visited[node] == visited[i]:  # 인접노드와 색깔이 같다면
  #           return False
  # return True

for _ in range(K):
    V, E = map(int, input().split()) #V는 정점의 개수, E는 간선의 개수

    graph = defaultdict(list) 
    # graph = [[] for _ in range(V + 1)]  # 빈 그래프 생성
    
    visited = {i: 0 for i in range(1,V+1)}  # 방문한 정점 체크
    # print(visited) {1: 0, 2: 0, 3: 0}
    # visited = [False] * (V + 1)  # 방문한 정점 체크

    # 관계정리 했고
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    # print(graph) defaultdict(<class 'list'>, {1: [3], 3: [1, 2], 2: [3]})

    res =1
    # 방명록에 흔적을 남길거임.
    for i in range(1, V+1):
      dfs(i, 1)
      # if visited[i]==False: #어차피 초기상태는 전부 False인데 왜 False인지 확인해?
      #     visited[i] = 'red'
      #     res = dfs(i, 1)
          
          # 이렇게 짜서 메모리 초과 뜸..(그냥 dfs(i)만 보내면 알아서 재귀돌면서 인접한놈들 탐색할텐데) 이터레이팅하고 재귀를 보내서 *n개(itr의 수만큼)로 더 재귀가 돌아버림.
          # for itr in graph[i]: #3
          #   result = dfs(itr) #return값 true/false

    if res == 0:
      print("NO")
    else:
      print("YES")
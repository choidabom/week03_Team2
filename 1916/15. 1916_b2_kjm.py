import queue
import sys
import heapq

input=sys.stdin.readline
INF = int(1e9)  #e??이게 뭐지?

def dijkstra(start, end):
  queue= [] #주머니를 만드네?bfs 원리가 적용되나?
  heapq.heappush(queue, (0, start)) #밑에 while문 돌려면 que에 뭐가 있어야하니 마중물 격으로 1일 때 cost와 시작점(1)넣어줌
  distance[start] = 0 #현재 모든 disctance는 무한으로 설정 되어있는데 1자기 자신까지 가는 데 걸리는 시간은 0이니까 0으로 바꿔줨 

  while queue:
    dist, now= heapq.heappop(queue) #튜플형식으로 저장되어있던 (cost, 시작점)이 cost가 가장 작은 순서로 튀어나옴.(heap은 기본적으로 최소힙이 디폴트임.)
    if distance[now] < dist:
      continue
    for next in graph[now]:
      cost= dist+next[0]
      if cost < distance[next[1]]:
        distance[next[1]] = cost
        heapq.heappush(queue, (cost, next[1]))
  return distance[end]
  

if __name__ == "__main__": #왜 이걸쓰지?
  N = int(input()) #도시의 개수
  M = int(input()) #버스의 개수
  
  graph= [[] for _ in range(N+1)]
  distance = [INF] * (N+1)

  for _ in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append((cost, end)) #cost를 먼저 받았네?
  start, end = map(int, input().split())

  print(dijkstra(start,end))
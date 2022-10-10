import queue
import sys
import heapq

input=sys.stdin.readline
INF = int(1e9)  #e??이게 뭐지?

def dijkstra(start, end):
  queue= [] #주머니를 만드네?
  heapq.heappush(queue, (0, start))
  distance[start] = 0
  

if __name__ == "__main__": #왜 이걸쓰지?
  N = int(input()) #도시의 개수
  M = int(input()) #버스의 개수
  
  graph= [[] for _ in range(N+1)]
  distance = [INF] * (N+1)

  for _ in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append((cost, end))
  start, end = map(int, input().split())

  print(dijkstra(start,end))
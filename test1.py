# https://www.acmicpc.net/problem/2667
# 1. 상하좌우니까 bfs로하고
# 2. 기록지를 하나만들고 1 단지 2단지,,, 숫자가 늘어나게하고
# 3. 마지막에 기록 결과를 배열에 넣고 sort?

#입력
import sys
from collections import deque
# sys.stdin= open("input.txt",'r')
input= sys.stdin.readline

N=int(input())
graph =[ list(map(int, input().strip()))   for _ in range(N)]
numbers = [ [(0) for _ in range(N)]   for _ in range(N)]
visited = [ [(False) for _ in range(N)]   for _ in range(N)]

dr = [1,-1,0,0]
dc = [0,0,-1,1]

que=deque()

def bfs(r, c): #row, col, num
  que.append((r,c))
  while que:
    r,c= que.popleft()
    visited[r][c] = True #방문하면 1
    for i in range(4):
      new_r = r +dr[i] 
      new_c = c +dc[i] 

      if 0 <= new_r < N and 0 <= new_c < N:
        if visited[new_r][new_c] == True: #새로운 좌표를 이미 탐색함?
          pass
        else: 
          if graph[new_r][new_c] == graph[r][c]: #새로운 좌표에 집이 있으면
            numbers[new_r][new_c] = numbers[r][c]
          else: #새로운 좌표에 집이 없으면
            if graph[new_r][new_c] == 0:
              numbers[new_r][new_c] = 0
            else:
              numbers[new_r][new_c] = numbers[r][c] +1
          que.append((new_r, new_c))
  print(numbers)
              
bfs(0,0)
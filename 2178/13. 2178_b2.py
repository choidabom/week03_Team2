# https://www.acmicpc.net/problem/2178
from collections import deque
N,M = map(int, input().split()) #행 N, 열 M

graph= []

for _ in range(N):
  graph.append(list(map(int, input())))
# print(graph) #[[1, 0, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 1], [1, 1, 1, 0, 1, 1]]

def bfs(row,col):  
  dr = [-1,1,0,0]  #이 코드는 for i in range(4)를 돌면서 동서남북으로 한 칸 씩을 의미함
  dc = [0,0,-1,1]

  queue = deque()
  queue.append((row,col))

  while queue:
    row, col = queue.popleft()
    for i in range(4):
      new_row = row + dr[i] #new_xxx은 다음에 갈 칸을 말하는 것.(그냥 row, col은 현재 위치고)
      new_col = col + dc[i]

      #아래 코드의 의미는 로봇청소기처럼 땅으로 꺼져선 안되고 범위 밖으로 나가선 안된다는 소리임.
      if new_row <0 or new_row >= N or new_col<0 or new_col >= M: 
        #등호를 빼면 왜 안되노? 리스트가 범위를 벗어났다? 규성이 말에 따르면 N-1까지의 범위라서 그렇다네
        
        continue
      if graph[new_row][new_col] ==0:
        # 벽을 만나면 안됨 (문제 조건상 0을 만나면 벽인거임..)
        continue #continue쓰면 이 코드만 건너 뛰게됨. break는 탈출
      if graph[new_row][new_col] ==1: #1이어야지만 유일하게 갈 수 있는 칸이 됨.
        graph[new_row][new_col] = graph[row][col]+1 #다음 칸이 갈 수 있는 칸이면 +1을 해서 저장하는거야. https://chanhuiseok.github.io/posts/algo-32/ 이 블로거가 설명하는 것처럼 row, col말고 현재 몇칸까지 왔나를 기록할 가상의 배열 new_row, new_col을 하나 만든다고 생각해도 됨. 
        queue.append((new_row, new_col)) 
        #bfs는 ㄴ처리 끝났다고 그 결과 값가지고 다음 단계 넘어가는게 아니라 ㄷ, ㄹ을 처리하러 가야함. 그래서 일단 주머니에 넣어놓는거임.
        
  return graph[N-1][M-1]


print(bfs(0,0))
from collections import deque
N,M = map(int, input().split()) #행 N, 열 M

graph= []

for _ in range(N):
  graph.append(list(map(int, input())))
# print(graph) #[[1, 0, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 1], [1, 1, 1, 0, 1, 1]]

def bfs(row,col):
  dr = [-1,1,0,0]
  dc = [0,0,-1,1]

  queue = deque()
  queue.append((row,col))

  while queue:
    row, col = queue.popleft()
    for i in range(4):
      new_row = row + dr[i] #new_xxx은 다음에 갈 칸을 말하는 것.(그냥 row, col은 현재 위치고)
      new_col = col + dc[i]

      if new_row <0 or new_row >= N or new_col<0 or new_col >= M: #등호를 빼면 왜 안되노? 리스트가 범위를 벗어났다?
        #로봇청소기처럼 땅으로 꺼져선 안되고 밖으로 나가선 안됨
        #new_row > N 등호가 붙어야하는지 여부?
        continue
      if graph[new_row][new_col] ==0:
        # 벽을 만나면 안됨 (문제 조건상 0을 만나면 벽인거임..)
        continue #continue쓰면 이 코드만 건너 뛰게됨. break는 탈출
      if graph[new_row][new_col] ==1: #1이어야지만 유일하게 갈 수 있는 칸이 됨.
        graph[new_row][new_col] = graph[row][col]+1 #우리는 몇번 전진 
        queue.append((new_row, new_col)) #나중에 볼게..
        
  return graph[N-1][M-1]


print(bfs(0,0))
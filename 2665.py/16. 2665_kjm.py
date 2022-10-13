# https://www.acmicpc.net/problem/2665
#10시 시작
# 상하좌우 봐야하니까 bfs이고, 갈 공간이 없을 때 벽을 부숴야하는데 그때 count가 +1올라가야하고 
# 최소의 개념이 들어가있으니 heap에 담아야하고.
# 방문여부 체크해야하니까 방명록 만들어야하고(False로 빈배열)
# 기록지는 필요 없어보이는데? distance([무한대]로 빈배열)를 체크해야하나? 가는 비용을 최적화 하는건 아니니까 필요 없어보이는데? 

# 입력
import sys
from heapq import heappush, heappop

input = sys.stdin.readline
n = int(input().rstrip())
# matrix = [ input().split() for _ in range(n)]
# print(matrix) #[['11100110'], ['11010010'], ['10011010'], ['11101100'], ['01000111'], ['00110001'], ['11011000'], ['11000111']]

matrix = [ list(map(int, input().strip())) for _ in range(n) ]
# print(matrix)
# [[1, 1, 1, 0, 0, 1, 1, 0], [1, 1, 0, 1, 0, 0, 1, 0], [1, 0, 0, 1, 1, 0, 1, 0], [1, 1, 1, 0, 1, 1, 0, 0], [0, 1, 0, 0, 0, 1, 1, 1], [0, 0, 1, 1, 0, 0, 0, 1], [1, 1, 0, 1, 1, 0, 0, 0], [1, 1, 0, 0, 0, 1, 1, 1]]

visited = [ [False] * (n+1) for _ in range(n) ] #0~n-1까지 n개의 방명록있음

def dijkstra() :
  dr = [-1,1,0,0] #delta row, col의 줄인말
  dc = [0,0,-1,1] 
  heap=[]
  heappush(heap, [0,0,0]) #시작점  [가중치, 시작점, 끝점]
  visited[0][0] = True
  # print(visited)
  while heap:
    count, row, col = heappop(heap)
    # print(count,row,col) 0 0 0

    if row==(n-1) and col ==(n-1): #끝나는 상황 정의(방명록은 n-1까지잇음)
      print(count)
      return

    # 좌표로 상하좌우 봐줘야함.
    for i in range(4):
      new_row = row + dr[i]
      new_col = col + dc[i]
      

      if (0<= new_row < n and 0<= new_col < n) and visited[new_row][new_col]==False:
        visited[new_row][new_col] = True #방명록에 체크하고
        if matrix[new_row][new_col] == False:#다음칸이 막혀있으면?
          heappush(heap, [count+1, new_row, new_col])#카운트를 +1올리고(벽을 부수고), new_row, new_col로 이동하는데, 다른것먼저 봐야하니까 주머니에 넣기)
        else:
          heappush(heap, [count, new_row, new_col]) #다음칸 안 막혀있으면 카운트 올릴 필요없이 전진

    # # 0,0만 볼게 아니니까 for문으로 matrix[0]을 돌아줘야지 (bfs)
    # for col in matrix[row]:
    #   if visited[row][col]

dijkstra()

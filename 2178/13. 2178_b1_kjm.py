# https://www.acmicpc.net/problem/2178
# 2시 시작
# 2시간 정도 넣었는데 안됨. 거의 완성하긴 햇는데 버그를 못잡것다..
# 찾아보니까 너 풀이처럼 재귀(dfs)로도 풀수있는데 그럼 시간초과가 뜬다네?
# bfs로 풀어야한대

# 이 문제 잘 이해하는게 좋은것 같은게 bfs가 dfs를 언제 써야하는지에 대한 대답이 될 문제같아서..


# 의사코드
  # 오른쪽에 0을 만나면 아래로 내려가 / 안만나면 계속 가
  # 디폴트는 오른쪽으로 가는거임.
  # 아래로 내려가는 경우
    # 0을 만나거나 끝에 도달하거나
  # 위로 올라가는 경우
    # 맨 밑엣줄에서 0을 만난 경우는 위로올라가
  # 입력은 2중 for문으로 받고, 한 row씩 배열을 돌다가 0을 만나면 row를 바꾸는대신 시작점은 이전 row에서 마지막에 돌았던 index부터 시작

  # 또는
  # 상단을 막아줘야하는 재귀(커지는 재귀)를 사용해서 a(n-1)까지 돌면 오른쪽과 아래를 봐서 1인곳을 찾아 글로 가게 셋팅(만약 둘다 1이면 오른쪽을 먼저가게 셋팅, 둘다 0인경우는 없음.)

import sys
sys.setrecursionlimit (10**9)
N,M = map(int, sys.stdin.readline().split()) # N(행)*M(열)
count = 0

def path_find(matrix, starting_row, starting_col): #1,1로 넣은걸 0,0으로 조정해줘야함.
  global count
  starting_row = starting_row-1 #0
  starting_col = starting_col-1 #0

  #(matrix) = [[101111], [101010], [101011], [111011]]
  current_val = matrix[starting_row][starting_col] #0,0은 currentval =1
  if starting_row==N-1 and starting_col ==M-1: 
    count +=1
    return count
  else:
    count +=1
    if starting_col < M-1: #index넘버 5에서 +1해버리면 열쪽 범위 넘어버리니까
      right_val = matrix[starting_row][starting_col+1] #0,1은 0
    if starting_row <N-1:
      down_val = matrix[starting_row+1][starting_col] #1,0은 1
    # if starting_row != 0: 
    #   up_val = matrix[starting_row-1][starting_col]
    
    if starting_row != N-1 : #맨 아래가 아닌경우
      if right_val =='1' and down_val == '0': #오른쪽이 1
        path_find(matrix, starting_row, starting_col+1)
      if right_val =='0' and down_val == '1': #아랫쪽이 1
        path_find(matrix, starting_row+1, starting_col)
    else: #맨 아래이면 오른쪽이 1이면 글로 가고 0이면 위로 가고
      if right_val =='1':
        path_find(matrix, starting_row, starting_col+1)
      if right_val =='0':
        path_find(matrix, starting_row-1, starting_col)


# 입력

def main():

  matrix = []
  # matrix = [[] for _ in range(N+1)] #4,6 일때 [[], [], [], [], []]
  # 인덱싱 편하게 하려고 빈 깡통 하나 넣을랬는데 행은 가능해도 열에서 입력은 0101111이렇게 받지 않는이상 열이 구현이 안됨.
  
  for _ in range(N):
      matrix.append(sys.stdin.readline().strip()) #숫자들을 string으로 안받으면 나중에 matrix[0][0]처럼 인덱싱으로 가공할 수 없게됨.. matrix[0][0]은 1이 나와야하는데 숫자는 배열이 아니니까 [0]이 안 먹음..
      # matrix.append(list(map(int, sys.stdin.readline().split())))
  # print(matrix) # ['101111', '101010', ]

  print(path_find(matrix,1,1)) #매트릭스, 시작점 행번호, 시작점 열번호 

main()


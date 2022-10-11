# https://www.acmicpc.net/problem/7569
# 1시에 시작

#3차원 배열입력 받는것부터 빡세보인다?
# 최소 며칠? -> 힙구조?
# 토마토 상태를 기록하는 기록지가 필요하고, 방분 여부를 체크하는 방명록이 필요하고,
# 하나씩 탐색해나가니까 탐색알고리즘인데 그 중에서 상 하 좌 우 앞 뒤 6면을 보니까 bfs가 필요하고

# 일단 토마토가 있는지부터 확인해
#   있으면 방문한 토마토인지 확인해 (방문한적 없으면 in)
#     방문했다고 방명록에 기록하고
#     익었는지 확인해 (안 익었으면 in)
#       기록지에 그 위치 토마토 익었다고 바꾸고
#       그 토마토의 상하좌우앞뒤를 for문으로 돌아
#       익었으면 +1 ...?


import sys
from collections import deque
input = sys.stdin.readline
sys.stdin = open("input.txt","r")
m,n,h = map(int,input().split())


dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

data = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
queue = deque()

#3차원 bfs문제
def bfs():
    while queue:
        # 높이, x,y 순서
        z,x,y = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if -1<nx<n and -1<ny<m and -1<nz<h:
                # 높이, x,y 순서
                if data[nz][nx][ny] == 0: #0은 안 익은 토마토
                    data[nz][nx][ny] = data[z][x][y]+1  #이거 그냥 +1만하면 틀리네? 당연하지 시작점에서 한칸씩 떨어진 친구들은 +1일, 두칸씩 떨어진 친구들은 +2가 되어야하니까 현재 위치까지 오는데 소요일수에다가 +1, 하루해서 다음위치의 날짜를 기록
                    queue.append((nz,nx,ny))
            
for i in range(h):
    for j in range(n):
        for k in range(m):
            # 높이, x,y 순서
            if data[i][j][k] == 1: 
                # 높이, x,y 순서
                queue.append((i,j,k)) #익은 토마토는 주머니에 넣어 놨다가 그 주위에 어느 토마토 감염시키는지 봐야지 
bfs()
# bfs돌리면 결과물 
#  0 -1 3 2 2
# -1 -1 2 1 1
#  4  3 2 1 1
flag = 0
result = -2
for i in range(h):
    for j in range(n):
        for k in range(m):
            # 높이, x,y 순서
            if data[i][j][k] == 0: #data를 bfs로 조회를 끝냈는데 0이 발견 되었다. =>  떨어져있어서 안 익는 토마토가 있다.
                flag = 1  #그냥 바로 -1출력하면 되지 왜 flag에 +1을 더하나?? 나라면 걍 -1바로 출력할 듯
            result = max(result,data[i][j][k]) #0만 없으면 data에서 최대값을 출력하면 되니까. 4가 나오겠네.(0이 없다고 가정하면..)
            # bfs돌리면 결과물에서 max값
            #  0 -1 3 2 2
            # -1 -1 2 1 1
            #  4  3 2 1 1
if flag == 1: 
    print(-1) #flag가 1이라는 소리는 data에서 0이 발견 되었다는 소리 -1을 프린트
elif result == -1:#최댓값을 뽑아라했는데 최댓값이 -1이래 전부다 -1로 되어있다는 소리겠지. = 애당초 다 익은 상태다.
    print(0) 
else:
    print(result-1) #data[nz][nx][ny] = data[z][x][y]+1 할 때 애당초 1부터 시작했기 때문에 날짜가 +1일 부풀려져있음. 따라서 -1
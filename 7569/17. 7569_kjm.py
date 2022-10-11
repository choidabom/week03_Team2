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
# sys.stdin = open("input.txt","r")
input = sys.stdin.readline

m,n,h = map(int,input().split())


dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

data =[[[map(int, input().split())] for _ in range(n) ] for _ in range(h)]

queue = deque()

#3차원 bfs문제
def bfs():
    while queue:
        # 높이, x,y 순서
        z,x,y = queue.popleft()
        for i in range(6): #x,y,z각각이 증가 또는 감소니까 총 6가지 경우 발생 
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if -1<nx<n and -1<ny<m and -1<nz<h:
                # 높이, x,y 순서
                if data[nz][nx][ny] == 0:
                    data[nz][nx][ny] = data[z][x][y]+1
                    queue.append((nz,nx,ny))
            
for i in range(h):
    for j in range(n):
        for k in range(m):
            # 높이, x,y 순서
            if data[i][j][k] == 1:
                # 높이, x,y 순서
                queue.append((i,j,k))
bfs()
flag = 0
result = -2
for i in range(h):
    for j in range(n):
        for k in range(m):
            # 높이, x,y 순서
            if data[i][j][k] == 0:
                flag = 1
                # 높이, x,y 순서
            result = max(result,data[i][j][k])
if flag == 1:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result-1)
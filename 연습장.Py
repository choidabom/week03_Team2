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
                    data[nz][nx][ny] = data[z][x][y]+1  #이거 그냥 +1만하면 틀리네? 왜지?(이게 날짜 카운팅인가?)
                    queue.append((nz,nx,ny))
            
for i in range(h):
    for j in range(n):
        for k in range(m):
            # 높이, x,y 순서
            if data[i][j][k] == 1: 
                # 높이, x,y 순서
                queue.append((i,j,k)) #익은 토마토는 주머니에 넣어 놨다가 그 주위에 어느 토마토 감염시키는지 봐야지 
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
    print(-1) #토마토가 모두 익지는 못하는 상황
elif result == -1:
    print(0) #토마토가 애당초 다 익어있던 상황
else:
    print(result-1)
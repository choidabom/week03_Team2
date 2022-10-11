import sys
from collections import deque
sys.stdin = open("17_input.txt","r")

def solution(q) :
    global raw_tomato
    q = deque(q)
    date = 0
    while q :
        cur = q.popleft()
        for mv in move :
            nextZ = cur[1] + mv[0]
            nextX = cur[2] + mv[1]
            nextY = cur[3] + mv[2]
        
        # 1. 토마토 상자의 범위를 벗어나거나, 
        # 2. 토마토가 없는 칸 이거나, 
        # 3, 이미 익은 토마토가 있는 칸 일 경우 
        # 진행하지 않음

            if check_tomato(nextZ, nextX, nextY) is False :
                continue

            if tomato_box[nextZ][nextX][nextY] == 0:
                raw_tomato -= 1
                date = cur[0] + 1
                tomato_box[nextZ][nextX][nextY] = 1
                q.append((date, nextZ, nextX, nextY))
    return date

def check_tomato(z, r, c):
    global h, m, n
    if z < 0 or z >= h:
        return False
    if r < 0 or r >= n:
        return False
    if c < 0 or c >= m:
        return False
    if tomato_box[z][r][c] < 0 or tomato_box[z][r][c] > 0:
        return False
    return True

move = [[1,0,0],[0,1,0],[0,0,1],[-1,0,0],[0,-1,0],[0,0,-1]]
m, n, h = map(int, sys.stdin.readline().split())
tomato_box = [[[0] * (m) for _ in range(n)] for _ in range(h)]
start = []
raw_tomato = 0
for i in range(h) :
    for j in range(n) :
        tmp = sys.stdin.readline().strip().split()
        for k in range(m) :
            if int(tmp[k]) == 1:
                start.append((0, i, j, k))  # z축, y축, x축 순으로 저장
            elif int(tmp[k]) == 0 :
                raw_tomato += 1
            tomato_box[i][j][k] = int(tmp[k])

ans = solution(start)
if raw_tomato > 0 :
    print('-1')
else :
    print(f'{ans}')
import sys
sys.stdin = open("7569/input.txt","r")
from collections import deque
input = sys.stdin.readline

def solution(queue):
    global raw_tomato
    queue = deque(queue)
    data = 0
    while queue:
        cur = queue.popleft()
        for mv in move:
            nextZ = cur[1] + mv[0]
            nextX = cur[2] + mv[1]
            nextY = cur[3] + mv[2]

            # 1. 토마토 상자의 범위를 벗어나거나,
            # 2. 토마토가 없는 칸이거나,
            # 3. 이미 익은 토마토가 있는 칸일 경우
            # 진행하지 않음
            if check_tomato(nextZ, nextX, nextY) is False:
                continue

            if tomato_box[nextZ][nextX][nextY] == 0:
                raw_tomato -= 1                                 # 익지 않은 토마토 개수 1 감소
                date = cur[0] + 1                               # 마지막으로 갱신된 날짜 = 모든 토마토가 익을 때까지 걸린 날
                tomato_box[nextZ][nextX][nextY] = 1             # 토마토 익히기
                queue.append((cur[0]+1, nextZ, nextX, nextY))   # 익은 토마토는 다른 토마토를 익힐 수 있으므로, append()

    return date

def check_tomato(r, c, z):
    global M, N, H
    if r < 0 or r >= n:
        return False
    if c < 0 or c >= m:
        return False
    if z < 0 or z >= h:
        return False
    if tomato_box[z][r][c] < 0 or tomato_box[z][r][c] > 0:
        return False
    return True
    
move = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [-1, 0, 0], [0, -1, 0], [0, 0, -1]]

# M: 상자 가로/N: 상자 세로/H: 상자 수
M, N, H = map(int, input().split())
# 3차원 배열 만들어주기 ~!
tomato_box = [[[0] * M for _ in range(N)] for i in range(H)]
start = []
raw_tomato = 0
# 3차원 배열에 값 넣어주기
for i in range(H):
    for j in range(N):
        tmp = sys.stdin.readline().split()
        for k in range(M):
            if int(tmp[k]) == 1:
                # 익은 토마토이면 start 배열에 해당 위치의 인덱스 튜플로 넣어주기
                start.append((0, i, j, k))
            elif int(tmp[k]) == 0:
                raw_tomato += 1
            tomato_box[i][j][k] = int(tmp[k])
# print(tomato_box)

answer = solution(start)
if raw_tomato > 0:
    sys.stdout.write('-1')
else:
    sys.stdout.write(f'{answer}')
# 7576: 토마토
# https://www.acmicpc.net/problem/7576
import sys
sys.stdin = open("input.txt","r")
from collections import deque
input = sys.stdin.readline

def bfs():
    # 이동할 네 가지 방향 정의(상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] == 0:
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append([nx, ny])    

# M: 상자의 가로 수, N: 상자의 세로 수
M, N = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
queue = deque([])

for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            queue.append([i, j])

print(matrix)
bfs()
day = 0
for i in matrix:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    day = max(day, max(i))
print(day-1)
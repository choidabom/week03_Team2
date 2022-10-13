# 2667: 단지 번호 붙이기 
import sys
from collections import deque
sys.stdin = open("choidabom/2667/input.txt","r")
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(a, b):
    global cnt
    visited[a][b] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if visited[nx][ny] == 1:
                    
                    cnt += 1
    return cnt                


cnt = 0
q = deque([])
N = int(input().rstrip())
house = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if house[i][j] == 1:
            q.append((i, j))
            dfs(i, j)

print(cnt)
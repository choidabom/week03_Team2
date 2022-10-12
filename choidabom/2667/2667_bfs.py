# 2667: 단지 번호 붙이기
# 집이 있는 곳: 1, 집이 없는 곳: 0
# 연결 요소 개수(단지수) 출력, 각 단지에 속하는 집의 수 오름차순으로 정렬
# BFS
# 그래프의 탐색 시작점을 모르기 때문에 전체를 돌면서 1인 지점에서 탐색을 시작한다.
# 탐색 중 1인 부분을 0으로 바꿔 다시 방문하지 않도록 하고
# 한 번의 BFS가 끝나게 되면 더이상 확장이 불가능하므로 마을 하나가 탄생한다.

import sys
from collections import deque
sys.stdin = open("choidabom/2667/input.txt","r")
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(house, a, b):
    queue = deque()
    queue.append((a, b)) # 집이 있는 곳(1)의 좌표를 queue에 삽입
    house[a][b] = 0 # 탐색 중 1인 부분을 0으로 바꿔 다시 방문하지 않도록 한다.
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and house[nx][ny] == 1:
                house[nx][ny] = 0
                queue.append((nx, ny))
                count += 1  # 집이 있는 곳(1)을 발견할 때 count를 세줌. 
    return count # 결국 while문이 끝나면 집이 몇 곳 있는지 count로 알 수 있다. 

N = int(input().rstrip())
house = [list(map(int, input().rstrip())) for _ in range(N)]
cnt = []
for i in range(N):
    for j in range(N):
        if house[i][j] == 1:
            cnt.append(bfs(house, i, j)) # 집이 있는 곳(1)의 좌표를 i, j로 넣는다.

cnt.sort() # 각 단지에 속하는 집의 수를 오름차순으로 정렬
print(len(cnt)) # cnt 배열 안에 있는 count 변수의 개수, 즉 단지수 출력
for i in range(len(cnt)): 
    print(cnt[i]) # 각 단지에 속하는 집의 수 
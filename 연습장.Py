import sys
from collections import deque
sys.stdin = open("choidabom/2667/input.txt","r")
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b):
    queue = deque()
    queue.append((a, b))
    house[a][b] = 0 # 탐색 중 1인 부분을 0으로 바꿔 다시 방문하지 않도록 한다.
    count = 1 # 탐색을 시작했기 때문에 초기화를 1로 함

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and house[nx][ny] == 1:
                house[nx][ny] = 0 
                queue.append((nx, ny)) 
                count += 1  # 집이 있는 곳(1)을 발견할 때 count를 세줌. 
    return count 

N = int(input().rstrip())
house = [list(map(int, input().rstrip())) for _ in range(N)]
count = [] # visited 겸사 겸사
for i in range(N):
    for j in range(N):
        if house[i][j] == 1: # 집이 있는 곳의 좌표 (i, j)
            count.append(bfs(i, j)) 

count.sort() 
print(len(count)) # cnt 배열 안에 있는 count 변수의 개수, 즉 단지수 출력
for i in range(len(count)): 
    print(count[i])
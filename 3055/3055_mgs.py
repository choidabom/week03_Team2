import sys
from collections import deque
sys.stdin = open("18_input.txt","r")

r, c = map(int, sys.stdin.readline().strip().split())
# print(r, c)

graph = [list(input()) for _ in range(r)]
visited = [[False] * c for _ in range(r)]

sonic = deque() # 고슴도치
water = deque() # 물
cnt = 0 # 시간 카운트

# 방향 설정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 물, 고슴도치 좌표 추가, 방문 True로 설정
for i in range(r) :
    for j in range(c) :
        if graph[i][j] == '*' : # 물
            water.append((i, j))
            visited[i][j] = True
        elif graph[i][j] == 'S' :   # 고슴도치
            sonic.append((i, j))
            visited[i][j] = True
        elif graph[i][j] == 'X' :   # 바위를 만나면 방문표시는 하되, 값이 append 되지 않음
            visited[i][j] = True

while sonic :   # 고슴도치가 있을 때
    for i in range(len(water)) :    # 물의 이동
        w_x, w_y = water.popleft()
        for j in range(4) :
            nx = w_x + dx[j]
            ny = w_y + dy[j]
            if 0 <= nx < r and 0 <= ny < c :
                if graph[nx][ny] == '.' :
                    water.append((nx, ny))
                    graph[nx][ny] = '*'
                    visited[nx][ny] = True
    cnt += 1    # 물이 이동하면 고슴도치가 이동할 수 없으므로 고슴도치 구현보다 먼저 카운트함.

    for _ in range(len(sonic)) :    # 고슴도치 이동
        s_x, s_y = sonic.popleft()
        for i in range(4) :
            nx = s_x + dx[i]
            ny = s_y + dy[i]
            if 0 <= nx < r and 0 <= ny < c :
                if graph[nx][ny] == '.' and visited[nx][ny] == False :
                    sonic.append((nx, ny))
                    visited[nx][ny] = True
                elif graph[nx][ny] == 'D' :
                    print(cnt)
                    exit()
print('KAKTUS')
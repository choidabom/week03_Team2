# 3055: 탈출
# https://sinsomi.tistory.com/entry/%EB%B0%B1%EC%A4%80-Python-3055%EB%B2%88-%ED%83%88%EC%B6%9C-%EC%B4%88%EC%BD%94%EB%8D%94
# deque의 특성인 appendleft를 이용한 코드

import sys
sys.stdin = open("3055/input.txt","r")
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
maps = [list(p for p in input().strip()) for _ in range(R)]
visited = [[0]*C for _ in range(R)]
dx = [1,0,-1,0]
dy = [0,-1,0,1]
queue = deque()

# 물, 고슴도치 위치 queue에 담기
# 굴의 위치는 target에 저장
for i in range(R):
    for j in range(C):
        if maps[i][j] == '*':       # 물이 차있는 지역 => '*'
            queue.append([i, j])
        elif maps[i][j] == "S":     # 고슴도치의 위치 'S'
            queue.appendleft([i, j])# 왼쪽에 입력됨.
        elif maps[i][j] == 'D':     # 비버의 굴 'D'
            target_x = i
            target_y = j

flag = False
# 물과 고슴도치 위치에서 BFS 탐색
while queue:
    # 굴에 도착하고 나면 while문 탈출
    if flag:
        break
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            continue
        
        # 현재 위치가 물이 차있는 지역이면서
        if maps[x][y] == '*':
            # 다음 위치가 비어있는 곳이거나 고슴도치의 위치이면
            if maps[nx][ny] == '.' or maps[nx][ny] == 'S':
                maps[nx][ny] = '*' # 물을 채워준다.
                queue.append([nx, ny]) # 그러고 더 뻗어나갈 수 있기 때문에 queue에 넣어준다.

        # 현재 위치가 도치가 있는 곳이면서
        elif maps[x][y] == 'S':
            # 다음 위치가 비어있는 곳이면
            if maps[nx][ny] == '.':
                maps[nx][ny] = 'S'  # 도치가 이동한다.
                visited[nx][ny] = visited[x][y] + 1
                queue.append([nx, ny])
            elif maps[nx][ny] == 'D':
                flag = True
                visited[nx][ny] = visited[x][y] + 1
                break

# 굴에 도착하지 못하면 visited[굴]이 0이므로
if visited[target_x][target_y] == 0:
    print('KAKTUS')
else:
    print(visited[target_x][target_y])    


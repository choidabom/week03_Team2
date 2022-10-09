# 2178: 미로 탐색
import sys
from collections import deque
sys.stdin = open("2178/input.txt","r")   
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for i in range(n)]
# 1: 이동 가능, 0: 이동 불가능
# dx, dy에 현재 좌표 기준 움질일 예정인 상대좌표값

for i in range(len(graph)):
    print(graph[i])
print() 

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    # queue에 들어가는 값 - 현재 좌표
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            # 다음에 갈 예상 위치(좌우하상 인덱스)
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                # 해당 위치 이동 가능
                queue.append((nx, ny))      
                graph[nx][ny] = graph[x][y] + 1
                for i in range(len(graph)):
                    print(graph[i])
                print()                
                
    return graph[n-1][m-1]

print(bfs(0, 0))
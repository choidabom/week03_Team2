import sys
from collections import deque
sys.stdin = open("7_input.txt","r")

def bfs(x, y) :

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    q.append((x, y))
    while q :
        x, y = q.popleft()
        for i in range(4):  # 현재 위치(x, y)에서 4가지 방향으로 확인
            nx = x + dx[i]  # 상하
            ny = y + dy[i]  # 좌우
            if nx < 0 or nx >=n or ny < 0 or ny >= m:  # 칸이 미로의 벽에 닿는지
                continue    # 위 조건 통과하면 아래로
            if graph[nx][ny] == 0 : # 칸이 0을 밟았는지
                continue # 위 조건 통과하면 아래로
            if graph[nx][ny] == 1:  # 
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
                print(graph)

    return graph[n-1][m-1]  # 마지막 return으로 카운트 값 추출(n*m 행렬의 인덱스임으로 n-1 * m-1이 맞음)

n, m = map(int, sys.stdin.readline().strip().split())
# print(n, m)
graph = []
for i in range(n) :
    graph.append(list(map(int, input())))   # list()로 넣어 각 원소 쪼개기


print(bfs(0,0))
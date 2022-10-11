import sys
from collections import deque
sys.stdin = open("16_input.txt","r")

def bfs() :
    q = deque()
    q.append((0,0))
    graph = [[-1] * n for _ in range(n)]
    graph[0][0] = 0 # 방문하면 0

    while q :
        x, y = q.popleft()
        if x == n-1 and y == n-1 :  # x와 y가 (n-1),(n-1)에 도착하면 종료
            return graph[x][y]

        for k in range(4):  # 방문한 점에서 상하좌우로 이동
            nx = x + dx[k]
            ny = y + dy[k]

            if 0<= nx < n and 0 <= ny < n and graph[nx][ny] == -1 :
                # (1,2)과 (2,1)에서 (2,2)로 가게 되는 경우가 있겠지만,
                # arr가 1인 경우를 먼저 appendleft처리 하기 때문에 먼저 셈이 되고
                # 해당 if문 조건 자체가 graph[nx][ny] 값이 -1이 아니라면 들어오지 않기 때문에 생각하지 않아도 됨
                if arr[nx][ny] == 1:
                    q.appendleft((nx, ny))  
                    graph[nx][ny] = graph[x][y]

                else :
                    q.append((nx, ny))
                    graph[nx][ny] = graph[x][y] + 1


n = int(input())
# print(n)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

arr = []
for i in range(n) :
    arr.append(list(map(int, sys.stdin.readline().strip())))

print(bfs())

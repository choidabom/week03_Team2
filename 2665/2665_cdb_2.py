# 2665: 미로 만들기

import sys
sys.stdin = open("2665/input.txt","r")
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
maze = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[0] * n for _ in range(n)] # 방문 체크할 리스트

def dijkstra():
    # 상하좌우
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    heap = []
    heappush(heap, [0, 0, 0])
    visited[0][0] = True

    while heap:
        cnt, x, y = heappop(heap)
        if x == n-1 and y == n-1:
            print(cnt)
            return

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 0: 검은 방, 1: 흰 방
            # nx, ny가 범위 안에 있으며, 방문하지 않은 곳일 때
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:    
                # 검은 방인 경우 흰 방으로 바꾼다.
                if maze[nx][ny] == 0:
                    heappush(heap, [cnt+1, nx, ny])
                else:
                    heappush(heap, [cnt, nx, ny])
                visited[nx][ny] = True


dijkstra()
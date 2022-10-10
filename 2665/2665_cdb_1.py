# 2665: 미로 만들기 (1261: 알고스팟과 같은 문제)
# 다익스트라 알고리즘 + heap
# 벽을 깨면서 cnt를 늘려나가는 방식으로 bfs를 한 번만 해도 동작 가능 

import sys
from heapq import heappush, heappop
sys.stdin = open("2665/input.txt","r")

input = sys.stdin.readline
n = int(input())
maze = [list(map(int, input().rstrip())) for i in range(n)]
visited = [[False] * n for _ in range(n)] # 방문 체크할 리스트

def dijkstra(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    heap = []
    heappush(heap, (0, x, y))

    while heap:
        cnt, curr_x, curr_y = heappop(heap)
        if curr_x == n-1 and curr_y == n-1: # 끝방 도달 결과값 리턴
            return cnt

        for i in range(4):
            # 다음에 갈 예상 위치
            next_x = curr_x + dx[i]
            next_y = curr_y + dy[i]

            if  0 <= next_x < n and 0 <= next_y < n and visited[next_x][next_y] == 0:
                
                # 검은 방인 경우 흰 방으로 바꾼다.
                if maze[next_x][next_y] == 0:
                    heappush(heap, (cnt+1, next_x, next_y))
                else:
                    heappush(heap, (cnt, next_x, next_y))
                visited[next_x][next_y] = True

print(dijkstra(0, 0))



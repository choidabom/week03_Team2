# https://www.acmicpc.net/problem/3055
# https://chldkato.tistory.com/22
 
# 이렇게 짜면 water한번하고 비버한번 가고 티키타카 없이
# 물먼저 전부 bfs해버리고, 그다음 비버가 가려하니까 
# 높은 확률로 비버는 집에 못감.. 
# 티키타카를 구현 못했음. (실패)

import sys
from collections import deque
sys.stdin = open("input.txt","r")

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def bfs():
    while bear_que:
        bear_r,bear_c = bear_que.popleft()
        for i in range(4):
            new_bear_r = bear_r + dx[i]
            new_bear_c = bear_c + dy[i]
            if 0<= new_bear_r < R and 0<= new_bear_c < C:
                if graph[new_bear_r][new_bear_c] == '.' and visited[new_bear_r][new_bear_c] ==0:
                    visited[new_bear_r][new_bear_c] = visited[bear_r][bear_c] + 1 #토마토때랑 똑같다!! (인접한곳으로 이동하면 +1씩 늘려서 방명록에 기록하는거임)
                    bear_que.append([new_bear_r, new_bear_c])
                elif graph[new_bear_r][new_bear_c] == 'D':
                    print(visited[bear_r][bear_c])
                    return
        water()
    print("KAKTUS")
    return
    
def water():
    while water_que:
        water_r, water_c =water_que.popleft()
        for i in range(4):
            new_water_r = water_r + dx[i]
            new_water_c = water_c + dy[i]

            if 0 <= new_water_r < R and 0 <= new_water_c < C :
                if graph[new_water_r][new_water_c] == '.':
                    graph[new_water_r][new_water_c] = '*'
                    water_que.append([new_water_r, new_water_c])

R, C = map(int, input().split())
graph = [list(map(str, input())) for _ in range(R)] 
#[['D', '.', '*'], ['.', '.', '.'], ['.', 'S', '.']]

visited = [[0]*C for _ in range(R)]
bear_que, water_que = deque(), deque()

for r in range(R):
    for c in range(C):
        if graph[r][c] == 'S':
            visited[r][c] =1
            bear_que.append([r, c])
            graph[r][c] =='.' #이거 왜해?
        elif graph[r][c] == '*':
            water_que.append([r,c])
water()
bfs()

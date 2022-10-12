# https://www.acmicpc.net/problem/3055
# https://chldkato.tistory.com/22
 

# 티키타카를 구현하자!

import sys
from collections import deque
# sys.stdin = open("input.txt","r")

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def bfs(r,c):
    visited[r][c]=1
    bear_que.append([r,c])
    while bear_que:
        bearq_len =len(bear_que) #water에서 왜 len 길이가 등장하는지 설명
        while bearq_len:
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
            bearq_len -=1 #4방향 다 조회했으면 1코인 빠지는거임. 
        water() #그러다가 0코인이 되면 water차례임 ()
        #근데 이거 의아했던게 분명 bear_que에는 인자들이 여러개 남아있었는데 bearq_len는 0이라고 해서 while문이 끝나고 water가 실행된단말이야?
        #그 이유는 이번 턴에 조사해야하는 것들은 다 조사해서 len는 0인데 이번턴 대상들 조사하면서 그 대상들이 또 다음턴에 조사할 것들을 que에 넣어놨을거아님?
        # 그것들이 que에 남아있는거임. 이것들은 이번턴 대상이 아님. 왜냐 비버는 이번 턴 다 써서 다음 물이 차오를 차례거든

    print("KAKTUS") #모든 네모들을 다 조회했는데도 'D'를 만나지 못했으면 비버는 굴로 이동할 수 없는 거임.
    return
    
def water():
    w_len=len(water_que) #이 길이로 표현하는 것 때문에 턴제가 가능한데..밑에 w_len -= 1 에서 추가 설명
    while w_len:
        water_r, water_c =water_que.popleft()
        for i in range(4):
            new_water_r = water_r + dx[i]
            new_water_c = water_c + dy[i]

            if 0 <= new_water_r < R and 0 <= new_water_c < C :
                if graph[new_water_r][new_water_c] == '.':
                    graph[new_water_r][new_water_c] = '*'
                    water_que.append([new_water_r, new_water_c])
        w_len -= 1 #for 문으로 사방을 조회하면 코인을 1 빼는거야. (코인은 큐에 들어있는 숫자만큼 생김 1,1과 인접한게 2개이면 2코인이 들어있음.)
                   # 코인이 떨어지면 water()가 끝나고 bfs()차례로 넘어감(=고슴도치 차례)

R, C = map(int, input().split())
graph = [list(map(str, input())) for _ in range(R)] 
#[['D', '.', '*'], ['.', '.', '.'], ['.', 'S', '.']]

visited = [[0]*C for _ in range(R)]
bear_que, water_que = deque(), deque()

for r in range(R):
    for c in range(C):
        if graph[r][c] == 'S':
            bear_r, bear_c = r,c
            # graph[r][c] =='.' #이거 왜해? #없어도 되네
        elif graph[r][c] == '*':
            water_que.append([r,c])
water()
bfs(bear_r,bear_c)

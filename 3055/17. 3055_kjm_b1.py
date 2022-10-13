# https://www.acmicpc.net/problem/3055
# 구현하다가 포기

# 인풋받는게 좀 특이했음
# graph[i]=input().strip() 하면 알아서 세자리에 맞춰 들어감.

# 고슴도치도 인접한 4곳을 탐색(BFS)
# 물도 인접한 4곳을 탐색
# 토마토랑 비슷하게 못가는 곳이 있네? 
# 방명록 필요함.

# 방명록에 돌의 위치와 고슴도치 위치, 물의 위치를 True로 표시하고,
# 돌, 고슴도치, 물 각각의 위치값을 따로 변수에 기록하고 물과, 고슴도차 좌표를 가지고 각각 bfs시작
# 물이 한턴 상하좌우 탐색하고 그다음 고슴도치 한턴 탐색.(True로 해놓은 곳은 안가도록)
import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline
R, C = map(int, input().split()) 

def bfs():
    dr = [-1,1, 0,0]
    dc = [0,0,-1,1]
    


graph = [[0] * C for _ in range(R)]
for i in range(R):
    graph[i]=(input().strip())
# ['D.*', '...', '.S.']

visit = [[False]*C for _ in range(R)] #[[False, False, False], [False, False, False], [False, False, False]]

warter_position=[]
for r in range(R):
    for c in range(C):
        if graph[r][c] == 'D': #곰
            visit[r][c] = True
            bear_r, bear_c = r,c
        if graph[r][c] == '*': #물
            visit[r][c] = True
            warter_position.append([r,c])
        if graph[r][c] =='X':
            visit[r][c] = True
        if graph[r][c] == 'S':
            visit[r][c] = 'destination'
print(warter_position)
bfs()

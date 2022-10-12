# 2667: 단지 번호 붙이기
# 집이 있는 곳: 1, 집이 없는 곳: 0
# 연결 요소 개수(단지수) 출력, 각 단지에 속하는 집의 수 오름차순으로 정렬
# DFS
# 그래프의 탐색 시작점을 모르기 때문에 전체를 돌면서 1인 지점에서 탐색을 시작한다.
# 큐 대신 재귀를 썼다.

import sys
sys.stdin = open("choidabom/2667/input.txt","r")
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    if 0 <= x < N and 0 <= y < N  and house[x][y] == 1:
        global count 
        count += 1  # 집의 갯수가 몇 개인지 count인데 global로 선언해줘서 밖에서도 알 수 있음
        house[x][y] = 0 # 탐색 중 1인 부분을 0으로 바꿔 다시 방문하지 않도록 한다.
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False    

N = int(input().rstrip())
house  = [list(map(int, input().rstrip())) for _ in range(N)] # 총 단지를 나타내는 2차원 배열

count = 0
danji_cnt = 0
cnt = []
for i in range(N):
    for j in range(N):
        if dfs(i, j) == True:
            cnt.append(count)
            danji_cnt += 1
            count = 0 # 다시 count를 초기화해줘야지 다음 단지의 집의 갯수가 몇 개인지 알 수 있다.

print(danji_cnt)
cnt.sort()
for i in range(len(cnt)):
    print(cnt[i])
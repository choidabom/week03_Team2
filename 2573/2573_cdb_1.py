# 2573: 빙산 
# 동서남북에 붙어있는 0의 개수만큼 빙산이 줄어듬.
# 빙산이 줄어들면서 덩어리로 분리되는데
# 두 덩어리 이상으로 분리되는 최초의 시간을 구함

# so, 해야할 작업 두 가지
# 1. 빙산 덩어리 개수 판단
# 2. 동서남북 0의 개수 세서 빙산 줄어들게 하기


# 파이썬: 시간초과, 파이파이: 메모리 초과
import sys
sys.stdin = open("2573/input.txt","r")
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

# 빙산이 둘 이상으로 나누어졌는지 탐색하는 함수
def dfs(x, y):
    if 0 <= x < N and 0 <= y < M:
        if ice[x][y] > 0:
            ice[x][y] = 0
            dfs(x, y-1)
            dfs(x, y+1)
            dfs(x+1, y)
            dfs(x-1, y)
            return True
    return False

# 상하좌우를 살필 좌표
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0] 
year = 0

N, M = map(int, input().split())
# 빙산 정보 리스트 
ice = [list(map(int, input().rstrip().split())) for i in range(N)] 
# 한 번 녹은 빙산을 잠시 저장시켜줄 리스트
new = [[0 for _ in range(M)] for _ in range(N)]

while True:
    no = 0
    for i in range(N):
        for j in range(M):
            if ice[i][j] > 0: # 빙산이라면 
                cnt = 0
                for k in range(4): # 상하좌우에 얼음이 있는지 몇 개인지 파악
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if 0 <= nx < M and 0 <= ny < N and ice[nx][ny] == 0:
                        cnt += 1 # 바닷물이라면 카운트 올려줌
                
                # 이제 현재 빙산을 녹여준다.
                # 
                if ice[i][j] - cnt >= 0:
                    new[i][j] = ice[i][j] - cnt
                else:
                    new[i][j] = 0
            else: # 바닷물이라면
                no += 1 # no 카운트 올려주고
    # 전부 바닷물이라면 0 출력 후 종료
    if no == N*M:
        print(0)
        break
    result = 0
    for i in range(N):
        for j in range(M):
            if dfs(i, j) == True:
                result += 1
    if result >= 2:
        print(year)
        break
    year += 1

    # 빙산 정보 업데이트
    ice = new
    new = [[0 for _ in range(M)] for _ in range(N)]


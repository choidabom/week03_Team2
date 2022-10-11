import sys
sys.stdin = open("11_input.txt","r")
sys.setrecursionlimit(10**4)

def dfs(x, y) :
    if x <= -1 or y <= -1 or x >= n or y >= m :
        return False
    if iceberg_list[x][y] > 0 : # 바닷물이 아닌 빙산
        iceberg_list[x][y] = 0 # 방문처리
        dfs(x, y-1)
        dfs(x, y+1)
        dfs(x+1, y)
        dfs(x-1, y)
        return True
    return False

n, m = map(int, sys.stdin.readline().strip().split())
iceberg_list = []
for _ in range(n) :
    iceberg_list.append(list(map(int, sys.stdin.readline().strip().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 녹은 빙산을 저장해줄 리스트
visited = [[0 for _ in range(m)] for _ in range(n)]




year = 0

while True:
    no = 0
    for i in range(n) :
        for j in range(m) :
            if iceberg_list[i][j] > 0 :
                cnt = 0
                for k in range(4) :
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if nx <= -1 or ny <= -1 or nx >= n or ny >= m :
                        continue
                    if iceberg_list[nx][ny] == 0 :  # 바닷물이라면 카운트 +1
                        cnt += 1
                if iceberg_list[i][j] - cnt >= 0 :
                    visited[i][j] = iceberg_list[i][j] - cnt
                else :
                    visited[i][j] = 0
            else :
                no += 1
    if no == n * m :
        print(0)
        break
    res = 0
    for i in range(n) :
        for j in range(m) :
            if dfs(i, j) == True :
                res += 1
    if res >= 2:
        print(year)
        break
    year += 1

    iceberg_list = visited
    visited = [[0 for _ in range(m)] for _ in range(n)]
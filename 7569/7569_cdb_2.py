# 7569: 토마토
# 문제에서 '최소일수', '주변의 토마토들을 익힘'을 보자마자 bfs 느낌 뽝 와야함
# 깊이 들어갈 일이 없기 때문에 dfs 쓰면 안 됨

# bfs 특 queue 사용하기 
# deque 모듈 안 쓰면 시간복잡도 박살남(pop(0)이 시간복잡도가 O(N)이고 popleft()가 O(1)이라고 함)
from collections import deque
import sys
sys.stdin = open("7569/input.txt","r")
input = sys.stdin.readline

m, n, h = map(int, input().split())
graph = []
queue = deque([])

for i in range(h):
    tmp = []
    for j in range(n):
        tmp.append(list(map(int,sys.stdin.readline().split())))
        for k in range(m):
            if tmp[j][k]==1:
                queue.append([i,j,k])
    graph.append(tmp)

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

# bfs 함수, 한 번 들어가면 다 돌고 나오니까 재귀할 필요 없음
def bfs():
    global m, n, h
    while queue:
        x, y, z = queue.popleft()

        for i in range(6):
            a = x + dx[i]
            b = y + dy[i]
            c = z + dz[i]
            # 해당 좌표가 좌표 크기를 넘어가면 안 되고, 그 좌표에 토마토가 익지 않은채로 있어야 함.(0)
            if 0 <= a < h and 0 <= b < n and 0 <= c < m and graph[a][b][c] == 0:
                # 익히고 1을 더해주면서 횟수를 세어주기
                # 여기서 나온 제일 큰 값이 정답이 될 것이다.
                queue.append([a, b, c])
                graph[a][b][c] = graph[x][y][z] + 1
bfs()
day = 0
for i in graph:
    for j in i:
        for k in j:
            # 다 찾아봤는데 토마토를 익히지 못 했다면 -1 출력
            if k == 0:
                print(-1)
                exit(0)
        # 다 익혔다면 최댓값이 정답
        day = max(day, max(j))
    # 처음 시작을 1로 표현했으니 1을 빼준다.
print(day -1)
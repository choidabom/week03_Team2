# 2573: 빙산
'''
풀이)
1. 각 빙산이 녹는 동작
2. 빙산이 녹은 후 두 개로 분리되었는지 찾는 동작

1. N*M만큼 빙산 배열을 순회하며 해당 좌표가 0이 아닌 값일 경우 주변의 0인 값들의 개수를 찾아서 그만큼 빼준다.
이 때, 이전 실행의 결과가 다음 실행에 영향을 미칠 수 있으므로 독립시행을 보장하기 위해 새로운 배열을 만들어서 N*M탐색이 끝난 후 덧씌워준다.
2. 빙산이 녹은 후 BFS를 동작한다. 이 때, BFS 동작 횟수를 카운트하며 이미 BFS가 동작했다면 정답을 출력하고 (빙산이 2개 이상 나눠진 경우이므로) 0번 실행인 경우 빙산이 모두 녹은 것이므로 0을 출력한다. 만약 1회만 실행된다면 1번 동작부터 반복한다.
'''
import sys
from collections import deque
sys.stdin = open("2573/input.txt","r")
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def melting():
    new_board = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if ice[i][j] == 0:
                continue
            cnt = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
    
    queue = deque([[a, b]])
    visited[a][b] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and  0 <= ny < N and not visited[nx][ny]:
                # 빙산이라면 큐에 추가
                if ice[nx][ny] != 0:
                    visited[nx][ny] = True
                    queue.append([nx, ny])

                # 빙산이 아니라면 바닷물로 카운트
                else:
                    cnt[x][y] += 1
    return 1

N, M = map(int, input().split())
ice = [list(map(int, input().split())) for i in range(N)]
year = 0


# 모든 얼음이 녹을 때까지 반복한다.
while True:
    answer = []
    visited = [[False] * M for _ in range(N)] # 방문 체크 리스트
    cnt = [[0] * M for _ in range(N)]

    # 빙산과 접촉되어 있는 바닷물 확인
    for i in range(N):
        for j in range(M):
            if ice[i][j] != 0 and not visited[i][j]:
                answer.append(bfs(i, j))
    
    # 빙산을 깎아줌
    for i in range(N):
        for j in range(M):
            ice[i][j] -= cnt[i][j]
            if ice[i][j] < 0 :
                ice[i][j] = 0
    
    if len(answer) == 0 or len(answer) >= 2:
        break

    year += 1

print(year) if len(answer) >= 2 else print(0)
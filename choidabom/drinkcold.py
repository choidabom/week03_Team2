import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline
from collections import deque

# DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

# N, M을 공백을 기준으로 구분하여 입력 받기
N, M = map(int, input().split())
# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(N):
    graph.append(list(map(int, input().rstrip())))
print(graph)

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(N):
    for j in range(M):
        # 현재 위치에서 DFS 수행
        # 특정 지점에서 DFS와 BFS를 수행해서 이동가능한 모든 경로에 대해서 방문처리를 하도록 처리할 수 있다.
        if dfs(i, j) == True:
            result += 1
print(result)
# for문에서 호출된 dfs가 True를 리턴할 때에만 result가 +1이 된다. 재귀함수 내에서 발생한 False나 True는 무시된다.

# 입력
# 4 5
# 00110
# 00011
# 11111
# 00000

# 출력
# 3


# 음료수 얼려 먹기 문제에서 0,0에서부터 n-1,m-1 까지 각 지점에서 dfs를 수행하기 때문에 dfs(x-1, y) 나 dfs(x, y-1)는 굳이 호출하지 않아도 될 것 같아서 저는 전진하는 방향으로만 dfs를 수행했는데, 혹시 호출하지 않았을 때 문제가 있는 예제가 있을까요?

# 갈고리나 십자 모양일 때 문제가 생길 것 같아요, 예를 들자면
# 11101    11011
# 10101    10001
# 10001    11011
# 11111    11111
# 이런 경우요
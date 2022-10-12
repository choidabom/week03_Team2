# # DFS
# # 각 노드가 연결된 정보를 표현 (2차원 리스트)
# graph = [
#     [],
#     [2, 3, 8],
#     [1, 7],
#     [1, 4, 5],
#     [3, 5], 
#     [3, 4],
#     [7],
#     [2, 6, 8],
#     [1, 7]
# ]

# # 각 노드가 방문된 정보를 표현 (1차원 리스트)
# visited = [False] * 9

# # DFS 메서드 정의 
# def dfs(start):
#     # 현재 노드를 방문 처리
#     visited[start] = True
#     print(start, end=" ")
#     for node in graph[start]:
#         if not visited[node]:
#             dfs(node)

# # 정의된 DFS 함수 호출
# # 실행 결과: 1 2 7 6 8 3 4 5 
# dfs(1) 


# BFS
from collections import deque
# 각 노드가 연결된 정보를 표현 (2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5], 
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9

# BFS 메서드 정의
def bfs(start):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft()
        print(v, end=" ")
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for node in graph[v]:
            if not visited[node]:
                visited[node] = True
                queue.append(node)

# 정의된 BFS 함수 호출
# 실행 결과: 1 2 3 8 7 4 5 6
bfs(1) 
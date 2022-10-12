# 24479: 알고리즘 수업 - 깊이 우선 탐색 1
# https://aigong.tistory.com/469
# N개의 정점과 M개의 간선으로 구성된 무방향 그래프(undirected graph)
# 출력 => i번째 줄에는 정점 i의 방문 순서를 출력함. 시작 정점의 방문 순서는 1이다. 시작 정점에서 방문할 수 없는 경우 0을 출력한다. 
# 결론: 출력은 visited에 몇 번째로 출력되는지 출력하는 것!
# 출력되는 순서대로 출력하는 것이 아니라 몇 번째로 출력되는지!
# pypy 성공/python 시간초과

import sys
sys.stdin = open("choidabom/24479/input.txt","r")
sys.setrecursionlimit(10**5)

def dfs(start):
    global cnt
    # dfs 할 때마다 visited에 cnt값 부여하기 + dfs 실행 후에는 cnt값 1 증가해서 순차적으로 값 부여하기
    visited[start] = cnt # 방문할 때마다 순차 값 변경
    graph[start].sort() # 그래프 간선에 따른 graph를 오름차순으로 변경해준다. 
    for node in graph[start]: # 연결된 노드 방문
        if not visited[node]: # 방문 안 한 노드일 경우
            cnt += 1 # 순차 증가
            dfs(node) # dfs 실행

# N: 정점의 수, M: 간선의 수, R: 시작 정점
N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
# 방문 순서 그래프 
visited = [0] * (N+1)

for i in range(M): # 정점 u와 정점 v의 가중치가 1인 양방향 간선
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 1
dfs(R)
# 방문할 수 없는 경우 0을 출력하기 때문에 visited의 초기값을 0으로 잡아주었다. 
for i in range(N+1):
    if i != 0:
        print(visited[i])
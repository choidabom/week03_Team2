# 1916: 최소비용 구하기

import sys
sys.stdin = open("1916/input.txt","r")
input = sys.stdin.readline
from collections import deque, defaultdict
INF = int(1e9)

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0 # 현재 가장 짧은 거리를 갖는 노드의 인덱스를 저장
    for i in range(1, N+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start, end):
    distance[start] = 0 # 시작 노드에 대해서 초기화 
    visited[start] = True
    
    for v in graph[start]: # 출발 노드 graph[start]로부터 인접 노드 
        distance[v[0]] = v[1]

    # 시작 노드를 제외한 전체 N-1개의 노드에 대해 반복
    for i in range(N-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
    print(cost)

N = int(input().rstrip())   # 도시의 개수
M = int(input().rstrip())   # 버스의 개수
graph = defaultdict(list)

visited = [False] * (N+1)   # 방문정보
distance = [INF] * (N+1)    # 최단거리테이블

for i in range(M):
    x, y, z = map(int, input().split()) # x: 출발 도시 번호, y: 도착 도시 번호, z: 버스 비용
    graph[x].append((y, z))             # x에서부터 y까지 가는 거리가 z이다.

start, end = map(int, input().split())  # 출발 도시 번호/도착 도시 번호

# print(graph)
# print(start, end)
# print(distance)

dijkstra(start, end)

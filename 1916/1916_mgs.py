import sys
import heapq
sys.stdin = open("15_input.txt","r")

# 데이크스트라 알고리즘(최단경로 탐색 알고리즘)
# 하나의 정점에서 모든 정점으로 가는 최단 경로를 알려줌(음의 간선이 존재하면 안됨)
# 현재까지 알고 있던 최단 경로를 계속해서 갱신하는 것

# 1. 출발 노드 설정
# 2. 출발 노드를 기준으로 각 노드의 최소 비용을 저장
# 3. 방문하지 않은 노드 중에서 가장 비용이 적은 노드 선택
# 4. 해당 노드를 거쳐 특정 노드로 가는 경우를 고려해 최소 비용을 갱신
# 5. 3~4번 과정을 계속 반복

def dijkstra(start_point) :
    graph_point[start_point] = 0
    heap = []
    heapq.heappush(heap, [0, start_point])
    while heap :
        cur_wage, cur_end = heapq.heappop(heap) # 첫 start_point에서 출발하여 2번째 도착점들 중 가장 비용이 낮은 곳에서 시작
        print(graph_point)
        if graph_point[cur_end] < cur_wage :    # 저장되어 있는 값이 현재값보다 더 적다면, 굳이 다시 체크할 필요가 없음.
            continue
        for new_node, new_wage in graph[cur_end] :  # for문을 돌면서 첫 start_point에서 갈 수 있는 모든 곳을 찍고 wage를 저장해놓고 탈출
            wage = cur_wage + new_wage
            print(graph_point)
            if graph_point[new_node] > wage :   # print찍어보면 알겠지만, 처음에 1에서 5를 갈 때는 비용이 10이었으나 1에서 4를 찍고 5를 가니 비용이 4로 줄기 때문에 10 대신 4를 저장
                graph_point[new_node] = wage
                print(graph_point)
                heapq.heappush(heap, [wage, new_node])

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
graph_point = [float('inf') for _ in range(n+1)]


for _ in range(m) :
    start, end, wage = map(int, sys.stdin.readline().strip().split())
    graph[start].append([end, wage])
# print(graph)

start_point, end_point = map(int,sys.stdin.readline().strip().split())
# print(start_point, end_point)

dijkstra(start_point)

# print(graph_point)
print(graph_point[end_point])



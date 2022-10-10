# 1916: 최소비용 구하기

import sys
from heapq import heappush, heappop
sys.stdin = open("1916/input.txt","r")
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start, end):
    queue = []
    # 시작 노드로 가기 위한 최단 거리는 0으로 설정하여,큐에 삽입
    heappush(queue, (0, start)) # 시작지점 힙에 추가
    distance[start] = 0 # 시작 지점 0으로 초기화
    
    while queue:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heappop(queue)
        
        # 이미 방문한 적 있는 도시이면 무시
        if distance[now] < dist:
            continue

        # 인접 노드 확인
        for next in graph[now]:
            # cost 계산: 현재 node의 누적 거리 + 현재 노드에서 다음 노드까지의 거리
            cost = dist + next[0]
            # cost가 distance에 저장된 값보다 작으면 갱신
            if cost < distance[next[1]]:
                distance[next[1]] = cost
                heappush(queue, (cost, next[1]))
    return distance[end]


if __name__ == "__main__":
    N = int(input())    # 도시의 개수
    M = int(input())    # 버스의 개수
    graph = [[] for _ in range(N+1)]
    distance = [INF] * (N+1)

    for _ in range(M):
        # 출발지, 도착지, 비용
        start, end, cost = map(int, input().split())
        graph[start].append((cost, end))
    # 찾고자하는 비용 경로(출발지, 도착지)
    start, end = map(int, input().split())

    print(dijkstra(start, end))

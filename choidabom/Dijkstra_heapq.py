import sys, heapq
sys.stdin = open("input.txt","r")
input = sys.stdin.readline
INF = int(1e9)  # 무한을 의미하는 값을 10억을 설정

def dijkstra(start):
    queue = []
    # 시작 노드로 가기 위한 최단 거리는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while queue: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(queue)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
# 0번은 취급하지 않기 위해 n+1 길이만큼 생성
graph = [[] for _ in range(n+1)] 

visited = [False] * (N+1)   # 방문정보: 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
distance = [INF] * (N+1)    # 최단거리테이블: 모두 무한으로 초기화

# 모든 간선 정보를 입력받기
for _ in range(n):
    a, b, c = map(int, input().split())
    graph[a].append((b, c)) # a에서부터 b까지 가는 거리가 c다.


# 다익스트라 알고리즘을 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우, 무한이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우, 거리를 출력
    else:
        print(distance[i])
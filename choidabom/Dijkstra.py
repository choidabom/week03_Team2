import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline
INF = int(1e9)  # 무한을 의미하는 값을 10억을 설정

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

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0 # 현재 가장 짧은거리를 갖는 노드의 인덱스를 저장
    # 1번 노드부터 n번 노드까지 모든 원소를 확인(순차 탐색)
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True

    # 출발 노드로부터 인접한 노드 
    for v in graph[start]:
        distance[v[0]] = v[1] # 시작노드와 인접한 노드들의 거리 갱신

    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]: # now번째 인덱스 노드와 연결된 노드와 거리
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

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
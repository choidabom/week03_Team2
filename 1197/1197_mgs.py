import sys
import heapq
sys.stdin = open("3_input.txt","r")

# 스패닝 트리 : 최소 연결 부분 그래프. 간선의 수가 가장 적은 걸 의미함. 
# 최소 스패닝 트리 : 간선의 수가 가장 적음과 동시에 최소 비용
    # 예시) 도시들을 모두 연결 할 때 도로의 길이가 최소가 되도록, 전화선 길이가 최소가 되도록 전화 케이블 망 구성

# Prim알고리즘, Kruskal알고리즘 두 가지가 존재함.


# Prim 알고리즘 풀이(가중치 최소 선택)

v, e = map(int, input().split())
# print(v, e)

visited = [False] * (v+1)   
line_list = [[] for _ in range(v+1)]    # v+1을 줘야 end값을 넣을 때 list range오류가 안 나옴
for _ in range(e) :
    start, end, wage = map(int, sys.stdin.readline().rstrip().split())
    line_list[start].append([wage, end])    # end나 start가 먼저가 아닌 이유는 wage별로 정렬하여 최소 가중치 선택하기 위해
    line_list[end].append([wage, start])
# print(line_list)
ans = 0
cnt = 0
heap = [[0, 1]] # 비용0, 출발점 1을 주고 시작
while heap :    # 현재 그래프에서 가장 짧은 간선을 고르기.
    if cnt == v :   # 모든 점을 방문했을 때
        break
    wage, start = heapq.heappop(heap)
    if not visited[start] :
        visited[start] = True   # 1번 선택 이후, wage값 순으로 정렬되기 때문에 2,3 중에서 wage가 더 작은 곳을 선택
        ans += wage
        cnt += 1
        for line in line_list[start] :
            heapq.heappush(heap, line)

print(ans)
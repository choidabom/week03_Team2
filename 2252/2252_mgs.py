import sys
from collections import deque
sys.stdin = open("20_input.txt","r")

#https://freedeveloper.tistory.com/390 위상정렬
"""
위상정렬 : 방향성에 거스르지 않도록 순서대로 나열(위상정렬은 순환하지않는 방향 그래프만 가능)
진입차수(inDegree) : 특정 노드로 들어오는 간선의 개수
진출차수(outDegree) : 특정 노드에서 나가는 간선의 개수

위상정렬 알고리즘
1. 진입차수가 0인 모든 노드를 큐에 넣기
2. while q : (1)원소를 꺼내 나가는 간선을 그래프에서 지우기 (2)진입차수가 0이 된 노드를 큐에 넣기
3. 각 노드가 큐에 들어온 순서가 위상정렬 결과
""" 

n, m = map(int, sys.stdin.readline().rstrip().split())
# print(n, m)
height_list = [[] for _ in range(n+1)]
inDegree = [0 for _ in range(n+1)]  # 진입차수
for _ in range(m) :
    start, end = map(int, sys.stdin.readline().strip().split())
    height_list[start].append(end)
    inDegree[end] += 1 # end 지점에 들어올 때마다 체크하기 
# print(height_list)
# print(inDegree)

q = deque()
for i in range(1, n+1) :
    if inDegree[i] == 0:
        q.append(i)

ans = []
while q :
    tmp = q.popleft()
    ans.append(tmp) # 진입차수(inDegree)가 0인 노드들이 최하단
    for i in height_list[tmp] : # 이 개념이 헷갈리면 안되는게 0부터 시작하는게 아니라, heigth_list[tmp]의 안에서 인덱스 0부터인 거임
        inDegree[i] -= 1
        if inDegree[i] == 0 :
            q.append(i)

print(*ans)
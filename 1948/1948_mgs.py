import sys
from collections import deque

sys.stdin = open("23_input.txt","r")

"""
https://hiruby.tistory.com/439 임계경로
- 어떤 사람은 이 시간에 만나기 위하여 1분도 쉬지 않고 달려야 한다.=> 임계경로
- 임계경로는 전체 중에서 여러 경로가 동시에 이루어질 때, 가장 오래 걸리는 경로를 의미한다. 
- 가장 오래 걸리는 경로를 구하고 백트래킹을 할 때 중복된 도로를 제거해주어야한다
   1->2 2->6 6->7 // 1->4 4->6 6->7 의 두가지 경우가 존재한다.
    6->7은 중복된 도로이므로 한 번만 카운트 해주어야 한다 

https://yabmoons.tistory.com/443 설명대박임
"""
def topology_sort(go, stop) :
    q.append(go)
    while q :
        cur = q.popleft()   # 임계경로 알고리즘 (최장길이 저장)
        for i, t in graph[cur] :
            indegree[i] -= 1
            res[i] = max(res[i], res[cur] + t)  # 현재까지 걸린 시간 + 추가될 시간
            if indegree[i] == 0:
                q.append(i)
    
    # 백트래킹
    cnt = 0 # 임계경로에 속하는 모든 경로의 개수
    q.append(stop)
    while q: # 도착점에서 시작점으로
        cur = q.popleft()
        for i, t in back_graph[cur] :
            # 도착점까지의 비용에서 시작점의 비용을 뺐을 때 그 간선비용과 같다면, 경로를 찾은거니까 cnt += 1
            if res[cur] - res[i] == t :
                cnt += 1
                if check[i] == 0 :
                    q.append(i)
                    check[i] = 1
    print(res[stop])
    print(cnt)



n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
back_graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
res = [0] * (n+1)
check = [0] * (n+1)
q = deque()
for _ in range(m) :
    start, end, wage = map(int, sys.stdin.readline().strip().split())
    graph[start].append((end, wage))
    back_graph[end].append((start, wage))
    indegree[end] += 1

go, stop = map(int, sys.stdin.readline().strip().split())


topology_sort(go, stop)
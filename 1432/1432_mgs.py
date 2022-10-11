import sys
sys.stdin = open("22_input.txt","r")

"""
https://wonyoung2257.tistory.com/80
이 문제의 핵심은 답이 여러 개일 경우에는 사전 순으로 제일 앞서는 것을 출력한다.

1. outdegree를 사용
2. 최대힙을 사용
3. answer를 N부터 대입
4. outdegree를 사용하는 건 간선의 방향을 뒤집어 주면된다.
"""

import sys
import heapq

def topology_sort(n) :
    q = []
    for i in range(1, n+1) :
        if indegree[i] == 0 :
            heapq.heappush(q, -i)
    
    while q :
        now = -heapq.heappop(q)
        ans[now] = n

        for i in node[now] :
            indegree[i] -= 1
            if indegree[i] == 0 :
                heapq.heappush(q, -i)
        n -= 1


n = int(input())
node = [[] for _ in range((n+1))]
indegree = [0] * (n+1)

# 인접행렬을 리스트로 변환
for i in range(1, n+1) :
    tmp = [0] + list(map(int, sys.stdin.readline().strip()))
    for j in range(1, n+1) :
        if tmp[j] == 1 :
            node[j].append(i)
            indegree[i] += 1

ans = [0] * (n+1)

topology_sort(n)
if ans.count(0) > 1 :
    print(-1)
else :
    print(*ans[1:])
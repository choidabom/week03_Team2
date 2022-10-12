# 11725: 트리의 부모 찾기
# https://yanoo.tistory.com/52
# 루트 없는 트리가 주어짐. 이 때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하라 ~!
# dfs로 들어가면서 방문하지 않았다면 현재 확인하는 노드가 부모 노드이다.

import sys
from collections import defaultdict
sys.stdin = open("RETRY/트리의부모찾기/input.txt","r")
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

# 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하라 ~!
def dfs(root):
    visited[root] = True
    for node in graph[root]:
        # 방문하지 않았다면 현재 확인하는 노드가 부모 노드다 !!!!!! 맞다...
        if not visited[node]:
            answer[node] = root
            dfs(node)
    return 

N = int(input().rstrip()) # 노드의 개수
graph = [[0] for _ in range(N+1)] # 트리
visited = [False for _ in range(N+1)]
answer = [0 for _ in range(N+1)]

# 조심해야할 점: 받아올 때 N-1개의 줄에 트리 상에 연결된 두 정점이 주어짐.
for i in range(N-1):
    k, v = map(int, input().split())
    graph[k].append(v)
    graph[v].append(k)
    
# 트리의 루트를 1이라고 정했을 때,
dfs(1)

# 어차피 graph의 인덱스 0은 안 쓰고, 루트를 1로 잡았기 때문에
# 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다. 
for i in range(2, len(answer)): 
    print(answer[i])
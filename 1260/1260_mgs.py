import sys
from collections import deque
sys.stdin = open("4_input.txt","r")

# 포인트) bfs는 deque, dfs는 스택으로 풀어야한다

def dfs(n) :
    visited[n] = True
    print(n, end = ' ')
    for i in graph[n] :     # n으로 들어간 값을 다 찍고 나옴. 
        if not visited[i] :
            dfs(i)

def bfs(n) :
    q = deque([n])
    visited[n] = True
    while q :
        v = q.popleft()
        print(v, end= ' ')
        for i in graph[v] :
            if not visited[i] :
                q.append(i)     # append로 찍히기 때문에 그 다음 값들어가서 처리해도 상관이 없음
                visited[i] = True

n, m, v = map(int, sys.stdin.readline().split())
graph =[[] for _ in range(n+1)]
for i in range(m) : 
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
# print(graph)
    
for i in range(1, n+1) :
    graph[i].sort()
# print(graph)

visited = [False] * (n+1)
dfs(v)
print()
visited = [False] * (n+1)
bfs(v)




# 다음과 같은 반례를 해결하려면 위와 같은 dfs 재귀를 해야함
# input:
# 5 5 1
# 1 2
# 2 3
# 3 1
# 1 4
# 3 5

# output:
# 1 2 3 4 5
# 1 2 3 4 5

# answer:
# 1 2 3 5 4
# 1 2 3 4 5
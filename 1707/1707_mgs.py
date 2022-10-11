import sys
sys.stdin = open("8_input.txt","r")

def dfs(start, group) :
    visited[start] = group  # 노드에 group값을 주고

    for node in graph[start] :
        if not visited[node] : # 아직 방문하지 않았다면 방문을 하는데
            a = dfs(node, -group)  # -group값으로 주는 이유는 
            if not a :
                return False
        elif visited[node] == visited[start] :
            return False
    return True

k = int(input())

for _ in range(k) :
    v, e = map(int, sys.stdin.readline().strip().split())
    graph = [[] for _ in range(v+1)]
    visited = [False] *(v+1)
    for _ in range(e) : 
        start, end = map(int, sys.stdin.readline().strip().split())
        graph[start].append(end)
        graph[end].append(start)
        
    for i in range(1, v+1) :
        if not visited[i] :
            res = dfs(i, 1)
            if not res :
                break
    print('YES' if res else 'NO')



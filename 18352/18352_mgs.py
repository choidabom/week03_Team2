import sys
from collections import deque
sys.stdin = open("14_input.txt","r")

n, m, k, x = map(int, sys.stdin.readline().split()) # 도시개수, 도로개수, 거리정보, 출발도시번호
# print(n, m, k, x)

road_list = [[] for _ in range(n+1)]
for _ in range(m) :
    start, end = map(int, sys.stdin.readline().strip().split())
    road_list[start].append(end)

# print(road_list)
visited = [False] * (n+1)
distance = [0] * (n+1)

# print(road_list)

def bfs(x) :
    ans = []
    visited[x] = True
    distance[x] = 0
    q = deque([x])
    while q :
        starting = q.popleft()
        for i in road_list[starting] :
            if visited[i] == False :
                q.append(i)
                visited[i] = True
                distance[i] = distance[starting] + 1
                if distance[i] == k:
                    ans.append(i)
    if len(ans) == 0 :
        print(-1)

    else :
        ans.sort()
        for i in ans:
            print(i, end = "\n")

bfs(x)


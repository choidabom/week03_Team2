import sys
from collections import defaultdict
sys.setrecursionlimit(10**9)
sys.stdin = open("9_input.txt","r")

def dfs(start) :
    cnt = 0
    for next in path[start] :
        if A[next] == '1' :
            cnt += 1
        else :
            if not visited[next] :
                visited[next] = True
                cnt += dfs(next)
    return cnt
           
n = int(input())
A = ' ' + sys.stdin.readline().strip()  # 정점의 실내/실외 정보를 담은 문자열. index와 정점번호를 맞춰주기 위해 공백 한 칸(' ')을 앞에 붙여줌
path = [[] for _ in range(n+1)] 
visited = [False] * (n+1)
ans = 0

for _ in range(n-1) :
    start, end = map(int, sys.stdin.readline().strip().split())
    path[start].append(end)
    path[end].append(start)

for i in range(1, n+1) :
    if A[i] == '1' :
        for j in path[i] :
            if A[j] == '1' :
                ans += 1
    else :
        if not visited[i] :
            visited[i] = True
            cnt = dfs(i)
            ans += cnt *(cnt-1)     # n개중 2개를 뽑고 순서가 있다면 nP2 = n(n-1)

print(ans)


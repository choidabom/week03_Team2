import sys
from collections import deque
sys.stdin = open("12_input.txt","r")

def dfs(arr, n) :
    global cnt
    for i in arr[n] :
        if not visited[i] :
            visited[i] = True
            cnt += 1
            dfs(arr, i)

n, m = map(int, sys.stdin.readline().strip().split())
bigger = [[] for _ in range(n+1)]   # 원소값보다 무거운 리스트
smaller = [[] for _ in range(n+1)]  # 원소값보다 가벼운 리스트
mid = (n+1)/2

for i in range(m) :
    start, end = map(int, sys.stdin.readline().strip().split())
    bigger[end].append(start)
    smaller[start].append(end)
# print(bigger)
# print(smaller)

ans = 0
for i in range(1, n+1) :
    visited = [False] * (n+1)

    cnt = 0
    dfs(bigger, i)
    if cnt >= mid :
        ans += 1
         
    cnt = 0
    dfs(smaller, i)
    if cnt >= mid :
        ans += 1

print(ans)
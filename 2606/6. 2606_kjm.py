# https://www.acmicpc.net/problem/2606

#입력받고 연결관계를 표현하기
#dfs로 1번 컴터부터 시작해서 맨 밑단까지 다 돌게하고 돈 피씨들은 True로 바꾸기

import sys
sys.setrecursionlimit (10**9)

def dfs(starting):
  visited[starting] = True
  for itr_edges in edges[starting]: #2,5
    if visited[itr_edges] == False:
      dfs(itr_edges)

# 입력과 관계설정
N = int(sys.stdin.readline()) #컴퓨터의 개수 (노드)
M = int(sys.stdin.readline()) #간선의 개수 

edges = [[] for _ in range(N+1)] #[[], [], [], [], [], [], []]

for _ in range(1,M+1): #1~6이하까지
  a,b = map(int, sys.stdin.readline().split()) #1,2 
  edges[a].append(b)
  edges[b].append(a)
# print(edges) [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]

visited = [False] * (N+1) # [False, False, False, False, False, False, False, False]
dfs(1)

count=0
for itr_visited in visited:
  if itr_visited == True:
    count+=1
print(count-1) #1번 컴터도 True설정되어있으니까 count에는 포함되는데 문제는 1번을 제외한 컴터의 숫자를 물어보니까 -1
# https://www.acmicpc.net/problem/11725

import sys
sys.stdin = open('input.txt','r')
input= sys.stdin.readline
N=int(input())

nodes = [[] for _ in range(N+1)]
# 부모노드를 기록할 기록지가 필요해
parents = [0 for _ in range(N+1)]

# 관계설정하고 
for _ in range(N-1):
  a,b = map(int, input().split())
  nodes[a].append(b)
  nodes[b].append(a)  
#내가 이 문제 틀린 이유가 관계를 받을 때 단방향으로 받아서 틀린거임. 참고로 단방향이면 문제에서 단방향이라고 언급을 해준다.
#언급이 없으면 양방향으로 전제하고 풀어야한다. 

def dfs(x):
  for itr in nodes[x]:
    if parents[itr] == 0: #6
      parents[itr] = x
      dfs(itr)

dfs(1)  
for i in range( 2, N+1):
  print(parents[i])
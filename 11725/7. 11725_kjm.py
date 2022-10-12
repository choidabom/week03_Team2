# https://www.acmicpc.net/problem/11725
#2시반
# 입력을 받고
# 관계를 표현하고

import sys
sys.stdin=open("input.txt", "r")
sys.setrecursionlimit(10**9)
input=sys.stdin.readline
N = int(input()) #7

Tree= [[] for _ in range(N+1)] #8개 트리 준비
Parents = [0 for _ in range(N+1)] 

for _ in range(1, N): #입력을 1, N+1 로 받으면 not enough values to unpack (expected 2, got 0) / 2개가 기대되는데 하나도 안왔다 에러 뜸.
  a,b=map(int, input().split()) #1,6
  Tree[a].append(b)
  Tree[b].append(a)

def dfs(start, tree, parents):
  for i in tree[start]: #6,4
    if parents[i]==0:
      parents[i] = start
      dfs(i, tree, parents)

dfs(1, Tree, Parents)

for i in range(2,N+1):
  print(Parents[i])


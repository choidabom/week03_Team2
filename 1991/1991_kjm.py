# https://www.acmicpc.net/problem/1991


# <루트를 기준으로 판단>
# 1. 프리오더(전위식) = 루트 - left - right
# 2. 인오더 (중위식) = left - 루트 - right
# 3. 포스트오더(후위식) = left - right -루트 
 

def pre_order(v):
  if v:
    print(v, end="")
    pre_order(tree[v][0])
    pre_order(tree[v][1])

def in_order(v):
  if v:
    in_order(tree[v][0])
    print(v, end="")
    in_order(tree[v][1])

def post_order(v):
  if v:
    post_order(tree[v][0])
    post_order(tree[v][1])
    print(v, end="")

N = int(input())
tree = {}
for i in range(65, 65+N):
  tree[chr(i)] = ['','',''] #왼쪽자식, 오른쪽자식, 부모

for _ in range(N):
  node, left, right = map(str, input().split)

pre_order(1)
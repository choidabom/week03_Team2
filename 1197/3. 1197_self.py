import sys
def find_parent(parent, x): 
  if parent[x] != x: 
    parent[x] = find_parent(parent, parent[x])
  return parent[x] 
def union_parent(parent, a, b): #뭔가를 합치니까 당연히 두 개a, b가 필요하겠지
  a=find_parent(parent, a)
  b=find_parent(parent,b)
  if a<b: 
    parent[b] = a
  else:
    parent[a] =b

input = sys.stdin.readline
v, e = map(int, input().split())
parent = [i for i in range(v+1)] #[0, 1, 2, 3.. v]
edges = []
result = 0

for _ in range(e):
  a,b,c = map(int, input().split())
  edges.append((c,a,b))

edges.sort() #오름차순으로 정렬
             #(112, 223, 313으로 정렬됨. 맨 앞자리가 c, cost임 순서대로 뽑아쓰면 크루스칼 알고리즘대로 하는 것)

for edge in edges:
  cost, a, b = edge
  

  if find_parent(parent,a) != find_parent(parent,b):
    union_parent(parent,a,b) 
    result = result+cost
print(result)
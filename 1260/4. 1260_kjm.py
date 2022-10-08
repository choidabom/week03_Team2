import sys
sys.stdin = open("input.txt","r")
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())


def bfs(start):
  deque=[]
  path_2 = f'{start} '
  deque.append(start)
  visited[start] = 1

  while deque:
    cur = deque.pop(0)
    for next in edges[cur]:
      



#1. n+1개의 빈 배열을 만드네? 대체 왜 why?
#edges = [[] , [], ...] n은 정점(edges)의 개수니까 0부터 세면 이상함. 자연수여야지.
#만약 n개를 만들었다고 치면 edges[0]이 1번 정점, edges[n-1]이 n번 정점을 가리키게 됨. (배열의 인덱스번호랑 실제 정점의 넘버링이 차이가 나서 헷갈림)

#2. 이 코드 지금 뭐하는거임? 
#결론부터 말하면 엣지(정점)들간에 관계를 배열로 표현하는 중임. 여기서 포인트는 1과 2가 연결 되어있으면 edges[1]에는 2가 edges[2]에는 1이 들어간다는 것.(즉 이어진다는건 쌍방향이라 서로에게 기록해줘야한다는 것)
edges =[[] for _ in range(n+1)] 
for i in range(m):
  a,b = map(int, sys.stdin.readline().split())
  edges[a].append(b)
  edges[b].append(a)

# #n+1로 안 만들고 평소처럼 n으로 만들었을 때 벌어지는 일들. (별거없긴한데.. edges에서 값을 빼올 때 항상 -1을 해줘야한다는 걸 생각해야함.)
# edges= [[] for _ in range(n)] 
# for i in range(m):
#   a, b = map(int, sys.stdin.readline().split())
#   edges[a-1].append(b)
#   edges[b-1].append(a)
# print(edges)

for i in range(1, n+1):
  edges[i].sort()

visited = [false] * (n+1)
print(visited)


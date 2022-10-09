# https://www.acmicpc.net/problem/1260
# https://naver.me/F1MJORkw  가장 설명 잘 된 블로그인듯!!! 이걸로 와꾸먼저 잡고보면 편한데 너처럼 디버거 써서 바텀업으로 전체 구조를 이해하려하면 너무 괴롭다..


import sys
# sys.stdin = open("input.txt","r") #이 코드 안 없애고 제출하면 런타임에러
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())

#1. n+1개의 빈 배열을 만드네? 대체 왜 why?
#2. 이 코드 지금 뭐하는거임? 
edges =[[] for _ in range(n+1)] 
for i in range(m):
  a,b = map(int, sys.stdin.readline().split())
  edges[a].append(b)
  edges[b].append(a)

#1. n+1개의 빈 배열을 만드네? 대체 왜 why?
#edges = [[] , [], ...] edges의 배열 하나하나는 정점을 뜻함. 즉 개수니까 0부터 세면 이상함. 자연수여야지.
#만약 n+1말고 n으로 만들었다고 치면 edges[0]이 1번 정점, edges[n-1]이 n번 정점을 가리키게 됨. (배열의 인덱스번호랑 실제 정점의 넘버링이 차이가 나서 헷갈림)

# #n+1로 안 만들고 평소처럼 n으로 만들었을 때 벌어지는 일들. (별거없긴한데.. edges에서 값을 빼올 때 항상 -1을 해줘야한다는 걸 생각해야함.)
# edges= [[] for _ in range(n)] 
# for i in range(m):
#   a, b = map(int, sys.stdin.readline().split())
#   edges[a-1].append(b)
#   edges[b-1].append(a)
# print(edges)

#2. 이 코드 지금 뭐하는거임? 
#결론부터 말하면 엣지(정점)들간에 관계(간선)를 배열로 표현하는 중임. 여기서 포인트는 1과 2가 연결 되어있으면 edges[1]에는 2가 edges[2]에는 1이 들어간다는 것.
#즉 이어져있다는 것의 본질은 나도 너의 흔적을 가지고 있고 너도 나의 흔적을 가지고 있는것. 뭔가 철학적임


def bfs(v):
  q = deque([v])
  # 이거랑 같은말
  # q=deque()
  # q.append(v)

  visited[v] = True #일단 최초 시작점은 방문한거니까 true로 바꾸고
  while q: #큐가 있으면 도는데 큐엔 뭐가 쌓이느냐
    v = q.popleft()
    print(v, end= ' ')
    
    for i in edges[v]:
      if not visited[i]:
        q.append(i) #v(1)과 인접해있는데 아직 방문은 하지 않은 놈들을 전부 큐에 넣어놓음(미뤄놓음)  #1과 인접한 2,3,4 각각을 큐에 넣어야지
        # dfs에서는 인접한 것 중 방문하지 않은 놈들 모두 넣는게 아니라, 한놈만 파서 계속 밑으로 내려가는것.
        visited[i] = True

# def dfs(n) :
#     visited[n] = True
#     print(n, end = ' ')
#     for i in edges[n] :     # n으로 들어간 값을 다 찍고 나옴. 
#         if not visited[i] :
#             dfs(i)

def dfs(v):
  visited[v] = True
  print(v, end=' ')
  for i in edges[v]:
    if visited[i]==False:
    # if visited[v]==False: (또 이걸 1 즉 v라고 해서 오류남)
      dfs(i)

# 문제의 조건에서 빠른 숫자를 먼저 출력하라(방문하라)라고 있어서 정렬해야함.
for i in range(1, n+1) :
    edges[i].sort()
# print(graph)

visited = [False] * (n+1)#[False, False, False, False] #방문여부 체킹하기 위해 노드 수에 맞춰서 false 넣어놓음
dfs(v)
print()

visited = [False] * (n+1)
bfs(v)
# https://www.acmicpc.net/problem/2252

import sys
from collections import deque

sys.stdin=open("input.txt", "r")

n,m =map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
inDegree = [0 for _ in range(n+1)] #화살표 몇표 받았는지 세는 배열

queue = deque()
answer = []

# 관계설정하고 각자 화살표 몇 표 받았는지도 기록함.
for i in range(m):
  a,b = map(int, sys.stdin.readline().split())
  graph[a].append(b) #[[], [3], [3], []]  #1이 3에게 쐈다는 의미
  inDegree[b] +=1 #진입차수를 기록하는 로직 ex) 3은 2번 화살표 받으니까 2

#노드들을 쏵 돌면서 진입차수가 0인 노드를 큐에 넣기
for i in range(1, n+1):
  if inDegree[i] == 0: 
    queue.append(i) 

# 큐가 빌때까지 다음 과정을 반복(큐에 있는놈들은 전부 진입차수가 0인놈들임)
while queue:
  tmp = queue.popleft() #큐에서 원소를 꺼내서 
  answer.append(tmp) #답에 기록(큐에서 원소를 꺼내는 순서가 곧 정렬순서가 됨) 왜그럴까?
  # 큐에 들어있는 것들은 진입차수가 0인 것들이 들어가 있는데 진입차수가 0이라는 소리는 누구한테 총맞은 적이 없다는 소리 즉, 선행과목이 없다는 소리임.
  # (=지가 젤 기초라서 선행과목이 없다는 것)

  # 큐에서 원소를 꺼내고 그 노드에서 출발하는 간선들을 제거하려고
  for i in graph[tmp]: #1번한테 총맞은 놈들(=1번이 총쏜놈들) For 문으로 돌아.
    inDegree[i] -= 1 #간선을 제거 했다는 표현을 이케 표현함. 기존에 총맞은 숫자에서 -1
    if inDegree[i] == 0:#만약 -1했는데 간선이 0으로 바뀌면
      queue.append(i) #역시 큐에 넣어(큐에 들어갔다는 소리가 선행과목이 됐다는 소리임.)
print(*answer)



  



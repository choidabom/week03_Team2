# https://www.acmicpc.net/problem/18352

# 1. 입력을 받는데 첨부터 관계 설정까지 해서 넣고 (단, 단방향으로) -> 막 받은 다음에 바꾸려하면 복잡하다.
# 2. 여기보고 저기보고 하는게 탐색하는 알고리즘인가? 라고 생각. 그럼 bfs, dfs 떠오르는데
# 3. 한 놈만 패는게 나을까? 아님 한대씩 골고루 때리는게 나을까 생각해보면?
#     한놈만 패다가 그놈이 중요한 놈이면 땡큔데 아닐수도 있잖아? 그러니까 골고루 한대씩 패다가 어라 저놈이 중요해보이는데? 하면 if문으로 안중요해보이는 놈들 다 거르고 중요한 놈에 집중하는 방향으로.
#     물론 한놈만 패다가 그놈이 중요한놈이 아닌 것 같으면 조건을 줘서 다른놈을 패게 할 수도 있음. 근데 한놈만 패기 위해 재귀를 쓰는데 탈출조건들을 추가해주느라 재귀가 덕지덕지 해지면 재귀의 매리트가 사라짐?(이건 뇌피셜)
# 4. 따라서 한대씩 골고루 때리는 알고리즘 사용예정(BFS)

# 5. BFS는 주머니를 수기로 만들어줘야하니까 deque를 생성하고

# 6. 1부터 출발하니까 2,3을 보는데 먼저 2를 본다.
#    2를 count +1해주고 (1~4까지 방문한 숫자를 체크할 배열을 하나 만들어줘야겠지?)
#    2와 연결된 다른놈을 보는게 아니라 3을 봐야하니까 주머니에 일단 넣어놓고(que에 2를 추가)
# 7. 이제 3을 보면, 3도 왔으니까 count +1로 바꿔주고 주머니에 넣어놓음.

# 8. while을 써서 주머니에 뭔가가 있는지 (할일이 남았는지 체크하는데, 2와3이 있네?)
#    2를 주머니에서 꺼내면서 (popleft)보자. 2는 3과 4가 연결 되어 있는데 
#    3부터 보면 3은 이미 count가 1로 되어있으니까 제외 (if문을 써서 count가 0이 아닌놈은 안들어가도 되도록 설정. 왜냐 최단거리를 구해야하는데 1에서 3은 바로갈 수 있으니까) bfs가 효율을 내는 순간임!
#    4를 보면 count는 0이니까 가도 되는거고, 4의 count를 +1해줘. (음.. 이러면 카운트 현황이 2도 1, 3도1,4도 1 이라서 cout가 2인놈을 찾질 못하는데..? )


#입력


import sys 
from collections import deque

def bfs(starting):
  # global N
  que = deque()
  que.append(starting)
  visited[starting] = True
  distance[starting] = 0

  while que:
    changed_starting = que.popleft() #2,3 중
    for itr_edges in edges[changed_starting]: #2와 3 각각을 의미함.
      if visited[itr_edges] == False: #2 방문했는지부터 체크
        visited[itr_edges] = True
        # distance[itr_edges] =1
        # distance[changed_staring] = distance[itr_edges] + 1
        distance[itr_edges] = distance[changed_starting] +1 #13번이랑 똑같은 로직 씀. #distance[1] + 1을 distance[2] 에 넣는다. (0+1)을 distance[2]에 넣으니 1이 됨.(1에서 2까지 1거리 걸림)
        if distance[itr_edges] ==K:
          answer.append(itr_edges)
        que.append(itr_edges)

  if len(answer)==0:
    print(-1)
  else:
    answer.sort()
    for i in answer:
      print( i, end='\n')




N, M, K, X =map(int, sys.stdin.readline().split())

edges= [[] for _ in range(N+1)] # [[], [], [], [], []]

for _ in range(M):
  a, b= map(int, sys.stdin.readline().split())
  edges[a].append(b) #[[], [2, 3], [3, 4], [], []]

visited = [False]*(N+1) #[False, False, False, False, False]
distance = [0]*(N+1) # [0, 0, 0, 0, 0]
answer=[]
# print(distance)
bfs(X)
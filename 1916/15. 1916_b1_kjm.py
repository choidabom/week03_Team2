# https://www.acmicpc.net/problem/1916
# 2시 반 시작 
# 4시 반 중단 
# 역시 비용을 카운팅해서 목표 지점까지 가는거에서 막혔음
# 이문제는 bfs로 풀면 안된대.. 다익스트라 알고리즘으로 풀어야함.


# 화살표? 또는 간선? => BFS 또는 DFS이군
# 최소비용? => 그리디 알고리즘? (크루시칼또는 크림?)
# 시간은 0.5초인데 한놈만 패다가 실패하면 곤란.. 대박은 없어도 평타는 치는 bfs로 가야해

# 관계를 입력받고 (이거 관계정보만 있는게 아니라 비용 정보도 함께 있어서 dict형식으로 해야하네?)
  # (1: [2,2]) 이렇게 받고 싶은데 중복이 안되는 dict특성상 1:[3,5]가 나오면 덮어써져버려서 dict로하면 안된다.
  # 대신 1번 배열에 [2,2] 를 넣는 방식으로 가보자.
# 주머니를 만들고
# 비용을 카운팅하는 로직이 필요해 (이게 어렵겠는데?)

import sys
from collections import deque

#bfs함수 설정
def bfs(starting, destination):
  # 방문여부를 체크하고
  visited[starting] = True
  que=deque([starting])
  # 방문하고 (dict는 어떻게 for문을 돌리지?)
  while que:
    new_starting=que.popleft()

    for itr_graphs in graphs[new_starting]: #graphs = [[]/ [ [2, 2], [3, 3], [4, 1], [5, 10] ]/ [ [4, 2] ]/ [ [4, 1], [5, 1] ]/ [ [5, 3] ]/ []]
      # print(itr_graphs) #[2, 2], [3, 3], [4, 1], [5,1]
      visited[itr_graphs[0]]=True #itr_graphs[0] = 2, 3, 4, 5를 의미


      # distance[itr_graphs[1]] = distance[new_starting] + [itr_graphs][1]
      # 이 코드 list out of index 떠서 당황했는데 아래처럼 하나씩 프린트 찍어서 찾음.
      # 디버깅 하는 과정 기록할 것!!
      # print(distance[itr_graphs[1]])
      # print(distance[new_starting])
      # print([itr_graphs[1]]) #이게 버그였음

      # 고쳐도 list_out_of range 뜨는데 그땐 디버거를 보면 됨. 막히기 딱 바로 전 정보가 들어가 있어서!
      # itr_graphs[1]이 10인데 distance는 최대 5까지니까 range 벗어나게 됨.
      distance[itr_graphs[0]] = distance[new_starting] + itr_graphs[1]
      #distance(2)번 에다가 1번에서 1번가는 거리에(1번에서 시작한다고 치면) + 1에서 2가는 거리 2를 더함.
      #즉 1에서 2까지 가는거리는 2

      que.append(itr_graphs[0]) #2, 3, 4를 큐에 넣어

    # 거리를 카운팅하고
      print(distance)

#입력 및 관계 설정

N=int(sys.stdin.readline().strip()) #N은 도시개수
M=int(sys.stdin.readline().strip()) #M은 버스의 개수

graphs=[[] for _ in range(N+1)] # [[], [], [], [], [], []]

for _ in range(M):
  a,b,c = map(int, sys.stdin.readline().split())
  graphs[a].append([b,c])
# #[[], [[2, 2], [3, 3], [4, 1], [5, 10]], [[4, 2]], [[4, 1], [5, 1]], [[5, 3]], []]


# graphs={}
# for _ in range(M):
#   a,b,c = map(int, sys.stdin.readline().split())
#   graphs[(a,b)]=c
# # print(graphs) = {(1, 2): 2, (1, 3): 3, (1, 4): 1, (1, 5): 10, (2, 4): 2, (3, 4): 1, (3, 5): 1, (4, 5): 3}
#  이렇게 딕트를 받으면 키값을 (1,2) 이렇게 불러와야하는데 키값 내에서 1과 2를 나눌수 없어서 활용이 불가능하고
#  {1:[2,3], 1:[4,3]} 이렇게는 키값이 중복될 수 없다는 딕트의 조건 때문에 1:[4,3]으로 덮어써져버리고..
#  그럼 리스트로 풀어야만 하는건가?? NO
#  {1: [(2,2), (3,3), (5,10)], 2: [(4,2), (3,4)] } 이렇게 받으면 된다.
starting, destination = map(int, sys.stdin.readline().split())

visited = [False] * (N+1)
distance = [0] * (N+1)
# print(distance) #[0, 0, 0, 0, 0, 0]
bfs(starting, destination)

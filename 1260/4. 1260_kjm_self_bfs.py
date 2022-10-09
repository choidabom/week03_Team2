from collections import deque
import sys
sys.stdin = open("input.txt","r")

# bfs구현
#edges는 = [[2, 3, 4], [1, 4], [1, 4], [1, 3, 2]]
def bfs(starting_point): #문제 조건에 따르면 1부터 조회(파리미터로 -1해서 들어오니까 현재 0임)
    visited = [False] * n 
    # visited = [False for _ in range(n)]
    deq=deque()
    deq.append(starting_point)

    visited[starting_point-1] = True

    while deq:
        starting_point=deq.popleft()
        print(starting_point, end='')

        for itr_edge in edges[starting_point-1]: #1과 인접한 2,3,4 각각을 큐에 넣어야지
            if visited[itr_edge-1] == False:
            # if visited[starting_point-1] == False: #나이거 헷갈리네 1을 봣으면 1 아래에 있는 2,3,4를 봐야하는데 starting_point로 해버리면 다시 1을 보겠다는 의미가 되어버림.
                deq.append(itr_edge)
                visited[itr_edge-1] =True

''' 
아래 방법은 내가 쓴 코드인데 for문이 먼저 나오고 while문을 썼다. 

    deq = deque()
    # 방문한 노드와 인접한 노드를 큐에 저장

    for itr_edges in edges[starting_point-1]: #1과 인접한 놈들 2,3,4 
        ##처음 edges =list([] for _ in range(n)) 에서 n+1까지로 했으면 계속 -1 빼주는거 신경 써야하는 고생 안했지

        deq.append(starting_point)
        while deq:
            starting_point=deq.popleft()
            print(starting_point, end='') #방문했으니까 print
      
            if visited[starting_point-1] == False:
                deq.append(itr_edges)
                visited[starting_point-1] = True # 방문했으니 True로 바꾸고 
'''    



# 입력
n, m, v= map(int, sys.stdin.readline().split())

''' 의식의 흐름대로 가면 아래처럼 코드를 쳤을 거 같거든? 매번 치듯이?
근데 이번에는 다른 문제랑 다르게 입력값을 문제에서 리스트를 주는대로 넣는게 아니라
관계에 따라서 재설정해서 넣어야한단 말이지? 

아래처럼 넣으면 문제에서 주는대로 일단 임시 리스트에 넣고, 그걸 어케 잘 가공해서 새로운 리스트를
만드는 방식인데. 일단, 잘 가공하는거 그게 빡세고 당연히 첨부터 잘넣으면 되는데 왜 일 두번해?가 된다.
따라서 첨부터 잘 넣는 방향으로 가자.

# 입력받기
tmp =[]
edges = []
for i in range(m):
    a,b = map(int, sys.stdin.readline().split())
    edges.append([a,b])
# edges= [[1, 2], [1, 3], [1, 4], [3, 4], [2, 4]]

# 간선간에 관계를 배열로 표현 (실패)
relationship_l = list(tmp for _ in range(n)) #[[], [], [], []]

for itr_list in edges: #[1,2]

    a = itr_list[0] #1
    b = itr_list[1] #2
    
    if b not in relationship_l[a-1]:
        relationship_l[a-1].append(b)
        relationship_l[b-1].append(a)
'''

# 관계 표현 
edges =list([] for _ in range(n)) #edges = [[], [], [], []]
for i in range(m):
    a,b = map(int, sys.stdin.readline().split())
    edges[a-1].append(b)
    edges[b-1].append(a)
#edges = [[2, 3, 4], [1, 4], [1, 4], [1, 3, 2]]

for itr_edges in edges:
    itr_edges.sort()



print()
bfs(v)


        
# 1707: 이분 그래프
'''
https://ambiguous-raver-03c.notion.site/BOJ-1707-e1bdc0f100df435684689966e470e4b2
이분 그래프 => 두 부분으로 나눠지는 그래프
결론은 인접한 애들끼리는 다른 value를 갖게 할 수 있으면 YES
value는 1, -1 두 가지
value 1그룹, value -1그룹 두 개로 구분 가능하냐는 거다

먼저, 이 문제는 받는거부터 빡셈
1) 테스트 케이스의 개수 K
2) 각 테스트 케이스의 첫째줄에는 그래프 정점의 개수 V와 간선의 개수 E 주어짐
3) E개의 줄에 걸쳐 간선에 대한 정보가 주어짐. 각 줄에 인접한 두 정점의 번호 u,v 가 주어짐

A) 각 test case에 대해서 돌게 하자 / 입력 받음
B) group 리스트를 vertex 수 + 1개로 만든다 / 0으로 초기화
C) DFS를 돈다
처음에 group(u) = 1 해주고 시작
그 다음 그룹은 얘에다가 -1을 곱해준 친구여야 함.
u의 인접 vertex = v라고 하자.
group(v)=0 이면 not visited이다.
그러면 group(v) = -group(u)
0 아닌데 group(v)==group(u)이면, 인접인데 같은 그룹이니까 이분그래프가 아니자ㅏ나???


'''
import sys
from collections import defaultdict, deque
sys.stdin = open("1707/input.txt","r")
input= sys.stdin.readline

def bfs(graph, u, group):
    q = deque([u])
    group[u] = 1 # 처음 group(u)=1 해주고 시작, 그럼 그 다음부터는 이 그룹의 -1이 곱해져있어야함.
    while q:    # u를 q에 넣었고, q가 끝날 때까지 ~
        u = q.popleft() # q에 있는 친구 빼줘, 
        for v in graph[u]: # u의 인접 친구인 v가 있을거야, 
            if group[v] == group[u]: # group[v]의 인접 group[u]가 같으면 이진트리가 아니겠지.
                return False # 이진트리가 아니니깐 False를 반환 
            elif group[v]: # 1, -1도 True이다. 0이 아니면 즉, 1과 -1이면 방문했다는거니깐 continue/ 가장 가까운 for문으로 돌아감.
                continue
            elif not group[v]: # 0. 즉, 방문을 안 했다면 group[v]와 인접한 group[u]에 -1을 곱해줌.
                group[v] = -group[u]
                q.append(v) # 인접 v를 q에 넣어줌 ~~~~~~~~
    return True # q가 비었다면 True 반환

def init():
    V, E = map(int, input().split())    # 정점 개수 V, 간선 개수 E
    graph = defaultdict(list)           # graph라는 딕셔너리에서 키에 대한 값을 list 값으로 지정
    group = [0] * (V+1)                 # visited 역할 겸 같은 그룹인지 다른 그룹인지 판별하는 group을 vertext 수 + 1 개를 만듬
    for _ in range(E):                  # 간선의 갯수만큼 인접한 두 정점의 u, v를 받음
        u, v = map(int, input().split())
        graph[u].append(v)              # 그래프, 방향이 없으므로 양방향으로 오갈 수 있게 만듬
        graph[v].append(u)

    # graph.keys()의 역할은 graph라는 딕셔너리에 존재하는 전체 key를 조회한다.  
    for node in graph.keys(): # 즉 dict_keys([1, 3, 2]), dict_keys([1, 2, 3, 4]) 확인
        if group[node]: # 아직 안 간 그룹인지 확인
            continue
        if not bfs(graph, node, group):
            print('NO')
            return
    print('YES')

K = int(input().rstrip()) # 테스트 케이스의 개수
for _ in range(K):  # 각각의 테스트 케이스마다 돌기 위한 for문
    init()
    
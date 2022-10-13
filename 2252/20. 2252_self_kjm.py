

#관계를 입력받고, 화살표 몇 표 받았는지도 기록해야함.

#For문 돌면서 화살표 0표인놈들 큐에 넣어 (0표라는 소리는 선행과목이라는 소리임)

#큐가 있는 동안 아래 행위를 반복할 거임.
    #큐에서 popleft한 값을 tmp라하면 tmp를 정답 배열에 넣고
    
    #for문으로 tmp한테 총맞은 애들을 찾아서
        #그놈들 간선 지우는 작업 (화살표 몇 표 받았는지 체크하는 배열에서 -1씩 뺌)
        #만약 간선이 0이 되면?
            #큐에 넣어

#큐가 없어지면 지금까지 모인 answer를 출력

import sys
from collections import deque
# sys.stdin = open("input.txt","r")
input = sys.stdin.readline

# 입력

# 관계설정하고 +a 노드별로 화살표 받은 개수도 설정
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)] #[[], [], [], []]
edges_count = [0 for _ in range(N+1)] #화살표 받은 개수 세려고 만든 배열
que=deque() #화살표 0개인 놈들 저장할 임시 저장할 공간
answer=[] #정답을 기록할 배열

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b) #1, 3
    edges_count[b]+=1
# print(edges_count) #[0, 0, 0, 2]

# 화살 하나도 못받은 놈들이 있는지 edges_count에서 전수 조사(그놈이 가장 선행되는 놈이거든!)
for i in range(1, N+1):
    if edges_count[i] == 0:
        #화살표 못 받은 놈들은 중요한 놈들임
        que.append(i)

# 주머니에 뭐 있는지 체크하고 있으면 아래 시행
while que:
    # 주머니에서 꺼내면서 답으로 기록하고(화살표 못받은 놈들이 더 원조라서 못받은거임)
    tmp=que.popleft() #tmp =1 
    answer.append(tmp)
    # 주머니에서 꺼낸 놈에게 총맞은 놈들 전수조사(for)해서 간선을 1씩 줄여주는 작업해야함
    for i in graph[tmp]: #3
        edges_count[i] -= 1
        if edges_count[i] == 0:
            que.append(i)
print(*answer)
        
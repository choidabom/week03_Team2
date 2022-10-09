# https://www.acmicpc.net/problem/11724
# 9시 반 시작

# 입력받을 때 노드와 간선들 관계 먼저 배열이나 딕셔너리로 받아주고 
# for로 노드들을 다 도는데(dfs로)
#   if 노드가 단독인 놈들이 아닌 경우 실행 (이코드는 안써도 되는게 문제 조건 상 단독일 수가 없음-입력에서 1, 2 이렇게 두개씩 주어지니까)
#     123 관계 부터 한다 치면) 방문한 곳은 true로 처리해 (예를들어 1에서 출발하면 2갔지 그럼 2는 5만가면 되지 1을 또 갈 필요는 없다. 3과 4는 애당초 관계설정 해놓은 배열에 없으니까 안가고)
#     다 돌았으면 정답 카운트 +1
    
#     34 관계도 반복
#     다 돌았으면 정답 카운트 +1
#   else:(단독이면)
#     pass(for문으로 돌아가)
# 정답 카운트 출력



# 1. 입력 및 관계 설정 
import sys
sys.setrecursionlimit(10**9)  #오 진짜로 이거 없으니까 런타임 에러 뜨네? 추가하니까 사라짐
N,M = map(int, sys.stdin.readline().split())
edges = [[] for _ in range(N+1)]
# [[], [], [], [], [], [], []]

# 2. dfs함수
def dfs(i):
  visited[i] =True
  for itr_edges in edges[i]: #2,5
    if visited[itr_edges] == False:
      dfs(itr_edges)
  

for _ in range(M):
  a,b=map(int,sys.stdin.readline().split())
  edges[a].append(b)
  edges[b].append(a)
# [[], [2, 5], [1, 5], [4], [3, 6], [2, 1], [4]]

visited = [False] * (N+1)
count= 0
# print(visited)
for i in range(1,N+1): #1부터 N까지
  if visited[i] == False:
    count += 1
    dfs(i)

print(count)
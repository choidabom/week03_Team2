import sys
sys.stdin = open("21606/input.txt","r")
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

'''문제 풀이 논리
1. 실외 점을 기준으로 인접해있는 실내 노드 개수를 count 한다.
2. 실외 점을 중간에 놓고 실내 점 n개가 붙어있을 때 갈 수 있는 경로의 수는 n * 1(중간 실외 점 선택) * (n-1) = n*(n-1)에 해당.
3. 실외 노드끼리 연결되는 경우는 1) 실외끼리 인접 노드로 연결될 때 2) 중간에 실내 노드를 끼고 연결할 때.
'''
# dfs(): 실외 정점과 연결된 실내 정점의 개수를 확인하는 메서드
def dfs(current: int, count:int):
    visited[current] = True         # 호출시 현재 정점(실외)에 대한 방문 체크

    # 현재 정점(실외)에서 갈 수 있는 정점(next) 순회
    for next in path[current]:
        # next가 실내일 경우
        if A[next] == '1':
            count += 1
        # next가 실외이고, 방문하지 않았을 경우
        elif visited[next] is False and A[next] == '0':
            # next(실외)에서 갈 수 있는 정점들을 탐색하기 위해 재귀 호출
            count = dfs(next, count)
    
    # 현재 정점(실외)에서 도달 가능한 실내 정점의 개수를 return 
    return count

n = int(input().rstrip())           # 전체 정점의 수
A = ' ' + input().rstrip()                # 정점의 실내/실외 정보를 담은 문자열. index와 정점번호를 맞춰주기 위해 공백 한 칸(' ')을 앞에 붙여줌
path = [[] for _ in range(n+1)]     # 인접 리스트 형태로 경로를 입력 받음
visited = [False] * (n+1)           # 방문 여부를 확인하기 위한 bool type 배열
answer = 0                          # 가능한 서로 다른 산책 경로의 수 (정답)

# n개의 정점을 n-1개의 간선으로 이어줌
for _ in range(n-1):
    u, v = map(int, input().split())
    # 방향이 존재하지 않기 때문에 입력된 간선의 두 정점 인접 리스트에 서로를 넣어줌
    path[u].append(v)
    path[v].append(u)

    # 연결된 두 정점이 모두 실내일 경우 경로가 2개(v->u, u->v) 생김
    if A[u] == '1' and A[v] =='1':
        answer += 2

# 전체 정점을 순회
for i in range(1, n+1):
    # 방문하지 않은 실외 정점을 시작으로 탐색
    if A[i] == '0' and visited[i] is False:
        count = dfs(i, 0)   # 현재 실외 정점에서 도달 가능한 실내 정점의 개수
        # '현재 실외 정점에 연결된 실내 정점간 연결 가능한 경우의 수 (n*(n-1))가
        # 현재 실외 정점을 포함한 '서로 다른 산책 경로의 수'이므로, 계산 후 가능한 전체 경로의 수에 더해줌
        answer += count * (count-1)

sys.stdout.write(f'{answer}')
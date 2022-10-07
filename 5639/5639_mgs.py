import sys
sys.setrecursionlimit(10**9) # 재귀 허용 깊이를 늘려줌(파이썬은 기본적으로 재귀 허용이 낮음)

def dfs(start, end) :

    if start > end :    
        return  # 함수에서 return을 만나면 함수가 종료됨

    mid = end + 1

    # 서브 트리 찾기
    for i in range(start + 1, end + 1) :    # start가 기준이기 때문에, i는 start+1부터. end 선언을 루트값을 제외한(len(graph)-1)로 했기 때문에 end+1
        if graph[start] < graph[i] :    # 이진탐색트리 만드는 방법. left는 루트보다 적고, right는 루트보다 크게. 
            mid = i
            break

    dfs(start+1, mid-1) # 왼쪽 서브트리 재귀 탐색(계속 루트값을 바꿔가면서 출력하기)
    dfs(mid, end)   # 오른쪽 서브트리 재귀탐색

    print(graph[start])

graph = []
# 입력이 언제까지 일지 모르기 때문에 while True: try, except을 활용해야한다.

while True :

    try :
        graph.append(int(sys.stdin.readline().rstrip()))

    except :
        break
# print(graph)
dfs(0, len(graph) - 1)
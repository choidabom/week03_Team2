# 이 풀이가 왼쪽, 오른쪽 노드를 새로운 배열에 넣는다는 점에서 메모리를 많이 차치하고 시간도 오래걸리긴 하는데 더 직관적이긴 함.
import sys
input = sys.stdin.readline
#recursion error 방지 : 파이썬은 1000번만 재귀를 허용해서 이거 설정안해주면 다 맞게했는데도 런타임 에러 떠서 억울하게 틀리는 상황 발생가능.
sys.setrecursionlimit(10**9)

arr = []
while True:  
    try:
        x = int(input())
        arr.append(x)
    except:
        break
# 입력을 다이나믹하게(사용자랑 소통하면서) 받는 방법(사용자가 입력을 멈추기 전까지 계속 입력을 받는법)
# 지금까지 입력은 입력의 끝부분이 언제까지인게 정해져있었는데 ex) 10까지만 작동하는 프로그램이고 11번째부터는 버그가 생김
# 근데 아래 코드는 일단 while이 실행되면서 고객한테 입력을 받다가 → 고객이 이제 그만 입력할래.. 하고 엔터를 치면? 
# 일단 while이 실행되고 append쪽에서 넣을 값이 없는데 배열에 추가하려하니 에러가 뜰거다. 그럼 그때서야 while문을 탈출하는 로직임.

def solution(A):
    # 받은 배열 길이가 0이면 return
    if len(A) == 0:
        return

    tempL, tempR = [], []

    # preorder순회는 첫번재 값이 루트니까 배열의 첫번째 값을 루트 노드로 설정
    mid = A[0]
    # 나머지 배열에 대해 for문을 돌면서 루트보다 커지는 부분을 기록해서 L과 R로 나눈다.
    for i in range(1, len(A)):
        if A[i] > mid:
            tempL = A[1:i]
            tempR = A[i:]
            break
        else:
    	#모두 mid보다 작은 경우라면 오른쪽은 없다는 소리니까 tempR는 없다.
            tempL = A[1:] 
            #재귀가 대체 언제 끝나는가? 딱 보면 안보이는데 디버거 돌려보면
            #예를들어 루트가 5처럼 딱 하나만 있으면 A[1:]해버리면 포함이 안되겠지? A[0:]이면 5도 포함될텐데..
            #그럼 len(tempL)에는 아무것도 안들어있으니까 if len(A) == 0: return 에서 재귀가 끝나게 됨.

    
    #문제가 요구하는 postorder순서로 왼쪽, 오른쪽 순으로 재귀 후 루트 노드 값 출력
    solution(tempL)
    solution(tempR)
    print(mid)

solution(arr)
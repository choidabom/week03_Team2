# 5639: 이진 검색 트리
# 노드의 왼쪽 서브 트리에 있는 모든 노드의 키는 노드의 키보다 작다.
# 노드의 오른쪽 서브 트리에 있는 모든 노드의 키는 노드의 키보다 크다. 
# 왼쪽, 오른쪽 서브트리도 이진 검색 트리이다. 

# 출력: 입력으로 주어진 이진 검색 트리를 후위 순회한 결과 출력하라 ~!
import sys
sys.stdin = open("RETRY/이진검색트리/input.txt","r")
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def postorder(preorder):
    if len(preorder) == 1: # 마지막 노드인 것
        print(preorder[0])
        return 
    if len(preorder) == 0: # 혹시 빈 배열이 걸린다면 아무것도 하지 않는다. 
        return 

    divider = 0
    root = preorder[0]
    for i in range(1, len(preorder)):
        if preorder[i] > root:
            divider = i
            break
    if divider:
        postorder(preorder[1:divider]) # 왼쪽 자식 노드
        postorder(preorder[divider:]) # 오른쪽 자식 노드
        print(preorder[0]) # 루트 
    else:
        postorder(preorder[1:])
        print(preorder[0])

preorder = []
while True:
    try:
        preorder.append(int(input()))
    except:
        break

postorder(preorder)
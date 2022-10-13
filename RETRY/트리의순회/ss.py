from sys import stdin, setrecursionlimit
setrecursionlimit(10**9)


def postorder(preorder, inorder):
    #종료 조건: len(preorder)가 2이하일 때
    if len(preorder) == 0:
        return # 왼쪽 자식 노드가 더이상 없음.
    elif len(preorder) ==1: # 노드 자신 뿐임. 
        print(preorder[0], end = ' ') # 전위순회의 노드 자신이자, 인덱스 0에 위치
        return
    elif len(preorder) == 2:
        print(preorder[1], preorder[0], end = ' ')
        return
    
    #노드 개수가 3이상부터면 재귀로 쪼갠다. 왼쪽/오른쪽/자기자신을 구분짓고 왼쪽/오른쪽 각각에 대해 재귀 돌리면 오케이
    root = preorder[0] # preorder[0]은 자기 자신! 전위순회는 루트>왼쪽>오른쪽이기에 인덱스 0이 루트 
    div = inorder.index(root) 
    
    #여기서부터 재귀
    # 전위순회: 루트 > 왼쪽 > 오른쪽
    # 중위순회: 왼쪽 > 루트 > 오른쪽
    # 후위순회: 왼쪽 > 오른쪽 > 루트
    postorder(preorder[1:div+1], inorder[0:div])
    postorder(preorder[div+1:], inorder[div+1:])
    print(preorder[0], end = ' ')

test_num = int(stdin.readline())

for _ in range(test_num):
    node_num = int(stdin.readline())
    preorder = list(map(int, stdin.readline().split())) # 전위순회
    inorder = list(map(int, stdin.readline().split()))  # 중위순회
    postorder(preorder, inorder)    # 후위순회
    print()
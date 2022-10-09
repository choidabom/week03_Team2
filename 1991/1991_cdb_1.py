# 1991: 트리 순회

import sys
# 트리의 순회(Tree Traversal)
class Node:
    def __init__(self, item, left, right):
        # item은 본인(root node가 됨), left, right는 각각 child node가 됨.
        self.item = item    # 부모 노드 저장
        self.left = left    # 왼쪽 자식 노드
        self.right = right  # 오른쪽 자식 노드

# 재귀 활용     
def preorder(node): # 전위 순회: 자기 자신 방문 -> 왼쪽 자식 -> 오른쪽 자식
    print(node.item, end="")
    if node.left != '.':
        preorder(tree[node.left])
    if node.right != '.':
        preorder(tree[node.right])

def inorder(node):  # 중위 순회: 왼쪽 자식 -> 자기 자신 방문 -> 오른쪽 자식
    if node.left != '.':
        inorder(tree[node.left])
    print(node.item, end="")
    if node.right != '.':
        inorder(tree[node.right])

def postorder(node):    # 후위 순회: 왼쪽 자식 -> 오른쪽 자식 -> 자기 자신 방문
    if node.left != '.':
        postorder(tree[node.left])
    if node.right != '.':
        postorder(tree[node.right])
    print(node.item, end="")

# 전체적인 구성은 똑같고 출력 위치만 바꿔주면 된다.
# if(left)/if(right)/print(자기자신)의 순서만 다르기 때문에 이에 유념해서 클래스를 생성해 코드는 짜면 된다.

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    tree = {}
    for _ in range(N):
        # 항상 A가 루트 노드가 된다.
        node, left, right = map(str, input().split())
        tree[node] = Node(item=node, left=left, right=right)

    preorder(tree['A'])
    print()
    inorder(tree['A'])
    print()
    postorder(tree['A'])

# 출력 값
# ABDCEFG
# DBAECFG
# DBEGFCA
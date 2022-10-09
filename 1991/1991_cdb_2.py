import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
# print = sys.stdout.write

n = int(input())
nodes = dict()

for _ in range(n):
    temp = input().split()
    # nodes라는 딕셔너리의 key 값에 root가 들어가고, value에 리스트 형태로 자식 노드들이 들어감
    nodes[temp[0]] = [temp[1], temp[2]]

# 딕셔너리의 키-값 쌍으로 출력하는 방법
# for key, value in nodes.items():
#     print(key, value)

def preorder(root): # 전위순회
    if root == '.':
        return
    print(f'{root}', end="")
    preorder(nodes[root][0])
    preorder(nodes[root][1])

def inorder(root):  # 중위순회
    if root == '.':
        return
    inorder(nodes[root][0])
    print(f'{root}', end="")
    inorder(nodes[root][1])

def postorder(root): # 후위순회
    if root == '.':
        return
    # nodes[root][0]와 nodes[root][1]는 root의 자식노드 !
    postorder(nodes[root][0]) # 왼쪽 자식 노드
    postorder(nodes[root][1]) # 오른쪽 자식 노드
    print(f'{root}', end="")          # 노드 방문

# temp[0] == 'A' 일 때~
preorder('A')
print()
inorder('A')
print()
postorder('A')
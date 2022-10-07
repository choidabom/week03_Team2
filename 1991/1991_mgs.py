import sys
sys.stdin = open("1_input.txt","r")

n = int(input())

insert_list = list(list(sys.stdin.readline().rstrip().split()) for _ in range(n))
# print(insert_list)

class Node() :
    def __init__(self, item, left, right) :
        self.item = item
        self.left = left
        self.right = right

def preorder(node) :
    print(node.item, end= '')   # 루트
    if node.left != '.' :
        preorder(tree[node.left]) # 왼쪽
    if node.right != '.' :
        preorder(tree[node.right])  # 오른쪽

def inorder(node) :
    if node.left != '.' :   # 왼쪽
        inorder(tree[node.left])
    print(node.item, end = '')  # 루트
    if node.right != '.' :      # 오른쪽
        inorder(tree[node.right])

def postorder(node) :
    if node.left != '.' :   # 왼쪽
        postorder(tree[node.left])
    if node.right != '.' :  # 오른쪽
        postorder(tree[node.right]) 
    print(node.item, end = '') # 루트

tree = {}
for item, left, right in insert_list:
    tree[item] = Node(item, left, right)

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])

""" dict

graph = {}

for _ in range(n):
    p, c1, c2 = sys.stdin.readline().rstrip().split()

    graph[p] = [c1, c2] # root를 key, left, right 자식들을 value로 할당함.

    # 예) graph['A'][0] : A를 key로 가지는 value인 B를 인덱싱하는 방법

# print(insert_list)

def preorder(N):
    global graph

    if N in graph:
        print(N, end="")
        preorder(graph[N][0])
        preorder(graph[N][1])


def inorder(N):
    global graph

    if N in graph:
        inorder(graph[N][0])
        print(N, end="")
        inorder(graph[N][1])


def postorder(N):
    global graph

    if N in graph:
        postorder(graph[N][0])
        postorder(graph[N][1])
        print(N, end="")



preorder('A')
print()
inorder('A')
print()
postorder('A')
"""
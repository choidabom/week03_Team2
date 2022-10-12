# 1991: 트리 순회
# 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드

import sys
from collections import defaultdict
sys.stdin = open("RETRY/트리순회/input.txt","r")
input = sys.stdin.readline

def preorder(root): # 전위 순회: 노드 자신을 방문 => 왼쪽 자식 노드 방문 => 오른쪽 자식 노드 방문
    if root == '.':
        return
    print(f'{root}', end="")
    preorder(graph[root][0]) # graph의 root 노드의 왼쪽 자식
    preorder(graph[root][1]) # graph의 root 노드의 오른쪽 자식

def inorder(root): # 중위 순회: 왼쪽 자식 노드 방문 => 노드 자신을 방문 => 오른쪽 자식 노드 방문
    if root == '.':
        return
    inorder(graph[root][0])
    print(f'{root}', end="")
    inorder(graph[root][1])

def postorder(root): # 후위 순회: 왼쪽 자식 노드 방문 => 오른쪽 자식 노드 방문 => 노드 자신을 방문
    if root == '.':
        return
    postorder(graph[root][0])
    postorder(graph[root][1])
    print(f'{root}', end="")

# N: 이진 트리의 노드의 개수
N = int(input().rstrip())
graph = defaultdict(list)
for i in range(N):
    # graph라는 딕셔너리의 key값에 root가 들어가고, value에 리스트 형태의 자식 노드들이 들어감.
    tmp = list(input().split())
    graph[tmp[0]].append(tmp[1])
    graph[tmp[0]].append(tmp[2])
    
# graph를 defaultdict로 선언했기 떄문에 graph를 출력하면
# defaultdict(<class 'list'>, {'A': ['B', 'C'], 'B': ['D', '.'], 'C': ['E', 'F'], 'E': ['.', '.'], 'F': ['.', 'G'], 'D': ['.', '.'], 'G': ['.', '.']}) 다음과 같이 나온다.

# print(graph['A'])를 출력하면 ['B', 'C']의 결과가 나온다. so, root의 값을 'A'로 준다. 

preorder('A')
print()
inorder('A')
print()
postorder('A')
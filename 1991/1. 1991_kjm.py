# https://www.acmicpc.net/problem/1991
import sys
 
N = int(sys.stdin.readline().strip())
tree = {}
 
for n in range(N):
    root, left, right = sys.stdin.readline().strip().split()
<<<<<<< HEAD
    tree[root] = [left, right]
 
 
def preorder(root): #루트먼저 처리하면 pre
    if root != '.':
=======
    tree[root] = [left, right] #{"root"="[left,right]"}
 
 
def preorder(root): #루트먼저 처리하면 pre
    if root != '.': #preorder라는 함수의 핵심은 다 제끼고 print를 하는거임 preorder재귀를 말로 설명해보면 Root 프린트하고, left프린트하고, right도 프린트하는거임.
>>>>>>> jaemin
        print(root, end='')  # root
        preorder(tree[root][0])  # left
        preorder(tree[root][1])  # right
 
 
def inorder(root):
    if root != '.':
        inorder(tree[root][0])  # left
        print(root, end='')  # root
        inorder(tree[root][1])  # right
 
 
def postorder(root):
    if root != '.':
        postorder(tree[root][0])  # left
        postorder(tree[root][1])  # right
        print(root, end='')  # root
 
 
preorder('A')
print()
inorder('A')
print()
postorder('A')
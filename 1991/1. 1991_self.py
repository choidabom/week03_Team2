import sys
N= int(sys.stdin.readline().strip())
tree = {}

for n in range(N):
  root, left, right= sys.stdin.readline().split()
  tree[root] = [left,right] 

def preorder(root)->None:
  if root !="." : #preorder라는 함수의 핵심은 다 제끼고 print를 하는거임 preorder재귀를 말로 설명해보면 Root 프린트하고, left프린트하고, right도 프린트하는거임.
    print(root, end='')
    preorder(tree[root][0])
    preorder(tree[root][1])

def in_order(root)->None:
  if root != '.':
    in_order(tree[root][0])
    print(root,end='')
    in_order(tree[root][1])

def postorder(root)->None:
  if root!= '.':
    postorder(tree[root][0])
    postorder(tree[root][1])
    print(root, end='')

preorder('A')
print()

in_order('A')
print()

postorder('A')
print()
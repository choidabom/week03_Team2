import sys
sys.setrecursionlimit(10**8)
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
class Node:
    def __init__(self, key, idx, left, right):
        self.key = key
        self.left = left
        self.right = right
        self.idx = idx

class BinarySearchTree:
    def __init__(self):
        self.root = None
    def add(self, key, idx):
        def add_node(node, key, idx):
            if key < node.key:
                if node.left is None:
                    node.left = Node(key, idx, None, None)
                else:
                    add_node(node.left, key, idx)
            else:
                if node.right is None:
                    node.right = Node(key, idx, None, None)
                else:
                    add_node(node.right, key, idx)
            return True
        if self.root is None:
            self.root = Node(key, idx, None, None)
            return True
        else:
            return add_node(self.root, key, idx)
    def dump(self):
        def print_subtree(node):
            if node is not None:
                print_subtree(node.left)
                print_subtree(node.right)
                print(node.key)
        print_subtree(self.root)
bst = BinarySearchTree()
idx = 1

while True:
    node = input().rstrip()
    if not node:
        break
    bst.add(int(node), idx)
    idx += 1
bst.dump()
# 들어오는 순서 -> 전위 순회 인걸 최대한 이용해야할듯
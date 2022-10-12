# 2263: 트리의 순회
# https://backtony.github.io/algorithm/2021-02-17-algorithm-boj-class4-17/
# n개의 정점을 갖는 이진 트리의 정점에 1부터 n까지의 번호가 중복없이 매겨져 있다.

# 1. 트리 전체에서 보면 후위 순회의 제일 마지막 값은 루트 노드에 해당한다.
# 2. 중위 순회에서 루트 노드에 해당하는 값의 인덱스를 기준으로 보면 왼쪽은 루트노드 기준 왼쪽 서브 트리, 오른쪽은 오른쪽 서브트리에 해당한다.
# 3. 전위 순회 출력이 목적이므로 현재의 루트를 찍고 왼쪽부터 재귀 반복, 오른쪽 재귀 반복한다.

# 모오오오오르겠다 ^^

import sys
sys.setrecursionlimit(10**6)
sys.stdin = open("RETRY/트리의순회/input.txt","r")
input = sys.stdin.readline

def preorder(in_left, in_right, po_left, po_right):
    # 역전되면 구분할 노드가 없는 것
    if in_left > in_right or po_left > po_right:
        return 
    
    root = postorder[po_right]
    print(root, end=" ")

    left = idx[root] - in_left      # 왼쪽 개수
    right = in_right - idx[root]    # 오른쪽 개수

    # 전위이므로 루트찍고 왼쪽부터
    preorder(in_left, in_left+left-1, po_left, po_left+left-1)
    # 오른쪽 
    preorder(in_right-right+1, in_right, po_right-right, po_right-1)

n = int(input().rstrip())
inorder = list(map(int, input().split()))   # 중위 순회 
postorder = list(map(int, input().split())) # 후위 순회

idx = [0] * (n+1)
# 후위순회의 끝값이 중위 순회의 어디 인덱스에 위치한지 확인을 위해
# 중위순회의 값들의 인덱스 값을 저장
for i in range(n):
    idx[inorder[i]] = i

preorder(0, n-1, 0, n-1)
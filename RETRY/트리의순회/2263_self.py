# 2263: 트리의 순회
# 후위 순회에서 부모 노드를 찾아 중위 순회에서 기준으로 삼아 왼쪽, 오른쪽으로 나눈다.
# 그리고 왼쪽 자식 트리 노드, 오른쪽 자식 트리 노드를 순회하며 앞의 과정을 반복한다. 
# 이해할 듯 모르겠다................................
import sys
sys.setrecursionlimit(10**6)
sys.stdin = open("RETRY/트리의순회/input.txt","r")
input = sys.stdin.readline

n = int(input())
in_order = list(map(int, input().split()))
po_order = list(map(int, input().split()))

pre = [0] * (n+1)
for i in range(n):
    pre[in_order[i]] = i

def preorder(in_start, in_end, po_start, po_end):
    if (in_start > in_end) or (po_start > po_end):
        return 
    root = po_order[po_end] # 후위순회의 마지막 인덱스에 루트가 있다. 
    print(root, end=" ")

    # 왼쪽 서브 트리의 노드 수
    left = pre[root] - in_start
    # 오른쪽 서브 트리의 노드 수
    right = in_end - pre[root]

    preorder(in_start, in_start+left-1, po_start, po_start+left-1)
    preorder(in_end-right+1, in_end, po_end-right, po_end-1)

preorder(0, n-1, 0, n-1)
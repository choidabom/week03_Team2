# 2263: 트리의 순회
# 후위 순회에서 부모 노드를 찾아 중위 순회에서 기준으로 삼아 왼쪽, 오른쪽으로 나눈다.
# 그리고 왼쪽 자식 트리 노드, 오른쪽 자식 트리 노드를 순회하며 앞의 과정을 반복한다. 
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

# 전위 순회
def divide(in_start, in_end, p_start, p_end):
    if (in_start > in_end) or (p_start > p_end):
        return
    root = po_order[p_end] # 후위순회에서 root 찾기
    print(root, end=" ")

    left = pre[root] - in_start # 왼쪽 인자 갯수
    right = in_end - pre[root] # 오른쪽 인자 갯수

    divide(in_start, in_start+left-1, p_start, p_start+left-1) # 왼쪽 노드
    divide(in_end-right+1, in_end, p_end-right, p_end-1) # 오른쪽 노드

divide(0, n-1, 0, n-1)
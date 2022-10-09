# 5639: 이진 탐색 트리
import sys
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
print = sys.stdout.write

preorder = []
while True:
    try:
        preorder.append(int(input().rstrip()))
    except:
        break

def solution(root_index, end):
    if root_index > end:
        return 
    if root_index == end:
        print(f'{preorder[root_index]}\n')
        return
    m = binary_search(root_index+1, end, preorder[root_index])
    solution(root_index+1, m-1)
    solution(m, end)
    print(f'{preorder[root_index]}\n')

def binary_search(start, end, key):
    while start < end:
        mid = (start + end) // 2
        if preorder[mid] > key:
            end = mid
        else:
            start = mid + 1

    return end if preorder[end] > key else end + 1

# 인덱스 0부터 len(preorder)-1 까지
solution(0, len(preorder)-1)
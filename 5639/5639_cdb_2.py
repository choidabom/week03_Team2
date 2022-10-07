# 5639: 이진 탐색 트리

import sys
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**9)

# dfs 탐색
def postorder(start, end):
    # 시작과 끝 값이 역전시 리턴
    if start > end:
        return
    temp = end + 1
    # 서브 트리 찾기
    for i in range(start+1, end+1):
        # 루트 보다 크면 오른쪽 서브 트리
        if preorder[start] < preorder[i]:
            temp = i
            break
    postorder(start+1, temp-1) # 왼쪽 서브 트리 재귀적으로 탐색
    postorder(temp, end) # 오른쪽 서브 트리 재귀적으로 탐색

    print(preorder[start])
                
# 입력 개수를 모르기에 while문과 try-except문을 통해 입력 받음
preorder = []
while True:
    try:
        preorder.append(int(input()))
    except:
        break

postorder(0, len(preorder)-1)

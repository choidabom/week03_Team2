# 5639: 이진 검색 트리
# 노드의 왼쪽 서브 트리에 있는 모든 노드의 키는 노드의 키보다 작다.
# 노드의 오른쪽 서브 트리에 있는 모든 노드의 키는 노드의 키보다 크다. 
# 왼쪽, 오른쪽 서브트리도 이진 검색 트리이다. 

# 출력: 입력으로 주어진 이진 검색 트리를 후위 순회한 결과 출력하라 ~!
import sys
sys.stdin = open("RETRY/이진검색트리/input.txt","r")
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def postorder(start, end):
    # start와 end는 arr의 시작 idxd와 끝 idx임.
    if start > end: 
        return
    # 순회는 재귀호출을 통해 자식노드를 순회하기 때문에 자식노드의 여부를 확인하여야함.
    root = preorder[start]
    idx = start + 1
    
    while idx <= end:
        if preorder[idx] > root:
            break
        idx += 1
        # preorder의 특징은 root > left > right 순으로 순회한다.
        # binary search tree의 특징은 left child는 root보다 작은 value가 들어가며 right child는 root보다 큰 숫자가 들어간다는 점이다.
        # 이러한 점을 이용하여 list에서 root보다 큰 숫자가 위치한 idx가 어디인지 확인할 수 있다. 

    postorder(start+1, idx-1)
    postorder(idx, end)
    print(root)
    # 문제에서 요구하는 것은 입력으로 주어진 이진 검색 트리를 후위순회하는 것이다.
    # 해당 함수는 root와 left, right를 구분했고 해당 함수를 left, right, root 순으로 다시 호출하여, 후위 순회를 완료하게 된다.
    
preorder = [] # 트리를 전위 순회한 결과 주어짐
while True: # 입력받는 값만 알고 입력의 개수를 모를 때
    try:
        preorder.append(int(input()))
    except:
        break
# 입력되는 값의 개수가 정해지지 않았기 때문에 반복문을 통해서 값을 리스트로 입력받게 될 경우 별도의 종료 조건을 설정하여야함.
# 예외처리를 하지 않으면 ValueError: invalid literal for int() with ~~ 가 발생되며 스크립트 실행이 중단됨.
# 따라서 이를 방지하기 위해 예외가 발생했을 때(except) 반복문을 종료하여 스크립트가 계속 실행되도록 함.

postorder(0, len(preorder)-1)


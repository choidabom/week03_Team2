# https://www.acmicpc.net/problem/5639
# 이 코드 짠사람이 변수명을 지랄같이 짜놔서 겁나 헷갈리긴 하는데.. 장점이 있음
# b1과 비교했을 때 메모리 쓰는게 10분의 1임. (왼쪽 노드, 오른쪽 노드의 배열을 따로 선언하지 않고 포인터로 구현했거든..)
import sys

sys.setrecursionlimit(10 ** 9)
preorder = []
while True:
    try:
        preorder.append(int(sys.stdin.readline()))
    except:
        break
postorder = []


def postorderset(preorder, left, right):
    if left > right: #이분탐색때처럼 왼쪽과 오른쪽이 바뀌는 순간 재귀 종료.
        return
    root = preorder[left]
    ls = left + 1 #left start의 줄인말(왼쪽 노드 시작)
    re = right
    rs = right + 1 #right start의 줄인말 (오른쪽 노드 시작)
    for i in range(right - left + 1): #왜 +1을 해줘야하나 한참 생각했는데 for i in n하면 n 미만까지 출력하지? 그럼 for i in n-1로 하면 n-2까지만 출력됨
        if i == 0:
            continue
        if preorder[left + i] > root:
            rs = left + i  # 루트보다 첫번째로 커지는 수를 오른쪽 프리오더의 시작으로 정해준다
            break
    le = rs - 1  #rs가 처음 루트보다 preorder[i]가 커진 순간이라면 ls는 i-1까지이겠지? 
<<<<<<< HEAD
    # 98루트는 52,60처럼 지가 젤 큰데 이놈은 어떻게 루프가 도는지 설명해보면, 자기보다 오른쪽으로 큰게 없으니 for 안에는 못들어가고 그냥 le = rs - 1 실행되는데 rs가 for문 못돌았으니 그냥 rs+1이니 le =rs(왼쪽 끝과 오른쪽 시작이 같다 => 하나다)
=======
    # 98루트는 52,60과 비교하면 지가 젤 큰데 이놈은 어떻게 루프가 도는지 설명해보면, 자기보다 오른쪽으로 큰게 없으니 23번줄 for문 안에는 못들어가고 그냥 le = rs - 1 실행되는데 rs가 for문 못돌았으니 그냥 rs+1이니 le =rs(왼쪽 끝과 오른쪽 시작이 같다 => 하나다)
>>>>>>> jaemin

    # 여기 아랫 부분이 후위 순회를 구현한 부분임 postorder의 본질은 루트를 postorder라는 배열에 찔러넣는 함수인데.
    # 왼쪽 먼저 찔러넣고, 오른쪽 찔러넣고, 비로소 루트에 찔러넣고 있다. => 후위순회를 구현한 것.
    postorderset(preorder, ls, le)  # 왼쪽 프리오더 순환
    postorderset(preorder, rs, re)  # 오른쪽 프리오더 순환
    postorder.append(root)  # 더이상 재귀가 돌지 않을 때까지 돌고(le와 rs가 뒤바뀔때) 그때의 root를 (5임) preorder 리스트에 추가하고 root 5재귀는 스택에서 pop됨
                            # 그다음 재귀인 root가 28이 postorder에 들어가고 재귀 28은 pop (잘봐.. append까지 들어가고 나서 pop임! 재귀 끝나고 바로 pop이 아니라. )
                            # 쭉 가다보면 30이 나오는데 왼쪽인 24는 이미 postorder에 박았고(왼쪽 프리오더 순환 끝났다는 이야기) 오른쪽 45를 postorder에 박으면서 오른쪽 프리오더 끝나고, 비로소 24, 45의 루트인 30을 postorder에 박으면서 질질 끌었던 재귀가 스택에서 pop됨  
    
<<<<<<< HEAD
    # 98부터 우측편은 노드가 서브트리가 하나씩 밖에 없는데 그 작동 방법을 아직 이해 못햇음.
=======
>>>>>>> jaemin
postorderset(preorder, 0, len(preorder) - 1)
for i in postorder:
    print(i)

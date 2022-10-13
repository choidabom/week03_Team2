from typing import Any, Type
from __future__ import annotations

class Node:
    # 이진 검색 트리의 노드
    def __init__(self, key: Any, value: Any, left: Node = None, right: Node = None):
        # 생성자 (constructor)
        self.key = key # 키
        self.value = value # 값
        self.left = left    # 왼쪽 자식 포인터
        self.right = right  # 오른쪽 자식 포인터
        
class BinarySearchTree:
    # 이진 검색 트리

    def __init__(self):
        # 초기화
        self.root = None    # root 
        # 노드가 하나도 없는 빈 트리 생성
    def search(self, key: Any) -> Any:
        # 키가 key 인 노드를 검색
        p = self.root   # 루트에 주목
        while True:
            if p is None:   # 더 이상 진행할 수 없으면
                return None # 검색 실패
            if key == p.key:    # key 와 노드 p 의 키가 같으면
                return p.value  # 검색 성공
            elif key < p.key:   # key쪽이 작으면
                p = p.left      # 왼쪽 서브트리에서 검색
            else:               # key쪽이 크면
                p = p.right     # 오른쪽 서브트리에서 검색
    
    def add(self, key: Any, value: Any) -> bool:
        # 키가 key이고 값이 value인 노드 삽입
        
        def add_node(node: Node, key: Any, value: Any) -> None:
            # node 를 루트로 하는 서브트리에 키가 key, 값이 value인 노드를 삽입
            if key == node.key:
                return False    # key 가 이진검색트리에 이미 존재하면 False. 삽입 실패
            elif key < node.key:
                if node.left is None: # 왼쪽 자식 노드 없으면
                    node.left = Node(key, value, None, None)    # 그 자리에 노드 삽입. 종료
                else:
                    add_node(node.left, key, value) # 왼쪽 자식 노드 있으면 주목 노드 이동
            else:
                if node.right is None:
                    node.right = Node(key, value, None, None)
                else:
                    add_node(node.right, key, value)
            return True
        
        if self.root is None:   # 빈 트리에 삽입 시도 하면
            self.root = Node(key, value, None, None) # 삽입되는 애 노드로 생성해줌 걔는 지가 루트고 혼자 존재하는 트리 그 자체
            return True
        else:   # 빈 트리 아니면 위에서 만든 함수로 트리에 노드 추가
            return add_node(self.root, key, value)
    
    def remove(self, key: Any) -> bool:
        # 키가 key인 노드를 삭제
        p = self.root   # 스캔 중인 노드
        parent = None   # 스캔 중인 노드의 부모 노드
        is_left_child = True    # p는 parent의 왼쪽 자식인지 확인

        while True:
            if p is None:   # 더 이상 진행할 수 없으면
                return False    # 그 키는 존재하지 않음
            
            if key == p.key:    # key와 노드 p의 키가 같으면
                break           # 검색 성공
            else:
                parent = p      # 가지를 내려가기 전에 부모로 현재 노드 설정. 스캔위치 자식으로 내려가면 현재 노드가 부모가 될거에요
                if key < p.key: # key쪽이 작으면
                    is_left_child = True    # 왼쪽 자식으로 가요
                    p = p.left              # 왼쪽 서브트리에서 검색
                else:
                    is_left_child = False   # 여기서는 오른쪽 자식으로 가요
                    p = p.right             # 오른쪽 서브트리로 스캔 고    
        
        if p.left is None:      # p에 왼쪽 자식이 없으면
            if p is self.root:  # 근데 찾으려고 한 노드가 루트에 있었던 거면
                self.root = p.right # 그러면 루트가 없어질거니까 새루트로 p오른쪽 자식
            elif is_left_child: # p는 p.left 에서 온거 맞음 지금 parent 가 원래 p였음 = True 
                parent.left = p.right # p부모의 왼쪽 포인터가 p의 오른쪽 자식을 가리킴
            else:
                parent.right = p.right  # p부모의 오른쪽 포인터가 p의 오른쪽 자식을 가리킴
        elif p.right is None:   # p에 오른쪽 자식이 없으면
            if p is self.root:
                self.root = p.left
            elif is_left_child:
                parent.left = p.left    # p부모의 왼쪽 포인터가 p왼쪽 자식을 가리킴
            else:
                parent.right = p.left   # p부모의 오른쪽 포인터가 p왼쪽 자식을 가리킴
        else:   # p에 왼쪽 자식 있으면
            parent = p
            left = p.left
            is_left_child = True
            while left.right is not None:   # 왼쪽 서브트리에서 가장 큰 키 찾기
                parent = left   
                left = left.right           # 온쪾 서브브트리에서 오른쪾 자식으로 계속 타고 내려감
                is_left_child = False
            
            p.key = left.key                # 왼쪽 서브트리에서 가장 큰 키 복사해오기
            p.value = left.value            # 그 키의 값도 복사해와
            if is_left_child:
                parent.left = left.left     # 원래 꺼랑 연결 끊고 복사해온 키로 부모랑 새로 연결해주기
            else:
                parent.right = left.left    
        return True

    def dump(self, reverse = False) -> None:
        # 덤프 (모든 노드를 키의 오름차순으로 출력)
        def print_subtree(node: Node):
            # node를 루트로 하는 서브트리의 노드를 키의 오름차순으로 출력
            if node is not None:
                print_subtree(node.left)           # 왼족 서브트리를 오름차순으로 출력
                print(f'{node.key} {node.value}')   # node를 출력
                print_subtree(node.right)           # 오른쪽 서브트리를 오름차순으로 출력

        def print_subtree_rev(node: Node):
            # reverse 인자 False 로 들어오면 내림차순으로 출력
            if node is not None:
                print_subtree_rev(node.right)   # 오른쪽 서브트리 내림차순으로 출력
                print(f'{node.key} {node.value}')   # node 출력
                print_subtree_rev(node.left)    # 왼쪽 서브트리 내림차순으로 출력

        print_subtree(self.root) if reverse else print_subtree(self.root)

    def min_key(self) -> Any:
        # 가장 작은 키 찾아서 왼쪽으로 세상끝까지 따라가기
        if self.root is None:
            return None
        p = self.root
        while p.left is not None:
            p = p.left
        
        return p.key

    def max_key(self) -> Any:
        # 가장 큰 키 찾아요
        if self.root is None:
            return None
        p = self.root
        while p.right is not None:
            p = p.right
        
        return p.key
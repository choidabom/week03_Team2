# 이진 탐색 트리 구현하기

from __future__ import annotations

# 트리를 구성하는 노드 클래스
class Node:
    '''이진 검색 트리의 노드'''
    def __init__(self, key, value, left, right):
        '''생성자'''
        self.key = key      # 키
        self.value = value  # 값
        self.left = left    # 왼쪽 포인터
        self.right = right  # 오른쪽 포인터

class BinarySearchTree:
    # 생성자
    def __init__(self):
        '''초기화'''
        self.root = None    # 트리의 root를 세팅한다. 초기에는 아무값도 넣지 않았으니 빈캆으로 둔다.
    
    # 검색하는 메소드
    def search(self, key):
        '''키가 key인 노드를 검색'''
        node = self.root       # 루트에 주목
        while True:
            if node is None:       # 더 이상 진행할 수 없으면
                return False       # 검색 실패
            if key == node.key:    # key와 노드의 p의 키가 같으면
                return node.value  # 검색 성공
            elif key < node.key    # key 쪽이 작으면
                node = node.left      # 왼쪽 서브트리에서 검색
            else:               # key 쪽이 크면
                node = node.right     # 오른쪽 서브트리에서 검색

    # 노드 추가하는 메소드
    def add(self, key, value):
        # 노드 추가하는 내부 함수
        def add_node(Node, key, value):
            # 탐색하고 적절한 자리에 삽입
            if key == node.key: # 이미 삽입하려는 키가 있는 false 처리
                return False    
            # 삽입하려는 키가 현재 탐색 노드의 키보다 작다면
            elif key < node.key:
                # 그 탐색 노드의 왼쪽 자식이 없다면 바로 그 자리에 삽입
                if node.left is None:
                    node.left = Node(key, value, None, None)
                else:
                    # 자식이 있으면 재귀함수 호출로 한 번 더 들어감
                    add_node(node.left, key, value)
            # 삽입하려는 키가 현재 탐색 노드의 키보다 크다면
            else:
                # 그 탐색 노드의 오른쪽 자식이 없다면 바로 그 자리에 삽입
                if node.right is None:
                    node.right = Node(key, value, None, None)
                else:
                    # 자식이 있으면 재귀함수 호출로 한 번 더 들어감
                    add_node(node.right, key, value)
            return True
        
        # 루트가 있는 경우 ?????????????
        if self.root is None:
            self.root = Node(key, value, None, None)
            return True
        # 루트가 없는 경우
        else:   # 리턴값은 내부함수 리턴 값
            return add_node(self.root, key, value)

    # 노드 삭제하는 메소드
    def remove(self, key):
        node = self.root    # 현재 노드로 지정
        parent = None       # 현재 노드의 부모 노드
        is_left_child = True # node는 parent의 왼쪽 자식 노드인지 오른쪽 자식 노드인지 확인

        # 삭제할 노드 탐색
        while True:
            if node is None:
                return False
            if key == node.key: # key와 노드의 키가 같으면 검색 성공
                break
            else:
                parent = node
                if key < node.key:
                    node = node.left
                    is_left_child = True # 왼쪽 자식 노드로 내려가니까 플래그를 True로 설정
                else:
                    node = node.right
                    is_left_child = False # 오른쪽 자식 노드로 내려가니까 플래그를 False로 설정

        # 키를 찾은 뒤에 자식이 없는 노드이면 or 자식이 1개 있는 노드이면
        if node.left is None: # 왼쪽 자식이 없으면
            if node is self.root: # 만약 삭제 노드가 root이면, 바로 오른쪽 자식으로 대체한다.
                self.root = node.right
            # 아래의 parent는 탐색 시 찾은 노드의 바로 위 부모가 됨. (탐색 로직에서 그렇게 적용)
            # parent - node - node의 자식의 구도가 있으면 node라는 중간이 빠지기 때문에 parent의 자식과 node의 자식을 연결
            elif is_left_child: # 왼쪽 자식 노드가 있는 것이니까
                parent.left = node.right    # 부모의 왼쪽 참조가 오른쪽 자식을 가리킴
            else:               # 오른쪽 자식 노드가 있는 것이니까
                parent.right = node.right # 부모의 오른쪽 참조가 오른쪽 자식을 가리킴

        elif node.right is None: # 오른쪽 자식이 없으면
            if node is self.root: 
                self.root = node.left #만약 삭제 노드가 root이면, 바로 왼쪽 자식으로 대체한다.
            elif is_left_child:
                parent.left = node.left # 부모의 왼쪽 참조가 왼쪽 자식을 가리킴
            else:
                parent.right = node.left # 부모의 오른쪽 참조가 왼쪽 자식을 가리킴
        
        # 자식이 2개 있는 노드이면
        else: # 무조건 왼쪽 서브트리에서 대체할 노드를 찾는다. 왼쪽 서브트리에서 가장 큰 노드로 대체한다.
            parent = node
        # parent를 지정한 이유 : 지우는 노드로 지정되는데, 하위 자식 노드가 많으면 node 삭제 시 조정이 일어남. 
        # node말고 그 하위 노드들을 관리할 주체가 필요함. 
        # 그때 가장 하단의 자식 노드의 연결을 끊기위해 parent를 일단 삭제할 node로 지정.
            node_max_left = node.left # 왼쪽 서브트리에서 가장 큰 노드를 찾기 위해 초기값 설정
            is_left_child = True # 왼쪽 서브트리에서 가장 큰 노드가 부모 노드와 어떤 관계(왼쪽,오른쪽)인지 파악하기 위해 세팅
            
        # 가장 큰 노드를 찾기 위해 탐색
            while node_max_left.right is not None:
                parent = node_max_left
                node_max_left = node_max_left.right
                is_left_child = False

            # 가장 큰 노드를 찾았으니 삭제하려는 노드를 대체
            node.key = node_max_left.key
            node.value = node_max_left.value

            # is_left_child가 트루가 되려면, 삭제 노드의 왼쪽 서브트리중 오른쪽 자식이 없어야 함. 
            if is_left_child:
        # 무조건 node_max_left.left로 지정하는 이유 : 
        # 1. 가장 큰 노드가 왼쪽 자식을 갖고 있을 수 있음.
        # 2. 이미 오른쪽 자식 노드는 위에서 탐색을 완료했기 때문에 여기서 추가적인 오른쪽 자식 노드를 지정할 수 없다.
        # 3. 그러므로 삭제 노드의 left를 node_max_left의 left로 연결(자식이 없으면 None을 가지게 됨.) 
        # node_max_left의 왼쪽 자식 노드만 있거나 자식이 없는 경우만 가능. 자식이 없으면 None으로 적용됨.
                parent.left = node_max_left.left
            else:
                parent.right = node_max_left.left
        return True # 정상적으로 조정되었으니 true

    # 노드 출력하는 메소드
    def dump(self):
        def print_subtree(node):
            # 전위 순회로 출력
            if node is not None:
                print(f'{node.key} {node.value}')
                print_subtree(node.left)
                print_subtree(node.right)
        root = self.root
        print_subtree(root)
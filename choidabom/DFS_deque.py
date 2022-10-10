# DFS by deque
# 성능면에서 list() 형태보다 deque 형태가 훨씬 좋다.
graph = dict()
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

def dfs2(graph, start_node):
    from collections import deque
    visited = []
    need_visited = deque()
    # 시작 노드 설정해주기
    need_visited.append(start_node)

    # 방문이 필요한 리스트가 아직 존재한다면
    while need_visited:
        # 시작 노드를 지정하고
        node = need_visited.pop()

        # 만약 방문한 리스트에 없다면
        if node not in visited:
            # 방문 리스트에 노드를 추가
            visited.append(node)
            # 인접 노드들을 방문 예정 리스트에 추가
            need_visited.extend(graph[node])

    return visited

dfs2(graph, 'A')
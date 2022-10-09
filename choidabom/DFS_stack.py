# DFS by stack
# list에서 pop을 활용하면 성능면에서 떨어지는 단점이 있다.

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

def dfs(graph, start_node):
    # 기본은 항상 두 개의 리스트를 별도로 관리해주는 것
    # "앞으로 찾아가야할 노드"와 "이미 방문한 노드"를 기준으로 데이터를 탐색
    need_visited, visited = list(), list()
    # 시작 노드를 정하기
    need_visited.append(start_node)

    # 만약 아직도 방문이 필요한 노드가 있다면, 
    while need_visited:
        # 그 중에서 가장 마지막 데이터를 추출(스택 구조의 활용)
        node = need_visited.pop()

        # 만약 그 노드가 방문한 목록에 없다면
        if node not in visited:
            # 방문한 목록에 추가하기
            visited.append(node)
            # 그 노드에 연결된 노드를
            need_visited.extend(graph[node])
        
    return visited

print(dfs(graph, 'A'))
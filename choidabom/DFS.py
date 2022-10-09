# DFS: 깊이 우선 탐색

from collections import deque
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


def dfs(graph, start):
    # visited: 방문 완료한 queue 생성
    # need_visited: 방문 대기열 stack 생성
    need_visited, visited = [], []

    # start를 맨 처음 방문 대기열에 추가
    need_visited.append(start)

    # 방문 대기열이 없을 때까지
    while need_visited:
        # 방문 대기열의 마지막를 제거하고 node에 담음
        node = need_visited.pop()
        # node가 방문 완료 queue에 있는지 확인
        if node not in visited:
            # 없으면 방문 완료 queue에 추가
            visited.append(node)
            # node와 연결된 Node들을 대기열에 추가
            need_visited.extend(graph[node])
    return visited

print(dfs(graph, 'A'))
# ['A', 'C', 'I', 'J', 'H', 'G', 'B', 'D', 'F', 'E']

print()
# 특징적인 것은 visited 자료형을 기본 함수 인자로 포함시키고,
# 방문한 리스트들을 재귀함수를 통해 visited에 담는 방식
def dfs_recursive(graph, start, visited=[]):
    visited.append(start)
    for node in graph[start]:
        if node not in visited:
            dfs_recursive(graph, node, visited)
    return visited

print(dfs_recursive(graph, 'A'))
# ['A', 'B', 'D', 'E', 'F', 'C', 'G', 'H', 'I', 'J']


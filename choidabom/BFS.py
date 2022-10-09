# BFS: 너비 우선 탐색

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


def bfs(graph, start):
    # visited: 방문 완료한 queue 생성
    # need_visited: 방문 대기열 queue 생성
    need_visited, visited = [], []

    # start를 맨 처음 방문 대기열에 추가
    need_visited.append(start)

    # 방문 대기열이 없을 때까지
    while need_visited:
        # 방문 대기열의 맨 처음 요소를 제거하고 node에 담음
        node = need_visited.pop(0)
        # node가 방문 완료 queue에 있는지 확인
        if node not in visited:
            # 없으면 방문 완료 queue에 추가
            visited.append(node)
            # node와 연결된 Node들을 대기열에 추가
            need_visited.extend(graph[node])
    return visited

print(bfs(graph, 'A'))
# ['A', 'B', 'C', 'D', 'G', 'H', 'I', 'E', 'F', 'J']
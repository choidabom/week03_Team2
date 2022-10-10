# DFS by recursive

graph = dict()
graph['1'] = ['2', '3', '4']
graph['2'] = ['4']
graph['3'] = ['4']
graph['4'] = []

# 특징적인 것은 visited 자료형을 기본 함수 인자로 포함시키고,
# 방문한 리스트들을 재귀함수를 통해 visited에 담는 방식
def dfs_recursive(graph, start, visited=[]):
    visited.append(start)

    for node in graph[start]:
        if node not in visited:
            dfs_recursive(graph, node, visited)

    return visited

print(dfs_recursive(graph, '1'))


# graph = dict()
# graph['1'] = ['2', '3', '4']
# graph['2'] = ['4']
# graph['3'] = ['4']

# def dfs_recursive(graph, start, visited=[]):
#     visited.append(start)

#     for node in graph[start]:
#         if node not in visited:
#             dfs_recursive(graph, node, visited)

#     return visited

# print(dfs_recursive(graph, '1'))
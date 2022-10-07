# https://www.acmicpc.net/problem/1197
#1시 시작 (문제가 너무..설명이 부족해.. 뭔말인지 그림이라도 하나 넣어주지..)
# 문제이해함.. A,B,C 노드가 있고 A-B간엔 1 가중치, B-C간엔 2 가중치, A-C간엔 3가중치이고 이 세노드를 전부 잇는데 최소 가중치는 1+2=3임. 3을 출력하면 됨.
import sys
input = sys.stdin.readline

#부모 노드를 찾는 함수
def getParent(arr, n):
    if arr[n] == n: return n
    return getParent(arr,arr[n])


#두 부모 노드를 합치는 함수
def unionParent(arr,n_1, n_2):
    a = getParent(arr,n_1)
    b = getParent(arr,n_2)
    if a < b : arr[b] = a
    else: arr[a] = b

#같은 부모를 가지는지 확인
def findParent(arr, n_1, n_2):
    a = getParent(arr,n_1)
    b = getParent(arr,n_2)
    if a==b: return 1
    else : return 0

edges = []
parent = {}
V, E = map(int,input().split())

#간선에 대한 정보를 입력받는다.
#문제에서 노드1, 노드2, 간선의 가중치 순으로 입력이 주어진다.
for _ in range(E):
    edges.append([*map(int,input().split())])

# 이렇게도 입력을 받을 수 있다.   
# [ edges.append(list(map(int, input().split()))) for _ in range(V)]
# [ edges.append([*map(int,input().split())]) for _ in range(E)]



#부모노드 dict를 초기화 한다.
#모든 노드가 자기 자신을 부모노드로 지정하게된다.
for i in range(V):
    parent[i+1] = i+1

#가중치의 오름차순으로 간선을 정렬한다.
# 이 코드를 간략히 설명하면 edges배열의 세번째인자를 기준으로 오름차순 정렬하라. 
edges.sort(key=lambda val: val[2])

MST = []
#Kruskal's  Algorithm
for e in edges:
    v, u, w = e #v: 화살표 쏘는 노드, u: 받는노드, w: 떨어진 거리(가중치)
    #두 노드의    같은지 비교하게 된다.
    if findParent(parent, v, u) == 0:
        #부모노드가 같지 않다면 두 노드를 연결해주고, 더 낮은 숫자를 가진 노드로 부모노드를 변경해준다.
        unionParent(parent,v,u)
        #최소 비용 신장트리의 결과 리스트에 현재 간선의 정보를 추가해준다.
        MST.append(e)
#문제의 답은 최소비용 간선트리의 "비용의 합" 이므로 출력 형식을 맞춰준다.
print(sum([w for v, u, w in MST]))
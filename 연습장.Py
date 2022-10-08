from errno import EDEADLK
import sys
sys.stdin = open("input.txt","r")
def bfs():
    pass

# 입력
n, m, v= map(int, sys.stdin.readline().split())

''' 의식의 흐름대로 가면 아래처럼 코드를 쳤을 거 같거든? 매번 치듯이?
근데 이번에는 다른 문제랑 다르게 입력값을 문제에서 리스트를 주는대로 넣는게 아니라
관계에 따라서 재설정해서 넣어야한단 말이지? 

아래처럼 넣으면 문제에서 주는대로 일단 임시 리스트에 넣고, 그걸 어케 잘 가공해서 새로운 리스트를
만드는 방식인데. 일단, 잘 가공하는거 그게 빡세고 당연히 첨부터 잘넣으면 되는데 왜 일 두번해?가 된다.
따라서 첨부터 잘 넣는 방향으로 가자.

# 입력받기
tmp =[]
list_l = []
for i in range(m):
    a,b = map(int, sys.stdin.readline().split())
    list_l.append([a,b])
# list_l= [[1, 2], [1, 3], [1, 4], [3, 4], [2, 4]]

# 간선간에 관계를 배열로 표현 (실패)
relationship_l = list(tmp for _ in range(n)) #[[], [], [], []]

for itr_list in list_l: #[1,2]

    a = itr_list[0] #1
    b = itr_list[1] #2
    
    if b not in relationship_l[a-1]:
        relationship_l[a-1].append(b)
        relationship_l[b-1].append(a)
'''
# 관계 표현 (관계라함은 첫번째 입력이 1,2 라면 list_l의 첫번째 인자에 2를 넣고, list_l의 두번째 인자에 1을 넣는 것(둘이 이어주는것) )
list_l =list([] for _ in range(n)) #list_l = [[], [], [], []]
for i in range(m):
    a,b = map(int, sys.stdin.readline().split())
    list_l[a-1].append(b)
    list_l[b-1].append(a)
#list_l = [[2, 3, 4], [1, 4], [1, 4], [1, 3, 2]]

# bfs구현
def bfs():
    pass
# https://www.acmicpc.net/problem/1197
# 이 코드가 훠어어얼씬 이해하기 편하다.아래 참고
# https://blog.naver.com/indiaesther/222574524645
import sys 
input =  sys.stdin.readline

<<<<<<< HEAD
def find_parent(parent, x):#112, 223, 313에 따라 12먼저, 23다음, 13이 올거임. 맨앞자리는 cost, c 가중치니까
  if parent[x] != x:  #이 말은 자기자신이 parent가 아닌 즉 부모님이 따로 있는. 즉 어딘가에 연결 되어있다면.. 
    parent[x] = find_parent(parent, parent[x]) 
    #이 부분 꽤나 이해하기 어려운데.. 만약 부모님이 따로있어? 그럼 부모님이 남긴 dna를 따라서 부모님을 찾아라는 뜻이거든?
    #그 dna가 어케 남아있냐면.. parent라는 리스트는 [0,1,1,3]으로 생겼을거야. 여기서 0은 자릿수 맞추려고 넣은거고, 2자리에 2가 아니라 1이 들어와있지? 그럼 그 1이 dna임. 
=======
def find_parent(parent, x):#parent배열인 112, 223, 313 중 12먼저, 23다음, 13이 올거임. 맨앞자리는 cost, c 가중치이고 파라미터로 보낸건 a,b니까
  if parent[x] != x:  #이 말은 자기자신이 parent가 아닌 즉 부모님이 따로 있는. 즉 어딘가에 연결 되어있다면.. 
    parent[x] = find_parent(parent, parent[x]) 
    #이 부분 꽤나 이해하기 어려운데.. 만약 부모님이 따로있어? 그럼 부모님이 남긴 dna를 따라서 부모님을 찾아라는 뜻이거든?
    #그 dna가 어케 남아있냐면.. parent라는 리스트는 [0,1,1,3]으로 생겼을거야. 여기서 0은 자릿수 맞추려고 넣은거고, index 2자리에 2가 아니라 1이 들어와있지? 그럼 그 1이 dna임. 
>>>>>>> jaemin
    #1의 부모를 찾으려면 find_parent에 넣으면 됨. (자기자신이 부모이면서 부모를 찾는다는게 좀 역설적이라 더 헷갈리는 듯..) 

  return parent[x] #find_parent함수는 결국 자기 자신이 paprent이든 어디에 종속되어있어 부모님이 따로 계시든 결국 parent[x], 부모님을 내뱉는 함수 

def union_parent(parent,a,b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)

<<<<<<< HEAD
  if a<b: #둘중 작은 놈을 부모노드로 하는 로직인데 이건 선택임. 
=======
  if a<b: #둘중 작은 놈을 부모노드로 하는 로직인데 이건 선택사항임. 
>>>>>>> jaemin
    parent[b] = a
  else:
    parent[a] =b

v,e=map(int, input().split())
parent = [ i for i in range(v+1) ]
<<<<<<< HEAD
edges= []
=======
edges= [] #흔히 edges는 선을 의미함(출발점, 도착점이 있어야 선이겟지? 탐욕알고리즘에서는 특별히 cost값도 들어가고)
>>>>>>> jaemin
result=0

for _ in range(e):
  a,b,c = map(int, input().split())
  edges.append((c,a,b))

<<<<<<< HEAD
edges.sort() #오름차순으로 정렬
=======
edges.sort() #오름차순으로 정렬 (cost가 작은것 부터 선을 그니까)
>>>>>>> jaemin

for edge in edges:
  cost, a,b = edge  #c를 cost라고하자

  #이 부분도 이해하기 쉽지 않은데..왜 부모가 다르기만 하면 전부 합쳐버리냐?(정답취급해버리냐? 또는 선을 이어버리냐?)
  #크루스칼이 일단 가중치가 최소로 정렬이 되어있을 때 싸이클만 생기지 않게 일단 선을 잇는 로직이라서 그럼.(싸이클 생성 여부를 if문에서 판단하는거고 그 상황만 아니면 선을 잇는거지.)
  if find_parent(parent,a) != find_parent(parent,b):
    union_parent(parent, a, b)
    result+= cost 
print(result)
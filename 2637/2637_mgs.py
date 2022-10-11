import sys
from collections import deque
sys.stdin = open("21_input.txt","r")

n = int(input())
m = int(input())
factory_list = [[] for _ in range(n+1)]
needs = [[0] * (n+1) for _ in range(n+1)]
# print(factory_list)
inDegree = [0 for _ in range(n+1)]
for _ in range(m) :
    start, end, wage = map(int, sys.stdin.readline().strip().split())
    factory_list[end].append((start, wage))     # 나는 start를 기준으로 잡았는데 end로 잡는게 더 편한듯
    inDegree[start] += 1

# print(factory_list)
# print(inDegree)

q = deque()
for i in range(1, n+1) :
    if inDegree[i] == 0 :
        q.append(i)

while q :
    tmp = q.popleft()

    for next, next_need in factory_list[tmp] :      # 내가 구현 못 한 부분
        # 그 배열이 0이 되었다는 건, 더 이상 나눌 하위 파츠가 없다는 걸 의미함(기본파츠)
        if needs[tmp].count(0) == n+1 :
            needs[next][tmp] += next_need   # 각 중간 부품마다 배열을 만들어주고 필요한 1,2,3,4의 개수를 저장해줌
        # 더 나눌 하위 파츠가 있다면 for문 돌면서 다 분해 ㄱㄱ
        else :
            for i in range(1, n+1) :
                needs[next][i] += needs[tmp][i] * next_need
        
        inDegree[next] -= 1
        if inDegree[next] == 0 :
            q.append(next)

for x in enumerate(needs[n]) : # 원소 인덱스도 출력하고 싶으면 enumerate를 쓰면 됨!
    if x[1] > 0 :
        print(*x)

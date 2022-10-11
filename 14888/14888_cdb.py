# 14888: 연산자 끼워넣기

# from daell 
# 재귀는 일종의 토너먼트이다. (just feeling)
# 이 문제는 연산자 총 4가지의 멀티버스를 만들어서 멀티버스에서 또 멀티버스를 만들어지고 또 멀티버스가 만들어진 다음에 결론적으로 최종 깊이에 도달했을 때 멀티버스가 접혀지면서 값들이 구해짐
# 총 4가지의 멀티버스에서 나온 친구들을 모아서 max 값과 min 값을 구하면 됨.

import sys
sys.stdin = open("14888/input.txt","r")
input = sys.stdin.readline

N = int(input().rstrip()) # 수의 개수
nums = list(map(int, input().split())) # 예제로 설명하자면 1) nums = [5, 6]
plus, minus, multi, div = list(map(int, input().split())) # 2) 0, 0, 1, 0

# 연산 결과로 나올 수 없는 값으로 최대값과 최소값을 초기화 해준다.
maxN = -sys.maxsize
minN = sys.maxsize

def dfs(num, idx, plus, minus, multi, div):
    # 4) dfs(5, 1, 0, 0, 1, 0)
    global maxN, minN
    # 최종 깊이에 도달했을 때 흩뿌려진 멀티버스가 다 모이면서 max와 min을 구한다. 
    # 6) dfs(30, 2, 0, 0, 0, 0) => idx == 2로 최종 깊이에 도달 !
    # 하나의 멀티버스만 생성되었기 때문에 maxN과 minN이 같다. 
    if idx == N:
        maxN = max(num, maxN)
        minN = min(num, minN)
        return # global 선언을 해줬기 때문에 따로 return 값 주지 않음

    if plus: 
        dfs(num+nums[idx], idx+1, plus-1, minus, multi, div)
    if minus:
        dfs(num-nums[idx], idx+1, plus, minus-1, multi, div)
    if multi: # 5) 예제에서 plus, minus, div 없기 때문에 multi 해주면 => dfs(30, 2, 0, 0, 0, 0)
        dfs(num*nums[idx], idx+1, plus, minus, multi-1, div)
    if div:
        dfs(int(num/nums[idx]), idx+1, plus, minus, multi, div-1)

# 3) nums = [5, 6]/ plus, minus, multi, div = 0, 0, 1, 0
dfs(nums[0], 1, plus, minus, multi, div)

print(maxN)
print(minN)
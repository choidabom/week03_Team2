# 2294: 동전 2
# n가지 종류의 동전, 동전 사용해서 그 가치의 합이 k원이 되도록 하고픔
# 동전의 개수가 최소가 되도록

# 로직
# 1. 데이터들을 1차원 배열에 담는다.
# 2. 최소 코인 갯수를 저장할 dp 배열을 만들고 max(10001)으로 초기화시켜준다.
# 3. 코인 배열의 값을 가져오고
# 4. 그 값만큼 올리면서 for문을 돌아주는데
# 5. 현재 값에서 가져온 코인 값을 빼주었을 때의 코인 사용 개수에 지금 코인 개수 하나를 더한 값과 이전 코인들로만 조합했을 때 사용된 코인 개수를 비교하여 더 작은 값을 dp 배열에 담는다.

import sys
sys.stdin = open("2294/input.txt","r")
input = sys.stdin.readline


n, k = map(int, input().split()) # n가지 종류의 동전, 가치의 합 k원
coin = [] # 코인을 담을 1차원 배열
for i in range(n):
    coin.append(int(input().rstrip()))
# print(coin)

dp = [10001] * (k+1) # 각 값마다 필요한 최소 코인 갯수를 저장할 dp 배열
dp[0] = 0
#  k의 최댓값이 10000이기 때문에 dp 리스트를 10001으로, 0원을 택하는 방법은 없으므로 dp[0]=0으로 초기화시킨다.

for num in coin: # 현재 테스트 케이스에서 coin = [1, 5, 12]
    for i in range(num, k+1):   # for i in range(1, 16) or range(5, 16) or range(12, 16)
        # 어떻게 
        # print(f'dp[{i}]: ', dp[i], dp[i-num]+1) 
        dp[i] = min(dp[i], dp[i-num]+1)
        # print(f'dp[{i}]: ', dp[i])
        
if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])
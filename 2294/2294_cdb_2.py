# 2294: 동전 2
# n가지 종류의 동전, 동전 사용해서 그 가치의 합이 k원이 되도록 하고픔
# 동전의 개수가 최소가 되도록

import sys
sys.stdin = open("2294/input.txt","r")
input = sys.stdin.readline

n, k = map(int, input().split()) # n가지 종류의 동전, 가치의 합 k원
coin = [] # 코인을 담을 1차원 배열
for i in range(n):
    coin.append(int(input().rstrip()))

dp = [0] * (k+1) # 각 값마다 필요한 최소 코인 갯수를 저장할 dp 배열

for i in range(1, k+1):
    a = []
    for j in coin:
        if j <= i and dp[i-j] != -1:
            a.append(dp[i-j])
    if not a:
        dp[i] = -1
    else:
        dp[i] = min(a) + 1
print(dp[k])


# 3 15

# 1

# 5

# 12

# 위와 같이 입력을 받았다고 하자.

# 1부터 15까지의 경우의 수를 담는 dp 리스트를 만들어준다.

# 1부터 15까지 필요한 동전의 개수를 최소로 나타내보자.

# i coin

# 0 - 0

# 1 - 1

# 2 - 1, 1

# 3 - 1, 1, 1

# 4 - 1, 1, 1, 1

# 5 - 5

# 6 - 5, 1

# 7 - 5, 1, 1

# 8 - 5, 1, 1, 1

# 9 - 5, 1, 1, 1, 1

# 10 - 5, 5

# 11 - 5, 5, 1

# 12 - 12

# 13 - 12, 1

# 14 - 12, 1, 1

# 15 - 5, 5, 5
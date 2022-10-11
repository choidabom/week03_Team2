import sys
sys.stdin = open("19_input.txt","r")

# dp코딩..? 이게 왜 bfs지..?

n, k = map(int, sys.stdin.readline().strip().split())
# print(n, k)

coin_list = []
for i in range(n) :
    coin_list.append(int(sys.stdin.readline().strip()))

dp = [10001] * (k+1)
dp[0] = 0

for coin in coin_list :
    for i in range(coin, k+1) :
        dp[i] = min(dp[i], dp[i-coin]+1)
if dp[k] == 10001 :
    print(-1)
else :
    print(dp[k])
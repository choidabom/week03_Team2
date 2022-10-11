import sys
sys.stdin = open("10_input.txt","r")

n = int(input())
num_list = list(map(int, sys.stdin.readline().strip().split()))
calcu_list = list(map(int, sys.stdin.readline().strip().split()))

max_val = float('-inf')
min_val = float('inf')

def dfs(index, res, plus, minus, multiply, divide) :
    global max_val, min_val
    if index == n :
        max_val = max(res, max_val)
        min_val = min(res, min_val)
        return

    if plus :
        dfs(index + 1, res + num_list[index], plus - 1, minus, multiply, divide)
    if minus :
        dfs(index + 1, res - num_list[index], plus, minus - 1, multiply, divide)
    if multiply :
        dfs(index + 1, res * num_list[index], plus, minus, multiply - 1, divide)
    if divide :
        dfs(index + 1, int(res / num_list[index]), plus, minus, multiply, divide - 1)

dfs(1, num_list[0], calcu_list[0], calcu_list[1], calcu_list[2], calcu_list[3])
print(max_val)
print(min_val)

import itertools
import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
plusnum, minnum, multinum, divnum = map(int, input().split())
minV = 987654321
maxV = -987654321

opers = []

while plusnum > 0:
    opers.append('+')
    plusnum -= 1
while minnum > 0:
    opers.append('-')
    minnum -= 1
while multinum > 0:
    opers.append('x')
    multinum -= 1
while divnum > 0:
    opers.append('÷')
    divnum -= 1


per_opers = list(itertools.permutations(opers))
per_opers = set(per_opers)

for i in per_opers:
    po = pn = 0
    arith_sum = num[pn]

    while po < len(i) and pn < len(num):
        pn += 1
        if i[po] == 'x':
            arith_sum *= num[pn]
        elif i[po] == '÷':
            if arith_sum < 0 or num[pn] < 0:
                arith_sum = int(arith_sum/num[pn])
            else:
                arith_sum //= num[pn]
        elif i[po] == '-':
            arith_sum -= num[pn]
        elif i[po] == '+':
            arith_sum += num[pn]
        po += 1

    maxV = arith_sum if arith_sum > maxV else maxV
    minV = arith_sum if arith_sum < minV else minV

print(maxV)
print(minV)
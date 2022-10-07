# 입력
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
arr = []
while True:
  try:
    x = int(input())
    arr.append(x)
  except:
    break

def solution(arr):
  if len(arr) == 0:
    return
  
  root=arr[0]
  arr_R = []
  arr_L = []
  for i in range(1, len(arr)): #이것도 배열길이보다 +1만큼 더 도네?
    if arr[i] > root :
      arr_R = arr[i:]
      arr_L = arr[1:i]
      break
  else:
    # 모두 root보다 작은 경우
    arr_L = arr[1:]

  solution(arr_L)
  solution(arr_R)
  print(root)

solution(arr)


# 7569: 토마토
# 상하좌우를 탐색해야했던 다른 최단거리탐색 bfs 문제들에서 위아래를 추가한 문제다
# 3차원 배열의 인덱스는 arr[z][x][y]이다. 인덱스 순서 기억하기 !!
# 배열 중첩해서 쓸 때는 [[]*N]*M 같은 표현 쓰지 말라 => 포인터만 복사되는 참사가 생길 것

import sys
sys.stdin = open("choidabom/7569/input.txt","r")
input = sys.stdin.readline
from heapq import heappush, heappop

# 익은 토마토 1
# 익지 않은 토마토 0
# 토마토가 없는 칸 -1

def bfs(pallet, M, N, H, q):
    global unripped

    
def init():
    M, N, H = map(int, input().split())
    pallet = [[[[0] for _ in range(M)] for _ in range(N)] for _ in range(H)]

    global unripped
    q = deque()

    for z in range(H):
        for x in range(N):
            row  = list(map(int, input().split()))
            for y in range(M):
                obj = row[y]
                pallet[z][x][y] = obj
                if obj == 0: # 익지 않은 토마토이면 
                    unripped += 1
                elif obj == 1: # 익은 토마토이면
                    q.append([0, x, y, z])
    
    if not unripped: # 익지 않은 토마토가 없으면 0을 출력
        print(0)
        return
    
    if q: # 익은 토마토가 있으면 탐색 시작 ~!
        bfs(pallet, M, N, H, q)

    if unripped: # 탐색을 했는데 익지 않은 토마토가 있으면 -1 출력 ????/
        print(-1)
        return
    
    result = []
    for box in pallet:
        for row in box:
            m = max(row)
            heappush(result, (-m, m))
    print(heappop(result)[1])

unripped = 0
init()
import heapq
# 파이썬에서는 min-heap으로 구현되어 있기 때문에 heappop을 하게 되면 우선순위가 낮은 순으로 출력된다.

# 오름차순 힙 정렬(Heap sort)
def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)

# 실행 결과
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
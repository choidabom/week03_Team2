import heapq
# 파이썬에서는 min-heap으로 구현되어 있기 때문에 heappop을 하게 되면 우선순위가 낮은 순으로 출력된다. SO, max-heap을 구현하고 싶다면 넣을 때 부호를 바꿔서 넣어주고, 꺼낼 때 부호를 바꿔서 꺼내준다. 

# 내림차순 힙 정렬(Heap sort)
def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)

# 실행 결과
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
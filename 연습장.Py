from email.errors import HeaderMissingRequiredValue
import heapq
list_l=[4,5,2,1,7]
heap = []

for list in list_l:
  heapq.heappush(heap, list)


# for i in range(len(a)):
#   a[i]=heapq.heappop(heap)
print(heap)
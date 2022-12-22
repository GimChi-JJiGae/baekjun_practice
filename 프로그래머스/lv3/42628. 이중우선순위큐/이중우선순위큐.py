import heapq
from heapq import heappop
from heapq import heappush

def solution(operations):
    heap = []
    for i in range(len(operations)):
        order, a = operations[i].split()
        num = int(a)


        if order == "I":
            heappush(heap, num)

        else:
            if not heap:  # 삭제할 데이터가 없다면
                continue
            if num == -1:
                heappop(heap)
            else:
                heap.remove(heapq.nlargest(1, heap)[0])

    if not heap:
        return [0, 0]
    else:
        return [heapq.nlargest(1, heap)[0],heap[0]]

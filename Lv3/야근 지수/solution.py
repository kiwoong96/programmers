import heapq

def solution(n, works):
    heap = []
    result = 0
    for data in works:
        heapq.heappush(heap,-1 * data)
    
    while n > 0:
        max_val = heapq.heappop(heap)
        max_val += 1
        heapq.heappush(heap, max_val)
        n -= 1
    
    for data in heap:
        if data > 0:
            continue
        result += pow(data,2)
    
    return result
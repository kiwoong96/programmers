import heapq
operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]	

def solution(operations):
    answer = [0,0]
    max_heap = []
    min_heap = []
    for operation in operations:
        oper, num = operation.split()
        #print(oper, num)
        if oper== 'I':
            heapq.heappush(max_heap,-int(num))
            heapq.heappush(min_heap, int(num)) 
        else:
            if num == "1":
                if max_heap:
                    max_val = heapq.heappop(max_heap)
                    min_heap.remove(-1 * max_val)
            else:
                if min_heap:
                    min_val = heapq.heappop(min_heap)
                    max_heap.remove(-1 * min_val)
        
    if min_heap:
        answer[0] = -1 * heapq.heappop(max_heap)
        answer[1] = heapq.heappop(min_heap)
    return answer
print(solution(operations))
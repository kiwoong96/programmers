import heapq

def solution(n, works):
    hq = []
    answer = 0
    for work in works:
        heapq.heappush(hq,-1 * work)
    
    for _ in range(n):
        max_val = heapq.heappop(hq) * -1
        if max_val == 0:
            answer = 0
            break
        else:
            heapq.heappush(hq, -1 * max_val + 1)
    
    for _ in range(len(hq)):
        answer += pow(heapq.heappop(hq),2)
    
    return answer

print(solution(4,[4,3,3]))
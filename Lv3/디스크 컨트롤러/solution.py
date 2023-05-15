import heapq
#[[0, 3], [1, 9], [2, 6]]	9
def solution(jobs):
    answer = 0
    hq = []
    for job in jobs:
        heapq.heappush(hq,(job[1], job[0]))
    
    now_time = 0
    while q:
        
    
    
    return answer
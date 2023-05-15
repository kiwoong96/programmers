import heapq
#[[0, 3], [1, 9], [2, 6]]	9
def solution(jobs):
    answer = 0
    now = 0 #현재시간
    i = 0   #처리개수
    start = -1 #마지막 완료시간
    heap = []
    
    while i < len(jobs):
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(heap,[job[1],job[0]])
        
        if heap:
            time, start_time = heapq.heappop(heap)
            start = now
            now += time
            answer += now - start_time #요청으로부터 처리시간
            i += 1
        else:
            now += 1
            
    return answer // len(jobs)


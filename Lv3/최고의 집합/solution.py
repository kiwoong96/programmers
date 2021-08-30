import heapq

def solution(n, s):
    answer = []
    
    if s//n == 0:
        answer.append(-1)
    else:
        for i in range(n-s%n):
            answer.append(s//n)
        for i in range(s%n):
            answer.append(s//n+1)
        
    
    answer.sort()
    
    return answer
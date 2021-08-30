def solution(A, B):
    answer = 0
    
    A.sort()
    B.sort()
    
    bIdx = 0;
    aIdx = 0;
    
    if B[-1] < A[0]:
        pass
    else:
        while aIdx < len(A) and bIdx < len(B):
            #B팀이 승리하는 경우
            if B[bIdx] > A[aIdx]: 
                answer += 1
                bIdx += 1
                aIdx += 1
            #동점이거나 A팀이 승리하는 경우
            else:
                bIdx += 1
                
    return answer
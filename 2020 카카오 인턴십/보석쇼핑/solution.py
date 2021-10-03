from collections import defaultdict

def solution(gems):
    answer = []
    count = defaultdict(int)
    gemSet = set(gems)
    
    sIdx = 0
    eIdx = 0
    count[gems[sIdx]] = 1

    while sIdx <= eIdx:
        
        #모든값을 찾은 경우
        if len(count) == len(gemSet):
            answer.append([sIdx,eIdx])
            count[gems[sIdx]] -= 1
            if count[gems[sIdx]] == 0:
                del count[gems[sIdx]]
            sIdx += 1
        #모든값을 찾지 못한 경우
        elif len(count) < len(gemSet):
            eIdx += 1
            if eIdx >= len(gems):
                break
            count[gems[eIdx]] += 1
            
    minVal = 1e9
    minS = 0
    minE = 0
    for x,y in answer:
        if y-x > minVal:
            continue
        elif y-x == minVal:
            if minS > x:
                minS, minE = x,y
        else:
            minS,minE,minVal = x,y,y-x
            
    
    return [minS+1,minE+1]
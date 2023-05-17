def solution(targets):
    answer = 0
    end = 0
    targets.sort(key=lambda x:(x[1],x[0]))
    
    for target in targets:
        if end <= target[0]:
            end = target[1]
            answer += 1
            
    return answer
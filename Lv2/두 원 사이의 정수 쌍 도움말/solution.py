import math

def solution(r1, r2):
    answer = 0
    for i in range(1,r2):
        y2 = math.floor(math.sqrt(math.pow(r2,2) - math.pow(i,2)))
        if i >= r1:
            y1 = 0
        else:
            y1 = math.ceil(math.sqrt(math.pow(r1,2) - math.pow(i,2)))
        answer += y2-y1+1
        if i >= r1:
            answer -= 1
    answer += r2-r1+1
    answer *= 4
    return answer

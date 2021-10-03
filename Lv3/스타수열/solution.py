#08:38 start
from collections import Counter

def solution(a):
    answer = 0
    counter = Counter(a)

    if len(a) < 2:
        return answer
    for max_val in list(counter.keys()):
        idx = 0
        tmp_answer = 0
        while idx < len(a)-1:
            if (a[idx] != a[idx+1]) and (a[idx]==max_val or a[idx+1]==max_val):
                tmp_answer += 2
                idx += 2;
                
            else:
                idx += 1;
        answer = max(tmp_answer, answer)
            
    return answer
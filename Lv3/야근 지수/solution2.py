from collections import defaultdict

def solution(n, works):
    answer = 0
    max_val = max(works)
    works_list = [0 for _ in range(50000)]
    for work in works:
        works_list[work] += 1
    
    for _ in range(n):
        if max_val < 0:
            answer = -1
            break
        else:
            works_list[max_val] -= 1
            n -= 1
            
            if max_val -1 > 0:
                works_list[max_val - 1] += 1
                
            if n == 0:
                break
            
                
            
            while max_val >= 0:
                if works_list[max_val] > 0:
                    break
                else:
                    max_val -= 1
        

    if answer != -1:
        for i in range(1,max_val+1):
            if works_list[i] != 0:
                answer += (i**2 * works_list[i])
    
    return answer

print(solution(2,[1,1]))
def solution(n, k):
    data = []
    answer = []
    for i in range(1,n+1):
        data.append(i)

    tmp = k-1
    div_val = 1
    
    for i in range(2,n):
        div_val *= i
    
    n -= 1
    
    while n > 0 :
        now = tmp // div_val
        answer.append(data[now])
        data.remove(data[now])
        tmp %= div_val
        div_val //= n
        n -= 1
    answer.append(data[0])
    
    return answer
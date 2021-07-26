def solution(n):
    data = [0 for _ in range(n+1)]
    data[1] = 1
    
    if n==1 :
        return data[1] % 1234567
    
    data[2] = 2
    
    for i in range(3,n+1):
        data[i] = data[i-1] + data[i-2]
    
    return data[n] % 1234567
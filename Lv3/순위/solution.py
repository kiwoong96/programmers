def solution(n, results):
    answer = 0
    graph = [[False for _ in range(n+1)] for _ in range(n+1)]
    
    for result in results:
        start, end = result[0], result[1]
        graph[start][end] = True
    
    
    
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if graph[i][k] == True and graph[k][j] == True:
                    graph[i][j] = True
                    
    """
    for col in graph:
        print(col)
    """
    
    for i in range(1,n+1):
        tmp = 0
        for j in range(1, n+1):
            tmp += graph[i][j]
        
        for j in range(1, n+1):
            tmp += graph[j][i]
        
        if tmp==n-1:
            answer += 1
            
        
    
    
    return answer
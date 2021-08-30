line = [0 for _ in range(12)]
result = 0

def nqueen(n,k,x):
    global result
    for i in range(k):
        #대각선
        if line[i] == x-(k-i) or line[i] == x+(k-i):
            return 
        
        #세로
        if line[i] == x:
            return 

    line[k] = x
    for i in range(n):
        if n == k+1:
            result += 1
            return
        else:
            nqueen(n,k+1,i)
    
    
def solution(n):
    for i in range(n):
        nqueen(n,0,i)
    
    return result
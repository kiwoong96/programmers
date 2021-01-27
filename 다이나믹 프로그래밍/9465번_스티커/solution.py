##내 풀이

"""
T = int(input())

for i in range(T):
    N = int(input())
    arr = []
    d = [[0 for _ in range(N)] for _ in range(2)]
    for j in range(2):
        arr.append(list(map(int,input().split())))

    d[0][0] = arr[0][0]
    d[0][1] = arr[1][0] + arr[0][1]
    d[1][0] = arr[1][0]
    d[1][1] = arr[0][0] + arr[1][1]
    for j in range(2, N):
        #print("i : ",i , ", j : ", j)
        d[0][j] = max(d[1][j-1] , d[1][j-2]) + arr[0][j]
        d[1][j] = max(d[0][j-1] , d[0][j-2]) + arr[1][j]
    max_val = -1
    for j in d:
        if max_val < max(j):
            max_val = max(j)
    print(max_val)
"""

##정석 풀이

T = int(input())

for i in range(T):
    N = int(input())
    arr = []
    #d = [[0 for _ in range(N)] for _ in range(2)]
    for j in range(2):
        arr.append(list(map(int,input().split())))

    arr[0][1] += arr[1][0]
    arr[1][1] += arr[0][0]

    for j in range(2,N):
        arr[0][j] += max(arr[1][j-2] , arr[1][j-1])
        arr[1][j] += max(arr[0][j - 2], arr[0][j - 1])
    #print(arr)
    print(max(arr[0][N-1],arr[1][N-1]))
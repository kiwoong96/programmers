import sys
input = sys.stdin.readline
INF = int(1e9)

N, M = map(int,input().split())

board = [[INF for _ in range(N+1)] for _ in range(N+1)]

for i in range(M):
    start, end = map(int,input().split())
    board[start][end] = 1

def floyd():
    distance = [[INF for _ in range(N+1)] for _ in range(N+1)]

    for i in range(N+1):
        for j in range(N+1):
            if i == j: continue
            else:
                distance[i][j] = board[i][j]

    for k in range(1,N+1):
        for i in range(1,N+1):
            for j in range(1,N+1):
                if i==j: continue
                if distance[i][j] > distance[i][k] + distance[k][j] :
                    distance[i][j] = distance[i][k] + distance[k][j]

    return distance

distance = floyd()


result = 0
for i in range(1,N+1):
    sumation = 0
    for j in range(1,N+1):
        if i==j: continue
        if distance[i][j] == INF and distance[j][i] == INF:
            break
        else:
            sumation +=1

    if sumation == N-1:
        result += 1

print(result)


import sys
input = sys.stdin.readline

INF = int(1e9)

N = int(input())
M = int(input())

graph = [[INF for _ in range(N+1)]for _ in range(N+1)]

for i in range(M):
    end, start = map(int,input().split())
    graph[start][end] = 1

def floyd():
    distance = [[INF for _ in range(N+1)] for _ in range(N+1)]

    for i in range(1,N+1):
        for j in range(1,N+1):
            if i == j : continue
            else:
                distance[i][j] = graph[i][j]

    for k in range(1,N+1):
        for i in range(1,N+1):
            for j in range(1,N+1):
                if i==j: continue
                else:
                    if distance[i][j] > distance[i][k] + distance[k][j]:
                        distance[i][j] = distance[i][k] + distance[k][j]

    return distance

distance = floyd()
"""for k in distance:
    print(k)"""

for i in range(1,N+1):
    result = 0
    for j in range(1,N+1):
        if i == j: continue
        if distance[i][j] == INF and distance[j][i] == INF:
            result +=1

    print(result)
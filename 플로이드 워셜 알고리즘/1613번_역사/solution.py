import sys
input = sys.stdin.readline

INF = int(1e9)

N, K = map(int,input().split())

graph = [[INF for _ in range(N+1)] for _ in range(N+1)]

def floyd():
    distance = [[INF for _ in range(N+1)] for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1,N+1):
            if i==j:
                continue
            else:
                distance[i][j] = graph[i][j]


    for k in range(1,N+1):
        for i in range(1,N+1):
            for j in range(1,N+1):
                if i==j:
                    continue
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]

    return distance

for _ in range(K):
    start, end = map(int,input().split())
    graph[start][end] = 1
    #graph[end][start] = 1



S = int(input())

distance = floyd()
"""for i in distance:
    print(i)
"""
for _ in range(S):
    start,end = map(int,input().split())
    if distance[start][end] !=INF:
        print(-1)
    elif distance[end][start] != INF:
        print(1)
    else:
        print(0)
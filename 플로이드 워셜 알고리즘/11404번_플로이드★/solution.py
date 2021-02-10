import sys
input = sys.stdin.readline
INF = int(1e9)
N = int(input())
M = int(input())

graph = [[INF for _ in range(N+1)] for i in range(N+1)]

for i in range(M):
    start, end, distance = map(int,input().split())
    if graph[start][end] > distance:
        graph[start][end] = distance


def floyd():
    distance = [[INF for _ in range(N+1)] for _ in range(N+1)]
    for i in range(1,N+1):
        for j in range(1,N+1):
            distance[i][j] = graph[i][j]



    for k in range(1,N+1):
        for i in range(1,N+1):
            for j in range(1,N+1):
                if i != j:
                    distance[i][j]  = min(distance[i][j] , distance[i][k] + distance[k][j])

    return distance


distance = floyd()

for i in range(1,N+1):
    for j in range(1,N+1):
        if distance[i][j] == INF:
            print(0,end=' ')
        else:
            print(distance[i][j] , end = ' ')
    print()

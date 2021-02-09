import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[0 for _ in range(N+1)] for i in range(N+1)]

for i in range(M):
    start, end, distance = map(int,input().split())
    if graph[start][end] != 0:
        graph[start][end] = min(distance,graph[start][end])
    else:
        graph[start][end] = distance

print(graph)
def floyd():
    distance = []
    for i in graph:
        distance.append(i)
    print(distance)
    for k in range(N):
        for i in range(N):
            for j in range(N):
                distance[i][j]  = min(distance[i][j] , distance[i][k] + distance[k][j])

    return distance


distance = floyd()

for i in range(N):
    for j in range(N):
        print(distance[i][j] , end = ' ')
    print()

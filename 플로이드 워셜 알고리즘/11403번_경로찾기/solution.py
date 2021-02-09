import sys
INF = int(1e9)
input = sys.stdin.readline

N = int(input())
graph = []

for i in range(N):
    graph.append(list(map(int,input().split())))


def floyd():
    distance = []
    for i in range(N):
        distance.append(graph[i])

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if min(distance[i][k],distance[k][j])==0:
                    continue
                else:
                    distance[i][j] = 1

    return distance

distance = floyd()
for i in range(N):
    for j in range(N):
        print(distance[i][j] , end=' ')
    print()

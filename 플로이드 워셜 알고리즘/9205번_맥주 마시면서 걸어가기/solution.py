import sys
import heapq

INF = int(1e9)

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    distance = [[INF for _ in range(N+2)] for _ in range(N+2)]
    graph = []
    for i in range(N+2):
        x,y = map(int,input().split())
        graph.append((x,y))

    for i in range(N+2):
        for j in range(N+2):
            if i == j:
                continue
            else:
                tmp =  abs(graph[i][0]-graph[j][0])+abs(graph[i][1]-graph[j][1])
                if tmp <= 1000:
                    distance[i][j] = 1
    #print(distance)
    for k in range(N+2):
        for i in range(N+2):
            for j in range(N+2):
                if i==j:
                    continue
                else:
                    distance[i][j] = min(distance[i][j], distance[i][k] +distance[k][j])
    #print(graph)
    #print(distance)

    if distance[0][N+1] >= INF:
        print("sad")
    else:
        print("happy")



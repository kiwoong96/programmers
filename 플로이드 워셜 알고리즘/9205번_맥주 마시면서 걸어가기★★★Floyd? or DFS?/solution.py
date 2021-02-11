#Floyd Warshell 시간초과

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
                tmp = abs(graph[i][0]-graph[j][0])+abs(graph[i][1]-graph[j][1])
                if tmp <= 1000:
                    distance[i][j] = 1

    #print(distance)
    for k in range(N+2):
        for i in range(N+2):
            for j in range(N+2):
                if i==j:
                    continue
                else:
                    if distance[i][j] > distance[i][k] + distance[k][j]:
                        distance[i][j] =distance[i][k] +distance[k][j]
    #print(graph)
    #print(distance)

    if distance[0][N+1] >= INF:
        print("sad")
    else:
        print("happy")






##DFS
"""
import sys
input = sys.stdin.readline

T = int(input())
def dfs(start):
    visited[start] = 1
    for i in range(N+2):
        if board[start][i] == 1 and visited[i] == False:
            dfs(i)
for _ in range(T):
    graph = []

    N = int(input())
    for i in range(N+2):
        x,y = map(int,input().split())
        graph.append((x,y))

    board = [[0 for _ in range(N+2)]for _ in range(N+2)]
    visited = [False for _ in range(N+2)]

    for i in range(N+2):
        for j in range(N+2):
            if i == j: continue
            if abs(graph[i][0] - graph[j][0]) + abs(graph[i][1] - graph[j][1]) <=1000:
                board[i][j] = 1

    dfs(0)
    if visited[N+1] == True:
        print('happy')
    else:
        print('sad')
"""

import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline

N = int(input())

graph = []
dxy = [[1,0],[-1,0],[0,1],[0,-1]]
for i in range(N):
    graph.append(input().strip('\n'))

distance = [[INF for _ in range(N)]for _ in range(N)]

def dijkstra(x,y):
    q = []
    heapq.heappush(q,(0,x,y))
    distance[x][y] = 0

    while q:
        tmp = heapq.heappop(q)
        change,x,y = tmp[0],tmp[1],tmp[2]
        if distance[x][y] < change:
            continue

        for dt in dxy:
            new_x,new_y = x+dt[0],y+dt[1]
            if 0<= new_x <N and 0<= new_y <N:
                if graph[new_x][new_y] == '0':
                    data = change + 1
                    if distance[new_x][new_y] > data:
                        distance[new_x][new_y] = data
                        heapq.heappush(q,(data,new_x,new_y))
                else:
                    if distance[new_x][new_y] > change:
                        distance[new_x][new_y] = change
                        heapq.heappush(q,(change,new_x,new_y))

dijkstra(0,0)

print(distance[N-1][N-1])
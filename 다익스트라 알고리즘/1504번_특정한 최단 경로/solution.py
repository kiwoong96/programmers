import sys
import heapq
INF = int(1e9)
input = sys.stdin.readline

N,E = map(int,input().split())

graph = [[]for _ in range(N+1)]
distance = [[INF for _ in range(N+1)]for _ in range(N+1)]

for i in range(E):
    start,end,dist = map(int,input().split())
    graph[start].append((end,dist))
    graph[end].append((start,dist))


V1, V2 = map(int,input().split())

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start][start] = 0

    while q:
        tmp = heapq.heappop(q)
        dist, now = tmp[0],tmp[1]
        if distance[start][now] < dist:
            continue

        for i in graph[now]:
            end, dist = i[0],i[1]
            data = distance[start][now] + dist
            if distance[start][end] > data:
                distance[start][end] = data
                heapq.heappush(q,(data,end))

dijkstra(1)
dijkstra(V1)
dijkstra(V2)

if min(distance[1][V1] + distance[V1][V2] + distance[V2][N],distance[1][V2] + distance[V2][V1] + distance[V1][N]) >= INF:
    print(-1)
else:
    print(min(distance[1][V1] + distance[V1][V2] + distance[V2][N],distance[1][V2] + distance[V2][V1] + distance[V1][N]))
import heapq
import sys
INF = int(1e9)
input = sys.stdin.readline


N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

distance = [INF for _ in range(N+1)]
for i in range(M):
    start, end, dist = map(int,input().split())
    graph[start].append((end,dist))

start,end = map(int,input().split())

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        tmp = heapq.heappop(q)
        dist, now = tmp[0], tmp[1]

        if distance[now] < dist:
            continue

        for k in graph[now]:
            end, data = k[0], k[1]
            value = distance[now] + data

            if distance[end] > value:
                distance[end] = value
                heapq.heappush(q,(data,end))


dijkstra(start)
print(distance[end])


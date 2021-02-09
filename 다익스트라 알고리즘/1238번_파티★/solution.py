import heapq
import sys
INF = int(1e9)
input = sys.stdin.readline


N,M,X = map(int,input().split())

graph = [[]for _ in range(N+1)]

distance = [[INF for _ in range(N+1)] for _ in range(N+1)]

for i in range(M):
    start,end,dist = map(int,input().split())
    graph[start].append((end,dist))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start][start] = 0

    while q:
        tmp = heapq.heappop(q)
        dist, now = tmp[0], tmp[1]
        if distance[start][now] < dist:
            continue

        for i in graph[now]:
            end, dist = i[0], i[1]
            data = distance[start][now] + dist
            if distance[start][end] > data:
                distance[start][end] = data
                heapq.heappush(q,(dist,end))

for i in range(1,N+1):
    dijkstra(i)

"""
for i in range(1,N+1):
    print(distance[i])
"""
max_value = -1
for i in range(1,N+1):
    tmp = distance[i][X] + distance[X][i]
    if max_value < tmp:
        max_value = tmp

print(max_value)
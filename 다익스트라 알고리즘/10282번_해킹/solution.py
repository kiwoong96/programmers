import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline

T = int(input())

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        tmp = heapq.heappop(q)
        dist, now = tmp[0], tmp[1]

        if distance[now] < dist:
            continue

        for i in graph[now]:
            end, dist = i[0], i[1]
            data = distance[now] + dist
            if distance[end] > data:
                distance[end] = data
                heapq.heappush(q,(data,end))




for _ in range(T):
    N,D,C = map(int,input().split())

    graph = [[] for _ in range(N+1)]
    distance = [INF for _ in range(N+1)]

    for _ in range(D):
        end,start,dist = map(int,input().split())
        graph[start].append((end,dist))

    dijkstra(C)
    count = 0
    max_value = 0
    for i in range(1,N+1):
        if distance[i] != INF:
            count += 1
            if distance[i] > max_value:
                max_value = distance[i]

    print(count, max_value)






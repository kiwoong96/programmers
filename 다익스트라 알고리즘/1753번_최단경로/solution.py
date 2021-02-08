import heapq
import sys
INF = int(1e9)

input = sys.stdin.readline

V,E = map(int,input().split())

##start
K = int(input())

graph = [[] for _ in range(V+1)]

distance = [INF for _ in range(V+1)]

for i in range(E):
    start, end, dist = map(int,input().split())
    graph[start].append((end,dist))

def dijkstra(start):
    ##heapq
    q = []
    heapq.heappush(q,(0,K))
    distance[K] = 0
    while q:
        tmp = heapq.heappop(q)
        dist, now = tmp[0],tmp[1]
        #print(tmp)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            #print("Succes",i)
            end, val = i[0],i[1]
            sumation = val + distance[now]
            #print(sumation)
            if distance[end] > sumation:
                distance[end] = sumation
                heapq.heappush(q,(sumation, end))

dijkstra(start)

for i in distance[1:]:
    if i == INF:
        print("INF")
    else:
        print(i)

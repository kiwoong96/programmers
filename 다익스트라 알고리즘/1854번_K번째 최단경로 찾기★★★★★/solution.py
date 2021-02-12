import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)


N,M,K =map(int,input().split())

graph = [[]for _ in range(N+1)]

distance = [INF for _ in range(N+1)]
full_distance = [[]for _ in range(N+1)]


for i in range(M):
    start,end,dist = map(int,input().split())
    graph[start].append((end,dist))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0


    while q:
        tmp = heapq.heappop(q)
        dist,new = tmp[0], tmp[1]

        for k in graph[new]:
            end, dista = k[0], k[1]
            data = distance[new] + dista
            heapq.heappush()
            """if distance[end] > data:
                heapq.heappush(q,(data,end))
                distance[end] = data
                full_distance[end].append(data)
            else:
                heapq.heappush(q,(dist,end))
                full_distance[end].append(dist+dista)"""

        print(full_distance)
dijkstra(1)
for i in range(1,N+1):
    if len(full_distance[i])>=K:
        full_distance[i].sort()
        print(full_distance[i][K-1])
    else:
        print(-1)
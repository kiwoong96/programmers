import heapq
import sys
INF = int(1e9)
input = sys.stdin.readline

N, K = map(int,input().split())

distance = [INF for _ in range(200001)]
dx = [-1,1,2]
def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        tmp = heapq.heappop(q)
        dist, now = tmp[0], tmp[1]
        if distance[now] < dist:
            continue
        if now == 0:
            new = now +1
            if distance[new] > distance[now] + 1:
                distance[new] = distance[now] +1
                heapq.heappush(q,(distance[new],new))

        elif now > K:
            new = now-1
            if distance[new] > distance[now] + 1:
                distance[new] = distance[now] +1
                heapq.heappush(q,(distance[new],new))

        else:
            for i in dx:
                if i == 2:
                    new = now *2
                    if distance[new] > distance[now]:
                        distance[new] = distance[now]
                        heapq.heappush(q,(distance[new],new))
                else:
                    new = now + i
                    if distance[new] > distance[now] + 1:
                        distance[new] = distance[now] + 1
                        heapq.heappush(q,(distance[new],new))

dijkstra(N)
print(distance[K])
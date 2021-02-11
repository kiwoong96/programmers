import heapq
import sys
INF = int(1e9)
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
distance = [[INF, []] for _ in range(N+1)]

for i in range(M):
    start, end, dist = map(int,input().split())
    graph[start].append((end,dist))

Start, End = map(int,input().split())

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start,[start]))
    distance[start][0] = 0

    while q:
        tmp = heapq.heappop(q)
        dist, now, arr= tmp[0], tmp[1],tmp[2]

        if distance[now][0] < dist:
            continue
        for k in graph[now]:
            end, dist = k[0], k[1]
            if now == start:
                distance[end][1].append(now)



            data = distance[now][0] + dist
            if distance[end][0] > data:
                distance[end][0] = data
                t = [] + arr
                t.append(end)
                distance[end][1] = t
                heapq.heappush(q,(data,end,t))



dijkstra(Start)

print(distance[End][0])
print(len(distance[End][1]))
for i in distance[End][1]:
    print(i, end=' ')

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

idx = 1
while True:
    N = int(input())
    if N ==0:
        break
    graph = []
    distance = [[INF for _ in range(N)] for _ in range(N)]
    dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    for i in range(N):
        graph.append(list(map(int, input().split())))


    def dijkstra(x, y):
        q = []
        heapq.heappush(q, (graph[x][y], x, y))
        distance[x][y] = graph[x][y]

        while q:
            tmp = heapq.heappop(q)
            dist, now_x, now_y = tmp[0], tmp[1], tmp[2]
            if distance[now_x][now_y] < dist:
                continue

            for dt in dxy:
                new_x, new_y = now_x + dt[0], now_y + dt[1]
                if 0 <= new_x < N and 0 <= new_y < N:
                    data = distance[now_x][now_y] + graph[new_x][new_y]
                    if distance[new_x][new_y] > data:
                        distance[new_x][new_y] = data
                        heapq.heappush(q, (data, new_x, new_y))


    dijkstra(0, 0)
    print("Problem",idx, end='')
    print(":",distance[N-1][N-1],end ='\n')
    idx +=1




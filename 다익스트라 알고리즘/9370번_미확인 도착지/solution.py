import sys
import heapq
INF = int(1e9)

input = sys.stdin.readline

T = int(input())

def dijkstra(start,count):
    q = []
    heapq.heappush(q,(0,start))
    distance[count][start] = 0

    while q:
        tmp = heapq.heappop(q)
        dist,now = tmp[0], tmp[1]

        if distance[count][now] < dist:
            continue
        for i in graph[now]:
            end,dist = i[0], i[1]
            data = distance[count][now] + dist
            if distance[count][end] > data:
                distance[count][end] = data
                heapq.heappush(q,(data,end))



for _ in range(T):
    N,M,destination_count = map(int,input().split())
    s,g,h = map(int,input().split())
    list = [s,g,h]

    graph = [[]for _ in range(N+1)]
    distance = [[INF for _ in range(N+1)] for _ in range(3)]

    fix_value = 0

    for _ in range(M):
        start,end,dist = map(int,input().split())
        graph[start].append((end,dist))
        graph[end].append((start,dist))
        if (start == list[1] and end == list[2]) or (start == list[2] and end == list[1]):
            fix_value = dist
            #print(dist)

    destination  = []
    for _ in range(destination_count):
        destination.append(int(input()))


    for k in range(3):
        dijkstra(list[k],k)
        #for j in distance:
            #print(j)

    root_a = distance[0][list[1]] + fix_value
    root_b = distance[0][list[2]] + fix_value
    #print(fix_value)
    #print("root_a : ",root_a , " root_b : ", root_b)
    result = []
    for i in destination:
        tmp_a = root_a + distance[2][i]
        tmp_b = root_b + distance[1][i]
        #print(tmp_a,tmp_b)
        if distance[0][i] == tmp_a or distance[0][i] == tmp_b:
            result.append(i)

    result.sort()

    #print("result")
    for i in result:
        print(i,end = ' ')
    print()

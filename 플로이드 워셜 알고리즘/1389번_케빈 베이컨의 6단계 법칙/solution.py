import sys
INF = int(1e9)

input = sys.stdin.readline

N, M = map(int,input().split())

arr = [[INF for _ in range(N+1)]for _ in range(N+1)]
for i in range(M):
    start,end = map(int,input().split())
    arr[start][end] = 1
    arr[end][start] = 1


def floyd():
    distance = []
    for i in arr:
        distance.append(i)

    for k in range(1,N+1):
        for i in range(1,N+1):
            for j in range(1,N+1):
                if i == j:
                    distance[i][j] = 0
                elif arr[i][k] != 0 and arr[k][j] != 0:
                    distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

    return distance
distance = floyd()

min_value = INF
idx = 1
for i in range(1,N+1):
    data = sum(distance[i][1:])
    if min_value > data:
        min_value = data
        idx = i
    else:
        continue

print(idx)
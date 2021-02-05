"""N = int(input())

arr = []

for i in range(N):
    arr.append(list(map(int,input().split())))

arr.sort(key = lambda x:x[1])

visited = [False for _ in range(N)]

result = 0
#print(arr)

for i in range(0,N):
    if visited[i] == False:
        visited[i] = True
        ##print("i : ",arr[i])
        result += 1
        end = arr[i][1]
        for j in range(i + 1, N):
            start = arr[j][0]
            if visited[j] == False and end <= start:
                ##print("check : ", arr[j])
                visited[j] = True
                end = arr[j][1]
    ##print(visited)


print(result)"""
##시간초과

import heapq

N = int(input())

arr = []
arr2 = []
for i in range(N):
    heapq.heappush(arr,list(map(int,input().split())))

result = 0

while True:
    if arr:
        now = heapq.heappop(arr)
        start, end = now[0], now[1]
        result += 1
    else:
        break
    while arr:
        now = heapq.heappop(arr)
        start = now[0]
        print(now[0], now[1])
        if end <= start:
            end = now[1]
        else:
            heapq.heappush(arr2,now)
        print("Arr : ", arr)
        print("Arr2 : ", arr2)

    if arr2:
        now = heapq.heappop(arr2)
        start, end = now[0], now[1]
        result += 1
    else:
        break
    while arr2:
        print(now[0], now[1])
        now = heapq.heappop(arr2)
        start = now[0]
        if end <= start:
            end = now[1]
        else:
            heapq.heappush(arr, now)
        print("arr : ", arr)
        print("arr2 : ", arr2)


print(result)
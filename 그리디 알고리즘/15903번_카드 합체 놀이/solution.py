import heapq

N, M = map(int,input().split())

arr = list(map(int,input().split()))

heapq.heapify(arr)

for i in range(M):
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    a,b = a+b, a+b
    heapq.heappush(arr,a)
    heapq.heappush(arr,b)

print(sum(arr))

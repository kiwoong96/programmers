import heapq


N = int(input())
K = int(input())
arr = list(map(int,input().split()))

arr.sort()

max_heap = []


for i in range(N-1):
    heapq.heappush(max_heap,(-(arr[i+1]-arr[i]),arr[i+1]-arr[i]))

result = 0

for i in range(N-1):
    if i <K-1:
        heapq.heappop(max_heap)[1]
    else:
        result +=heapq.heappop(max_heap)[1]


print(result)
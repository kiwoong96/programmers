import heapq

N = int(input())

arr = []


for i in range(N):
    heapq.heappush(arr,int(input()))

sum_val = 0
while True:
    if len(arr) >= 2:
        first = heapq.heappop(arr)
        second = heapq.heappop(arr)
        heapq.heappush(arr,first+second)
        sum_val += (first+second)
    else:
        break

print(sum_val)





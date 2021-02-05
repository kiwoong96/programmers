import heapq
import sys

N = int(input())
arr = []

for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().rstrip("\n").split())))



minheap = []

arr.sort(key = lambda x:x[0])

heapq.heapify(minheap)
heapq.heappush(minheap, arr[0][1])

for i in range(1,N):
    if minheap[0] <= arr[i][0]:
        heapq.heappop(minheap)
        heapq.heappush(minheap, arr[i][1])
    else:
        heapq.heappush(minheap, arr[i][1])

print(len(minheap))
N = int(input())
array = list(map(int,input().split()))

d = [0 for _ in range(N)]
d[0] = array[0]

for i in range(1,N):
    d[i] = max(array[i],d[i-1] + array[i])

print(max(d))


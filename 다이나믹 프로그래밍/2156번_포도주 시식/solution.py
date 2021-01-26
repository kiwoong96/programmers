N = int(input())

array = [0 for _ in range(10001)]

d = [0 for _ in range(10001)]

for i in range(1,N+1):
    array[i] = int(input())

d[1] = array[1]
d[2] = array[1] + array[2]
#d[3] = max(array[1]+array[3], array[2] + array[3])

for i in range(3,N+1):
    d[i] = max(d[i-2] + array[i], d[i-3] + array[i-1] + array[i],d[i-1])

print(d[N])



N = int(input())

d = [0 for _ in range(1001)]

d[0] = 0
d[1] = 1
d[2] = 3

for i in range(3, N+1):
    d[i] = (d[i-1] + d[i-2] * 2) % 10007

print(d[N])

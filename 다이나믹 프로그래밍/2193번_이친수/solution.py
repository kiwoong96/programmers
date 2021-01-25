N = int(input())

d = [[0,0] for _ in range(N+1)]

d[1] = [0,1]


for i in range(2,N+1):
    d[i] = [d[i-1][0]+d[i-1][1],d[i-1][0]]

print(sum(d[N]))


d = [0 for _ in range(101)]

d[1] = 1
d[2] = 1
d[3] = 1
d[4] = 2


for i in range(5,101):
    d[i] = d[i-1] + d[i-5]



T = int(input())

for i in range(T):
    N = int(input())
    print(d[N])




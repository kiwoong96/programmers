N = int(input())

array = []
d = []

for i in range(N):
    array.append(list(map(int,input().split())))

for i in range(N+1):
    d.append([0,0,0])

d[1] = array[0]
for i in range(2,N+1):
    for j in range(3):
        #print("i : ", i , ", j : " , j)
        if j == 0:
            d[i][j] = min(d[i-1][1],d[i-1][2]) + array[i-1][j]
        elif j == 1:
            d[i][j] = min(d[i-1][0], d[i-1][2]) + array[i-1][j]
        else:
            d[i][j] = min(d[i-1][0], d[i-1][1]) + array[i-1][j]

print(min(d[N]))





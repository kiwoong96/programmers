N = int(input())

array = []
d = []
for i in range(N):
    array.append(list(map(int,input().split())))
    d.append([0]*(i+1))
#print("array : " , array)
#print("d : " ,d )
d[0] = array[0]
for i in range(1,N):
    for j in range(len(array[i])):
        if j==0:
            #print("j == 0 : d[i-1][0] : ",d[i-1][0],", array[i][j] : ", array[i][j])
            d[i][j] = int(d[i-1][0]) + array[i][j]
        elif j == len(array[i])-1:
            d[i][j] = d[i-1][len(array[i-1])-1] + array[i][j]
        else:
            d[i][j] = max(d[i-1][j-1],d[i-1][j]) + array[i][j]

print(max(d[N-1]))
T = int(input())

d = [[0,0]] * (41)


d[0] = [1,0]
d[1] = [0,1]
#print(d)
for i in range(2,41):
    d[i] = [d[i-1][0] + d[i-2][0],d[i-1][1] + d[i-2][1]]
    #print("i : ", i,",d : " ,d)


for i in range(T):
    for j in d[int(input())]:
        print(j, end = ' ')
    print()

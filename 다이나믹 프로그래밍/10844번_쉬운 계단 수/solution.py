##내풀이

"""
N = int(input())

d= [[0,0,0,0,0,0,0,0,0,0,0] for _ in range(101)]

d[1] = [1,1,1,1,1,1,1,1,1,1, 9]

for i in range(2, N+1):
    d[i] = [d[i-1][1],
            d[i-1][0]+d[i-1][2],
            d[i-1][1]+d[i-1][3],
            d[i-1][2]+d[i-1][4],
            d[i-1][3]+d[i-1][5],
            d[i-1][4]+d[i-1][6],
            d[i-1][5]+d[i-1][7],
            d[i-1][6]+d[i-1][8],
            d[i-1][7]+d[i-1][9],
            d[i-1][8],0]
    d[i][10]= sum(d[i][0:9])%1000000000

print(d[N][10])
"""

##정석풀이

N = int(input())

d = [[0 for _ in range(10)] for _ in range(N+1)]

d[1] = [0,1,1,1,1,1,1,1,1,1]

for i in range(2,N+1):
    for j in range(10):
        if j == 0:
            d[i][j] = d[i-1][j+1]
        elif j == 9:
            d[i][j] = d[i-1][j-1]
        else:
            d[i][j] = d[i-1][j-1] + d[i-1][j+1]

print(sum(d[N]))
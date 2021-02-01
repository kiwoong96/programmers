M, N = map(int,input().split())

arr = []
dp = [[0 for _ in range(M+2)] for _ in range(N+2)]

dxy = [[1,0][0,-1],[-1,0],[0,1]]

for i in range(M):
    tmp = list(map(int,input().split()))
    tmp.insert(0,0)
    arr.append(tmp)


for i in range(1,M+1):
    for j in range(1,N+1):
        for c in dxy:
            tmp_x = i+c[0]
            tmp_y = j+c[1]
            if arr[tmp_x][tmp_y] < arr[i][j]:
                if dp[tmp_x][tmp_y] == dp[i][j]:
                    dp[tmp_x][tmp_y] = dp[tmp_x][tmp_y]*2





